from app.models.role import Role
from app.models.reservation import Reservation
from app.utils.container import Container
from datetime import datetime
from typing import Tuple

class User:
  def __init__(
    self, 
    id: int,
    full_name: str,
    age: int, 
    role: Role, 
    phone: int, 
    email: str, 
    password: str,
    reservations: list[Reservation]
  ):
    if not isinstance(role, Role):
      raise ValueError(f"Invalid role: {role}")
    self.id = id
    self.full_name = full_name
    self.age = age
    self.role = role
    self.phone = phone
    self.email = email
    self.__password = password
    self.reservations = reservations # association
    
  def verify_password(self, password: str) -> bool:
    """Verify if the provided password matches the user's password."""
    return self.__password == password
    
  def get_reservations(self):
    return self.get_upcoming_reservations_for_display(), self.get_past_reservations_for_display()
    
      # mporei na min prepei na einai edw
  def get_upcoming_reservations_for_display(self):
    upcoming = [r for r in self.reservations if r.date > datetime.now()]
    return upcoming
  
  def get_past_reservations_for_display(self):
    past = [r for r in self.reservations if r.date < datetime.now()]
    return past
  