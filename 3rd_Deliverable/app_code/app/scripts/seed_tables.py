from app.data.database import SessionLocal
from app.models import Club, Customer, Event, Reservation, Order, Table, Role, TableType, Staff, Manager
from datetime import datetime, date, time

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
                full_name="Alice",
                age=30,
                role=Role.MANAGER,
                phone=1234567890,
                email="alice@example.com",
                password="password"
            ),
            Manager(
                full_name="Bob",
                age=35,
                role=Role.MANAGER,
                phone=2345678901,
                email="bob@example.com",
                password="password"
            ),
            Manager(
                full_name="Charlie",
                age=32,
                role=Role.MANAGER,
                phone=3456789012,
                email="charlie@example.com",
                password="password"
            ),
            Manager(
                full_name="Toulas",
                age=40,
                role=Role.MANAGER,
                phone=4567890123,
                email="toulas@ceid.gr",
                password="slet"
            ),
            Manager(
                full_name="BIG FUCKING SIOU",
                age=50,
                role=Role.MANAGER,
                phone=1234567890,
                email="spiros@ceid.gr",
                password="slet"
            )
        ]
        session.add_all(managers)
        session.flush()  # Flush to get the IDs

        # 3. Create Customer
        customers = [
            Customer(
                full_name="BIG PSARAKIS GOAT",
                age=55,
                role=Role.CUSTOMER,
                phone=1234567890,
                email="fishakis@ceid.gr",
                password="slet"
            ),
            Customer(
                full_name="GABRIEL",
                age=23,
                role=Role.CUSTOMER,
                phone=1234567890,
                email="gabriel@ceid.gr",
                password="slet"
            ),
            Customer(
                full_name="FARMAKIS O FARMAKOPOIOS",
                age=23,
                role=Role.CUSTOMER,
                phone=1234567890,
                email="aofarmakis@ceid.gr",
                password="slet"
            ),
            Customer(
                full_name="Drivi",
                age=21,
                role=Role.CUSTOMER,
                phone=1234567890,
                email="drivi@ceid.gr",
                password="oly"
            ),
            Customer(
                full_name="SKEGIAS O DIAKSTIS",
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
                date=date(2025, 6, 1),
                time=time(22, 0),
                club=dummy_clubs[3]
            ),
            Event(
                title="Kultura",
                description="Gxhan",
                music="Hip-Hop/Rap",
                date=date(2025, 6, 1),
                time=time(23, 0),
                club=dummy_clubs[3]
            ),
            Event(
                title="RnB Night",
                description="Brent Faiyaz",
                music="R&B",
                date=date(2025, 6, 2),
                time=time(23, 0),
                club=dummy_clubs[3]
            ),
            Event(
                title="Lules Culpa",
                description="Liva K",
                music="House",
                date=date(2025, 6, 3),
                time=time(23, 0),
                club=dummy_clubs[3]
            ),
            Event(
                title="Greek Night",
                description="patris thriskeia oikogeneia",
                music="Laika",
                date=date(2025, 6, 4),
                time=time(23, 0),
                club=dummy_clubs[3]
            ),
            Event(
                title="boy lover night",
                description="Drake",
                music="drake-music",
                date=date(2025, 6, 10),
                time=time(23, 0),
                club=dummy_clubs[3]
            ),
            Event(
                title="Old skool",
                description="oldheadades elate edw",
                music="Hip-Hop/Rap",
                date=date(2025, 6, 12),
                time=time(23, 0),
                club=dummy_clubs[3]
            ),
        ]
        session.add_all(events)

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
            )
        ]
        session.add_all(tables)

        # 7. Create Order
        orders = [
            Order(cost=150.0, delivered=True, paid=True, regular_bottles=2),
            Order(cost=120.0, delivered=True, paid=True, regular_bottles=1),
            Order(cost=130.0, delivered=True, paid=False, regular_bottles=2),
            Order(cost=140.0, delivered=False, paid=True, regular_bottles=1),
            Order(cost=160.0, delivered=True, paid=True, regular_bottles=3),
            Order(cost=170.0, delivered=True, paid=True, regular_bottles=4)
        ]
        session.add_all(orders)
        
# 8. Create Reservations and link them to individual orders
        dummy_reservations = [
            Reservation(
                user=customers[0],
                table=tables[0],
                num_of_people=4,
                order=orders[0],
                date=datetime(2026, 1, 1, 22, 0),
                club=dummy_clubs[3],
                event=events[0]
            ),
            Reservation(
                user=customers[0],
                table=tables[1],
                num_of_people=2,
                order=orders[1],
                date=datetime(2024, 8, 1, 22, 0),
                club=dummy_clubs[3],
                event=events[1]
            ),
            Reservation(
                user=customers[2],
                table=tables[1],
                num_of_people=2,
                order=orders[2],
                date=datetime(2024, 7, 1, 22, 0),
                club=dummy_clubs[3],
                event=events[1]
            ),
            Reservation(
                user=customers[3],
                table=tables[1],
                num_of_people=2,
                order=orders[3],
                date=datetime(2024, 6, 1, 22, 0),
                club=dummy_clubs[3],
                event=events[1]
            ),
            Reservation(
                user=customers[1],
                table=tables[1],
                num_of_people=2,
                order=orders[4],
                date=datetime(2025, 12, 9, 23, 30),
                club=dummy_clubs[3],
                event=events[1]
            ),
            Reservation(
                user=customers[1],
                table=tables[1],
                num_of_people=3,
                order=orders[5],
                date=datetime(2025, 10, 28, 22, 0),
                club=dummy_clubs[3],
                event=events[0]
            )
        ]
        session.add_all(dummy_reservations)


        # 9. Commit all
        session.commit()
        print("✅ Dummy data successfully seeded.")

    except Exception as e:
        session.rollback()
        print("❌ Error seeding data:", e)

    finally:
        session.close()

if __name__ == "__main__":
    seed()
