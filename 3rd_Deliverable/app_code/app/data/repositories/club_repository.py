from typing import Optional, Dict
from app.models.club import Club
from app.utils.container import Container
from datetime import datetime
from app.data.repositories.user_repository import UserRepository

class ClubRepository:
    def __init__(self):
        """Initialize the ReservationRepository with an empty dictionary and add dummy resevations."""
        self._clubs: Dict[str, Club] = {}  # club name -> Club mapping
        
        # Add dummy reservations
        dummy_clubs = [
            Club(1, "Navona", "Patra", "Alice"),
            Club(2, "Saint", "Patra", "Bob"),
            Club(3, "Omnia", "Patra", "Charlie")
        ]
        
        # Save dummy Reservations to the repository
        for club in dummy_clubs:
            self.save(club)
            
    def save(self, club: Club) -> Club:
        """Save a club to the in-memory dictionary."""
        self._clubs[club.name] = club
        return club

    # def find_by_email(self, email: str) -> Optional[User]:
    #     """Find a user by their email."""
    #     return self._reservations.get(email)

    def find_by_name(self, club_name: str) -> Optional[Club]:
        return self._clubs.get(club_name)

    def get_all(self) -> Optional[Club]:
        return self._clubs.values()

    # def update(self, user: User) -> User:
    #     """Update an existing user."""
    #     if user.email not in self._reservations:
    #         raise ValueError(f"User with email {user.email} not found")
    #     self._reservations[user.email] = user
    #     return user

    # def delete(self, user_id: str) -> bool:
    #     """Delete a user by their ID."""
    #     for email, user in list(self._reservations.items()):
    #         if user.id == user_id:
    #             del self._reservations[email]
    #             return True
    #     return False