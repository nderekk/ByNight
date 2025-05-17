from PySide6.QtCore import QObject, Signal
from app.views import CustomerHomePage
from app.controllers import ClubMainPageController
from app.models import User, Role, Club
from app.utils.container import Container

class HomePageController(QObject):
  # Signals for view updates
  view_reservations_pushed = Signal()
  
  def __init__(self, user: User, show_page: callable):
    super().__init__()
    self.user = user
    self.clubs = Club.get_clubs_all()
    self.filters = Club.get_club_filters()
    self.show_page = show_page
    self.view = CustomerHomePage(clubs=self.clubs, filters=self.filters)
    self.setup_connections()

  def setup_connections(self):
    self.view.viewResButton.clicked.connect(self.hand_view_res)
    self.view.more_button_clicked.connect(self.handle_club_mainpage)
    self.view.addressDropdown.currentTextChanged.connect(self.apply_filters)
    self.view.musicDropdown.currentTextChanged.connect(self.apply_filters)
    self.view.eventDropdown.currentTextChanged.connect(self.apply_filters)
    self.view.searchLineEdit.textChanged.connect(self.apply_filters)
    
  def hand_view_res(self):
    from app.controllers import ViewReservationsController
    
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
    
  def apply_filters(self):
    address_filter = self.view.addressDropdown.currentText()
    music_filter = self.view.musicDropdown.currentText()
    event_filter = self.view.eventDropdown.currentText()
    search_text = self.view.searchLineEdit.text().lower()
    
    self.filtered_clubs = Club.get_filtered_clubs(address_filter, music_filter, event_filter)
    if search_text:
      self.filtered_clubs = [club for club in self.filtered_clubs if search_text in club.name.lower()]
    
    self.view.update_club_display(self.filtered_clubs)
    
  