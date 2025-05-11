from app.models.user import User
from datetime import datetime

class ViewReservationController:
  def get_upcoming_reservations_for_display(user: User):
    all_reservations = user.get_reservations()
    upcoming = [r for r in all_reservations if r.date > datetime.now()]
    return upcoming
  
  def get_past_reservations_for_display(user: User):
    all_reservations = user.get_reservations()
    past = [r for r in all_reservations if r.date < datetime.now()]
    return past