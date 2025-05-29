from app.data.database import SessionLocal
from app.models import Club, Customer, Event, Reservation, Order, Table, Role, TableType, Staff, Manager
from app.models.review import Review
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
                date=date(2024, 6, 1),
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
                date=date(2023, 6, 15),
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
                date=date(2024, 6, 18),
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
            Order(cost=250.0, delivered=True, paid=True, regular_bottles=2, premium_bottles=3),
            # Additional orders for past reservations
            Order(cost=280.0, delivered=True, paid=True, regular_bottles=3, premium_bottles=3),
            Order(cost=260.0, delivered=True, paid=True, regular_bottles=4, premium_bottles=2),
            Order(cost=290.0, delivered=True, paid=True, regular_bottles=2, premium_bottles=4),
            Order(cost=270.0, delivered=True, paid=True, regular_bottles=5, premium_bottles=1),
            Order(cost=300.0, delivered=True, paid=True, regular_bottles=3, premium_bottles=4),
            Order(cost=320.0, delivered=True, paid=True, regular_bottles=4, premium_bottles=3),
            Order(cost=340.0, delivered=True, paid=True, regular_bottles=5, premium_bottles=2),
            Order(cost=360.0, delivered=True, paid=True, regular_bottles=2, premium_bottles=5),
            Order(cost=380.0, delivered=True, paid=True, regular_bottles=3, premium_bottles=5),
            Order(cost=400.0, delivered=True, paid=True, regular_bottles=4, premium_bottles=4),
            Order(cost=420.0, delivered=True, paid=True, regular_bottles=5, premium_bottles=3),
            Order(cost=440.0, delivered=True, paid=True, regular_bottles=3, premium_bottles=5),
            Order(cost=460.0, delivered=True, paid=True, regular_bottles=4, premium_bottles=5),
            Order(cost=480.0, delivered=True, paid=True, regular_bottles=5, premium_bottles=4),
            Order(cost=500.0, delivered=True, paid=True, regular_bottles=4, premium_bottles=5),
            Order(cost=520.0, delivered=True, paid=True, regular_bottles=5, premium_bottles=5)
        ]
        session.add_all(orders)
        session.flush()  # Flush to get order IDs

        # Create past events for Marquee
        past_events = [
            Event(
                title="Past Trap Night 1",
                description="DJ Past",
                music="Trap",
                date=date(2024, 1, 15),
                time=time(22, 0),
                club=dummy_clubs[3]
            ),
            Event(
                title="Past Hip Hop Night",
                description="Past Artist",
                music="Hip-Hop/Rap",
                date=date(2024, 1, 20),
                time=time(23, 0),
                club=dummy_clubs[3]
            ),
            Event(
                title="Past RnB Night",
                description="Past RnB Artist",
                music="R&B",
                date=date(2024, 2, 1),
                time=time(22, 0),
                club=dummy_clubs[3]
            ),
            Event(
                title="Past House Night",
                description="Past House DJ",
                music="House",
                date=date(2024, 2, 10),
                time=time(23, 0),
                club=dummy_clubs[3]
            ),
            Event(
                title="Past Latin Night",
                description="Past Latin DJ",
                music="Latin",
                date=date(2024, 2, 20),
                time=time(22, 0),
                club=dummy_clubs[3]
            ),
            Event(
                title="Past Rock Night",
                description="Past Rock Band",
                music="Rock",
                date=date(2024, 3, 1),
                time=time(21, 0),
                club=dummy_clubs[3]
            ),
            Event(
                title="Past Jazz Night",
                description="Past Jazz Band",
                music="Jazz",
                date=date(2024, 3, 10),
                time=time(20, 0),
                club=dummy_clubs[3]
            ),
            Event(
                title="Past Pop Night",
                description="Past Pop Artist",
                music="Pop",
                date=date(2024, 3, 20),
                time=time(22, 0),
                club=dummy_clubs[3]
            ),
            Event(
                title="Past EDM Night",
                description="Past EDM DJ",
                music="EDM",
                date=date(2024, 4, 1),
                time=time(23, 0),
                club=dummy_clubs[3]
            ),
            Event(
                title="Past Reggae Night",
                description="Past Reggae Band",
                music="Reggae",
                date=date(2024, 4, 10),
                time=time(22, 0),
                club=dummy_clubs[3]
            )
        ]
        session.add_all(past_events)
        session.flush()  # Flush to get event IDs

        # Add past reservations for Marquee
        past_reservations = []
        for i in range(20):
            # Create and add reservation
            reservation = Reservation(
                user=customers[i % 5],
                table=tables[0] if i % 2 == 0 else tables[7],  # Alternate between VIP and PASS tables
                num_of_people=2 + (i % 5),  # Vary number of people from 2 to 6
                order=orders[i % 30],  # Cycle through available orders
                club=dummy_clubs[3],
                event=past_events[i % 10]  # Cycle through past events
            )
            session.add(reservation)
            session.flush()  # Flush to get the ID
            
            # Refresh the reservation with all relationships loaded
            session.refresh(reservation, ['event', 'user', 'table', 'order', 'club'])
            past_reservations.append(reservation)

        # Add reviews for past reservations
        reviews = [
            Review(
                reservation=past_reservations[0],
                music_rating=4,
                atmosphere_rating=3,
                service_rating=4,
                overall_experience=4,
                comments="Great night, a bit crowded but fun."
            ),
            Review(
                reservation=past_reservations[1],
                music_rating=3,
                atmosphere_rating=3,
                service_rating=3,
                overall_experience=3,
                comments="It was okay. Nothing too exciting."
            ),
            Review(
                reservation=past_reservations[2],
                music_rating=2,
                atmosphere_rating=2,
                service_rating=1,
                overall_experience=2,
                comments="Poor service and the music was too loud."
            ),
        ]

        # Add reviews and commit
        session.add_all(reviews)
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
