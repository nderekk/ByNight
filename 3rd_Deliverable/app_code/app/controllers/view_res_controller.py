from app.utils.container import Container
from PySide6.QtCore import QObject, Signal
from app.models.user import User
from app.views.customer_view_res import CustomerViewReservations
from app.utils.container import Container
class ViewReservationsController(QObject):
  # Signals for view updates
  # login_successful = Signal()
  # login_failed = Signal(str)
  # signup_successful = Signal()
  # signup_failed = Signal(str)
  
  def __init__(self):
    super().__init__()
    # upcoming, past = self.get_dummy_data()
    self.upcoming, self.past = Container.resolve(User).get_reservations()
    self.fomrat_for_card()
    if not Container.is_initialized(CustomerViewReservations):
      self.view = CustomerViewReservations(self.upcoming, self.past)
      Container.add_existing_instance(CustomerViewReservations, self.view)
    else:
      self.view = Container.resolve(CustomerViewReservations)
    self.setup_connections()
  
  def setup_connections(self):
    # Connect view signals to controller methods
    self.view.back_btn.clicked.connect(self.handle_back)
      
  def fomrat_for_card(self):
    self.upcoming = [(r.club, r.date, r.id, r.event) for r in self.upcoming]
    self.past = [(r.club, r.date, r.id, r.event) for r in self.past]
    
  def handle_back(self):
    from app.controllers.home_page_controller import HomePageController
        
    self.home_page_controller = Container.resolve(HomePageController)
    self.show_page('customer_home_page', self.home_page_controller)
  
  def show(self):
    self.view.show() 