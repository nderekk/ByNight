from sqlalchemy import func
from app.models import Reservation
from app.models import Club
from app.data.database import Base
from app.services.db_session import DatabaseSession
from app.utils.container import Container

class Statistics(Base):
    
    __abstract__ = True


    @classmethod
    def get_attendance_percentage(cls, from_datetime, to_datetime, club_id):
        session = Container.resolve(DatabaseSession)

        reservations = session.query(Reservation).filter(
            Reservation.date >= from_datetime,
            Reservation.date <= to_datetime,
            Reservation.club_id == club_id
        ).all()

        print(f"From: {from_datetime}, To: {to_datetime}, Club ID: {club_id}")
        print(f"Found reservations: {reservations}")
        
        total_attendance = sum(res.num_of_people for res in reservations)

        max_capacity = session.query(Club.max_capacity).filter(Club.id == club_id).scalar() or 0

        if max_capacity == 0:
            return 0
        return min(100, (total_attendance / max_capacity) * 100)
    
    
    

