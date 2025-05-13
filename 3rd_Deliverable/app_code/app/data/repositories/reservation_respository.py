from typing import Optional, Dict
from app.models.reservation import Reservation
from app.utils.container import Container
from datetime import datetime
from app.data.repositories.user_repository import UserRepository

class ReservationRepository:
    def __init__(self):
        """Initialize the ReservationRepository with an empty dictionary and add dummy resevations."""
        self._reservations: Dict[int, Reservation] = {}  # reservation id -> Reservation mapping
        self.find_user = Container.resolve(UserRepository).find_by_email
        
        # Add dummy reservations
        dummy_reservations = [
              Reservation(
                id=9432,
                user= self.find_user('john@example.com'),
                table = 'No 26',
                num_of_people= 4,
                order= 'Order',
                date= datetime.now(tz=None),
                club= 'MAGENTA',
                qrcode= 'Qrcode',
                event= 'GREEK NIGHT'
            ),
            Reservation(
                id=2321,
                user= self.find_user('john@example.com'),
                table = 'No 12',
                num_of_people= 2,
                order= 'Order',
                date= datetime.now(tz=None),
                club= 'SAINT',
                qrcode= 'Qrcode',
                event= 'Lules culpa'
            ),
            Reservation(
                id=1123,
                user= self.find_user('john@example.com'),
                table = 'No 23',
                num_of_people= 3,
                order= 'Order',
                date= datetime.now(tz=None),
                club= 'OMNIA',
                qrcode= 'Qrcode',
                event= 'Trap Night'
            )
        ]
        
        # Save dummy Reservations to the repository
        for reservation in dummy_reservations:
            self.save(reservation)
            
    def save(self, reservation: Reservation) -> Reservation:
        """Save a user to the in-memory dictionary."""
        self._reservations[reservation.id] = reservation
        return reservation

    # def find_by_email(self, email: str) -> Optional[User]:
    #     """Find a user by their email."""
    #     return self._reservations.get(email)

    def find_by_id(self, res_id: int) -> Optional[Reservation]:
        """Find a user by their ID."""
        for res in self._reservations.values():
            if res.id == res_id:
                return res
        return None

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