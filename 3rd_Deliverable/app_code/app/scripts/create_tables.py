from app.data.database import Base, engine
from models.user import User
from models.reservation import Reservation
from models.club import Club

Base.metadata.create_all(bind=engine)
