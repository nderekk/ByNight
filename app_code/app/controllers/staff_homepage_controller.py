from PySide6.QtCore import QObject, Signal
from app.models import User, Reservation
from app.views import StaffHomePage, MessagePopup
from app.utils import Container

class StaffHomePageController(QObject):
  def __init__(self, show_page: callable):
    super().__init__()
    self.show_page = show_page
    self.user = Container.resolve(User)
    print(self.user.full_name)
    reservations = self.user.get_upcoming_club_reservations()
    reservations_data = [
      {
        "id": res.id,
        "full_name": res.get_user_name()
      } 
      for res in reservations
    ] 
    self.view = StaffHomePage(self.user.works_at.name, reservations_data)
    self.setup_connections()

  def setup_connections(self):
    self.view.camera_clicked.connect(self.handle_scanqrcode)
    
  def handle_scanqrcode(self):
    from app.utils import decode_qr
    detected_id = decode_qr()
    if detected_id in self.view.cards.keys() and detected_id != -1:
      card = self.view.cards.get(detected_id)
      res = Reservation.get_res_from_id(detected_id)
      if card:
        card.checkbox.setChecked(True)
        MessagePopup(success=True, message=f"ID: {detected_id} | {res.get_user_name()}\nChecked In")
        # TODO notification code
        