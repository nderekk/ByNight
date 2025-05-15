from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# ✅ Change to MySQL later if needed
# Example for MySQL: "mysql+mysqlconnector://user:password@localhost/dbname"
DATABASE_URL = "sqlite:///app_data.db"

engine = create_engine(DATABASE_URL, echo=True, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, expire_on_commit=False)

Base = declarative_base()
