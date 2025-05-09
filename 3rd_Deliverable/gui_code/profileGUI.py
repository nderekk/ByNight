from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
)
from PySide6.QtGui import QPixmap, QPainter, QBrush, QColor
from PySide6.QtCore import Qt, QRect
import sys


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

        # Circular Profile Image Placeholder
        profile_image = CircleImage(100)
        layout.addWidget(profile_image, alignment=Qt.AlignHCenter)
        layout.addSpacing(20)

        # Name and Surname
        name_row = self.create_info_row("name", "surname", "Nick", "Dagkalis")
        layout.addLayout(name_row)

        # Date of Birth and Email
        dob_row = self.create_info_row("date of birth", "email", "30/10/2004", "nickdagkalis@gmail.com")
        layout.addLayout(dob_row)

        # Phone Number (aligned left under email)
        phone_row = QHBoxLayout()
        label = QLabel("phone number")
        label.setStyleSheet("font-weight: bold;")
        value = QLabel("6911122223")
        value.setStyleSheet("font-size: 10pt;")
        phone_row.addWidget(label)
        phone_row.addSpacing(20)
        phone_row.addWidget(value)
        phone_row.addStretch()
        layout.addLayout(phone_row)

        layout.addStretch()

        # Button
        work_btn = QPushButton("work with us")
        work_btn.setStyleSheet("padding: 10px 20px; font-size: 11pt; background-color: black; color: white; border-radius: 16px;")
        layout.addWidget(work_btn, alignment=Qt.AlignHCenter)

        self.setLayout(layout)

    def create_info_row(self, label1, label2, val1, val2):
        row = QHBoxLayout()

        col1 = QVBoxLayout()
        label1_widget = QLabel(label1)
        label1_widget.setStyleSheet("font-weight: bold;")
        val1_widget = QLabel(val1)
        col1.addWidget(label1_widget)
        col1.addWidget(val1_widget)

        col2 = QVBoxLayout()
        label2_widget = QLabel(label2)
        label2_widget.setStyleSheet("font-weight: bold;")
        val2_widget = QLabel(val2)
        col2.addWidget(label2_widget)
        col2.addWidget(val2_widget)

        row.addLayout(col1)
        row.addSpacing(30)
        row.addLayout(col2)
        row.addStretch()

        return row


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProfileApp()
    window.show()
    sys.exit(app.exec())
