from PySide6.QtCore import QObject, Signal
from app.services.auth_service import AuthService
from app.views.login_view import LoginView

class LoginController(QObject):
  # Signals for view updates
  login_successful = Signal()
  login_failed = Signal(str)
  signup_successful = Signal()
  signup_failed = Signal(str)

  def __init__(self):
    super().__init__()
    # self.auth_service = auth_service
    self.view = LoginView()
    self.setup_connections()

  def setup_connections(self):
    # Connect view signals to controller methods
    self.view.login_attempted.connect(self.handle_login)
    self.view.signup_attempted.connect(self.handle_signup)
    self.view.google_login_attempted.connect(self.handle_google_login)
    self.view.apple_login_attempted.connect(self.handle_apple_login)

    # Connect controller signals to view methods
    self.login_successful.connect(self.view.reset)
    self.login_failed.connect(self.view.show_error)
    self.signup_successful.connect(self.view.reset)
    self.signup_failed.connect(self.view.show_error)

  def handle_login(self, email: str, password: str):
    try:
      user = self.auth_service.login(email, password)
      if user:
        self.login_successful.emit()
      else:
        self.login_failed.emit("Invalid email or password")
    except Exception as e:
      self.login_failed.emit(str(e))

  def handle_signup(self, email: str, password: str, user_type: str):
    try:
      user = self.auth_service.signup(email, password, user_type)
      if user:
        self.signup_successful.emit()
      else:
        self.signup_failed.emit("Failed to create account")
    except Exception as e:
      self.signup_failed.emit(str(e))

  def handle_google_login(self):
    self.login_failed.emit("Feature Not Yet Implimented")

  def handle_apple_login(self):
    self.login_failed.emit("Feature Not Yet Implimented")

  def show(self):
    self.view.show() 