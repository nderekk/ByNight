 
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QTextEdit,
    QVBoxLayout, QHBoxLayout, QGridLayout
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QTextEdit, QScrollArea, QWidget


class ReviewPopup(QDialog):
    from app.models.review import Review
    def __init__(self, reviews: list[Review]):
        super().__init__()
        self.setWindowTitle("Other Users' Reviews")
        self.setMinimumSize(400, 300)
        layout = QVBoxLayout()

        scroll_area = QScrollArea()
        scroll_content = QWidget()
        scroll_layout = QVBoxLayout()

        if not reviews:
            scroll_layout.addWidget(QLabel("No other reviews available."))
        else:
            for r in reviews:
                text = (
                    f"<b>Music:</b> {r.music_rating} | "
                    f"<b>Atmosphere:</b> {r.atmosphere_rating} | "
                    f"<b>Service:</b> {r.service_rating} | "
                    f"<b>Overall:</b> {r.overall_experience}<br>"
                    f"<i>{r.comments}</i>"
                )
                label = QLabel(text)
                label.setWordWrap(True)
                scroll_layout.addWidget(label)
                scroll_layout.addWidget(QLabel("—" * 40))

        scroll_content.setLayout(scroll_layout)
        scroll_area.setWidget(scroll_content)
        scroll_area.setWidgetResizable(True)
        layout.addWidget(scroll_area)

        self.setLayout(layout)


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


class ReviewPage(QWidget):
    def __init__(self, event_info: tuple):
     super().__init__()
     self.event_info=event_info
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
        date, event_title = self.event_info
        info_label = QLabel(f"Date: {date}  Event: {event_title}")
        info_layout.addWidget(info_label)

        top_info = QHBoxLayout()
        top_info.addWidget(image)
        top_info.addLayout(info_layout)
        top_info.addStretch()

        layout.addLayout(top_info)

        # Rating labels and stars
        rating_layout = QGridLayout()

        self.rating_widgets = {}

        criteria = ["Music", "Atmosphere", "Service", "Overall Experience"]
        for i, label in enumerate(criteria):
            rating_label = QLabel(f"<b>{label}</b>")
            rating_widget = StarRating()
            rating_layout.addWidget(rating_label, i, 0)
            rating_layout.addWidget(rating_widget, i, 1)
            self.rating_widgets[label] = rating_widget

        layout.addLayout(rating_layout)

        
        self.comment_box = QTextEdit()
        self.comment_box.setPlaceholderText("Leave a comment here...")
        self.comment_box.setStyleSheet("font-size: 10pt; padding: 5px;")
        layout.addWidget(self.comment_box)

             
        self.submit_btn = QPushButton("Submit Review")
        self.submit_btn.setStyleSheet("padding: 10px; font-size: 12pt; background-color: #333; color: white;")
        layout.addWidget(self.submit_btn)

        self.setLayout(layout)
    

    
