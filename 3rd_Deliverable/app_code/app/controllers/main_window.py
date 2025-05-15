from app.controllers.login_controller import LoginController
from app.services.auth_service import AuthService
from app.utils.container import Container
from PySide6.QtWidgets import QStackedWidget, QMainWindow
from PySide6.QtCore import QObject, Signal

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("ByNight")
    self.setMinimumSize(360*1.5, 480*1.5)
    
    # Create central widget and stack
    self.stack = QStackedWidget()
    self.setCentralWidget(self.stack)
    
    # Initialize pages dictionary
    self.pages = {}

    # set up controllers
    Container.register(AuthService, AuthService)
    self.auth_service = Container.resolve(AuthService)
    self.login_controller = LoginController(self.show_page)
    
    # self.view_res = ViewReservationsController()
    # Start with login page
    self.show_page('login_page', self.login_controller)
    # self.show_page('customer_view_res_page', self.view_res)

  def show_page(self, page_name: str, page_controller: QObject):
    if page_name not in self.pages:
      self.pages[page_name] = page_controller.view
      self.stack.addWidget(self.pages[page_name])
    self.stack.setCurrentWidget(self.pages[page_name])

  # def show_login(self):
  #   if 'login_page' not in self.pages:
  #     self.login_page = self.login_controller.view
  #     self.stack.addWidget(self.login_page)
  #     self.pages['login_page'] = self.login_page
  #   self.stack.setCurrentWidget(self.login_page)
    
  # def show_customer_home_page(self):
  #   if 'customer_home_page' not in self.pages:
  #     self.customer_home_page = self.home_page_controller.view
  #     self.stack.addWidget(self.customer_home_page)
  #     self.pages['customer_home_page'] = self.customer_home_page
  #   self.stack.setCurrentWidget(self.customer_home_page)

  # def show_customer_view_reservations(self):
  #   if 'customer_view_res_page' not in self.pages:
  #     self.customer_view_res_page = self.view_res_controller.view
  #     self.stack.addWidget(self.customer_view_res_page)
  #     self.pages['customer_view_res_page'] = self.customer_view_res_page
  #   self.stack.setCurrentWidget(self.customer_view_res_page)
  
