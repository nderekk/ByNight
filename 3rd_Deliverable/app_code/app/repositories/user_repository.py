from typing import Optional
from ..models.user import User

class UserRepository:
  def __init__(self):
    # In-memory storage for demo purposes
    self.users = {}

  def save(self, user: User) -> User:
    """Save a user to the repository"""
    self.users[user.email] = user
    return user

  def find_by_email(self, email: str) -> Optional[User]:
    """Find a user by email"""
    return self.users.get(email)

  def find_by_id(self, user_id: str) -> Optional[User]:
    """Find a user by ID"""
    for user in self.users.values():
      if user.id == user_id:
        return user
    return None

  def update(self, user: User) -> User:
    """Update a user in the repository"""
    if user.email not in self.users:
      raise ValueError("User not found")
    self.users[user.email] = user
    return user

  def delete(self, user_id: str) -> bool:
    """Delete a user from the repository"""
    for email, user in self.users.items():
      if user.id == user_id:
        del self.users[email]
        return True
    return False 