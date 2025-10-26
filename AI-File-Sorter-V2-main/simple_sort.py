import os
import shutil
from datetime import datetime

def get_file_type(file_path):
    """Get the file type based on extension."""
    ext = os.path.splitext(file_path)[1].lower()
    if not ext:
        return 'other'
    return ext[1:]  # Remove the dot

def create_type_folder(root_dir, file_type):
    """Create a folder for the file type if it doesn't exist."""
    type_folder = os.path.join(root_dir, file_type)
    os.makedirs(type_folder, exist_ok=True)
    return type_folder

def simple_sort(root_directory, progress_callback=None):
    """Organize files by their type (extension)."""
    if not os.path.isdir(root_directory):
        raise ValueError(f"Directory not found: {root_directory}")
    
    # Get all files in the directory
    files = [f for f in os.listdir(root_directory) 
             if os.path.isfile(os.path.join(root_directory, f))]
    
    if not files:
        if progress_callback:
            progress_callback("No files found to organize.")
        return
    
    # Create a timestamped backup folder
    backup_dir = os.path.join(root_directory, f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}")
    os.makedirs(backup_dir, exist_ok=True)
    
    total_files = len(files)
    processed_files = 0
    
    # Organize files
    for filename in files:
        try:
            file_path = os.path.join(root_directory, filename)
            file_type = get_file_type(filename)
            
            # Create type folder and move file
            type_folder = create_type_folder(root_directory, file_type)
            shutil.move(file_path, os.path.join(type_folder, filename))
            
            # Create backup
            shutil.copy2(os.path.join(type_folder, filename), 
                        os.path.join(backup_dir, filename))
            
            processed_files += 1
            if progress_callback:
                progress = (processed_files / total_files) * 100
                progress_callback(f"Organizing: {filename} -> {file_type}/ ({int(progress)}%)")
            
        except Exception as e:
            if progress_callback:
                progress_callback(f"! Failed to organize {filename}: {str(e)}")
    
    if progress_callback:
        progress_callback(f"✓ Organization complete! Backup created in: {backup_dir}")
