from PySide6.QtCore import QObject
from app.models.user import User
from app.views.manager_home_page_view import ManagerUI

class ManagerHomePageController(QObject):
    def __init__(self, user: User, show_page: callable):
        super().__init__()
        self.user = user
        self.show_page = show_page
        self.view = ManagerUI()
        self.setup_connections()

    def setup_connections(self):
        # Hook up manager UI buttons here
        pass
