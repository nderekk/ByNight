from role import Role
from reservation import Reservation

class User:
  
  def __init__(
      self, 
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
    self.full_name = full_name
    self.age = age
    self.role = role
    self.phone = phone
    self.email = email
    self.__password = password
    self.reservations = reservations
    
    
  def get_reservations():
    pass
  