from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QScrollArea, QFrame, QHBoxLayout
from PySide6.QtGui import QPixmap, QCursor, QMouseEvent
from PySide6.QtCore import Qt, Signal, QDateTime
from datetime import datetime


class ClickableReservationCard(QFrame):
    clicked = Signal(object)  

    def __init__(self, reservation_data, card_widget):
        super().__init__()
        self.reservation_data = reservation_data
        self.setLayout(card_widget.layout())  # use the passed layout from original card
        self.setStyleSheet("background-color: #444; color: white; border-radius: 5px;")
        self.setCursor(QCursor(Qt.PointingHandCursor))

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.clicked.emit(self.reservation_data)


class CustomerViewReservations(QWidget):
    reservation_clicked = Signal(int)
    review_button_clicked = Signal(int)  # NEW SIGNAL for review buttons 

    def __init__(self, upcoming_reservations: list, past_reservations: list):
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
        subtitle = QLabel("Observe your reservations any time and don't forget to leave a review within 30 days.")
        subtitle.setWordWrap(True)
        subtitle.setStyleSheet("color: gray; font-size: 10pt;")
        layout.addWidget(subtitle)

        # Upcoming Reservations Scroll Area
        layout.addWidget(self.section_label("Upcoming Reservations"))
        upcoming_container = QWidget()
        upcoming_layout = QVBoxLayout()
        for reservation in self.upcoming_reservations:
            card = self.reservation_card(*reservation, upcoming=True)
            upcoming_layout.addWidget(card)
        upcoming_layout.addStretch()
        upcoming_container.setLayout(upcoming_layout)

        upcoming_scroll = QScrollArea()
        upcoming_scroll.setWidgetResizable(True)
        upcoming_scroll.setWidget(upcoming_container)
        upcoming_scroll.setFixedHeight(250)
        layout.addWidget(upcoming_scroll)

        # Past Reservations Scroll Area
        layout.addWidget(self.section_label("Past Reservations"))
        past_container = QWidget()
        past_layout = QVBoxLayout()
        for reservation in self.past_reservations:
            card = self.reservation_card(*reservation, upcoming=False)
            past_layout.addWidget(card)
        past_layout.addStretch()
        past_container.setLayout(past_layout)

        past_scroll = QScrollArea()
        past_scroll.setWidgetResizable(True)
        past_scroll.setWidget(past_container)
        past_scroll.setFixedHeight(250)
        layout.addWidget(past_scroll)

        self.setLayout(layout)

    def section_label(self, text):
        label = QLabel(text)
        label.setStyleSheet("font-weight: bold; font-size: 12pt; margin-top: 15px;")
        return label

    def reservation_card(self, club_name: str, date: datetime, id: int, event: str, upcoming: bool):
        # Create the original card layout
        card = QFrame()
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
        layout.addLayout(details_layout)

        if not upcoming:
            review_button = QPushButton("+ Add Review")
            review_button.setCursor(QCursor(Qt.PointingHandCursor))
            review_button.setStyleSheet("""
                padding: 10px;
                font-size: 12pt;
                background-color: #111;
                color: white;
                border-radius: 8px;
            """)
            review_button.setFixedWidth(180)
            review_button.clicked.connect(lambda _, res_id=id: self.review_button_clicked.emit(res_id))
            layout.addWidget(review_button)

        card.setLayout(layout)

        # Only make upcoming reservations clickable
        if upcoming:
            clickable = ClickableReservationCard(
                reservation_data={"club_name": club_name, "date": date, "id": id, "event": event, "upcoming": upcoming},
                card_widget=card
            )
            clickable.clicked.connect(self.handle_card_click)
            return clickable
        else:
            # For past reservations, just return the regular card
            card.setStyleSheet("background-color: #444; color: white; border-radius: 5px;")
            return card

    def handle_card_click(self, reservation_data):
        print("Reservation clicked:", reservation_data)
        self.reservation_clicked.emit(reservation_data["id"])
