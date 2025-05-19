from app.data.database import SessionLocal
from app.models import Club, User, Event, Reservation, Order, Table, Role, TableType
from datetime import datetime, date, time

# WINDOWS
# $env:PYTHONPATH = "."
# python app/scripts/seed_tables.py
# UNIX:
# PYTHONPATH=. python app/scripts/seed_tables.py
def seed():
  session = SessionLocal()

  try:
    # 1. Create Club
    dummy_clubs = [
            Club(name="Navona", address="Hfaistou 8", location="Patra", manager="Alice", vip_available=0),
            Club(name="Saint", address="Kanakari 99", location="Patra", manager="Bob", vip_available=0),
            Club(name="Omnia", address="Gamveta 17", location="Patra", manager="Charlie", vip_available=0),
            Club(name="Marquee", address="Kalampakistan", location="Kalampaka", manager="Toulas", vip_available=0)
    ]
    session.add_all(dummy_clubs)
    # (session.add(c) for c in dummy_clubs)

    # 2. Create User
    user = User(
      full_name="BIG FUCKING SIOU",
      age=25,
      role=Role.CUSTOMER,
      phone=1234567890,
      email="spiros@ceid.gr",
      password="slet"
    )
    session.add(user)
    
    staff = User(
      full_name="BIG FUCKING SIOU",
      age=25,
      role=Role.STAFF,
      phone=1234567890,
      email="skerdi@ceid.gr",
      password="slet"
    )
    session.add(staff)

    # 3. Create Event
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

    # 4. Create Table
    tables = [
      Table(
        capacity=6,
        club=dummy_clubs[3],
        table_type = TableType.VIP
      ),
      Table(
        capacity=4,
        club=dummy_clubs[2],
        table_type = TableType.PASS
      )
    ]
    session.add_all(tables)

    # 5. Create Order
    order = Order(
      cost=150.0,
      delivered=True,
      paid=True
    )
    session.add(order)

    # 6. Create Reservation and link everything
    
    dummy_reservations = [
              Reservation(
                user= user,
                table = tables[0],
                num_of_people= 4,
                order= order,
                date=datetime(2026, 1, 1, 22, 0),
                club= dummy_clubs[3],
                qrcode= 'Qrcode',
                event= events[0]
            ),
            Reservation(
                user= user,
                table = tables[1],
                num_of_people= 2,
                order= order,
                date=datetime(2024, 6, 1, 22, 0),
                club= dummy_clubs[0],
                qrcode= 'Qrcode',
                event= events[1]
            ),
            Reservation(
                user= user,
                table = tables[1],
                num_of_people= 3,
                order= order,
                date=datetime(2025, 6, 1, 22, 0),
                club= dummy_clubs[2],
                qrcode= 'Qrcode',
                event= events[0]
            )
    ]
    session.add_all(dummy_reservations)

    # 7. Commit all
    session.commit()
    print("✅ Dummy data successfully seeded.")

  except Exception as e:
    session.rollback()
    print("❌ Error seeding data:", e)

  finally:
    session.close()

if __name__ == "__main__":
  seed()
