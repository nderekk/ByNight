from sqlalchemy import Column, Integer, Float , Boolean, ForeignKey, Enum as SQLAlchemyEnum
from sqlalchemy.orm import relationship
from app.data.database import Base
import app.models
from enum import Enum

class BottleType(str, Enum):
    Premium='Premium'
    Normal='Normal'
class Order(Base):
  __tablename__ = "orders"

  id = Column(Integer, primary_key=True)
  cost = Column(Float, nullable=False)
  delivered = Column(Boolean, default=False)
  paid = Column(Boolean, default=False)
  bottle_type = Column(SQLAlchemyEnum(BottleType), nullable=False)
  regular_bottles = Column(Integer, default=0)
  premium_bottles = Column(Integer, default=0)
  reservation_id = Column(Integer, ForeignKey("reservations.id"), unique=True)
  
  reservation = relationship("Reservation", back_populates="order")