from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, 
    QScrollArea, QFrame, QHBoxLayout
)
from PySide6.QtGui import QPixmap, QCursor
from PySide6.QtCore import Qt
import sys

class ReservationApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Reservations")
        self.setMinimumSize(400, 600)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        # Header with back button
        header_layout = QHBoxLayout()
        back_btn = QPushButton("←")
        back_btn.setFixedSize(30, 30)
        back_btn.setStyleSheet("font-size: 14pt;")
        back_btn.clicked.connect(self.go_back)
        header_layout.addWidget(back_btn)
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

        # Sections
        layout.addWidget(self.section_label("Active Reservations"))
        layout.addWidget(self.reservation_card(active=True))

        layout.addWidget(self.section_label("Expired Reservations"))
        for _ in range(3):
            layout.addWidget(self.reservation_card(active=False))

        self.setLayout(layout)

    def section_label(self, text):
        label = QLabel(text)
        label.setStyleSheet("font-weight: bold; font-size: 12pt; margin-top: 15px;")
        return label

    def reservation_card(self, active=True):
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
        details_layout.addWidget(QLabel("Saint Club"))
        details_layout.addWidget(QLabel("30/5/2025 | 00:30 | ID: 123456789"))

        # Clickable event label
        event_label = QLabel('<a href="#">Event: Kultura</a>')
        event_label.setTextInteractionFlags(Qt.TextBrowserInteraction)
        event_label.setOpenExternalLinks(False)
        event_label.linkActivated.connect(self.open_event_details)
        event_label.setStyleSheet("color: #7ec8e3; font-weight: bold;")
        details_layout.addWidget(event_label)

        layout.addLayout(details_layout)

        if not active:
            review_button = QPushButton("+ Add Review")
            review_button.setCursor(QCursor(Qt.PointingHandCursor))
            review_button.setStyleSheet("background-color: #666; color: white; border-radius: 4px; padding: 4px 8px;")
            layout.addWidget(review_button)

        card.setLayout(layout)
        return card

    def open_event_details(self):
        print("Opening event details...")  # You can replace this with actual logic

    def go_back(self):
        # No pop-up, define navigation logic here if needed
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ReservationApp()
    window.show()
    sys.exit(app.exec())
