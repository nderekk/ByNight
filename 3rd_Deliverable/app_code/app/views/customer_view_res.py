from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QScrollArea, QFrame, QHBoxLayout
from PySide6.QtGui import QPixmap, QCursor
from PySide6.QtCore import Qt
from datetime import datetime

class CustomerViewReservations(QWidget):
    def __init__(self, upcoming_reservations: str, past_reservations: str):
        super().__init__()
        self.upcoming_reservations = upcoming_reservations
        self.past_reservations = past_reservations
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        # Header with back button
        header_layout = QHBoxLayout()
        self.back_btn = QPushButton("←")
        self.back_btn.setFixedSize(30, 30)
        self.back_btn.setStyleSheet("font-size: 14pt;")
        header_layout.addWidget(self.back_btn)
        header_layout.addStretch()
        layout.addLayout(header_layout)

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
        card.setFixedHeight(100)
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

        # # Clickable event label
        # event_label = QLabel(f'<a href="#">Event: {event}</a>')
        # event_label.setTextInteractionFlags(Qt.TextBrowserInteraction)
        # event_label.setOpenExternalLinks(False)
        # event_label.linkActivated.connect(self.open_event_details)
        # event_label.setStyleSheet("color: #7ec8e3; font-weight: bold;")
        # details_layout.addWidget(event_label)

        layout.addLayout(details_layout)

        if not upcoming:
            review_button = QPushButton("+ Add Review")
            review_button.setCursor(QCursor(Qt.PointingHandCursor))
            review_button.setStyleSheet("background-color: #666; color: white; border-radius: 4px; padding: 4px 8px;")
            layout.addWidget(review_button)

        card.setLayout(layout)
        return card

    def open_event_details(self):
        print("Opening event details...")  # You can replace this with actual logic
        

