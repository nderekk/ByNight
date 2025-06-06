from app.utils.container import Container
from PySide6.QtCore import QObject, Signal
from app.models.user import User
from app.views.manager_reservations_view import ManagerReservationPage

from app.utils.container import Container
class ManagerViewReservationsController(QObject):
  # Signals for view updates
  # login_successful = Signal()
  # login_failed = Signal(str)
  # signup_successful = Signal()
  # signup_failed = Signal(str)
  
  def __init__(self, show_page: callable):
    super().__init__()
    # upcoming, past = self.get_dummy_data()
    self.show_page = show_page
    self.view = ManagerReservationPage()
    self.setup_connections()
  
  def setup_connections(self):
    # Connect view signals to controller methods
    self.view.back_btn.clicked.connect(self.handle_back)
          
  def handle_back(self):
    from app.controllers.manager_home_page_controller import ManagerHomePageController
        
    self.manager_home_page_controller = Container.resolve(ManagerHomePageController)
    self.show_page('manager_home_page_controller', self.manager_home_page_controller)
  
  def show(self):
    self.view.show() 