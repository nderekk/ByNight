from sqlalchemy import func
from app.models import Reservation, Club, Order
from app.data.database import Base
from app.services.db_session import DatabaseSession
from app.utils.container import Container
import matplotlib.pyplot as plt
from collections import defaultdict


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
        
        # Safety: convert to list if it's a generator
        reservations_id = list(reservations_id)
        print("Looking for orders with reservation_id in:", reservations_id)

        if not reservations_id:
            print("No reservation IDs provided.")
            return []

        # Print all orders in the DB to compare
        all_orders = session.query(Order).all()
        print("All orders in DB with reservation_id:")
        for order in all_orders:
            print(f"Order ID: {order.id}, Reservation ID: {order.reservation_id}, Cost: {order.cost}")

        # Actual query
        orders = session.query(Order).filter(Order.reservation_id.in_(reservations_id)).all()
        print(f"Found {len(orders)} matching orders.")

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
        print("ORDERS", orders)
        sales = sum(ord.cost for ord in orders)

        print("SALES", sales) 

        return sales


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

        # Map reservation_id to date
        reservation_date_map = {res.id: res.date.strftime('%Y-%m-%d') for res in reservations}

        # Aggregate sales by date
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

    