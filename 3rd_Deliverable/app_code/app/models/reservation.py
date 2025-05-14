from app.models.table import Table
from app.models.order import Order
from datetime import datetime


class Reservation:
  def __init__(
    self,
    id: int,
    user: 'User',
    table: Table,
    num_of_people: int,
    order: Order,
    date: datetime,
    club: str,
    qrcode: str,
    event: str
  ):
    self.id = id
    self.user = user # association
    self.table = table
    self.num_of_people = num_of_people
    self.order = order
    self.date = date
    self.club = club
    self.qrcode = qrcode
    self.event = event