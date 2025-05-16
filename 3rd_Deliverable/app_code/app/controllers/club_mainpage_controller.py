from PySide6.QtCore import QObject
from app.views.customer_club_mainpage import CustomerClubMainPage
from app.utils.container import Container
from app.models.club import Club

class ClubMainPageController(QObject):
    def __init__(self, show_page: callable, club: Club):
        super().__init__()
        self.club = club

        if not Container.is_initialized(CustomerClubMainPage):
            self.view = CustomerClubMainPage(club)
            Container.add_existing_instance(CustomerClubMainPage, self.view)
        else:
            self.view = Container.resolve(CustomerClubMainPage)

        self.view.set_name(club)

        self.show_page = show_page
        self.setup_connections()

    def set_club(self, club: Club):
        self.club = club
        self.view.set_name(club)

    def setup_connections(self):
        self.view.back_btn.clicked.connect(self.handle_back)
        self.view.btn_reserve.clicked.connect(lambda: self.handle_make_res(self.club))


    def handle_back(self):
        from app.controllers.home_page_controller import HomePageController
        
        self.home_page_controller = Container.resolve(HomePageController)
        self.show_page('customer_home_page', self.home_page_controller)


    def handle_make_res(self,club):
        from app.controllers.make_reservation_controller import MakeReservationController

        if not Container.is_initialized(MakeReservationController):
         self.make_res_controller =MakeReservationController(self.show_page,club)
         Container.add_existing_instance(MakeReservationController, self.make_res_controller)
        else:
         self.make_res_controller = Container.resolve(MakeReservationController)
         self.make_res_controller.set_club(club)
        self.show_page('customer_club_main_page', self.make_res_controller)


