from PySide6.QtCore import QObject
from app.views.customer_club_mainpage import CustomerClubMainPage
from app.utils.container import Container
from app.models.club import Club
from app.views.make_reservation_page import MakeReservationPage
from app.services.db_session import DatabaseSession
from app.models.user import User      

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
        self.view.confirm_btn.clicked.connect(self.handle_submit)


    def handle_back(self):
        from app.controllers.home_page_controller import ClubMainPageController
        
        self.controller = ClubMainPageController(self.show_page, self.club)
        self.show_page('customer_club_main_page', self.controller)

    
    def handle_submit(self):
        people = int(self.view.guest_input.text())
        table_type = self.view.table_dropdown.currentText()
        bottles = (int(self.view.premium_spinbox.value()) , int(self.view.regular_spinbox.value()))
        event_id = int(self.view.event_dropdown.currentData())  
        club = self.club

     
        from app.services.reservation_validator import ReservationValidator
        valid = ReservationValidator.check(table_type, people, bottles, club)

        if not valid[0]:
            from PySide6.QtWidgets import QMessageBox
            QMessageBox.warning(self.view, "Validation Error", valid[1])
            return

    
        session = Container.resolve(DatabaseSession)
        from app.models import Reservation, Order, Table,TableType

        table = Table(
            capacity=6,
            club=self.club,
            table_type = TableType(table_type)
        )
        #table = club.get_available_table(table_type)   
        

        order = Order(
        reservation=reservation,
        premium_bottles=bottles[1],
        regular_bottles=bottles[0]
        )

        user=Container.resolve(User)
        reservation = Reservation(
            user=user,  
            club=self.club,
            event_id=event_id,
            table=table,
            num_of_people= people
        )

         

        session.add(reservation)
        session.commit()

        from PySide6.QtWidgets import QMessageBox
        QMessageBox.information(self.view, "Success", "Reservation Confirmed!")