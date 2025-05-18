from PySide6.QtCore import QObject
from app.views.customer_club_mainpage import CustomerClubMainPage
from app.utils.container import Container
from app.models.club import Club
from app.views.make_reservation_page import MakeReservationPage

class MakeReservationController(QObject):
    def __init__(self, show_page: callable, club: Club):
        super().__init__()
        self.club = club

        # if not Container.is_initialized(MakeReservationPage):
        #     self.view = MakeReservationPage(club)
        #     Container.add_existing_instance(MakeReservationPage, self.view)
        # else:
        #     self.view = Container.resolve(MakeReservationPage)

        self.view = MakeReservationPage(club)
        self.view.set_name(club)

        self.show_page = show_page
        self.setup_connections()

    def set_club(self, club: Club):
        self.club = club
        self.view.set_name(club)

    def setup_connections(self):
        self.view.back_button.clicked.connect(self.handle_back)

    def handle_back(self):
        from app.controllers.home_page_controller import ClubMainPageController
        
        self.controller = ClubMainPageController(self.show_page, self.club)
        self.show_page('customer_club_main_page', self.controller)