from PySide6.QtCore import QObject, Signal
from app.services.auth_service import AuthService
from app.views.login_view import LoginView
from app.controllers.base_controller import BaseController
from app.utils.event_bus import EventBus

class LoginController(BaseController):
  def __init__(self):
    super().__init__()
    # self.main_window = main_window
    self.view = LoginView()
    self.setup_connections()

  def setup_connections(self):
    self.view.continue_btn.clicked.connect(self.handle_login)
    
    # Connect view signals to controller methods
    # self.view.login_attempted.connect(self.handle_login)
    # self.view.signup_attempted.connect(self.handle_signup)
    # self.view.google_login_attempted.connect(self.handle_google_login)
    # self.view.apple_login_attempted.connect(self.handle_apple_login)

    # # Connect controller signals to view methods
    # self.login_successful.connect(self.show_customer_view_reservations)
    # self.login_failed.connect(self.view.show_error)
    # self.signup_successful.connect(self.view.reset)
    # self.signup_failed.connect(self.view.show_error)

  def handle_login(self, email: str, password: str):
    user = self.auth_service.authenticate(email, password)
    if user:
      self.event_bus.publish("login_success", {"page": "next_page"})
    else:
      self.event_bus.publish("login_fail", {"page": "next_page"})

  def handle_signup(self, email: str, password: str, user_type: str):
    self.login_failed.emit("Feature Not Yet Implimented")
    # try:
    #   user = self.auth_service.signup(email, password, user_type)
    #   if user:
    #     self.signup_successful.emit()
    #   else:
    #     self.signup_failed.emit("Failed to create account")
    # except Exception as e:
    #   self.signup_failed.emit(str(e))

  def handle_google_login(self):
    self.login_failed.emit("Feature Not Yet Implimented")

  def handle_apple_login(self):
    self.login_failed.emit("Feature Not Yet Implimented")

  def show(self):
    self.view.show() 
    
    