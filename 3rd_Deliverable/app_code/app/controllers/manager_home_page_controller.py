from PySide6.QtCore import QObject
from app.models.user import User
from app.views.manager_home_page_view import ManagerUI
from app.utils.container import Container

class ManagerHomePageController(QObject):
    def __init__(self, show_page: callable):
        super().__init__()
        self.user = Container.resolve(User)
        self.club = self.user.managed_club
        if not self.club:
            self.club_registered = False
        self.show_page = show_page
        self.view = ManagerUI(self.club_registered)
        self.load_club_info()
        self.setup_connections()

    def setup_connections(self):
        self.view.viewResButton.clicked.connect(self.handle_view_man_res_page)
        self.view.addEventButton.clicked.connect(self.handle_add_event_page)
        self.view.viewStatsButton.clicked.connect(self.handle_stats_page)
        self.view.giveDiscountsButton.clicked.connect(self.handle_discount_page)
        self.view.urClubButton.clicked.connect(self.handle_ur_club)


    def load_club_info(self):
        from app.services.db_session import DatabaseSession
        from app.models.club import Club

        session = Container.resolve(DatabaseSession)
        manager_id = self.user.id

        club = session.query(Club).filter_by(manager_id=manager_id).first()

        if club:
            self.view.clubName.setText(f"Club Name: {club.name}")
            self.view.clubDesc.setText(f"{club.address}, {club.location}")
        else:
            
            self.view.clubName.setText("Club Name: -")
            self.view.clubDesc.setText("Club Details: -")

    
    
    def handle_view_man_res_page(self):
        from app.controllers.manager_reservations_controller import ManagerViewReservationsController

        self.manager_reservations_controller = ManagerViewReservationsController(self.show_page)
        self.show_page('manager_view_res_page', self.manager_reservations_controller)

    def handle_add_event_page(self):
         from app.controllers.add_event_controller import AddEventController

         self.add_event_controller = AddEventController(self.club, self.show_page)
         self.show_page('add_event_view_page', self.add_event_controller)

    def handle_stats_page(self):
         from app.controllers.club_stats_controller import ClubStatsController

         self.club_stats_controller = ClubStatsController(self.show_page)
         self.show_page('club_stats_view_page', self.club_stats_controller)

    def handle_ur_club(self):
        from app.services.club_creator import ClubCreator
        self.club_creator = ClubCreator(self.show_page, self.club_details)
        self.club_creator.ur_club()     

    def club_details(self, details:dict):
         self.update_club_view(details)

    def update_club_view(self, club_data: dict):
        self.view.clubName.setText(f"Club Name: {club_data['name']}")
        self.view.clubDesc.setText(f"Address: {club_data['address']}, Location: {club_data['location']}")

    def handle_discount_page(self):
         from app.controllers.discount_controller import DiscountController

         self.discount_controller = DiscountController(self.show_page)
         self.show_page('discount_view_page', self.discount_controller)
         
    def enable_buttons(self):
        self.view.viewResButton.setDisabled(False)
        self.view.addEventButton.setDisabled(False)
        self.view.viewStatsButton.setDisabled(False)
        self.view.giveDiscountsButton.setDisabled(False)
