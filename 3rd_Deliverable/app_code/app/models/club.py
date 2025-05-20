from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.data.database import Base
from app.utils.container import Container
from app.services.db_session import DatabaseSession
from sqlalchemy import distinct, and_
from sqlalchemy.orm import joinedload
from datetime import datetime

class Club(Base):
  __tablename__ = "clubs"

  id = Column(Integer, primary_key=True)
  name = Column(String, unique=True, nullable=False)
  address = Column(String, nullable=False)
  location = Column(String, nullable=False)
  manager_id = Column(Integer, ForeignKey("managers.id"), nullable=True)
  vip_available = Column(Integer, nullable=False, default=5)
  pass_available = Column(Integer, nullable=False, default=30)
  bar_available = Column(Integer, nullable=False, default=30)

  # Placeholder relationships — define actual classes later
  events = relationship("Event", back_populates="club", cascade="all, delete-orphan")
  tables = relationship("Table", back_populates="club", cascade="all, delete-orphan")
  reservations = relationship("Reservation", back_populates="club", cascade="all, delete-orphan")
  
  staff_id = Column(Integer, ForeignKey("staff.id"))
  staff = relationship("Staff", back_populates="works_at")

  # staff_members = relationship("StaffMember", back_populates="club", cascade="all, delete-orphan")
  # statistics = relationship("ClubStatistics", back_populates="club", uselist=False)
  
  manager = relationship("Manager", back_populates="managed_clubs")
  
  def get_upcoming_club_reservations(self):
    from app.models import Reservation
    session = Container.resolve(DatabaseSession)
    return session.query(Reservation).filter(
      Reservation.club_id == self.id,
      Reservation.date > datetime.now()
    ).all()
  
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
  
  def table_available(self, table_type: str) -> bool:
    mapper = {
      "bar": self.bar_available,
      "VIP": self.vip_available,
      "Pass": self.pass_available
    }
    if mapper[table_type] > 0:
      return True
    return False
  
  def get_available_table(self, table_type: str):
    
    for table in self.tables:
        if table.table_type.value == table_type and table.is_available:
            return table
    raise Exception("No available table found")
