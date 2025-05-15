from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.data.database import Base

class Reservation(Base):
  __tablename__ = "reservations"

  id = Column(Integer, primary_key=True)
  user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
  table = Column(String)
  num_of_people = Column(Integer)
  order = Column(String)
  date = Column(DateTime)
  club = Column(String)
  qrcode = Column(String)
  event = Column(String)

  user = relationship("User", back_populates="reservations")
