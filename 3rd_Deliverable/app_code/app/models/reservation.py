from sqlalchemy import Column, Computed, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.data.database import Base
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
