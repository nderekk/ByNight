from PySide6.QtWidgets import (
  QWidget, QVBoxLayout, QLabel, QPushButton,
  QHBoxLayout, QFrame, QSpacerItem, QSizePolicy
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QCursor

class ReservationDetailsPage(QWidget):
  def __init__(self, res_details: dict[str, str]):
    super().__init__()
    self.res_details = res_details
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

    # Details section
    self.details_card = QFrame()
    self.details_card.setStyleSheet("background-color: #444; color: white; border-radius: 8px; padding: 12px;")
    self.card_layout = QVBoxLayout()
    self.card_layout.setSpacing(4)
    self.details_card.setLayout(self.card_layout)
    layout.addWidget(self.details_card)

    self.populate_details()

    layout.addSpacerItem(QSpacerItem(0, 10, QSizePolicy.Minimum, QSizePolicy.Expanding))

    # Modify and Cancel buttons
    self.modify_btn = QPushButton("Modify Reservation")
    self.cancel_btn = QPushButton("Cancel Reservation")

    for btn in (self.modify_btn, self.cancel_btn):
      btn.setCursor(QCursor(Qt.PointingHandCursor))
      btn.setStyleSheet("background-color: #666; color: white; border-radius: 5px; padding: 10px; font-size: 11pt;")
      btn.setMinimumHeight(40)
      layout.addWidget(btn)

    self.setLayout(layout)

  def populate_details(self):
    # Clear existing widgets
    while self.card_layout.count():
      child = self.card_layout.takeAt(0)
      if child.widget():
        child.widget().deleteLater()

    # Re-add labels
    def add_detail(label, value):
      lbl = QLabel(f"<b>{label}:</b> {value}")
      lbl.setStyleSheet("font-size: 10pt;")
      self.card_layout.addWidget(lbl)

    d = self.res_details
    add_detail("Club", d.get("Club", "N/A"))
    add_detail("Reservation ID", d.get("Reservation ID", "N/A"))
    add_detail("User", d.get("User", "N/A"))
    add_detail("Event", d.get("Event", "N/A") or "N/A")
    add_detail("Table No", d.get("Table No", "N/A") or "N/A")
    add_detail("Number of People", d.get("Number of People", "N/A"))
    add_detail("Date", d.get("Date", "N/A") or "N/A")

  def refresh_details(self, res_details: dict[str, str]):
    self.res_details = res_details
    self.populate_details()
