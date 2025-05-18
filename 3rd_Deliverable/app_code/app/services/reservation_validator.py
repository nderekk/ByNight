class ReservationValidator:
  @staticmethod
  def bottles_required(people: int) -> int:
    return max(1, (people + 3) // 4)
  
  @classmethod
  def check(cls, table_type: str, people: str, bottles: str, club) -> bool | tuple[bool, str]:
    from app.models import Reservation, Table, TableType, Club
    people = int(people)
    bottles = int(bottles)
    required_capacity = Table.get_capacity_on_table_type(table_type)
    # print(f"table type: {table_type}\npeople: {people}")
    if not club.table_available(table_type):
      return (False, f"No {table_type} Tables Available \n:(")
    elif cls.bottles_required(people) < bottles:
      return (False, "Minimum Order Not Satisfied \nPlease Increase Bottle Number")
    elif people > required_capacity:
      return (False, "Too Many People for Table Type")
    return True
