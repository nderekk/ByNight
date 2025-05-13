from app.controllers.view_res_controller import ViewReservationController
from app.controllers.login_controller import LoginController
from app.services.auth_service import AuthService
from app.data.repositories.user_repository import UserRepository
from PySide6.QtWidgets import QStackedWidget, QMainWindow, QWidget

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("ByNight")
    self.setMinimumSize(360, 480)
    
    # Create central widget and stack
    self.stack = QStackedWidget()
    self.setCentralWidget(self.stack)
    
    # Initialize pages dictionary
    self.pages = {}

    # set up controllers
    self.user_repo = UserRepository()
    self.auth_service = AuthService(self.user_repo)
    self.login_controller = LoginController(self.auth_service, self.show_customer_view_reservations)
    
    self.view_res_controller = ViewReservationController()
     
    # Start with login page
    self.show_login()

  def show_login(self):
    if 'login_page' not in self.pages:
      self.login_page = self.login_controller.view
      self.stack.addWidget(self.login_page)
      self.pages['login_page'] = self.login_page
    self.stack.setCurrentWidget(self.login_page)

  def show_customer_view_reservations(self):
    if 'customer_view_res_page' not in self.pages:
      self.customer_view_res_page = self.view_res_controller.view
      self.stack.addWidget(self.customer_view_res_page)
      self.pages['customer_view_res_page'] = self.customer_view_res_page
    self.stack.setCurrentWidget(self.customer_view_res_page)
  
