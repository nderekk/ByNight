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
    self.keep_button = QPushButton("Keep Reservation")
    self.cancel_button = QPushButton("Cancel Reservation")

    # Set "Keep Reservation" as default
    self.keep_button.setDefault(True)

    # Button styles
    self.keep_button.setStyleSheet("background-color: #5cb85c; color: white;")  # green
    self.cancel_button.setStyleSheet("background-color: #f8d7da; color: #333;") # subtle gray
    self.keep_button.setStyleSheet("""
        QPushButton {
          background-color: #5cb85c; color: white;
        }
        QPushButton:hover {
          background-color: #4cae4c;
        }
      """)


    button_layout.addWidget(self.keep_button)
    button_layout.addWidget(self.cancel_button)

    layout.addLayout(button_layout)

    # Connect buttons
    self.keep_button.clicked.connect(self.reject)
    self.cancel_button.clicked.connect(self.accept)
