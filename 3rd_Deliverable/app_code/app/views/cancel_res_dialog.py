from PySide6.QtWidgets import (
  QDialog, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
)

class CancelReservationDialog(QDialog):
  def __init__(self, club: str, date: str, event: str, parent=None):
    super().__init__(parent)
    self.setWindowTitle("Cancel Reservation??")
    self.setMinimumWidth(300)

    layout = QVBoxLayout(self)

    # Message
    message = QLabel(
      f"You are about to cancel your reservation for <b>{club}</b> on <b>{date}</b>.<br>"
      f"Event: <b>{event}</b><br><br>Are you sure?"
    )
    message.setWordWrap(True)
    layout.addWidget(message)

    # Buttons
    button_layout = QHBoxLayout()
    self.cancel_button = QPushButton("Cancel Reservation")
    self.keep_button = QPushButton("Keep Reservation")

    button_layout.addWidget(self.cancel_button)
    button_layout.addWidget(self.keep_button)

    layout.addLayout(button_layout)
