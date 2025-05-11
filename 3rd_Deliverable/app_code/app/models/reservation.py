from user import User
from table import Table
from order import Order

class Reservation:
  def __init__(
    self,
    id: int,
    user: User,
    table: Table,
    num_of_people: int,
    order: Order,
    date: datetime,
    club: 'Club',
    qrcode: 'Qrcode',
    by_user: User
  ):
    self.id = id
    self.user = user
    self.table = table
    self.num_of_people = num_of_people
    self.order = order
    self.timedate = date
    self.club = club
    self.qrcode = qrcode
    self.by_user = by_user # association