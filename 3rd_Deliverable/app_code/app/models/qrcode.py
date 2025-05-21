import qrcode
from PySide6.QtGui import QPixmap, QImage
from io import BytesIO

class QRcode:
  def __init__(self, reservation_data):
    qr_string = f"{reservation_data['club_name']} | {reservation_data['date']} | ID: {reservation_data['id']}"
    self.pixmap = self.__generate_qr_pixmap(qr_string)
  
  def __generate_qr_pixmap(self, data: str) -> QPixmap:
    # Create QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=2)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Convert PIL image to QPixmap
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    qimage = QImage.fromData(buffer.getvalue(), "PNG")
    return QPixmap.fromImage(qimage)
  
  def get_qrcode(self):
    return self.pixmap