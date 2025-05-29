from PySide6.QtCore import QObject, Signal
from app.views import CustomerHomePage
from app.views.manager_home_page_view import ManagerUI
from app.controllers import ClubMainPageController
from app.models import User, Role, Club
from app.utils.container import Container
from app.controllers.make_reservation_controller import MakeReservationController

class HomePageController(QObject):
  # Signals for view updates
  view_reservations_pushed = Signal()
  
  def __init__(self, show_page: callable):
    super().__init__()
    self.clubs = Club.get_clubs_all()
    self.filters = Club.get_club_filters()
    self.show_page = show_page
    self.view = CustomerHomePage(self.clubs,self.filters)
    self.setup_connections()

  def setup_connections(self):
    self.view.viewResButton.clicked.connect(self.hand_view_res)
    self.view.more_button_clicked.connect(self.handle_club_mainpage)
    self.view.addressDropdown.currentTextChanged.connect(self.apply_filters)
    self.view.musicDropdown.currentTextChanged.connect(self.apply_filters)
    self.view.eventDropdown.currentTextChanged.connect(self.apply_filters)
    self.view.searchLineEdit.textChanged.connect(self.apply_filters)
    self.view.make_reservation_clicked.connect(self.handle_make_res_page)
    self.view.menuButton.clicked.connect(self.handle_work_with_us)
    
  def hand_view_res(self):
    from app.controllers import ViewReservationsController
    self.view_res_controller = ViewReservationsController(self.show_page)
    self.show_page('customer_view_res_page', self.view_res_controller)
    
  def handle_club_mainpage(self, club: Club):
    from app.controllers import ClubMainPageController 
    self.club_mainpage_controller = ClubMainPageController(self.show_page, club)
    self.show_page('customer_club_main_page', self.club_mainpage_controller)
    
  def handle_make_res_page(self, club: Club):
    from app.controllers import MakeReservationController
    self.make_res_controller = MakeReservationController(self.show_page,club)
    self.show_page('customer_club_main_page', self.make_res_controller)


  def apply_filters(self):
    address_filter = self.view.addressDropdown.currentText()
    music_filter = self.view.musicDropdown.currentText()
    event_filter = self.view.eventDropdown.currentText()
    search_text = self.view.searchLineEdit.text().lower()
    
    self.filtered_clubs = Club.get_filtered_clubs(address_filter, music_filter, event_filter)
    if search_text:
      self.filtered_clubs = [club for club in self.filtered_clubs if search_text in club.name.lower()]
    
    self.view.update_club_display(self.filtered_clubs)
    
  def handle_work_with_us(self):
    from app.controllers.work_with_us_controller import WorkWithUsController
    self.access_work_with_us = WorkWithUsController(self.show_page)
    self.show_page('work_with_us_page', self.access_work_with_us)

  def update(self):
    user=Container.resolve(User)
    user = user.update_to_manager()
    Container.replace_existing_instance(User, user)
    
    from app.controllers.manager_home_page_controller import ManagerHomePageController
    self.manager_controller = ManagerHomePageController(self.show_page)
    Container.add_existing_instance(ManagerHomePageController, self.manager_controller)
    self.show_page("manager_home_page", self.manager_controller)



