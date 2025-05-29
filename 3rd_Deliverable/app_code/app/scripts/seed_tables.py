from app.data.database import SessionLocal
from app.models import Club, Customer, Event, Reservation, Order, Table, Role, TableType, Staff, Manager
from app.models.review import Review
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
            Club(name="Marquee", address="Plateia Dhmoula", location="Kalampaka", manager_id=managers[3].id, vip_available=0)
        ]
        session.add_all(dummy_clubs)
        session.flush()  # Flush to get the IDs

        # Set staff's club
        stf.works_at = dummy_clubs[0]  # Assign staff to Marquee club
        session.flush()
        
        # Debug prints
        print("\nVerifying relationships:")
        print(f"Staff's club: {stf.works_at.name if stf.works_at else 'None'}")
        print(f"Club's staff: {dummy_clubs[3].staff.full_name if dummy_clubs[3].staff else 'None'}")
        print()

        # 5. Create Event (expanded with events for all clubs)
        events = [
            # Existing Marquee events
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
            # Navona events
            Event(
                title="Latin Night",
                description="DJ Carlos",
                music="Latin",
                date=date(2025, 6, 15),
                time=time(22, 0),
                club=dummy_clubs[0]
            ),
            Event(
                title="Rock Night",
                description="Live Band",
                music="Rock",
                date=date(2025, 5, 29),
                time=time(19, 0),
                club=dummy_clubs[0]
            ),
            # Saint events
            Event(
                title="Jazz Evening",
                description="Jazz Quartet",
                music="Jazz",
                date=date(2025, 6, 17),
                time=time(20, 0),
                club=dummy_clubs[1]
            ),
            Event(
                title="Pop Night",
                description="Top 40 Hits",
                music="Pop",
                date=date(2025, 6, 18),
                time=time(22, 0),
                club=dummy_clubs[1]
            ),
            # Omnia events
            Event(
                title="EDM Night",
                description="DJ Max",
                music="EDM",
                date=date(2025, 6, 19),
                time=time(23, 0),
                club=dummy_clubs[2]
            ),
            Event(
                title="Reggae Night",
                description="Live Reggae Band",
                music="Reggae",
                date=date(2025, 6, 20),
                time=time(22, 0),
                club=dummy_clubs[2]
            ),
            # Past events for all clubs
            Event(
                title="Summer Party",
                description="Summer Hits",
                music="Pop",
                date=date(2024, 7, 15),
                time=time(22, 0),
                club=dummy_clubs[0]
            ),
            Event(
                title="Winter Ball",
                description="Classical Music",
                music="Classical",
                date=date(2024, 12, 20),
                time=time(20, 0),
                club=dummy_clubs[1]
            ),
            Event(
                title="Spring Festival",
                description="Various Artists",
                music="Mixed",
                date=date(2024, 4, 1),
                time=time(21, 0),
                club=dummy_clubs[2]
            ),
            Event(
                title="New Year's Eve",
                description="Special Countdown",
                music="Mixed",
                date=date(2024, 12, 31),
                time=time(23, 0),
                club=dummy_clubs[3]
            )
        ]
        session.add_all(events)
        session.flush()  # Flush to get event IDs

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
            # New tables for Navona
            Table(
                capacity=8,
                club=dummy_clubs[0],
                table_type=TableType.VIP
            ),
            Table(
                capacity=4,
                club=dummy_clubs[0],
                table_type=TableType.PASS
            ),
            # New tables for Saint
            Table(
                capacity=6,
                club=dummy_clubs[1],
                table_type=TableType.VIP
            ),
            Table(
                capacity=4,
                club=dummy_clubs[1],
                table_type=TableType.PASS
            ),
            # Additional tables for Omnia
            Table(
                capacity=8,
                club=dummy_clubs[2],
                table_type=TableType.VIP
            ),
            # Additional tables for Marquee
            Table(
                capacity=4,
                club=dummy_clubs[3],
                table_type=TableType.PASS
            ),
            Table(
                capacity=8,
                club=dummy_clubs[3],
                table_type=TableType.VIP
            )
        ]
        session.add_all(tables)
        session.flush()  # Flush to get table IDs

        # 7. Create Order
        orders = [
            Order(cost=150.0, delivered=True, paid=True, regular_bottles=2, premium_bottles=1),
            Order(cost=120.0, delivered=True, paid=True, regular_bottles=1, premium_bottles=2),
            Order(cost=130.0, delivered=True, paid=False, regular_bottles=3, premium_bottles=0),
            Order(cost=140.0, delivered=False, paid=True, regular_bottles=0, premium_bottles=3),
            Order(cost=160.0, delivered=True, paid=True, regular_bottles=4, premium_bottles=1),
            Order(cost=170.0, delivered=True, paid=True, regular_bottles=2, premium_bottles=2),
            # New orders for additional reservations
            Order(cost=200.0, delivered=True, paid=True, regular_bottles=3, premium_bottles=2),
            Order(cost=180.0, delivered=True, paid=True, regular_bottles=1, premium_bottles=3),
            Order(cost=220.0, delivered=True, paid=True, regular_bottles=4, premium_bottles=1),
            Order(cost=190.0, delivered=True, paid=True, regular_bottles=2, premium_bottles=2),
            Order(cost=210.0, delivered=True, paid=True, regular_bottles=3, premium_bottles=2),
            Order(cost=230.0, delivered=True, paid=True, regular_bottles=5, premium_bottles=0),
            Order(cost=240.0, delivered=True, paid=True, regular_bottles=1, premium_bottles=4),
            Order(cost=250.0, delivered=True, paid=True, regular_bottles=2, premium_bottles=3)
        ]
        session.add_all(orders)
        session.flush()  # Flush to get order IDs
        
        # 8. Create Reservations and link them to individual orders
        dummy_reservations = [
            # Existing reservations
            Reservation(
                user=customers[0],
                table=tables[0],
                num_of_people=4,
                order=orders[0],
                club=dummy_clubs[3],
                event=events[0]
            ),
            Reservation(
                user=customers[0],
                table=tables[1],
                num_of_people=2,
                order=orders[1],
                club=dummy_clubs[3],
                event=events[1]
            ),
            Reservation(
                user=customers[2],
                table=tables[1],
                num_of_people=2,
                order=orders[2],
                club=dummy_clubs[3],
                event=events[1]
            ),
            Reservation(
                user=customers[3],
                table=tables[1],
                num_of_people=2,
                order=orders[3],
                club=dummy_clubs[3],
                event=events[1]
            ),
            Reservation(
                user=customers[1],
                table=tables[1],
                num_of_people=2,
                order=orders[4],
                club=dummy_clubs[3],
                event=events[1]
            ),
            Reservation(
                user=customers[1],
                table=tables[1],
                num_of_people=3,
                order=orders[5],
                club=dummy_clubs[3],
                event=events[0]
            ),
            Reservation(
                user=customers[4],
                table=tables[0],
                num_of_people=1,
                order=orders[0],
                club=dummy_clubs[3],
                event=events[0]
            ),
            # New reservations for Navona
            Reservation(
                user=customers[0],
                table=tables[2],
                num_of_people=6,
                order=orders[6],
                club=dummy_clubs[0],
                event=events[7]
            ),
            Reservation(
                user=customers[1],
                table=tables[3],
                num_of_people=3,
                order=orders[7],
                club=dummy_clubs[0],
                event=events[8]
            ),
            # New reservations for Saint
            Reservation(
                user=customers[2],
                table=tables[4],
                num_of_people=4,
                order=orders[8],
                club=dummy_clubs[1],
                event=events[9]
            ),
            Reservation(
                user=customers[3],
                table=tables[5],
                num_of_people=3,
                order=orders[9],
                club=dummy_clubs[1],
                event=events[10]
            ),
            # New reservations for Omnia
            Reservation(
                user=customers[4],
                table=tables[6],
                num_of_people=6,
                order=orders[10],
                club=dummy_clubs[2],
                event=events[11]
            ),
            Reservation(
                user=customers[0],
                table=tables[7],
                num_of_people=4,
                order=orders[11],
                club=dummy_clubs[2],
                event=events[12]
            ),
            # Past reservations
            Reservation(
                user=customers[1],
                table=tables[2],
                num_of_people=5,
                order=orders[12],
                club=dummy_clubs[0],
                event=events[13]
            ),
            Reservation(
                user=customers[2],
                table=tables[4],
                num_of_people=4,
                order=orders[13],
                club=dummy_clubs[1],
                event=events[14]
            )
        ]
        session.add_all(dummy_reservations)

        reviews = [
        
        Review(
            reservation_id=3,
            music_rating=4,
            atmosphere_rating=3,
            service_rating=4,
            overall_experience=4,
            comments="Great night, a bit crowded but fun."
        ),
        Review(
            reservation_id=4,
            music_rating=3,
            atmosphere_rating=3,
            service_rating=3,
            overall_experience=3,
            comments="It was okay. Nothing too exciting."
        ),
        Review(
            reservation_id=5,
            music_rating=2,
            atmosphere_rating=2,
            service_rating=1,
            overall_experience=2,
            comments="Poor service and the music was too loud."
        ),
    ]

        session.add_all(reviews)
     

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
