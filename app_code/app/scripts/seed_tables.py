from app.data.database import SessionLocal
from app.models import Club, Customer, Event, Reservation, Order, Table, Role, TableType, Staff, Manager, Review
from datetime import datetime, date, time
from sqlalchemy.orm import joinedload

# WINDOWS
# $env:PYTHONPATH = "."
# python app/scripts/seed_tables.py
# UNIX:
# PYTHONPATH=. python app/scripts/seed_tables.py
def seed():
    session = SessionLocal()

    try:
        # 1. Create Managers first
        managers = [
            Manager(
                full_name="Giannis Papadopoulos",
                age=30,
                role=Role.MANAGER,
                phone=1234567890,
                email="papadopoulos@ceid.gr",
                password="password"
            ),
            Manager(
                full_name="Konstantinos Georgiou",
                age=35,
                role=Role.MANAGER,
                phone=2345678901,
                email="georgiou@ceid.gr",
                password="password"
            ),
            Manager(
                full_name="Dimitris Ioannou",
                age=32,
                role=Role.MANAGER,
                phone=3456789012,
                email="ioannou@ceid.gr",
                password="password"
            ),
            Manager(
                full_name="Athanasios Toulas",
                age=40,
                role=Role.MANAGER,
                phone=4567890123,
                email="toulas@ceid.gr",
                password="slet"
            ),
            Manager(
                full_name="Spyros Sioufas",
                age=50,
                role=Role.MANAGER,
                phone=1234567890,
                email="sioufas@ceid.gr",
                password="slet"
            )
        ]
        session.add_all(managers)
        session.flush()  # Flush to get the IDs

        # 3. Create Customer
        customers = [
            Customer(
                full_name="Marios Psaras",
                age=55,
                role=Role.CUSTOMER,
                phone=1234567890,
                email="psaras@ceid.gr",
                password="slet"
            ),
            Customer(
                full_name="Gabriel Gavrilidis",
                age=23,
                role=Role.CUSTOMER,
                phone=1234567890,
                email="gavrilidis@ceid.gr",
                password="slet"
            ),
            Customer(
                full_name="Alexandros Farmakis",
                age=23,
                role=Role.CUSTOMER,
                phone=1234567890,
                email="farmakis@ceid.gr",
                password="slet"
            ),
            Customer(
                full_name="Dimitris Drivis",
                age=21,
                role=Role.CUSTOMER,
                phone=1234567890,
                email="drivis@ceid.gr",
                password="oly"
            ),
            Customer(
                full_name="Nikos Skegias",
                age=23,
                role=Role.CUSTOMER,
                phone=1234567890,
                email="skegias@ceid.gr",
                password="slet"
            )
        ]
        session.add_all(customers)
        
        # 4. Create Staff
        stf = Staff(
            full_name="Paris",
            age=21,
            role=Role.STAFF,
            phone=1234567890,
            email="giparis@ceid.gr",
            password="slet"
        )
        session.add(stf)
        session.flush()
        
        # 2. Create Clubs with manager references
        dummy_clubs = [
            Club(name="Navona", address="Hfaistou 8", location="Patra", manager_id=managers[0].id, vip_available=0),
            Club(name="Saint", address="Kanakari 99", location="Patra", manager_id=managers[1].id, vip_available=0),
            Club(name="Omnia", address="Gamveta 17", location="Patra", manager_id=managers[2].id, vip_available=0),
            Club(name="Marquee", address="Kalampakistan", location="Kalampaka", manager_id=managers[3].id, vip_available=0)
        ]
        session.add_all(dummy_clubs)
        session.flush()  # Flush to get the IDs

        # Set staff's club
        stf.works_at = dummy_clubs[3]  # Assign staff to Marquee club
        session.flush()
        
        # Debug prints
        print("\nVerifying relationships:")
        print(f"Staff's club: {stf.works_at.name if stf.works_at else 'None'}")
        print(f"Club's staff: {dummy_clubs[3].staff.full_name if dummy_clubs[3].staff else 'None'}")
        print()

        # 5. Create Event
        events = [
            Event(
                title="Trap Night",
                description="DJ Marinos",
                music="Trap",
                date=date(2024, 6, 1),
                time=time(22, 0),
                club=dummy_clubs[3]
            ),
            Event(
                title="Kultura",
                description="Gxhan",
                music="Hip-Hop/Rap",
                date=date(2024, 6, 1),
                time=time(23, 0),
                club=dummy_clubs[3]
            ),
            Event(
                title="RnB Night",
                description="Brent Faiyaz",
                music="R&B",
                date=date(2024, 6, 2),
                time=time(23, 0),
                club=dummy_clubs[3]
            ),
            Event(
                title="Lules Culpa",
                description="Liva K",
                music="House",
                date=date(2024, 6, 3),
                time=time(23, 0),
                club=dummy_clubs[3]
            ),
            Event(
                title="Greek Night",
                description="patris thriskeia oikogeneia",
                music="Laika",
                date=date(2024, 6, 4),
                time=time(23, 0),
                club=dummy_clubs[3]
            ),
            Event(
                title="Summer Vibes",
                description="DJ Summer",
                music="House",
                date=date(2025, 7, 15),
                time=time(22, 0),
                club=dummy_clubs[0]
            ),
            Event(
                title="Rock Night",
                description="Rock Band Live",
                music="Rock",
                date=date(2025, 7, 20),
                time=time(21, 0),
                club=dummy_clubs[1]
            ),
            Event(
                title="Jazz Evening",
                description="Jazz Quartet",
                music="Jazz",
                date=date(2025, 8, 5),
                time=time(20, 0),
                club=dummy_clubs[2]
            ),
            Event(
                title="Latin Night",
                description="Salsa Band",
                music="Latin",
                date=date(2025, 8, 12),
                time=time(22, 0),
                club=dummy_clubs[0]
            ),
            Event(
                title="EDM Festival",
                description="Multiple DJs",
                music="EDM",
                date=date(2025, 8, 25),
                time=time(23, 0),
                club=dummy_clubs[3]
            )
        ]
        session.add_all(events)
        session.flush()

        # 6. Create Table
        tables = [
            Table(
                capacity=6,
                club=dummy_clubs[3],
                table_type=TableType.VIP
            ),
            Table(
                capacity=4,
                club=dummy_clubs[2],
                table_type=TableType.PASS
            ),
            Table(
                capacity=8,
                club=dummy_clubs[3],
                table_type=TableType.VIP
            ),
            Table(
                capacity=4,
                club=dummy_clubs[3],
                table_type=TableType.PASS
            )
        ]
        session.add_all(tables)
        session.flush()

        # 7. Create Order
        orders = [
            Order(cost=150.0, delivered=True, paid=True, regular_bottles=2),
            Order(cost=120.0, delivered=True, paid=True, regular_bottles=1),
            Order(cost=130.0, delivered=True, paid=False, regular_bottles=2),
            Order(cost=140.0, delivered=False, paid=True, regular_bottles=1),
            Order(cost=160.0, delivered=True, paid=True, regular_bottles=3),
            Order(cost=170.0, delivered=True, paid=True, regular_bottles=4),
            Order(cost=200.0, delivered=False, paid=False, regular_bottles=3),
            Order(cost=180.0, delivered=False, paid=False, regular_bottles=2),
            Order(cost=250.0, delivered=False, paid=False, regular_bottles=4),
            Order(cost=300.0, delivered=False, paid=False, regular_bottles=5),
            Order(cost=220.0, delivered=True, paid=True, regular_bottles=3),
            Order(cost=190.0, delivered=True, paid=True, regular_bottles=2),
            Order(cost=280.0, delivered=True, paid=True, regular_bottles=4)
        ]
        session.add_all(orders)
        session.flush()
        
        # 8. Create Reservations and link them to individual orders
        dummy_reservations = [
            Reservation(
                user=customers[0],
                table=tables[0],
                num_of_people=4,
                order=orders[0],
                date=datetime(2024, 6, 1, 22, 0),
                club=dummy_clubs[3],
                event=events[0]
            ),
            Reservation(
                user=customers[1],
                table=tables[1],
                num_of_people=2,
                order=orders[1],
                date=datetime(2024, 6, 1, 23, 0),
                club=dummy_clubs[3],
                event=events[1]
            ),
            Reservation(
                user=customers[2],
                table=tables[2],
                num_of_people=6,
                order=orders[2],
                date=datetime(2024, 6, 2, 23, 0),
                club=dummy_clubs[3],
                event=events[2]
            ),
            Reservation(
                user=customers[3],
                table=tables[3],
                num_of_people=3,
                order=orders[3],
                date=datetime(2024, 6, 3, 23, 0),
                club=dummy_clubs[3],
                event=events[3]
            ),
            Reservation(
                user=customers[4],
                table=tables[0],
                num_of_people=5,
                order=orders[4],
                date=datetime(2024, 6, 4, 23, 0),
                club=dummy_clubs[3],
                event=events[4]
            ),
            Reservation(
                user=customers[0],
                table=tables[2],
                num_of_people=7,
                order=orders[5],
                date=datetime(2025, 7, 15, 22, 0),
                club=dummy_clubs[0],
                event=events[5]
            ),
            Reservation(
                user=customers[1],
                table=tables[1],
                num_of_people=3,
                order=orders[6],
                date=datetime(2025, 7, 20, 21, 0),
                club=dummy_clubs[1],
                event=events[6]
            ),
            Reservation(
                user=customers[2],
                table=tables[3],
                num_of_people=3,
                order=orders[7],
                date=datetime(2025, 8, 5, 20, 0),
                club=dummy_clubs[2],
                event=events[7]
            ),
            Reservation(
                user=customers[3],
                table=tables[0],
                num_of_people=5,
                order=orders[8],
                date=datetime(2025, 8, 12, 22, 0),
                club=dummy_clubs[0],
                event=events[8]
            ),
            Reservation(
                user=customers[4],
                table=tables[2],
                num_of_people=6,
                order=orders[9],
                date=datetime(2025, 8, 25, 23, 0),
                club=dummy_clubs[1],
                event=events[9]
            ),
            Reservation(
                user=customers[1],
                table=tables[0],
                num_of_people=4,
                order=orders[10],
                date=datetime(2024, 6, 1, 23, 0),
                club=dummy_clubs[3],
                event=events[1]
            ),
            Reservation(
                user=customers[2],
                table=tables[2],
                num_of_people=6,
                order=orders[11],
                date=datetime(2024, 6, 1, 23, 0),
                club=dummy_clubs[3],
                event=events[1]
            ),
            Reservation(
                user=customers[4],
                table=tables[3],
                num_of_people=3,
                order=orders[12],
                date=datetime(2024, 6, 1, 23, 0),
                club=dummy_clubs[3],
                event=events[1]
            )
        ]
        session.add_all(dummy_reservations)
        session.flush()

        dummy_review = [
            Review(
                music_rating=5,
                atmosphere_rating=5,
                service_rating=5,
                overall_experience=5,
                reservation=dummy_reservations[2]
            ),
            Review(
                music_rating=4,
                atmosphere_rating=5,
                service_rating=4,
                overall_experience=4,
                reservation=dummy_reservations[10]
            ),
            Review(
                music_rating=5,
                atmosphere_rating=4,
                service_rating=5,
                overall_experience=5,
                reservation=dummy_reservations[11]
            ),
            Review(
                music_rating=3,
                atmosphere_rating=4,
                service_rating=3,
                overall_experience=3,
                reservation=dummy_reservations[12]
            )
        ]
        session.add_all(dummy_review)

        # 9. Commit all
        session.commit()
        print("✅ Dummy data successfully seeded.")

    except Exception as e:
        session.rollback()
        print("❌ Error seeding data:", e)
        raise  # Re-raise the exception to see the full traceback

    finally:
        session.close()

if __name__ == "__main__":
    seed()
