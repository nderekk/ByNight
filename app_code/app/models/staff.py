from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from app.models import User
from app.models.role import Role

class Staff(User):
    __tablename__ = "staff"

    id = Column(Integer, ForeignKey("users.id"), primary_key=True)

    # One-to-one relationship with Club
    works_at = relationship("Club", back_populates="staff", uselist=False)

    __mapper_args__ = {
        "polymorphic_identity": Role.STAFF,
    }

    # Extra method
    def get_upcoming_club_reservations(self) -> list[dict]:
        print(f"\n{self.works_at}\n")
        if not self.works_at:
            return []
        return self.works_at.get_upcoming_club_reservations()