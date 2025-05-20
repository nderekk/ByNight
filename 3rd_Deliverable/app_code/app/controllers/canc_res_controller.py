from PySide6.QtCore import QObject, Signal
from app.utils.container import Container
from app.models import Reservation
from app.views import CancelReservationDialog, MessagePopup

class CancelReservationController(QObject):
  def __init__(self, res_id: int, show_page: callable):
    super().__init__()
    self.res_id = res_id
    self.reservation = Reservation.get_res_from_id(res_id)
    self.show_page = show_page
    self.view = CancelReservationDialog(self.reservation.get_club_name(), self.reservation.date, self.reservation.get_event_name())
    self.setup_connections()
    self.cancelation_procedure()
    
  def setup_connections(self):
    self.view.cancel_button.clicked.connect(self.confirm_cancellation)
    self.view.keep_button.clicked.connect(self.abort)
  
  def cancelation_procedure(self):
    from app.services import ReservationValidator
    allowed = ReservationValidator.is_cancellable(self.reservation.date)
    if allowed:
      self.view.exec()
    else:
      popup = MessagePopup(success=False, message="Cancellations less than 2 hours before are prohibited!")
      popup.exec()
  
  def confirm_cancellation(self):
    self.reservation.cancel_res(self.reservation)
    
    popup = MessagePopup(success=True, message="Your Reservation has been Cancelled.\nWe're Sorry to see you go :(")
    popup.exec()
    
    from app.controllers import ViewReservationsController
    self.controller = ViewReservationsController(self.show_page)
    self.show_page('view_res_controller', self.controller)    
  
  def abort(self):
    pass