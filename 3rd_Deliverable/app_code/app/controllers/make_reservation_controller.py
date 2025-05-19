from PySide6.QtCore import QObject
from app.models.club import Club
from app.views.make_reservation_page import MakeReservationPage    

class MakeReservationController(QObject):
    def __init__(self, show_page: callable, club: Club):
        super().__init__()
        self.club = club
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
        bottles = (int(self.view.regular_spinbox.value()) , int(self.view.premium_spinbox.value()))
        event_id = int(self.view.event_dropdown.currentData())  
        club = self.club

        print(table_type, people, bottles, club)
        from app.services.reservation_validator import ReservationValidator
        valid = ReservationValidator.check(table_type, people, bottles, club)

        if not valid[0]:
            from PySide6.QtWidgets import QMessageBox
            QMessageBox.warning(self.view, "Validation Error", valid[1])
        else:
            from app.models import Reservation
            ok = Reservation.create_res(club, event_id, table_type, people, bottles)
            if ok:
                from PySide6.QtWidgets import QMessageBox
                QMessageBox.information(self.view, "Success", "Reservation Confirmed!")
            else:
                from PySide6.QtWidgets import QMessageBox
                QMessageBox.warning(self.view, "Sorry", "An Error has Occured")
        self.handle_back()