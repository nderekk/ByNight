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
  
  @staticmethod
  def get_dummy_data():
    upcoming = [
      ("Saint Club", datetime(2025, 5, 30, 0, 30), "123456789", "Kultura"),
      ("Magenta", datetime(2025, 3, 2, 0, 30), "984313241", "GREEK NIGHT"),
    ]

    past = [
      ("Vibe Lounge", datetime(2025, 3, 20, 22, 0), "987654321", "Retro Night"),
      ("The Garden", datetime(2025, 2, 14, 20, 0), "456789123", "Valentine's Special"),
    ]
    return upcoming, past
  
  def show(self):
    self.view.show() 