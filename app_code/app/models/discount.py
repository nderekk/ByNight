from app.data.database import Base
from app.models import Reservation, Event
from app.services.db_session import DatabaseSession
from app.utils.container import Container
from datetime import datetime
from sqlalchemy import func, Date

class Discount(Base):
    __abstract__ = True

    @classmethod
    def _get_session(cls):
        return Container.resolve(DatabaseSession)

    @classmethod
    def give_discounts(cls, club_id, date, regular_disc, premium_disc, ):  
        session = cls._get_session()
        if isinstance(date, datetime):
          date = date.date()

        
        reservations = session.query(Reservation)\
            .join(Reservation.event)\
            .filter(Event.date == date, Event.club_id == club_id)\
            .all()

        print(f"DEBUG: Found {len(reservations)} reservations on {date}")

        for res in reservations:
            if not res.order:
                print(f"DEBUG: Skipping reservation {res.id} (no order)")
                continue

            # Apply the discounts
            event = res.event
            event.regular_discount = regular_disc
            event.premium_discount = premium_disc

            # Recalculate cost
            new_cost = (
                res.order.regular_bottles * 80 * (1 - regular_disc) +
                res.order.premium_bottles * 120 * (1 - premium_disc)
            )
            res.order.cost = new_cost

            print(f"DEBUG: Updated reservation {res.id} - New cost: {new_cost}")

        session.commit()
        print("DEBUG: Discounts applied and session committed")
    
    @classmethod
    def get_discounts_by_date(cls, selected_date, club_id):
        session = Container.resolve(DatabaseSession)

        # Find one event on the selected date for the club
        event = session.query(Event).filter(
            Event.date == selected_date,
            Event.club_id == club_id
        ).first()

        if not event:
            return {}

        return {
            "regular": event.regular_discount,
            "premium": event.premium_discount
        }

