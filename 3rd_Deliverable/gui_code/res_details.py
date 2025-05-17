from PySide6.QtWidgets import (
  QWidget, QVBoxLayout, QLabel, QPushButton,
  QHBoxLayout, QFrame, QSpacerItem, QSizePolicy
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QCursor
from datetime import datetime

class ReservationDetailsPage(QWidget):
  def __init__(self, reservation):
    super().__init__()
    self.reservation = reservation
    self.setup_ui()

  def setup_ui(self):
    layout = QVBoxLayout()

    # Header with back and QR buttons
    header_layout = QHBoxLayout()
    self.back_btn = QPushButton("←")
    self.back_btn.setFixedSize(30, 30)
    self.back_btn.setStyleSheet("font-size: 14pt;")
    header_layout.addWidget(self.back_btn)

    header_layout.addStretch()

    self.qr_btn = QPushButton("Show QR Code")
    self.qr_btn.setCursor(QCursor(Qt.PointingHandCursor))
    self.qr_btn.setStyleSheet(
      "background-color: #666; color: white; border-radius: 5px; padding: 6px 10px; font-size: 10pt;"
    )
    header_layout.addWidget(self.qr_btn)
    layout.addLayout(header_layout)

    # Title
    title = QLabel("Reservation Details")
    title.setStyleSheet("font-weight: bold; font-size: 18pt;")
    layout.addWidget(title)

    # Reservation Details Section
    details_card = QFrame()
    details_card.setStyleSheet("background-color: #444; color: white; border-radius: 8px; padding: 12px;")
    card_layout = QVBoxLayout()
    card_layout.setSpacing(4)  # Smaller gap between detail labels

    def add_detail(label, value):
      lbl = QLabel(f"<b>{label}:</b> {value}")
      lbl.setStyleSheet("font-size: 10pt;")
      card_layout.addWidget(lbl)

    add_detail("Reservation ID", self.reservation.id)
    add_detail("User ID", self.reservation.user_id)
    add_detail("Club ID", self.reservation.club_id)
    add_detail("Event ID", self.reservation.event_id or "N/A")
    add_detail("Table ID", self.reservation.table_id or "N/A")
    add_detail("Number of People", self.reservation.num_of_people)
    add_detail("Date", self.reservation.date.strftime('%d/%m/%Y %H:%M') if self.reservation.date else "N/A")
    add_detail("QR Code", self.reservation.qrcode or "Not generated")

    details_card.setLayout(card_layout)
    layout.addWidget(details_card)

    layout.addSpacerItem(QSpacerItem(0, 10, QSizePolicy.Minimum, QSizePolicy.Expanding))

    # Modify and Cancel buttons (full-width)
    self.modify_btn = QPushButton("Modify Reservation")
    self.cancel_btn = QPushButton("Cancel Reservation")

    for btn in (self.modify_btn, self.cancel_btn):
      btn.setCursor(QCursor(Qt.PointingHandCursor))
      btn.setStyleSheet("background-color: #666; color: white; border-radius: 5px; padding: 10px; font-size: 11pt;")
      btn.setMinimumHeight(40)
      layout.addWidget(btn)

    self.setLayout(layout)



# Dummy reservation object simulating a SQLAlchemy-like instance
class DummyReservation:
    def __init__(self):
        self.id = 101
        self.user_id = 5
        self.club_id = 3
        self.event_id = 12
        self.table_id = 7
        self.num_of_people = 4
        self.date = datetime(2025, 6, 10, 21, 30)
        self.qrcode = "sample_qrcode_data"

if __name__ == "__main__":
    app = QApplication(sys.argv)

    reservation = DummyReservation()
    window = ReservationDetailsPage(reservation)
    window.setWindowTitle("Reservation Details")
    window.resize(400, 500)
    window.show()

    sys.exit(app.exec())
