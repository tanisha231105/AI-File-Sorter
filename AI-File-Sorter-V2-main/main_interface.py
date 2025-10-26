import sys
import os
import shutil
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                            QPushButton, QLabel, QFileDialog, QRadioButton, 
                            QButtonGroup, QMessageBox, QProgressBar, QHBoxLayout,
                            QListWidget, QListWidgetItem)
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QFont, QIcon
from simple_sort import simple_sort
from advanced_sort import ai_based_sort

class SortingThread(QThread):
    """Thread for running the sorting process to prevent GUI freezing."""
    progress = pyqtSignal(str)
    finished = pyqtSignal()
    error = pyqtSignal(str)

    def __init__(self, directory, method):
        super().__init__()
        self.directory = directory
        self.method = method

    def run(self):
        try:
            if self.method == 'simple':
                simple_sort(self.directory, progress_callback=self.progress.emit)
            else:
                ai_based_sort(self.directory, progress_callback=self.progress.emit)
            self.finished.emit()
        except Exception as e:
            self.error.emit(str(e))

class FileOrganizerGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.sorting_thread = None
        self.current_directory = None
        self.backup_dirs = []

    def init_ui(self):
        self.setWindowTitle('AI File Organizer')
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f0f0;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                font-size: 14px;
                min-width: 150px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:disabled {
                background-color: #cccccc;
            }
            QLabel {
                font-size: 14px;
                color: #333333;
            }
            QRadioButton {
                font-size: 14px;
                color: #333333;
                padding: 5px;
            }
            QProgressBar {
                border: 1px solid #ccc;
                border-radius: 4px;
                text-align: center;
                background-color: white;
            }
            QProgressBar::chunk {
                background-color: #4CAF50;
                border-radius: 4px;
            }
            QListWidget {
                background-color: white;
                border: 1px solid #ccc;
                border-radius: 4px;
                padding: 5px;
            }
            QListWidget::item {
                padding: 5px;
                border-bottom: 1px solid #eee;
            }
            QListWidget::item:selected {
                background-color: #e0e0e0;
            }
        """)

        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setSpacing(20)
        layout.setContentsMargins(30, 30, 30, 30)

        # Title
        title = QLabel("AI File Organizer")
        title.setFont(QFont('Arial', 24, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        # Description
        desc = QLabel("Organize your files automatically using AI or simple file type sorting")
        desc.setFont(QFont('Arial', 12))
        desc.setAlignment(Qt.AlignCenter)
        desc.setWordWrap(True)
        layout.addWidget(desc)

        # Directory selection
        self.dir_label = QLabel("No directory selected")
        self.dir_label.setWordWrap(True)
        self.dir_label.setStyleSheet("padding: 10px; background-color: white; border-radius: 4px;")
        layout.addWidget(self.dir_label)

        select_btn = QPushButton("Select Folder to Organize")
        select_btn.clicked.connect(self.select_directory)
        layout.addWidget(select_btn)

        # Sorting method selection
        method_group = QButtonGroup(self)
        self.simple_rb = QRadioButton("Simple Sort (by file type)")
        self.advanced_rb = QRadioButton("Advanced Sort (AI-based)")
        method_group.addButton(self.simple_rb)
        method_group.addButton(self.advanced_rb)
        self.simple_rb.setChecked(True)
        
        method_layout = QVBoxLayout()
        method_layout.addWidget(self.simple_rb)
        method_layout.addWidget(self.advanced_rb)
        layout.addLayout(method_layout)

        # Progress bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        self.progress_bar.setTextVisible(True)
        layout.addWidget(self.progress_bar)

        # Status label
        self.status_label = QLabel("")
        self.status_label.setWordWrap(True)
        self.status_label.setStyleSheet("padding: 10px; background-color: white; border-radius: 4px;")
        layout.addWidget(self.status_label)

        # Start button
        self.start_btn = QPushButton("Start Organizing")
        self.start_btn.clicked.connect(self.start_sorting)
        self.start_btn.setEnabled(False)
        layout.addWidget(self.start_btn)

        # Backup Management Section
        backup_label = QLabel("Backup Management")
        backup_label.setFont(QFont('Arial', 16, QFont.Bold))
        backup_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(backup_label)

        # Backup list
        self.backup_list = QListWidget()
        self.backup_list.setMaximumHeight(150)
        layout.addWidget(self.backup_list)

        # Backup buttons
        backup_btn_layout = QHBoxLayout()
        self.refresh_backups_btn = QPushButton("Refresh Backups")
        self.refresh_backups_btn.clicked.connect(self.refresh_backups)
        self.delete_backup_btn = QPushButton("Delete Selected Backup")
        self.delete_backup_btn.clicked.connect(self.delete_selected_backup)
        self.delete_backup_btn.setEnabled(False)
        
        backup_btn_layout.addWidget(self.refresh_backups_btn)
        backup_btn_layout.addWidget(self.delete_backup_btn)
        layout.addLayout(backup_btn_layout)

        # Connect backup list selection
        self.backup_list.itemSelectionChanged.connect(self.update_delete_button)

    def select_directory(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Directory")
        if directory:
            self.current_directory = directory
            self.dir_label.setText(f"Selected: {directory}")
            self.start_btn.setEnabled(True)
            self.status_label.setText("Ready to organize files")
            self.refresh_backups()

    def refresh_backups(self):
        if not self.current_directory:
            return
            
        self.backup_list.clear()
        self.backup_dirs = []
        
        # Find all backup directories
        for item in os.listdir(self.current_directory):
            if item.startswith("backup_") and os.path.isdir(os.path.join(self.current_directory, item)):
                self.backup_dirs.append(item)
                self.backup_list.addItem(item)
        
        if not self.backup_dirs:
            self.backup_list.addItem("No backups found")

    def update_delete_button(self):
        self.delete_backup_btn.setEnabled(bool(self.backup_list.selectedItems()))

    def delete_selected_backup(self):
        selected_items = self.backup_list.selectedItems()
        if not selected_items:
            return
            
        backup_name = selected_items[0].text()
        if backup_name == "No backups found":
            return
            
        reply = QMessageBox.question(self, 'Confirm Delete',
                                   f'Are you sure you want to delete the backup "{backup_name}"?',
                                   QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            try:
                backup_path = os.path.join(self.current_directory, backup_name)
                shutil.rmtree(backup_path)
                self.refresh_backups()
                QMessageBox.information(self, "Success", "Backup deleted successfully")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to delete backup: {str(e)}")

    def start_sorting(self):
        if not hasattr(self, 'current_directory'):
            QMessageBox.warning(self, "Error", "Please select a directory first.")
            return

        method = 'simple' if self.simple_rb.isChecked() else 'advanced'
        
        # Disable UI elements during sorting
        self.start_btn.setEnabled(False)
        self.progress_bar.setVisible(True)
        self.progress_bar.setValue(0)
        self.status_label.setText("Initializing...")

        # Start sorting in a separate thread
        self.sorting_thread = SortingThread(self.current_directory, method)
        self.sorting_thread.progress.connect(self.update_status)
        self.sorting_thread.finished.connect(self.sorting_finished)
        self.sorting_thread.error.connect(self.sorting_error)
        self.sorting_thread.start()

    def update_status(self, message):
        self.status_label.setText(message)
        # Try to extract progress percentage from message
        try:
            progress = int(message.split('(')[-1].split('%')[0])
            self.progress_bar.setValue(progress)
        except:
            pass

    def sorting_finished(self):
        self.progress_bar.setVisible(False)
        self.start_btn.setEnabled(True)
        self.refresh_backups()  # Refresh backup list after sorting
        QMessageBox.information(self, "Success", "File organization completed successfully!")

    def sorting_error(self, error_message):
        self.progress_bar.setVisible(False)
        self.start_btn.setEnabled(True)
        QMessageBox.critical(self, "Error", f"An error occurred: {error_message}")

def main():
    app = QApplication(sys.argv)
    window = FileOrganizerGUI()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()