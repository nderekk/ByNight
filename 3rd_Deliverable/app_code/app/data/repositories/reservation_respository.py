from typing import Optional, Dict
from app.models.reservation import Reservation
from app.models.role import Role
from app.models.user import User
from app.services.auth_service import AuthService

class ReservationRepository:
    def __init__(self):
        """Initialize the ReservationRepository with an empty dictionary and add dummy resevations."""
        self._reservations: Dict[str, Reservation] = {}  # email -> Reservation mapping
        self.auth_service = AuthService()
        
        # Add dummy reservations
        dummy_reservations = [
            Reservation(
                self,
                id=1,
                user=User,
                table: Table,
                num_of_people: int,
                order: Order,
                date: datetime,
                club: 'Club',
                qrcode: 'Qrcode'
            ),
            Reservation(
                self,
                id: int,
                user: 'User',
                table: Table,
                num_of_people: int,
                order: Order,
                date: datetime,
                club: 'Club',
                qrcode: 'Qrcode'
            ),
            Reservation(
                self,
                id: int,
                user: 'User',
                table: Table,
                num_of_people: int,
                order: Order,
                date: datetime,
                club: 'Club',
                qrcode: 'Qrcode'
            )
        ]
        
        # Save dummy Reservations to the repository
        for reservation in dummy_Reservations:
            self.save(Reservation)
            
    def save(self, user: User) -> User:
        """Save a user to the in-memory dictionary."""
        self._users[user.email] = user
        return user

    def find_by_email(self, email: str) -> Optional[User]:
        """Find a user by their email."""
        return self._users.get(email)

    def find_by_id(self, user_id: str) -> Optional[User]:
        """Find a user by their ID."""
        for user in self._users.values():
            if user.id == user_id:
                return user
        return None

    def update(self, user: User) -> User:
        """Update an existing user."""
        if user.email not in self._users:
            raise ValueError(f"User with email {user.email} not found")
        self._users[user.email] = user
        return user

    def delete(self, user_id: str) -> bool:
        """Delete a user by their ID."""
        for email, user in list(self._users.items()):
            if user.id == user_id:
                del self._users[email]
                return True
        return False