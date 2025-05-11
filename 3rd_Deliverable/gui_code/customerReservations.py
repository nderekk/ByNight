from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QScrollArea, QFrame, QHBoxLayout
from PySide6.QtGui import QPixmap
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
        layout.addWidget(self.section_label("Upcoming Reservations"))
        layout.addWidget(self.reservation_card(upcoming=True))

        layout.addWidget(self.section_label("Past Reservations"))
        for _ in range(3):
            layout.addWidget(self.reservation_card(upcoming=False))

        self.setLayout(layout)

    def section_label(self, text):
        label = QLabel(text)
        label.setStyleSheet("font-weight: bold; font-size: 12pt; margin-top: 15px;")
        return label

    def reservation_card(self, upcoming=True):
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
        details_layout.addWidget(QLabel("Saint Club"))
        details_layout.addWidget(QLabel("30/5/2025 | 00:30 | ID: 123456789"))
        details_layout.addWidget(QLabel("Event: Kultura"))

        layout.addLayout(details_layout)

        if not upcoming:
            review_button = QPushButton("+ Add Review")
            layout.addWidget(review_button)

        card.setLayout(layout)
        return card


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ReservationApp()
    window.show()
    sys.exit(app.exec())
