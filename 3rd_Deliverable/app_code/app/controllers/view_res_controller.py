from app.utils.container import Container
from PySide6.QtCore import QObject, Signal
from app.models import User
from app.views import CustomerViewReservations
from app.utils.container import Container

class ViewReservationsController(QObject):
  # Signals for view updates
  # login_successful = Signal()
  # login_failed = Signal(str)
  # signup_successful = Signal()
  # signup_failed = Signal(str)
  
  def __init__(self, show_page: callable):
    super().__init__()
    # upcoming, past = self.get_dummy_data()
    self.show_page = show_page
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
    self.view.reservation_clicked.connect(self.handle_res_details)
      
  def fomrat_for_card(self):
    self.upcoming = [(r.club.name, r.date, r.id, r.event.title) for r in self.upcoming]
    self.past = [(r.club.name, r.date, r.id, r.event.title) for r in self.past]
    
  def handle_back(self):
    from app.controllers import HomePageController
        
    self.home_page_controller = Container.resolve(HomePageController)
    self.show_page('customer_home_page', self.home_page_controller)
    
  def handle_res_details(self, id: int):
    from app.controllers import ReservationDetailsController
    if not Container.is_initialized(ReservationDetailsController):
      self.res_details_controller = ReservationDetailsController(id, self.show_page)
      Container.add_existing_instance(ReservationDetailsController, self.res_details_controller)
    else:
      self.res_details_controller = Container.resolve(ReservationDetailsController)
      self.res_details_controller.set_reservation(id)
    self.show_page("res_details_page", self.res_details_controller)
    
  
  def show(self):
    self.view.show() 