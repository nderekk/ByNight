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
            )
        ]
        session.add_all(managers)
        session.flush()  # Flush to get the IDs

        # 3. Create Customer
        customers = [
            Customer(
                full_name="BIG FUCKING SIOU",
                age=50,
                role=Role.CUSTOMER,
                phone=1234567890,
                email="spiros@ceid.gr",
                password="slet"
            ),
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
                full_name="SKEGIAS O DIAKSTIS",
                age=23,
                role=Role.CUSTOMER,
                phone=1234567890,
                email="skegias@ceid.gr",
                password="slet"
            ),
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
                date=date(2025, 7, 1),
                time=time(23, 0),
                club=dummy_clubs[1]
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
        order = Order(
            cost=150.0,
            delivered=True,
            paid=True
        )
        session.add(order)

        # 8. Create Reservation and link everything
        dummy_reservations = [
            Reservation(
                user=customers[0],
                table=tables[0],
                num_of_people=4,
                order=order,
                date=datetime(2026, 1, 1, 22, 0),
                club=dummy_clubs[3],
                event=events[0]
            ),
            Reservation(
                user=customers[0],
                table=tables[1],
                num_of_people=2,
                order=order,
                date=datetime(2024, 6, 1, 22, 0),
                club=dummy_clubs[3],
                event=events[1]
            ),
            Reservation(
                user=customers[2],
                table=tables[1],
                num_of_people=2,
                order=order,
                date=datetime(2027, 6, 1, 22, 0),
                club=dummy_clubs[3],
                event=events[1]
            ),
            Reservation(
                user=customers[3],
                table=tables[1],
                num_of_people=2,
                order=order,
                date=datetime(2027, 6, 1, 22, 0),
                club=dummy_clubs[3],
                event=events[1]
            ),
            Reservation(
                user=customers[4],
                table=tables[1],
                num_of_people=2,
                order=order,
                date=datetime(2025, 12, 9, 23, 30),
                club=dummy_clubs[3],
                event=events[1]
            ),
            Reservation(
                user=customers[1],
                table=tables[1],
                num_of_people=3,
                order=order,
                date=datetime(2025, 10, 28, 22, 0),
                club=dummy_clubs[3],
                event=events[0]
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
