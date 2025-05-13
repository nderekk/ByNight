import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
)
from PySide6.QtGui import QPainter, QBrush, QColor
from PySide6.QtCore import Qt, QRect


class CircleImage(QLabel):
    def __init__(self, diameter=100):
        super().__init__()
        self.diameter = diameter
        self.setFixedSize(diameter, diameter)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QBrush(QColor(200, 200, 200)))
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(QRect(0, 0, self.diameter, self.diameter))


class ProfileApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Profile")
        self.setMinimumSize(360, 480)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)

        # Header with Back Button
        header_layout = QHBoxLayout()
        back_btn = QPushButton("←")
        back_btn.setStyleSheet("font-size: 20px; background-color: transparent; border: none;")
        back_btn.setFixedSize(40, 40)
        back_btn.clicked.connect(self.on_back_clicked)
        header_layout.addWidget(back_btn, alignment=Qt.AlignLeft)
        header_layout.addStretch()
        layout.addLayout(header_layout)

        # Centered Profile Image
        profile_layout = QVBoxLayout()
        profile_layout.setAlignment(Qt.AlignHCenter)
        profile_image = CircleImage(100)
        profile_layout.addWidget(profile_image)
        profile_layout.addSpacing(20)
        layout.addLayout(profile_layout)

        # Individual Info Fields (each below the other)
        layout.addLayout(self.create_info_column("name", "Nick"))
        layout.addLayout(self.create_info_column("surname", "Dagkalis"))
        layout.addLayout(self.create_info_column("date of birth", "30/10/2004"))
        layout.addLayout(self.create_info_column("email", "nickdagkalis@gmail.com"))
        layout.addLayout(self.create_info_column("phone number", "6911122223"))

        layout.addStretch()

        # Work With Us Button
        work_btn = QPushButton("work with us")
        work_btn.setStyleSheet(
            "padding: 10px 20px; font-size: 11pt; background-color: black; color: white; border-radius: 16px;"
        )
        work_btn.clicked.connect(self.on_work_with_us_clicked)
        layout.addWidget(work_btn, alignment=Qt.AlignHCenter)

        self.setLayout(layout)

    def create_info_column(self, label_text, value_text):
        column = QVBoxLayout()
        label = QLabel(label_text)
        label.setStyleSheet("font-weight: bold;")
        value = QLabel(value_text)
        value.setStyleSheet("font-size: 10pt;")
        column.addWidget(label)
        column.addWidget(value)
        column.setSpacing(4)
        return column

    def on_back_clicked(self):
        QMessageBox.information(self, "Back", "Going back to the previous screen.")
        self.close()

    def on_work_with_us_clicked(self):
        QMessageBox.information(self, "Work with Us", "Thank you for your interest! We’ll contact you soon.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProfileApp()
    window.show()
    sys.exit(app.exec())
