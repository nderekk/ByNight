import hashlib
from typing import Optional, Tuple
from app.models.user import User
from app.data.repositories.user_repository import UserRepository

class AuthService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def authenticate(self, email: str, password: str) -> Tuple[bool, Optional[User]]:
        """Authenticate a user with email and password.
        
        Returns:
            Tuple[bool, Optional[User]]: (success, user) where success is True if authentication
            was successful, and user is the authenticated user if successful, None otherwise.
        """
        user = self.user_repository.find_by_email(email)
        if user and user.verify_password(password):
            return True, user
        return False, None

    def register_user(self, user: User):
        """Register a new user"""
        pass
        # # Hash the password before storing
        # user._password = self._hash_password(user._password)
        # self.user_repository.save(user)

    def user_exists(self, email: str) -> bool:
        """Check if a user with the given email exists"""
        return self.user_repository.find_by_email(email) is not None

    def get_next_user_id(self) -> int:
        """Get the next available user ID"""
        return self.user_repository.get_next_id()

    def _hash_password(self, password: str) -> str:
        return password
        # """Hash a password using SHA-256"""
        # return hashlib.sha256(password.encode()).hexdigest()

    def _verify_password(self, password: str, hashed_password: str) -> bool:
        """Verify a password against its hash"""
        return self._hash_password(password) == hashed_password
