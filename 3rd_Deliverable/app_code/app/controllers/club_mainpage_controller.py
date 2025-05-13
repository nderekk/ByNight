from PySide6.QtCore import QObject
from app.views.customer_club_mainpage import CustomerClubMainPage
from app.utils.container import Container

class ClubMainPageController(QObject):
    def __init__(self, show_page: callable):
        super().__init__()
        if not Container.is_initialized(CustomerClubMainPage):
            self.view = CustomerClubMainPage()
            Container.add_existing_instance(CustomerClubMainPage, self.view)
        else:
            self.view = Container.resolve(CustomerClubMainPage)
        self.show_page = show_page
        self.setup_connections()

     
    def setup_connections(self):
        # Connect view signals to controller methods
        self.view.back_btn.clicked.connect(self.handle_back)
        
    def handle_back(self):
        from app.controllers.home_page_controller import HomePageController
        
        self.home_page_controller = Container.resolve(HomePageController)
        self.show_page('customer_home_page', self.home_page_controller)

