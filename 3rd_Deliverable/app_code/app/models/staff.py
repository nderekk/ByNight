from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from app.models import User
from app.models.role import Role

class Staff(User):
    __tablename__ = "staff"

    id = Column(Integer, ForeignKey("users.id"), primary_key=True)

    # New relationship example
    works_at = relationship("Club", back_populates="staff")

    __mapper_args__ = {
        "polymorphic_identity": Role.STAFF.value,
    }

    # Extra method
    def get_upcoming_club_reservations(self) -> list[dict]:
        return self.works_at.get_club_reservations()