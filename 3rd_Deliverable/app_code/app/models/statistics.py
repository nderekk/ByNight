from sqlalchemy import func
from app.models import Reservation, Club, Order, Review
from app.data.database import Base
from app.services.db_session import DatabaseSession
from app.utils.container import Container
import matplotlib.pyplot as plt
from collections import defaultdict
from statistics import mean


class Statistics(Base):
    __abstract__ = True

    @classmethod
    def _get_session(cls):
        return Container.resolve(DatabaseSession)

    @classmethod
    def _get_reservations(cls, from_datetime, to_datetime, club_id):
        session = cls._get_session()
        return session.query(Reservation).filter(
            Reservation.date >= from_datetime,
            Reservation.date <= to_datetime,
            Reservation.club_id == club_id
        ).all()

    @classmethod
    def get_orders(cls, reservations_id):
        session = cls._get_session()
        
        if not reservations_id:
            print("No reservation IDs provided.")
            return []
        
        orders = session.query(Order).filter(Order.reservation_id.in_(reservations_id)).all()
        return orders


    @classmethod
    def get_attendance_percentage(cls, from_datetime, to_datetime, club_id):
        reservations = cls._get_reservations(from_datetime, to_datetime, club_id)

        total_attendance = sum(res.num_of_people for res in reservations)

        session = cls._get_session()
        max_capacity = session.query(Club.max_capacity).filter(Club.id == club_id).scalar() or 0

        if max_capacity == 0:
            return 0

        return min(100, (total_attendance / max_capacity) * 100)

    @classmethod
    def get_sale(cls, from_datetime, to_datetime, club_id):
        reservations = cls._get_reservations(from_datetime, to_datetime, club_id)
        reservations_id = [res.id for res in reservations]

        orders = cls.get_orders(reservations_id)
        sales = sum(ord.cost for ord in orders)

        return sales
    
    @classmethod
    def get_drinks(cls, from_datetime, to_datetime, club_id):
        reservations = cls._get_reservations(from_datetime, to_datetime, club_id)
        reservations_id = [res.id for res in reservations]

        orders = cls.get_orders(reservations_id)
        total_premium = sum(ord.premium_bottles for ord in orders)
        total_regular = sum(ord.regular_bottles for ord in orders) 
        
        total_bottles = total_premium + total_regular

        larger = max(total_premium, total_regular)
        percentage_larger_drinks = (larger / total_bottles) * 100

        return percentage_larger_drinks


    @classmethod
    def get_rating(cls, from_datetime, to_datetime, club_id):
        session = cls._get_session()

        reviews = session.query(Review).join(Review.reservation).filter(
          Reservation.date >= from_datetime,
          Reservation.date <= to_datetime,
          Reservation.club_id == club_id
        ).all()
    
        if not reviews:
            return 0.0  

        total_score = sum(review.overall_experience for review in reviews)
        average_score = total_score / len(reviews)
        return average_score



    @classmethod
    def plot_reservation_attendance(cls, from_datetime, to_datetime, club_id):
        reservations = cls._get_reservations(from_datetime, to_datetime, club_id)

        if not reservations:
            print("No reservations found.")
            return

        # Aggregate number of people per reservation date
        date_counts = defaultdict(int)
        for res in reservations:
            date_str = res.date.strftime('%Y-%m-%d')
            date_counts[date_str] += res.num_of_people

        # Sort by date
        sorted_dates = sorted(date_counts)
        sorted_counts = [date_counts[date] for date in sorted_dates]

        # Plotting
        cls.plot_attendance_graph(sorted_dates, sorted_counts)

    @staticmethod
    def plot_attendance_graph(dates, counts):
        plt.figure(figsize=(10, 5))
        plt.plot(dates, counts, marker='o', linestyle='-', color='skyblue')
        plt.xlabel("Reservation Date")
        plt.ylabel("Number of People")
        plt.title("Reservation Attendance Over Time")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.grid(True)
        plt.show()
    
    @classmethod
    def plot_daily_sales(cls, from_datetime, to_datetime, club_id):
        reservations = cls._get_reservations(from_datetime, to_datetime, club_id)

        if not reservations:
            print("No reservations found.")
            return

        reservation_ids = [res.id for res in reservations]

        session = cls._get_session()
        try:
            orders = session.query(Order).filter(Order.reservation_id.in_(reservation_ids)).all()
        finally:
            session.close()

        if not orders:
            print("No orders found for selected reservations.")
            return

        reservation_date_map = {res.id: res.date.strftime('%Y-%m-%d') for res in reservations}

        sales_by_date = defaultdict(float)
        for order in orders:
            date_str = reservation_date_map.get(order.reservation_id)
            if date_str:
                sales_by_date[date_str] += order.cost

        # Sort by date
        sorted_dates = sorted(sales_by_date)
        sorted_sales = [sales_by_date[date] for date in sorted_dates]

        cls.plot_sales_graph(sorted_dates, sorted_sales)

    @staticmethod
    def plot_sales_graph(dates, sales):
        plt.figure(figsize=(10, 5))
        plt.plot(dates, sales, marker='o', linestyle='-', color='green')
        plt.xlabel("Reservation Date")
        plt.ylabel("Total Sales (€)")
        plt.title("Daily Sales Over Time")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.grid(True)
        plt.show()

    @classmethod
    def plot_bottle_amounts(cls, from_datetime, to_datetime, club_id):
        reservations = cls._get_reservations(from_datetime, to_datetime, club_id)
        if not reservations:
            print("No reservations found.")
            return

        reservation_ids = [res.id for res in reservations]
        reservation_labels = [f"Res {res.id}" for res in reservations]  # Or res.date.strftime('%Y-%m-%d')

        session = cls._get_session()
        try:
            orders = session.query(Order).filter(Order.reservation_id.in_(reservation_ids)).all()
        finally:
            session.close()

        if not orders:
            print("No orders found for selected reservations.")
            return

        data = defaultdict(lambda: {"premium": 0, "regular": 0})

        for order in orders:
            data[order.reservation_id]["premium"] += order.premium_bottles
            data[order.reservation_id]["regular"] += order.regular_bottles

        premium_values = [data[res_id]["premium"] for res_id in reservation_ids]
        regular_values = [data[res_id]["regular"] for res_id in reservation_ids]

        cls.plot_bottle_amounts_graph(reservation_labels, premium_values, regular_values)

    @staticmethod
    def plot_bottle_amounts_graph(reservation_labels, premium_values, regular_values):
        import numpy as np

        x = np.arange(len(reservation_labels))
        width = 0.35

        plt.figure(figsize=(12, 6))
        plt.bar(x - width / 2, premium_values, width, label='Premium Bottles', color='orange')
        plt.bar(x + width / 2, regular_values, width, label='Regular Bottles', color='blue')

        plt.xlabel('Reservation')
        plt.ylabel('Number of Bottles')
        plt.title('Bottle Amounts by Category for Each Reservation')
        plt.xticks(x, reservation_labels, rotation=45)
        plt.legend()
        plt.tight_layout()
        plt.grid(axis='y')
        plt.show()


    @classmethod
    def plot_rating(cls, from_datetime, to_datetime, club_id):
        reservations = cls._get_reservations(from_datetime, to_datetime, club_id)

        if not reservations:
            print("No reservations found.")
            return

        reservation_ids = [res.id for res in reservations]

        session = cls._get_session()
        try:
            reviews = (
                session.query(Review)
                .filter(Review.reservation_id.in_(reservation_ids))
                .all()
            )
        finally:
            session.close()

        if not reviews:
            print("No reviews found.")
            return

       
        reservation_date_map = {res.id: res.date.strftime('%Y-%m-%d') for res in reservations}

        ratings_by_date = defaultdict(list)
        for review in reviews:
            date_str = reservation_date_map.get(review.reservation_id)
            if date_str:
                ratings_by_date[date_str].append(review.overall_experience)

        
        sorted_dates = sorted(ratings_by_date)
        avg_ratings = [mean(ratings_by_date[date]) for date in sorted_dates]

        cls.plot_rating_graph(sorted_dates, avg_ratings)

    @staticmethod
    def plot_rating_graph(dates, ratings):
        plt.figure(figsize=(10, 5))
        plt.plot(dates, ratings, marker='o', linestyle='-', color='blue')
        plt.xlabel("Reservation Date")
        plt.ylabel("Average Overall Experience Rating")
        plt.title("Overall Experience Rating Over Time")
        plt.xticks(rotation=45)
        plt.ylim(0, 5.5)
        plt.tight_layout()
        plt.grid(True)
        plt.show()
