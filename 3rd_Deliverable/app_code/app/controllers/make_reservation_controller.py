from PySide6.QtCore import QObject
from app.views.customer_club_mainpage import CustomerClubMainPage
from app.utils.container import Container
from app.models.club import Club
from app.views.make_reservation_page import MakeReservationPage

class MakeReservationController(QObject):
    def __init__(self, show_page: callable, club: Club):
        super().__init__()
        self.club = club
        self.view=MakeReservationPage(club)
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
        
        self.home_page_controller = Container.resolve(HomePageController)
        self.show_page('customer_home_page', self.home_page_controller)
