from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.data.database import Base
from app.utils.container import Container
from app.services.db_session import DatabaseSession
from sqlalchemy import distinct, and_
from sqlalchemy.orm import joinedload

class Club(Base):
  __tablename__ = "clubs"

  id = Column(Integer, primary_key=True)
  name = Column(String, unique=True, nullable=False)
  address = Column(String, nullable=False)
  location = Column(String, nullable=False)
  manager = Column(String, nullable=False)

  # Placeholder relationships — define actual classes later
  events = relationship("Event", back_populates="club", cascade="all, delete-orphan")
  tables = relationship("Table", back_populates="club", cascade="all, delete-orphan")
  reservations = relationship("Reservation", back_populates="club", cascade="all, delete-orphan")

  # staff_members = relationship("StaffMember", back_populates="club", cascade="all, delete-orphan")
  # statistics = relationship("ClubStatistics", back_populates="club", uselist=False)
  
  @classmethod
  def get_clubs_all(cls):
    session = Container.resolve(DatabaseSession)
    return session.query(Club).all()
  
  @classmethod
  def get_club_filters(cls):
    from app.models import Event
    session = Container.resolve(DatabaseSession)
    
    return {
      "location": [loc for (loc,) in session.query(distinct(Club.location)).order_by(Club.location).all()],
      "music": [music for (music,) in session.query(distinct(Event.music)).order_by(Event.music).all()],
      "event": [title for (title,) in session.query(distinct(Event.title)).order_by(Event.title).all()],
    }
    
  @classmethod
  def get_filtered_clubs(cls, address_filter: str, music_filter: str, event_filter: str):
    from app.models import Event    
    session = Container.resolve(DatabaseSession)

    query = session.query(Club).options(joinedload(Club.events))  # eager load events

    if address_filter != "Any":
      query = query.filter(Club.location == address_filter)

    if music_filter != "Any":
      query = query.join(Club.events).filter(Event.music == music_filter)

    if event_filter != "Any":
      # Rejoin if not already joined by music filter
      if music_filter == "Any":
        query = query.join(Club.events)
      query = query.filter(Event.title == event_filter)

    query = query.distinct()  # avoid duplicates when multiple events match
    return query.all()
