from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.data.database import Base

class Club(Base):
  __tablename__ = "clubs"

  id = Column(Integer, primary_key=True)
  name = Column(String, unique=True, nullable=False)
  location = Column(String, nullable=False)
  manager = Column(String, nullable=False)

  # Placeholder relationships — define actual classes later
  events = relationship("Event", back_populates="club", cascade="all, delete-orphan")
  staff_members = relationship("StaffMember", back_populates="club", cascade="all, delete-orphan")
  statistics = relationship("ClubStatistics", back_populates="club", uselist=False)
