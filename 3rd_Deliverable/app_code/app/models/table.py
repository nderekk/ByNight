from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.data.database import Base
import app.models


class Table(Base):
  __tablename__ = "tables"

  id = Column(Integer, primary_key=True)
  capacity = Column(Integer, nullable=False)
  min_order = Column(Float, nullable=False)

  # Assuming a club owns tables
  club_id = Column(Integer, ForeignKey("clubs.id"), nullable=False)
  club = relationship("Club", back_populates="tables")

  reservations = relationship("Reservation", back_populates="table", cascade="all, delete-orphan")
