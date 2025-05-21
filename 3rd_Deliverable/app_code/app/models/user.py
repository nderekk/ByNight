from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from app.data.database import Base
from app.models.role import Role
import app.models
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    full_name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    role = Column(Enum(Role), nullable=False)
    phone = Column(Integer, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    reservations = relationship("Reservation", back_populates="user", cascade="all, delete-orphan")
    
    __mapper_args__ = {
        'polymorphic_on': role,
        'with_polymorphic': '*',  # Ensures subclass is always returned
    }

    def verify_password(self, password: str) -> bool:
        return self.password == password
    
    def get_reservations(self):
        return self.get_upcoming_reservations_for_display(), self.get_past_reservations_for_display()
    
    def get_upcoming_reservations_for_display(self):
        upcoming = [r for r in self.reservations if r.date > datetime.now()]
        return upcoming
    
    def get_past_reservations_for_display(self):
        past = [r for r in self.reservations if r.date < datetime.now()]
        return past
  