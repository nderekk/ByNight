from app.models import Reservation, Table, TableType, Club

class ReservationValidator:  
  @classmethod
  def check(cls, res: Reservation, table_type: str, people: int) -> bool | bool, str:
    print(f"table type: {table_type}\npeople: {people}")
    if people > res.get_table.capacity:
      pass