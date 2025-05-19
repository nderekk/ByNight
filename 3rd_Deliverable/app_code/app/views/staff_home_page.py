from PySide6.QtWidgets import (
  QWidget, QVBoxLayout, QLabel, QScrollArea, QFrame,
  QCheckBox, QHBoxLayout, QPushButton
)
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QIcon


class ReservationCard(QFrame):
  def __init__(self, reservation_id: int, full_name: str):
    super().__init__()
    self.reservation_id = reservation_id
    self.full_name = full_name

    self.setFrameShape(QFrame.Box)
    self.setStyleSheet("background-color: #222; color: white; border-radius: 8px;")
    self.setFixedHeight(60)

    layout = QHBoxLayout()
    layout.setContentsMargins(10, 5, 10, 5)

    info_label = QLabel(f"ID: {reservation_id} | {full_name}")
    info_label.setStyleSheet("font-size: 11pt;")
    layout.addWidget(info_label)

    layout.addStretch()

    self.checkbox = QCheckBox()
    layout.addWidget(self.checkbox)

    self.setLayout(layout)


class StaffHomePage(QWidget):
  camera_clicked = Signal()  # ✅ Signal for camera icon

  def __init__(self, reservations: list[dict]):
    super().__init__()
    self.setWindowTitle("Staff Home Page")
    self.cards = {}  # ✅ Dictionary to keep track of cards
    self.setup_ui(reservations)

  def setup_ui(self, reservations):
    layout = QVBoxLayout(self)

    # Header with title and camera button
    header_layout = QHBoxLayout()
    title = QLabel("Tonight's Reservations")
    title.setStyleSheet("font-weight: bold; font-size: 18pt; margin: 10px 0;")

    camera_btn = QPushButton("📷")
    camera_btn.setFixedSize(32, 32)
    camera_btn.setCursor(Qt.PointingHandCursor)
    camera_btn.setStyleSheet("border: none; font-size: 18pt;")
    camera_btn.clicked.connect(self.camera_clicked.emit)

    header_layout.addWidget(title)
    header_layout.addStretch()
    header_layout.addWidget(camera_btn)

    layout.addLayout(header_layout)

    # Scroll area for reservations
    scroll_area = QScrollArea()
    scroll_area.setWidgetResizable(True)
    scroll_area.setStyleSheet("border: none;")

    content_widget = QWidget()
    content_layout = QVBoxLayout(content_widget)
    content_layout.setSpacing(10)

    for res in reservations:
      card = ReservationCard(res['id'], res['full_name'])
      self.cards[res['id']] = card  # ✅ Store reference
      content_layout.addWidget(card)

    content_layout.addStretch()
    scroll_area.setWidget(content_widget)
    layout.addWidget(scroll_area)
