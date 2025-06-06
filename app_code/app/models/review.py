from sqlalchemy import Column, Integer, String, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from app.data.database import Base
from app.utils.container import Container
from app.services.db_session import DatabaseSession 

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True)
    
    music_rating = Column(Integer, nullable=False)
    atmosphere_rating = Column(Integer, nullable=False)
    service_rating = Column(Integer, nullable=False)
    overall_experience =  Column(Integer, nullable=False)
    comments = Column(String)

    reservation_id = Column(Integer, ForeignKey("reservations.id"), nullable=False, unique=True)
     
    
    reservation = relationship("Reservation", back_populates="review")
    

    # Έλεγχος valid range για τα ratings
    __table_args__ = (
        CheckConstraint('music_rating BETWEEN 1 AND 5', name='music_rating_range'),
        CheckConstraint('atmosphere_rating BETWEEN 1 AND 5', name='atmosphere_rating_range'),
        CheckConstraint('service_rating BETWEEN 1 AND 5', name='service_rating_range'),
        CheckConstraint('overall_experience BETWEEN 1 AND 5', name='overall_rating_range')

    )


    @classmethod
    def create_review(cls, music_rating: int, atmosphere_rating: int, service_rating: int,overall_experience: int,  comment: str, reservation_id: int) :
        from app.models import Reservation

        session = Container.resolve(DatabaseSession)
        reservation=Reservation.get_res_from_id(reservation_id)

        review = Review(
        reservation=reservation,
        music_rating=music_rating,
        atmosphere_rating=atmosphere_rating,
        service_rating=service_rating,
        overall_experience=overall_experience,
        comments=comment

    )

        session.add(review)
        session.commit()


    @classmethod
    def get_reviews(cls, event_id: int):
        from app.models import Reservation

        session = Container.resolve(DatabaseSession)
        return session.query(cls).join(cls.reservation).filter(Reservation.event_id == event_id).all()