from sqlalchemy import Column, Computed, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship
from app.data.database import Base
from app.utils.container import Container
from app.services.db_session import DatabaseSession
from datetime import datetime
import app.models

class Reservation(Base):
  __tablename__ = "reservations"

  id = Column(Integer, primary_key=True)
  user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
  club_id = Column(Integer, ForeignKey("clubs.id"), nullable=False)
  event_id = Column(Integer, ForeignKey("events.id"))
  table_id = Column(Integer, ForeignKey("tables.id")) 
  
  num_of_people = Column(Integer)
  date = Column(DateTime)
  date = Column(DateTime)
  qrcode = Column(String) # to do

  club = relationship("Club", back_populates="reservations")
  order = relationship("Order", back_populates="reservation", uselist=False, cascade="all, delete-orphan")
  user = relationship("User", back_populates="reservations")
  event = relationship("Event", back_populates="reservations")
  table = relationship("Table", back_populates="reservations")
  review = relationship("Review", back_populates="reservation", uselist=False, cascade="all, delete-orphan")

  
  @classmethod
  def create_res(cls, club, event_id: int, table_type: str, people: str, bottles: tuple[str]):
    session = Container.resolve(DatabaseSession)
    from app.models import Order, Table,TableType, User, Event
    from datetime import datetime
    event = session.get(Event, event_id)

    table = Table(
      capacity=6,
      club=club,
      table_type = TableType(table_type)
    )

    user=Container.resolve(User)
    reservation = Reservation(
      user=user,  
      club=club,
      event_id=event_id,
      table=table,
      num_of_people= people,
      date=Event.get_event_datetime(event_id),
      date=Event.get_event_datetime(event_id),
    )

    order = Order(
      cost=bottles[1]*120*(1 - event.premium_discount) + bottles[0]*80*(1 - event.regular_discount),
      reservation=reservation,
      premium_bottles=bottles[1],
      regular_bottles=bottles[0]
    )

    session.add(reservation)
    mapper = {
      "bar": "bar_available",
      "VIP": "vip_available",
      "Pass": "pass_available"
    }
    new_type = TableType(table_type)
    setattr(club, f"{new_type.lower()}_available", getattr(club, f"{new_type.lower()}_available") - 1)
    session.commit()
    return True
  
  def update_res(self, table_type: str, people: str, bottles: tuple[str]):
    from app.models import Table, Order, TableType, Event
    from app.models import Table, Order, TableType, Event
    from app.services import ReservationValidator
    session = Container.resolve(DatabaseSession)
    event = session.get(Event, self.event_id)
    bottles = [int(bottle) for bottle in bottles]

      
    mapper = {
      "bar": "bar_available",
      "VIP": "vip_available",
      "Pass": "pass_available"
    }
    old_type = self.get_table_type()
    new_type = TableType(table_type)
    setattr(self.club, f"{old_type.lower()}_available", getattr(self.club, f"{old_type.lower()}_available") + 1)
    response = ReservationValidator.check(table_type, people, bottles, self.club)
    setattr(self.club, f"{new_type.lower()}_available", getattr(self.club, f"{new_type.lower()}_available") - 1)

    if not response[0]:
      return response
    
    self.table.table_type = TableType(table_type)

    self.cost=bottles[1]*120*(1 - event.premium_discount) + bottles[0]*80*(1 - event.regular_discount)
    self.order.regular_bottles=bottles[0]
    self.order.premium_bottles=bottles[1]
    
    self.num_of_people = people
    
    print("Record Updated")
    
    session.commit()
    return response
  
  def cancel_res(self, reservation):
    session = Container.resolve(DatabaseSession)
    session.delete(reservation)
    print("Reservation Deleted")
    session.commit()
  
  def get_club(self):
    return self.club
  
  def get_club_name(self) -> str:
    return self.club.name
  
  def get_user_name(self) -> str:
    from app.models import User
    return self.user.full_name

  def get_event_name(self) -> str:
    from app.models import Event
    return self.event.title
  
  def get_event_date(self):
    from app.models import Event
    return self.event.date

  
  def get_table(self):
    from app.models import Table 
    return self.table
  
  def get_table_type(self):
    from app.models import Table, TableType
    return self.table.table_type.value
  
  @classmethod
  def get_res_from_id(cls, res_id):
    session = Container.resolve(DatabaseSession) 
    return session.get(cls, res_id)
