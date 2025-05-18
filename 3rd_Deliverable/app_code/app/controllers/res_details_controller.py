from PySide6.QtCore import QObject, Signal
from app.utils.container import Container
from app.views import ReservationDetailsPage
from app.models import Reservation

class ReservationDetailsController(QObject):
  def __init__(self, res_id: int, show_page: callable):
    super().__init__()
    self.reservation = Reservation.get_res_from_id(res_id)
    self.show_page = show_page
    self.view = ReservationDetailsPage(self.format_res_details())
    self.setup_connections()
    
  def setup_connections(self):
    self.view.back_btn.clicked.connect(self.handle_back)
  
  def format_res_details(self):
    details = {
      "Club": self.reservation.get_club_name(),
      "Reservation ID": self.reservation.id,
      "User": self.reservation.get_user_name(),
      "Event": self.reservation.get_event_name(),
      "Table No": self.reservation.id,
      "Number of People": self.reservation.num_of_people,
      "Date": self.reservation.date.strftime('%d/%m/%Y %H:%M')
    }
    return details
  
  def set_reservation(self, id: int):
    self.reservation = Reservation.get_res_from_id(id)
    self.view.refresh_details(self.format_res_details())
  
  def handle_back(self):
    from app.controllers import ViewReservationsController
        
    self.controller = Container.resolve(ViewReservationsController)
    self.show_page('view_res_controller', self.controller)