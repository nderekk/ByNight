from typing import Optional, Dict
from app.models.user import User
from app.models.role import Role
from app.models.reservation import Reservation
from app.utils.container import Container
from datetime import datetime

class UserRepository:
    def __init__(self):
        """Initialize the UserRepository with an empty dictionary and add dummy users."""
        self._users: Dict[str, User] = {}  # email -> User mapping
        
        dummy_reservations = [
              Reservation(
                id=9432,
                user= self.find_by_email('john@example.com'),
                table = 'No 26',
                num_of_people= 4,
                order= 'Order',
                date= datetime(2021, 12, 12),
                club= 'MAGENTA',
                qrcode= 'Qrcode',
                event= 'GREEK NIGHT'
            ),
            Reservation(
                id=2321,
                user= self.find_by_email('john@example.com'),
                table = 'No 12',
                num_of_people= 2,
                order= 'Order',
                date= datetime(2025, 12, 12),
                club= 'SAINT',
                qrcode= 'Qrcode',
                event= 'Lules culpa'
            ),
            Reservation(
                id=1123,
                user= self.find_by_email('john@example.com'),
                table = 'No 23',
                num_of_people= 3,
                order= 'Order',
                date= datetime(2020, 1, 1),
                club= 'OMNIA',
                qrcode= 'Qrcode',
                event= 'Trap Night'
            )
        ]
        
        # Add dummy users
        dummy_users = [
            User(
                id=1,
                full_name="John Doe",
                age=25,
                role=Role.CUSTOMER,
                phone=1234567890,
                email="john@example.com",
                password="password123",
                reservations=dummy_reservations
            ),
            User(
                id=2,
                full_name="Jane Smith",
                age=28,
                role=Role.MANAGER,
                phone=9876543210,
                email="jane@example.com",
                password="password456",
                reservations=[]
            ),
            User(
                id=3,
                full_name="Bob Wilson",
                age=22,
                role=Role.STAFF,
                phone=5555555555,
                email="bob@example.com",
                password="password789",
                reservations=[]
            )
        ]
        
        # Save dummy users to the repository
        for user in dummy_users:
            self.save(user)

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