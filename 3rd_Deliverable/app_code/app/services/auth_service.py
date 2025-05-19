import hashlib
from typing import Optional, Tuple
from app.models.user import User
from app.utils.container import Container
from app.services.db_session import DatabaseSession

class AuthService:
    def __init__(self):
        self.session = Container.resolve(DatabaseSession)

    def authenticate(self, mail: str, password: str) -> Tuple[bool, Optional[User]]:
        """Authenticate a user with email and password.
        
        Returns:
            Tuple[bool, Optional[User]]: (success, user) where success is True if authentication
            was successful, and user is the authenticated user if successful, None otherwise.
        """
        user = self.session.query(User).filter_by(email=mail).first()
        if user and user.verify_password(password):
            return True, user
        return False, None

    def register_user(self, user: User):
        """Register a new user"""
        self.session.add(user)
        self.session.commit()
        # # Hash the password before storing
        # user._password = self._hash_password(user._password)
        # self.user_repository.save(user)

    def user_exists(self, mail: str) -> bool:
        """Check if a user with the given email exists"""
        return self.session.query(User).filter_by(email=mail).first() is not None

    def _hash_password(self, password: str) -> str:
        return password
        # """Hash a password using SHA-256"""
        # return hashlib.sha256(password.encode()).hexdigest()

    def _verify_password(self, password: str, hashed_password: str) -> bool:
        """Verify a password against its hash"""
        return self._hash_password(password) == hashed_password
