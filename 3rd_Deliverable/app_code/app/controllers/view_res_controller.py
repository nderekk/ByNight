from typing import Tuple
from PySide6.QtCore import QObject, Signal
from app.models.user import User
from app.views.customer_view_res import CustomerViewReservations
from datetime import datetime

class ViewReservationController(QObject):
  # Signals for view updates
  # login_successful = Signal()
  # login_failed = Signal(str)
  # signup_successful = Signal()
  # signup_failed = Signal(str)
  
  def __init__(self):
    super().__init__()
    upcoming, past = self.get_dummy_data()
    self.view = CustomerViewReservations(upcoming, past)
    self.setup_connections()
  
  def setup_connections(self):
    # Connect view signals to controller methods
    pass
  
  # mporei na min prepei na einai edw
  @staticmethod
  def get_upcoming_reservations_for_display(user: User):
    all_reservations = user.get_reservations()
    upcoming = [r for r in all_reservations if r.date > datetime.now()]
    return upcoming
  
  @staticmethod
  def get_past_reservations_for_display(user: User):
    all_reservations = user.get_reservations()
    past = [r for r in all_reservations if r.date < datetime.now()]
    return past
  
  @staticmethod
  def get_dummy_data():
    upcoming = [
      ("Saint Club", datetime(2025, 5, 30, 0, 30), "123456789", "Kultura"),
    ]

    past = [
      ("Vibe Lounge", datetime(2025, 3, 20, 22, 0), "987654321", "Retro Night"),
      ("The Garden", datetime(2025, 2, 14, 20, 0), "456789123", "Valentine's Special"),
    ]
    return upcoming, past
  
  def show(self):
    self.view.show() 