import os
import shutil
import re
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from datetime import datetime
from file_categories import (
    FILE_PATTERNS,
    CONTENT_KEYWORDS,
    COMMON_PATTERNS,
    TRAINING_EXAMPLES
)

class FileSorter:
    def __init__(self):
        # Load patterns and keywords from dataset
        self.file_patterns = FILE_PATTERNS
        self.content_keywords = CONTENT_KEYWORDS
        self.common_patterns = COMMON_PATTERNS
        
        # Create training data
        self._create_training_data()
        
        # Initialize and train the model
        self.vectorizer = TfidfVectorizer(
            tokenizer=self._custom_tokenizer,
            token_pattern=None,
            ngram_range=(1, 3)  # Increased to capture more context
        )
        self.clf = DecisionTreeClassifier(
            random_state=42,
            max_depth=10,  # Prevent overfitting
            min_samples_split=5
        )
        self._train_model()

    def _custom_tokenizer(self, text):
        """Custom tokenizer that handles special cases and patterns."""
        # Convert to lowercase and split on common delimiters
        tokens = re.split(r'[_\-.\s]', text.lower())
        
        # Extract date patterns
        for date_pattern in self.common_patterns['dates']:
            dates = re.findall(date_pattern, text)
            if dates:
                tokens.extend(['date_token'])
        
        # Extract version patterns
        for version_pattern in self.common_patterns['versions']:
            versions = re.findall(version_pattern, text)
            if versions:
                tokens.extend(['version_token'])
        
        # Extract status patterns
        for status_pattern in self.common_patterns['status']:
            statuses = re.findall(status_pattern, text.lower())
            if statuses:
                tokens.extend(['status_token'])
        
        # Remove empty tokens and duplicates
        tokens = [t for t in tokens if t]
        return list(dict.fromkeys(tokens))

    def _create_training_data(self):
        """Create comprehensive training data from patterns and keywords."""
        self.file_names = []
        self.categories = []
        
        # Add extension-based examples
        for category, extensions in self.file_patterns.items():
            for ext in extensions:
                examples = [
                    f"file.{ext}",
                    f"document_{ext}",
                    f"my_{ext}_file",
                    f"{ext}_document",
                    f"project.{ext}",
                    f"example.{ext}",
                    f"test.{ext}",
                    f"final.{ext}",
                    f"draft.{ext}"
                ]
                self.file_names.extend(examples)
                self.categories.extend([category] * len(examples))
        
        # Add content-based examples
        for category, keywords in self.content_keywords.items():
            for keyword in keywords:
                examples = [
                    f"{keyword}_file",
                    f"my_{keyword}",
                    f"{keyword}_document",
                    f"project_{keyword}",
                    f"final_{keyword}",
                    f"{keyword}_v1",
                    f"{keyword}_2024",
                    f"{keyword}_draft",
                    f"{keyword}_final"
                ]
                self.file_names.extend(examples)
                self.categories.extend([category] * len(examples))
        
        # Add pattern-based examples
        for category, patterns in self.common_patterns.items():
            for pattern in patterns:
                examples = [
                    f"file_{pattern}",
                    f"{pattern}_document",
                    f"project_{pattern}",
                    f"{pattern}_final",
                    f"{pattern}_backup",
                    f"{pattern}_archive",
                    f"{pattern}_latest"
                ]
                self.file_names.extend(examples)
                self.categories.extend([category] * len(examples))
        
        # Add real-world examples from training dataset
        for filename, category in TRAINING_EXAMPLES:
            self.file_names.append(filename)
            self.categories.append(category)

    def _train_model(self):
        """Train the classification model."""
        X = self.vectorizer.fit_transform(self.file_names)
        self.clf.fit(X, self.categories)

    def _get_extension_category(self, filename):
        """Get category based on file extension."""
        ext = os.path.splitext(filename)[1].lower()[1:]  # Remove the dot
        for category, extensions in self.file_patterns.items():
            if ext in extensions:
                return category, 1.0  # High confidence for exact extension match
        return None, 0.0

    def _get_keyword_category(self, filename):
        """Get category based on keyword matching."""
        filename_lower = filename.lower()
        max_confidence = 0.0
        best_category = None
        
        for category, keywords in self.content_keywords.items():
            for keyword in keywords:
                if keyword.lower() in filename_lower:
                    confidence = len(keyword) / len(filename_lower)  # Length-based confidence
                    if confidence > max_confidence:
                        max_confidence = confidence
                        best_category = category
        
        return best_category, max_confidence

    def predict_category(self, filename):
        """Predict the category for a given filename using multiple methods."""
        # Try extension-based categorization first
        ext_category, ext_confidence = self._get_extension_category(filename)
        if ext_confidence > 0.9:  # Very high confidence for extension match
            return ext_category
        
        # Try keyword-based categorization
        keyword_category, keyword_confidence = self._get_keyword_category(filename)
        
        # Get ML model prediction
        features = self.vectorizer.transform([filename.lower()])
        ml_category = self.clf.predict(features)[0]
        probabilities = self.clf.predict_proba(features)[0]
        ml_confidence = max(probabilities)
        
        # Weighted decision based on all methods
        if ext_confidence > 0.9:
            return ext_category
        elif keyword_confidence > 0.8:
            return keyword_category
        elif ml_confidence > 0.6:
            return ml_category
        elif ext_category:
            return ext_category
        else:
            return ml_category

    def sort_files(self, source_dir, backup=True, progress_callback=None):
        """Sort files in the source directory."""
        if not os.path.isdir(source_dir):
            raise ValueError(f"Directory not found: {source_dir}")
        
        if progress_callback:
            progress_callback("Initializing AI model...")
        
        # Create backup if requested
        if backup:
            backup_dir = os.path.join(source_dir, f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}")
            os.makedirs(backup_dir, exist_ok=True)
            if progress_callback:
                progress_callback(f"Created backup directory: {backup_dir}")
        
        # Get all files
        files = [f for f in os.listdir(source_dir) 
                if os.path.isfile(os.path.join(source_dir, f))]
        
        if not files:
            if progress_callback:
                progress_callback("No files found to organize.")
            return
        
        total_files = len(files)
        processed_files = 0
        
        # Sort files
        for filename in files:
            try:
                file_path = os.path.join(source_dir, filename)
                category = self.predict_category(filename)
                
                # Create category folder
                category_dir = os.path.join(source_dir, category)
                os.makedirs(category_dir, exist_ok=True)
                
                # Move file
                shutil.move(file_path, os.path.join(category_dir, filename))
                
                # Create backup
                if backup:
                    shutil.copy2(os.path.join(category_dir, filename),
                               os.path.join(backup_dir, filename))
                
                processed_files += 1
                if progress_callback:
                    progress = (processed_files / total_files) * 100
                    progress_callback(f"AI organizing: {filename} -> {category}/ ({int(progress)}%)")
                
            except Exception as e:
                if progress_callback:
                    progress_callback(f"! Failed to organize {filename}: {str(e)}")
        
        if backup and progress_callback:
            progress_callback(f"✓ AI organization complete! Backup created in: {backup_dir}")

def ai_based_sort(root_directory, progress_callback=None):
    """Main function to perform AI-based file sorting."""
    sorter = FileSorter()
    sorter.sort_files(root_directory, progress_callback=progress_callback)