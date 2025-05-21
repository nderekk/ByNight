from PySide6.QtCore import QObject
from app.models.user import User
from app.views.manager_home_page_view import ManagerUI
from app.utils.container import Container


class ManagerHomePageController(QObject):
    def __init__(self, user: User, show_page: callable):
        super().__init__()
        self.user = user
        self.show_page = show_page
        self.view = ManagerUI()
        self.setup_connections()

    def setup_connections(self):
            self.view.viewResButton.clicked.connect(self.handle_view_man_res_page)
            self.view.addEventButton.clicked.connect(self.handle_add_event_page)
    
    
    def handle_view_man_res_page(self):
        from app.controllers.manager_reservations_controller import ManagerViewReservationsController

        self.manager_reservations_controller = ManagerViewReservationsController(self.show_page)
        self.show_page('manager_view_res_page', self.manager_reservations_controller)

    def handle_add_event_page(self):
         from app.controllers.add_event_controller import AddEventController

         self.add_event_controller = AddEventController(self.show_page)
         self.show_page('add_event_view_page', self.add_event_controller)
         

