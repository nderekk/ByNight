from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel

class QRCodeDialog(QDialog):
  def __init__(self, pixmap):
    super().__init__()
    self.setWindowTitle("Reservation QR Code")
    layout = QVBoxLayout()
        
    label = QLabel()
    label.setPixmap(pixmap)
    layout.addWidget(label)

    self.setLayout(layout)
