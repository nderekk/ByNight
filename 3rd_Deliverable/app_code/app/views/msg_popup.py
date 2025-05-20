from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton
from PySide6.QtCore import Qt

class MessagePopup(QDialog):
  def __init__(self, success: bool, message: str):
    super().__init__()
    self.setWindowTitle("Notification")
    self.setFixedSize(300, 150)
    self.setModal(True)

    layout = QVBoxLayout()

    # Main result label (Success / Failure)
    result_label = QLabel("Success!" if success else "Failure")
    result_label.setAlignment(Qt.AlignCenter)
    result_label.setStyleSheet(f"""
      font-size: 16pt;
      font-weight: bold;
      color: {'#4CAF50' if success else '#F44336'};
    """)
    layout.addWidget(result_label)

    # Custom message
    msg_label = QLabel(message)
    msg_label.setWordWrap(True)
    msg_label.setAlignment(Qt.AlignCenter)
    msg_label.setStyleSheet("font-size: 10pt; color: white;")
    layout.addWidget(msg_label)

    # OK button
    ok_btn = QPushButton("OK")
    ok_btn.setStyleSheet("padding: 6px 12px; background-color: #666; color: white; border-radius: 4px;")
    ok_btn.clicked.connect(self.accept)
    layout.addWidget(ok_btn, alignment=Qt.AlignCenter)

    self.setLayout(layout)
    self.setStyleSheet("background-color: #333;")
