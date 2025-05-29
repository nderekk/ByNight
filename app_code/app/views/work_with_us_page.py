from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,
    QFrame, QFileDialog, QMessageBox
)
from PySide6.QtCore import Qt
import sys
class FileUploadField(QWidget):
    def __init__(self, label_text):
        super().__init__()
        self.file_path = None

        layout = QHBoxLayout()
        layout.setContentsMargins(10, 5, 10, 5)

        label = QLabel(label_text)
        label.setStyleSheet("font-weight: bold; font-size: 10pt; color: black;")
        label.setFixedWidth(120)

        self.button = QPushButton("Input File")
        self.button.setStyleSheet("""
            QPushButton {
                background-color: black;
                color: white;
                padding: 4px 10px;
                font-size: 9pt;
                border-radius: 4px;
            }
        """)
        self.button.clicked.connect(self.select_file)

        self.remove_btn = QPushButton("✕")
        self.remove_btn.setFixedSize(24, 24)
        self.remove_btn.setStyleSheet("""
            QPushButton {
                background-color: black;
                color: white;
                font-size: 10pt;
                border-radius: 12px;
            }
        """)
        self.remove_btn.clicked.connect(self.remove_clicked)

        layout.addWidget(label)
        layout.addStretch()
        layout.addWidget(self.button)
        layout.addWidget(self.remove_btn)
        self.setLayout(layout)
        self.setStyleSheet("background-color: #eae6ef; border: 1px solid gray; border-radius: 4px;")

    def select_file(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Select File")
        if file_path:
            self.file_path = file_path 
            self.button.setText("✔ Υποβλήθηκε")

    def remove_clicked(self):
        self.file_path = None  # <- καθάρισε
        self.button.setText("Input File")
        print(f"Remove clicked for {self.label_text}")

    def get_file_path(self):
        return self.file_path


class WorkWithUsPage(QWidget):

    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setSpacing(15)

        # Header
        header_layout = QHBoxLayout()
        self.back_btn = QPushButton("←")
        self.back_btn.setFixedSize(30, 30)
        self.back_btn.setStyleSheet("""
            QPushButton {
                font-size: 14pt;
                background-color: black;
                color: white;
                border-radius: 4px;
            }
        """)
        #back_btn.clicked.connect(self.on_back_clicked)

        title = QLabel("Work With Us")
        title.setStyleSheet("font-size: 12pt; font-weight: bold;")
        header_layout.addWidget(self.back_btn)
        header_layout.addWidget(title)
        header_layout.addStretch()
        main_layout.addLayout(header_layout)

        # Underline
        underline = QFrame()
        underline.setFrameShape(QFrame.HLine)
        underline.setFrameShadow(QFrame.Sunken)
        underline.setStyleSheet("margin-top: -10px; margin-bottom: 10px;")
        main_layout.addWidget(underline)

        # Greek title
        greek_title = QLabel("Αίτηση υποβολής")
        greek_title.setStyleSheet("font-size: 12pt; font-weight: bold;")
        greek_title.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(greek_title)

        # Upload fields
        field_labels = ["ΑΦΜ", "ΚΑΔ", "Επωνυμία", "Άδεια Λειτουργίας"]
        self.upload_fields = []

        for label_text in field_labels:
            field_widget = FileUploadField(label_text)
            self.upload_fields.append(field_widget)
            main_layout.addWidget(field_widget)

        main_layout.addStretch()

        # Submit button (black)
        self.submit_btn = QPushButton("✓ Υποβολή")
        self.submit_btn.setStyleSheet("""
            QPushButton {
                padding: 10px;
                font-size: 11pt;
                background-color: black;
                color: white;
                border-radius: 6px;
            }
        """)
        self.submit_btn.setFixedSize(140, 40)
        #submit_btn.clicked.connect(self.submit_clicked)

        submit_layout = QHBoxLayout()
        submit_layout.addStretch()
        submit_layout.addWidget(self.submit_btn)
        main_layout.addLayout(submit_layout)

        self.setLayout(main_layout)



    def get_uploaded_files(self) -> list[str]:
        return [field.get_file_path() for field in self.upload_fields if field.get_file_path() is not None]
    



    def show_error(self, message: str):
        QMessageBox.critical(self, "Σφάλμα", message)


