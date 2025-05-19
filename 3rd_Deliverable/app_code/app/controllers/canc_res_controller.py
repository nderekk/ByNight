from PySide6.QtCore import QObject, Signal
from app.utils.container import Container
from app.models import Reservation
from app.views import CancelReservationDialog

class CancelReservationController(QObject):
  def __init__(self, res_id: int, show_page: callable):
    super().__init__()
    self.res_id = res_id
    self.reservation = Reservation.get_res_from_id(res_id)
    self.show_page = show_page
    self.begin_cancelation_procedure()
    self.setup_connections()
    
  def setup_connections(self):
    self.view.cancel_button.clicked.connect(self.confirm_cancellation)   # You can change this to emit a signal
    self.view.keep_button.clicked.connect(self.abort)
  
  def begin_cancelation_procedure(self):
    self.view = CancelReservationDialog(self.reservation.get_club_name(), self.reservation.date, self.reservation.get_event_name())
  
  def confirm_cancellation(self):
    print("CNANCELLED")
    # self.reservation.cancel()
  
  def abort(self):
    pass