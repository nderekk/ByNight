from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QTextEdit,
    QVBoxLayout, QHBoxLayout, QGridLayout, QFrame
)
from PySide6.QtGui import QPixmap, QMouseEvent
from PySide6.QtCore import Qt
import sys


class StarRating(QWidget):
    def __init__(self, stars=5):
        super().__init__()
        self.num_stars = stars
        self.current_rating = 0
        self.stars = []
        self.layout = QHBoxLayout(self)
        self.layout.setSpacing(5)
        for i in range(1, stars + 1):
            label = QLabel("☆")
            label.setStyleSheet("font-size: 20pt;")
            label.mousePressEvent = lambda event, rating=i: self.set_rating(rating)
            self.layout.addWidget(label)
            self.stars.append(label)

    def set_rating(self, rating):
        self.current_rating = rating
        for i in range(self.num_stars):
            self.stars[i].setText("★" if i < rating else "☆")


class AddReviewApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Review")
        self.setMinimumSize(400, 600)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        # Title with Back Button
        title_layout = QHBoxLayout()
        self.back_btn = QPushButton("←")
        self.back_btn.setFixedSize(30, 30)
        self.back_btn.setStyleSheet("font-size: 14pt;")
        title_layout.addWidget(self.back_btn)

        title = QLabel("Add Review")
        title.setStyleSheet("font-size: 16pt; font-weight: bold;")
        title_layout.addWidget(title)
        title_layout.addStretch()
        layout.addLayout(title_layout)

        # Club image and info
        image = QLabel()
        pixmap = QPixmap(80, 80)
        pixmap.fill(Qt.black)  # Replace with: QPixmap("your_image_path.jpg")
        image.setPixmap(pixmap)
        image.setFixedSize(80, 80)
        image.setScaledContents(True)

        info_layout = QVBoxLayout()
        info_layout.addWidget(QLabel("Date: 3/4/2025  Event: Kultura"))

        top_info = QHBoxLayout()
        top_info.addWidget(image)
        top_info.addLayout(info_layout)
        top_info.addStretch()

        layout.addLayout(top_info)

        # Rating labels and stars
        rating_layout = QGridLayout()
        criteria = ["Music", "Atmosphere", "Service", "Price", "Overall Experience"]

        for i, label in enumerate(criteria):
            rating_layout.addWidget(QLabel(f"<b>{label}</b>"), i, 0)
            rating_layout.addWidget(StarRating(), i, 1)

        layout.addLayout(rating_layout)

        # Comment box
        comment_box = QTextEdit()
        comment_box.setPlaceholderText("Leave a comment here...")
        comment_box.setStyleSheet("font-size: 10pt; padding: 5px;")
        layout.addWidget(comment_box)

        # Submit Button (Optional)
        submit_btn = QPushButton("Submit Review")
        submit_btn.setStyleSheet("padding: 10px; font-size: 12pt; background-color: #333; color: white;")
        layout.addWidget(submit_btn)

        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AddReviewApp()
    window.show()
    sys.exit(app.exec())
