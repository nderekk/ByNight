from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QScrollArea, QFrame, QHBoxLayout
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import sys
from datetime import datetime

class CustomerViewReservations(QWidget):
    def __init__(self, upcoming_reservations, past_reservations):
        super().__init__()
        self.upcoming_reservations = upcoming_reservations
        self.past_reservations = past_reservations
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        # Title
        title = QLabel("Reservations")
        title.setStyleSheet("font-weight: bold; font-size: 18pt;")
        layout.addWidget(title)

        # Subtitle
        subtitle = QLabel("Observe your reservations any time and don’t forget to leave a review within 30 days.")
        subtitle.setWordWrap(True)
        subtitle.setStyleSheet("color: gray; font-size: 10pt;")
        layout.addWidget(subtitle)

        # Upcoming
        layout.addWidget(self.section_label("Upcoming Reservations"))
        for reservation in self.upcoming_reservations:
            layout.addWidget(self.reservation_card(*reservation, upcoming=True))

        # Past
        layout.addWidget(self.section_label("Past Reservations"))
        for reservation in self.past_reservations:
            layout.addWidget(self.reservation_card(*reservation, upcoming=False))

        self.setLayout(layout)

    def section_label(self, text):
        label = QLabel(text)
        label.setStyleSheet("font-weight: bold; font-size: 12pt; margin-top: 15px;")
        return label

    def reservation_card(self, club_name: str, date: datetime, id: int, event: str, upcoming=True):
        card = QFrame()
        card.setStyleSheet("background-color: #444; color: white; border-radius: 5px;")
        card.setFixedHeight(80)
        layout = QHBoxLayout()

        # Image (placeholder)
        pixmap = QPixmap(50, 50)
        pixmap.fill(Qt.black)
        image = QLabel()
        image.setPixmap(pixmap)
        layout.addWidget(image)

        # Texts
        details_layout = QVBoxLayout()
        details_layout.addWidget(QLabel(club_name))
        details_layout.addWidget(QLabel(f"{date.strftime('%d/%m/%Y')} | {date.strftime('%H:%M')} | ID: {id}"))
        details_layout.addWidget(QLabel(f"Event: {event}"))

        layout.addLayout(details_layout)

        if not upcoming:
            review_button = QPushButton("+ Add Review")
            layout.addWidget(review_button)

        card.setLayout(layout)
        return card

