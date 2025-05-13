from PySide6.QtCore import QObject
from app.views.customer_club_mainpage import CustomerClubMainPage

class ClubMainPageController(QObject):
    def __init__(self, show_page: callable):


        super().__init__()
        self.view = CustomerClubMainPage()
        self.show_page = show_page
        self.setup_connections()

     
    def setup_connections(self):
            # Connect view signals to controller methods
        pass

