from sqlalchemy import Column, Integer, String, Enum, Date, Time, ForeignKey
from sqlalchemy.orm import relationship
from app.data.database import Base
import app.models

class Event(Base):
  __tablename__ = "events"
        
  id = Column(Integer, primary_key=True)
  title = Column(String, nullable=False)
  description = Column(String)
  date = Column(Date, nullable=False)
  time = Column(Time, nullable=False)
  
  club_id = Column(Integer, ForeignKey("clubs.id"), nullable=False)
  club = relationship("Club", back_populates="events")
   
  reservations = relationship("Reservation", back_populates="event", cascade="all, delete-orphan")     