from PySide6.QtCore import QObject, Signal
from app.models import Staff
from app.views import StaffHomePage, MessagePopup
from app.utils import Container

class StaffHomePageController(QObject):
  def __init__(self, show_page: callable):
    super().__init__()
    self.show_page = show_page
    self.user = Container.resolve(Staff)
    reservations = self.user.get_upcoming_club_reservations()
    print(reservations)
    reservations_data = [
      {
        "id": res.id,
        "full_name": self.user.full_name
      } 
      for res in reservations
    ] 
    # reservations_data = [
    # {"id": 1, "full_name": "Alice Johnson"},
    # {"id": 102, "full_name": "Bob Smith"},
    # {"id": 103, "full_name": "Carla Gomez"},
    # ]
    self.view = StaffHomePage(reservations_data)
    self.setup_connections()

  def setup_connections(self):
    self.view.camera_clicked.connect(self.handle_qrcode)
    
  def handle_qrcode(self):
    from app.utils import decode_qr
    detected_id = decode_qr()
    if detected_id in self.view.cards.keys() and detected_id != -1:
      card = self.view.cards.get(detected_id)
      if card:
        card.checkbox.setChecked(True)
        popup = MessagePopup(success=True, message=f"Reservation {detected_id}\nChecked In")
        popup.exec()
        # TODO notification code
        