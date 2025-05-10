"""
Database configuration settings
"""

# MySQL Configuration
MYSQL_CONFIG = {
    'host': 'localhost',      # Your MySQL server host
    'user': 'root',          # Your MySQL username
    'password': '',          # Your MySQL password
    'database': 'bynight_db' # Your database name
}

# Connection pool settings
POOL_CONFIG = {
    'pool_name': 'bynight_pool',
    'pool_size': 5
} 