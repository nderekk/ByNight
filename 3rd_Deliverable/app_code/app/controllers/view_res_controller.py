from app.utils.container import Container
from PySide6.QtCore import QObject, Signal
from app.models.user import User
from app.views.customer_view_res import CustomerViewReservations
from datetime import datetime

class ViewReservationsController(QObject):
  # Signals for view updates
  # login_successful = Signal()
  # login_failed = Signal(str)
  # signup_successful = Signal()
  # signup_failed = Signal(str)
  
  def __init__(self):
    super().__init__()
    # upcoming, past = self.get_dummy_data()
    self.upcoming, self.past = Container.resolve(User).get_reservations()
    self.fomrat_for_card()
    self.view = CustomerViewReservations(self.upcoming, self.past)
    self.setup_connections()
  
  def setup_connections(self):
    # Connect view signals to controller methods
    pass
  
  def fomrat_for_card(self):
    self.upcoming = [(r.club, r.date, r.id, r.event) for r in self.upcoming]
    self.past = [(r.club, r.date, r.id, r.event) for r in self.past]
  
  def show(self):
    self.view.show() 