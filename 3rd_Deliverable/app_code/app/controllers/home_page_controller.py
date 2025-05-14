from PySide6.QtCore import QObject, Signal
from app.views.customer_homepage import CustomerHomePage
from app.controllers.view_res_controller import ViewReservationsController
from app.controllers.club_mainpage_controller import ClubMainPageController
from app.models.user import User
from app.models.role import Role
from app.utils.container import Container
from app.data.repositories.club_repository import ClubRepository
from app.models.club import Club

class HomePageController(QObject):
  # Signals for view updates
  view_reservations_pushed = Signal()
  
  def __init__(self, user: User, show_page: callable):
    super().__init__()
    self.user = user
    self.clubs = Container.resolve(ClubRepository).get_all()
    self.show_page = show_page
    if self.user.role == Role.CUSTOMER:
      self.view = CustomerHomePage(self.clubs)
    else:
      print("KANE TO GUI TBOY")
    self.setup_connections()

  def setup_connections(self):
    self.view.viewResButton.clicked.connect(self.hand_view_res)
    self.view.more_button_clicked.connect(self.handle_club_mainpage)
    
  def hand_view_res(self):
    if not Container.is_initialized(ViewReservationsController):
      self.view_res_controller = ViewReservationsController(self.show_page)
      Container.add_existing_instance(ViewReservationsController, self.view_res_controller)
    else:
      self.view_res_controller = Container.resolve(ViewReservationsController)
    self.show_page('customer_view_res_page', self.view_res_controller)
    
  def handle_club_mainpage(self, club: Club):
    if not Container.is_initialized(ClubMainPageController):
      self.club_mainpage_controller = ClubMainPageController(self.show_page,club)
      Container.add_existing_instance(ClubMainPageController, self.club_mainpage_controller)
    else:
      self.club_mainpage_controller = Container.resolve(ClubMainPageController)
      self.club_mainpage_controller.set_club(club)
    self.show_page('customer_club_main_page', self.club_mainpage_controller)
    
  