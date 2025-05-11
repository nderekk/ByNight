import mysql.connector
from config.database import MYSQL_CONFIG

def init_database():
    # Connect to MySQL server
    conn = mysql.connector.connect(
        host=MYSQL_CONFIG['host'],
        user=MYSQL_CONFIG['user'],
        password=MYSQL_CONFIG['password']
    )
    cursor = conn.cursor()

    try:
        # Create database if it doesn't exist
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {MYSQL_CONFIG['database']}")
        print(f"Database '{MYSQL_CONFIG['database']}' created or already exists")

        # Switch to the database
        cursor.execute(f"USE {MYSQL_CONFIG['database']}")

        # Create users table
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
        print("Users table created or already exists")

        conn.commit()
        print("Database initialization completed successfully")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    init_database() 