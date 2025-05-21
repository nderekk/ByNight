from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer
from app.models import User
from app.models.role import Role

class Customer(User):
    __tablename__ = "customers"

    id = Column(Integer, ForeignKey("users.id"), primary_key=True)

    __mapper_args__ = {
        "polymorphic_identity": Role.CUSTOMER,
    }

    # Customer-specific methods can be added here
    def get_loyalty_points(self) -> int:
        # Example method - implement your loyalty system logic here
        return len(self.get_past_reservations_for_display()) 