from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer
from app.models import User
from app.models.role import Role

class Manager(User):
    __tablename__ = "managers"

    id = Column(Integer, ForeignKey("users.id"), primary_key=True)

    # Relationship to managed clubs
    managed_clubs = relationship("Club", back_populates="manager", cascade="all, delete-orphan")

    __mapper_args__ = {
        "polymorphic_identity": Role.MANAGER.value,
    }

    # Manager-specific methods
    def get_managed_clubs(self):
        return self.managed_clubs

    def get_club_statistics(self):
        # Example method - implement your club statistics logic here
        stats = {}
        for club in self.managed_clubs:
            stats[club.name] = {
                "total_reservations": len(club.reservations),
                "total_staff": len(club.staff)
            }
        return stats 