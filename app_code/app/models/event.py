from sqlalchemy import Column, Integer, String, Enum, Date, Time, ForeignKey, Float
from sqlalchemy.orm import relationship
from app.data.database import Base
from datetime import timedelta
import app.models

class Event(Base):
  __tablename__ = "events"
        
  id = Column(Integer, primary_key=True)
  title = Column(String, nullable=False)
  description = Column(String)
  music = Column(String)
  date = Column(Date, nullable=False)
  time = Column(Time, nullable=False)
  
  club_id = Column(Integer, ForeignKey("clubs.id"), nullable=False)
  club = relationship("Club", back_populates="events")

  regular_discount = Column(Float, default=0.0)
  premium_discount = Column(Float, default=0.0)
   
  reservations = relationship("Reservation", back_populates="event", cascade="all, delete-orphan")
  
  @classmethod
  def get_event_datetime(cls, event_id: int):
    from app.utils.container import Container
    from app.services.db_session import DatabaseSession
    session = Container.resolve(DatabaseSession)
    return session.get(cls, event_id).date
  
  @classmethod 
  def create_event(cls, title, description, music, date, time, club):
    from app.utils.container import Container
    from app.services.db_session import DatabaseSession
    session = Container.resolve(DatabaseSession)
    
    event = Event(
      title=title,
      description=description,
      music=music,
      date=date,
      time=time,
      club=club
    )
    
    session.add(event)
    session.commit()
    return True
