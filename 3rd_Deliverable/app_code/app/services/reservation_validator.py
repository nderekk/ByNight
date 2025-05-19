from datetime import datetime, timedelta

class ReservationValidator:
  @staticmethod
  def bottles_required(people: int) -> int:
    return max(1, (people + 3) // 4)
  
  @classmethod
  def check(cls, table_type: str, people: str, bottles: tuple[str], club) -> tuple[bool, str]:
    from app.models import Table
    people = int(people)
    regular, premium = (int(bottle) for bottle in bottles)
    required_capacity = Table.get_capacity_on_table_type(table_type)
    # print(f"table type: {table_type}\npeople: {people}")
    print(f"req: {cls.bottles_required(people)}\t bottles: {regular+premium} \t res: {cls.bottles_required(people) < regular+premium}")
    if not club.table_available(table_type):
      return (False, f"No {table_type} Tables Available \n:(")
    elif cls.bottles_required(people) > regular+premium:
      return (False, "Minimum Order Not Satisfied \nPlease Increase Bottle Number")
    elif people > required_capacity:
      return (False, "Too Many People for Table Type")
    return (True, "Your reservation has been updated successfully.") 
  
  @classmethod
  def is_cancellable(cls, res_date: datetime) -> bool:
    now = datetime.now()
    if res_date - now < timedelta(hours=2):
      return False
    return True
    
    