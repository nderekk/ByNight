import mysql.connector
from typing import Optional, List
from app.models.user import User, Customer, Owner

class UserRepository:
    def __init__(self, host: str, user: str, password: str, database: str):
        self.config = {
            'host': host,
            'user': user,
            'password': password,
            'database': database
        }
        self._init_db()

    def _get_connection(self):
        """Create and return a new database connection"""
        return mysql.connector.connect(**self.config)

    def _init_db(self):
        """Initialize the database with required tables"""
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    user_id INT AUTO_INCREMENT PRIMARY KEY,
                    username VARCHAR(255) NOT NULL,
                    email VARCHAR(255) UNIQUE NOT NULL,
                    password VARCHAR(255) NOT NULL,
                    user_type ENUM('customer', 'owner') NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            conn.commit()

    def save(self, user: User):
        """Save a user to the database"""
        with self._get_connection() as conn:
            cursor = conn.cursor()
            if user.user_id is None:  # New user
                cursor.execute('''
                    INSERT INTO users (username, email, password, user_type)
                    VALUES (%s, %s, %s, %s)
                ''', (
                    user.username,
                    user.email,
                    user._password,
                    user.get_role()
                ))
                user._user_id = cursor.lastrowid
            else:  # Update existing user
                cursor.execute('''
                    UPDATE users 
                    SET username = %s, email = %s, password = %s, user_type = %s
                    WHERE user_id = %s
                ''', (
                    user.username,
                    user.email,
                    user._password,
                    user.get_role(),
                    user.user_id
                ))
            conn.commit()

    def find_by_email(self, email: str) -> Optional[User]:
        """Find a user by email"""
        with self._get_connection() as conn:
            cursor = conn.cursor(dictionary=True)
            cursor.execute('SELECT * FROM users WHERE email = %s', (email,))
            row = cursor.fetchone()
            
            if row:
                if row['user_type'] == "customer":
                    user = Customer(
                        user_id=row['user_id'],
                        username=row['username'],
                        email=row['email'],
                        password=row['password']
                    )
                else:
                    user = Owner(
                        user_id=row['user_id'],
                        username=row['username'],
                        email=row['email'],
                        password=row['password']
                    )
                return user
            return None

    def find_by_id(self, user_id: int) -> Optional[User]:
        """Find a user by ID"""
        with self._get_connection() as conn:
            cursor = conn.cursor(dictionary=True)
            cursor.execute('SELECT * FROM users WHERE user_id = %s', (user_id,))
            row = cursor.fetchone()
            
            if row:
                if row['user_type'] == "customer":
                    user = Customer(
                        user_id=row['user_id'],
                        username=row['username'],
                        email=row['email'],
                        password=row['password']
                    )
                else:
                    user = Owner(
                        user_id=row['user_id'],
                        username=row['username'],
                        email=row['email'],
                        password=row['password']
                    )
                return user
            return None

    def get_next_id(self) -> int:
        """Get the next available user ID"""
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT MAX(user_id) FROM users')
            max_id = cursor.fetchone()[0]
            return (max_id or 0) + 1

    def delete(self, user_id: int):
        """Delete a user by ID"""
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM users WHERE user_id = %s', (user_id,))
            conn.commit()

    def list_all(self) -> List[User]:
        """List all users"""
        with self._get_connection() as conn:
            cursor = conn.cursor(dictionary=True)
            cursor.execute('SELECT * FROM users')
            users = []
            for row in cursor.fetchall():
                if row['user_type'] == "customer":
                    user = Customer(
                        user_id=row['user_id'],
                        username=row['username'],
                        email=row['email'],
                        password=row['password']
                    )
                else:
                    user = Owner(
                        user_id=row['user_id'],
                        username=row['username'],
                        email=row['email'],
                        password=row['password']
                    )
                users.append(user)
            return users 