from PySide6.QtCore import QObject, Signal
from app.views.customer_homepage import CustomerHomePage
from app.controllers.view_res_controller import ViewReservationsController
from app.controllers.club_mainpage_controller import ClubMainPageController
from app.models.user import User
from app.models.role import Role

class HomePageController(QObject):
  # Signals for view updates
  view_reservations_pushed = Signal()

  def __init__(self, user: User, show_page: callable):
    super().__init__()
    self.user = user
    self.show_page = show_page
    if self.user.role == Role.CUSTOMER:
      self.view = CustomerHomePage()
    else:
      print("KANE TO GUI TBOY")
    self.setup_connections()

  def setup_connections(self):
    self.view.viewResButton.clicked.connect(self.handle_next_page)
    self.view.more_button.clicked.connect(self.handle_club_mainpage)
    
  def handle_next_page(self):
    self.view_res_controller = ViewReservationsController()
    self.show_page('customer_view_res_page', self.view_res_controller)
    
  def handle_club_mainpage(self):
    self.club_mainpage_controller= ClubMainPageController(self.show_page)
    self.show_page('customer_club_main_page', self.club_mainpage_controller)
    
  