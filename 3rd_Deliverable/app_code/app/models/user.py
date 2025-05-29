from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from app.data.database import Base
from app.models.role import Role
import app.models
from datetime import datetime, date

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

    
    def update_to_manager(self):
     from app.utils.container import Container
     from app.services.db_session import DatabaseSession
     from app.models.manager import Manager

     session = Container.resolve(DatabaseSession)

     
     customer_entry = session.query(app.models.Customer).filter_by(id=self.id).first()
     if customer_entry:
        session.delete(customer_entry)
        session.commit()

     
     new_manager = Manager(
        id=self.id,   
        full_name=self.full_name,
        age=self.age,
        role=Role.MANAGER,
        phone=self.phone,
        email=self.email,
        password=self.password
    )

     session.merge(new_manager)   
     session.commit() 
     return new_manager

    def verify_password(self, password: str) -> bool:
        return self.password == password
    
    def get_reservations(self):
        return self.get_upcoming_reservations_for_display(), self.get_past_reservations_for_display()
    
    def get_upcoming_reservations_for_display(self):
        upcoming = [r for r in self.reservations if r.date.date() >= date.today()]
        return upcoming
    
    def get_past_reservations_for_display(self):
        past = [r for r in self.reservations if r.date.date() < date.today()]
        return past
  