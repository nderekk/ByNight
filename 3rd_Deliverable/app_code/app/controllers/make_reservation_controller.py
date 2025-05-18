from PySide6.QtCore import QObject
from app.views.customer_club_mainpage import CustomerClubMainPage
from app.utils.container import Container
from app.models.club import Club
from app.views.make_reservation_page import MakeReservationPage

class MakeReservationController(QObject):
    def __init__(self, show_page: callable, club: Club,flag):
        super().__init__()
        self.club = club
        self.flag=flag
        print(flag)

        if not Container.is_initialized(MakeReservationPage):
            self.view = MakeReservationPage(club)
            Container.add_existing_instance(MakeReservationPage, self.view)
        else:
            self.view = Container.resolve(MakeReservationPage)

        self.view.set_name(club)

        self.show_page = show_page
        self.setup_connections()

    def set_club(self, club: Club):
        self.club = club
        self.view.set_name(club)

    def setup_connections(self):
        self.view.back_button.clicked.connect(self.handle_back)

    def handle_back(self):
        from app.controllers.home_page_controller import HomePageController
        from app.controllers.club_mainpage_controller import ClubMainPageController
        
        if self.flag=='from_homepage':
         self.home_page_controller = Container.resolve(HomePageController)
         self.show_page('customer_home_page', self.home_page_controller)

        else:
         self.club_mainpage_controller = Container.resolve(ClubMainPageController)
         self.show_page('customer_club_main_page', self.club_mainpage_controller)
        

