from typing import Optional, Tuple
from ..models.user import User, Customer, Owner
from ..services.auth_service import AuthService

class AuthController:
    def __init__(self, auth_service: AuthService):
        self.auth_service = auth_service
        self.current_user: Optional[User] = None

    def login(self, email: str, password: str) -> Tuple[bool, str]:
        """
        Attempt to log in a user
        Returns: (success, message)
        """
        try:
            user = self.auth_service.authenticate(email, password)
            if user:
                self.current_user = user
                return True, "Login successful"
            return False, "Invalid email or password"
        except Exception as e:
            return False, f"Login failed: {str(e)}"

    def signup(self, email: str, password: str, user_type: str) -> Tuple[bool, str]:
        """
        Create a new user account
        Returns: (success, message)
        """
        try:
            if self.auth_service.user_exists(email):
                return False, "Email already registered"

            if user_type == "customer":
                user = Customer(
                    user_id=self.auth_service.get_next_user_id(),
                    username=email.split('@')[0],
                    email=email,
                    password=password
                )
            elif user_type == "owner":
                user = Owner(
                    user_id=self.auth_service.get_next_user_id(),
                    username=email.split('@')[0],
                    email=email,
                    password=password
                )
            else:
                return False, "Invalid user type"

            self.auth_service.register_user(user)
            self.current_user = user
            return True, "Account created successfully"
        except Exception as e:
            return False, f"Signup failed: {str(e)}"

    def social_login(self, provider: str) -> Tuple[bool, str]:
        """
        Handle social login (Google/Apple)
        Returns: (success, message)
        """
        try:
            # TODO: Implement social login logic
            return False, f"{provider} login not implemented yet"
        except Exception as e:
            return False, f"Social login failed: {str(e)}"

    def logout(self):
        """Log out the current user"""
        self.current_user = None

    def get_current_user(self) -> Optional[User]:
        """Get the currently logged in user"""
        return self.current_user 