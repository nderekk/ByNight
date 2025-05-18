from sqlalchemy import Column, Computed, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.data.database import Base
from app.utils.container import Container
from app.services.db_session import DatabaseSession
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
  qrcode = Column(String) # to do

  club = relationship("Club", back_populates="reservations")
  order = relationship("Order", back_populates="reservation", uselist=False, cascade="all, delete-orphan")
  user = relationship("User", back_populates="reservations")
  event = relationship("Event", back_populates="reservations")
  table = relationship("Table", back_populates="reservations")
  
  def get_club_name(self) -> str:
    return self.club.name
  
  def get_user_name(self) -> str:
    from app.models import User
    return self.user.full_name

  def get_event_name(self) -> str:
    from app.models import Event
    return self.event.title
  
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
