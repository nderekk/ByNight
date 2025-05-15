from sqlalchemy import Column, Integer, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.data.database import Base
import app.models

class Order(Base):
  __tablename__ = "orders"

  id = Column(Integer, primary_key=True)
  cost = Column(Float, nullable=False)
  delivered = Column(Boolean, default=False)
  paid = Column(Boolean, default=False)
  reservation_id = Column(Integer, ForeignKey("reservations.id"), unique=True)
  
  reservation = relationship("Reservation", back_populates="order")