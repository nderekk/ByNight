from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,
    QFileDialog, QFrame
)
from PySide6.QtCore import Qt
import sys


class FileUploadField(QWidget):
    def __init__(self, label_text):
        super().__init__()
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        label = QLabel(label_text)
        label.setStyleSheet("font-size: 9pt;")

        self.button = QPushButton("Input File")
        self.button.setStyleSheet("padding: 4px; font-size: 9pt; background-color: #e0dfe6;")

        self.remove_btn = QPushButton("✕")
        self.remove_btn.setFixedSize(24, 24)
        self.remove_btn.setStyleSheet("font-size: 10pt; background: none;")

        layout.addWidget(label)
        layout.addStretch()
        layout.addWidget(self.button)
        layout.addWidget(self.remove_btn)
        self.setLayout(layout)


class WorkWithUsApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Work With Us")
        self.setMinimumSize(360, 640)
        self.setup_ui()

    def setup_ui(self):
        main_layout = QVBoxLayout()

        # Header
        header_layout = QHBoxLayout()
        back_btn = QPushButton("←")
        back_btn.setFixedSize(30, 30)
        back_btn.setStyleSheet("font-size: 14pt;")
        title = QLabel("Work With Us")
        title.setStyleSheet("font-size: 12pt; font-weight: bold;")
        header_layout.addWidget(back_btn)
        header_layout.addWidget(title)
        header_layout.addStretch()
        main_layout.addLayout(header_layout)

        # Tab underline (simulated)
        underline = QFrame()
        underline.setFrameShape(QFrame.HLine)
        underline.setFrameShadow(QFrame.Sunken)
        underline.setStyleSheet("margin-top: -10px; margin-bottom: 10px;")
        main_layout.addWidget(underline)

        # Greek Title
        greek_title = QLabel("Αίτηση υποβολής")
        greek_title.setStyleSheet("font-size: 12pt; font-weight: bold;")
        greek_title.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(greek_title)

        # Upload fields
        upload_fields = [
            "ΑΦΜ",
            "ΚΑΔ",
            "Επωνυμία",
            "Άδεια Λειτουργίας"
        ]

        for field in upload_fields:
            field_widget = FileUploadField(field)
            field_widget.setStyleSheet("background-color: #eae6ef; padding: 8px; border: 1px solid gray;")
            main_layout.addWidget(field_widget)

        main_layout.addStretch()

        # Submit Button
        submit_btn = QPushButton("✓ Υποβολής")
        submit_btn.setStyleSheet("padding: 10px; font-size: 11pt; background-color: #c8b8d7;")
        submit_btn.setFixedWidth(120)
        submit_btn.setFixedHeight(40)
        submit_layout = QHBoxLayout()
        submit_layout.addStretch()
        submit_layout.addWidget(submit_btn)
        main_layout.addLayout(submit_layout)

        self.setLayout(main_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WorkWithUsApp()
    window.show()
    sys.exit(app.exec())
