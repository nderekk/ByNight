from PySide6.QtWidgets import (
  QDialog, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
)
from PySide6.QtCore import Qt

class CancelReservationDialog(QDialog):
  def __init__(self, club: str, date: str, event: str, parent=None):
    super().__init__(parent)
    self.setWindowTitle("Cancel Reservation")
    self.setMinimumWidth(300)

    layout = QVBoxLayout(self)

    # Message
    message = QLabel(
      f"You are about to cancel your reservation for <b>{club}</b> on <b>{date}</b>.<br>"
      f"Event: <b>{event}</b><br><br>Are you sure?"
    )
    message.setWordWrap(True)
    message.setAlignment(Qt.AlignCenter)
    layout.addWidget(message)

    # Buttons
    button_layout = QHBoxLayout()
    self.cancel_button = QPushButton("Cancel Reservation")
    self.keep_button = QPushButton("Keep Reservation")

    # Button styles
    self.cancel_button.setStyleSheet("background-color: #d9534f; color: white;")
    self.keep_button.setStyleSheet("background-color: #5bc0de; color: white;")

    button_layout.addWidget(self.cancel_button)
    button_layout.addWidget(self.keep_button)

    layout.addLayout(button_layout)

    # Optional: connect button signals
    self.cancel_button.clicked.connect(self.accept)
    self.keep_button.clicked.connect(self.reject)
