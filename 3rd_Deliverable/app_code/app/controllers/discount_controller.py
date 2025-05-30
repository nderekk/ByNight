from app.utils.container import Container
from PySide6.QtCore import QObject, Signal
from app.utils.container import Container
from app.views.discount_page import DiscountPage
from PySide6.QtCore import QDate
from app.models import Event, User, Discount

class DiscountController(QObject):
  
  def __init__(self, show_page: callable):
    super().__init__()
    self.show_page = show_page
    self.view = DiscountPage()
    self.manager_club = Container.resolve(User)
    self.setup_connections()
  
  def setup_connections(self):
    # Connect view signals to controller methods
    self.view.back_button.clicked.connect(self.handle_back)
    self.view.load_button.clicked.connect(self.handle_input)     
  
  def handle_back(self):
    from app.controllers.manager_home_page_controller import ManagerHomePageController
        
    self.manager_home_page_controller = Container.resolve(ManagerHomePageController)
    self.show_page('manager_home_page_controller', self.manager_home_page_controller)
  
  def show(self):
    self.view.show() 

  def handle_input(self):
      selected_qdate = self.view.get_selected_date()
      selected_date = selected_qdate.toPython()

      regular_discount = 0.0
      premium_discount = 0.0

      for name, lineedit, checkbox in self.view.discount_fields:
          if checkbox.isChecked():
              try:
                  value = lineedit.value()
                  if not (0.0 <= value <= 1.0):
                      raise ValueError
                  if name == "Regular":
                      regular_discount = value
                  elif name == "Premium":
                      premium_discount = value
              except ValueError:
                  print(f"Invalid discount value for {name}")
                  return

      print(f"Applying Discounts for {selected_date}:")
      print(f"  Regular: {regular_discount}")
      print(f"  Premium: {premium_discount}")

    # Call your model logic
      Discount.give_discounts(self.manager_club.id, date=selected_date, regular_disc=regular_discount, premium_disc=premium_discount)
 


