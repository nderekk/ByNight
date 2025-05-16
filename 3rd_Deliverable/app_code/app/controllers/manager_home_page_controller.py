from PySide6.QtCore import QObject
from app.models.user import User
from app.views.manager_home_page_view import ManagerUI
from app.views.manager_reservations_view import ReservationCard
from app.utils.container import Container


class ManagerHomePageController(QObject):
    def __init__(self, user: User, show_page: callable):
        super().__init__()
        self.user = user
        self.show_page = show_page
        self.view = ManagerUI()
        self.setup_connections()

    def setup_connections(self):
            self.view.viewResButton.clicked.connect(self.viewResButton)
    
    
    def hand_view_res(self):
        if not Container.is_initialized(ReservationCard):
            self.view_res_controller = ReservationCard(self.show_page)
            Container.add_existing_instance(ReservationCard, self.view_res_controller)
        else:
            self.view_res_controller = Container.resolve(ReservationCard)
            self.show_page('customer_view_res_page', self.view_res_controller)    
