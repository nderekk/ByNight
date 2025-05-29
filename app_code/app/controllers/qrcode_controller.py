from PySide6.QtCore import QObject
from app.models import Reservation, QRcode
from app.views import QRCodeDialog

class QRcodeController(QObject):
  def __init__(self, reservation: Reservation, show_page: callable):
    super().__init__()
    self.reservation = reservation
    self.show_page = show_page
    reservation_data = {
      'club_name': self.reservation.get_club_name,
      'date': self.reservation.date,
      'id': reservation.id
    }
    self.__qr_pixmap = QRcode(reservation_data).get_qrcode()
    self.__show_qr()
    
  def __show_qr(self):
    QRCodeDialog(self.__qr_pixmap).exec()
    

    