from PySide6.QtCore import QObject, Signal
from app.services.auth_service import AuthService
from app.views import LoginView
from app.controllers import HomePageController
from app.utils.container import Container
from app.models import User

class LoginController(QObject):
  # Signals for view updates
  login_successful = Signal(User)
  login_failed = Signal(str)
  signup_successful = Signal()
  signup_failed = Signal(str)

  def __init__(self, show_page):
    super().__init__()
    self.auth_service = Container.resolve(AuthService)
    self.show_page = show_page
    self.view = LoginView()
    self.setup_connections()

  def setup_connections(self):
    # Connect view signals to controller methods
    # self.view.login_attempted.connect(self.handle_login)
    self.view.signup_attempted.connect(self.handle_signup)
    self.view.google_login_attempted.connect(self.handle_google_login)
    self.view.apple_login_attempted.connect(self.handle_apple_login)

    # Connect controller signals to view methods
    self.login_successful.connect(self.handle_next_page)
    self.login_failed.connect(self.view.show_error)
    self.signup_successful.connect(self.view.reset)
    self.signup_failed.connect(self.view.show_error)
    
    self.view.continue_btn.clicked.connect(self.on_continue_clicked)

  def handle_login(self, email: str, password: str):
    try:
      success, user = self.auth_service.authenticate(email, password)
      if success:
        self.login_successful.emit(user)
      else:
        self.login_failed.emit("Invalid email or password")
    except Exception as e:
      self.login_failed.emit(str(e))

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
    
  def on_continue_clicked(self):
    email = self.view.email_input.text().strip()
    if not self.view.password_input.isVisible():
      # First step: email validation
      if not self.validate_email(email):
        self.view.show_error("Please enter a valid email address")
        return
      self.view.show_password_step()
    else:
      # Second step: password and login/signup
      password = self.view.password_input.text()
      if not password:
        self.view.show_error("Please enter your password")
        return
      self.handle_login(email, password)
      
  def validate_email(self, email):
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

  def handle_google_login(self):
    self.login_failed.emit("Feature Not Yet Implimented")

  def handle_apple_login(self):
    self.login_failed.emit("Feature Not Yet Implimented")
    
  def handle_next_page(self, user: User):
    Container.add_existing_instance(User, user)
    self.home_page_controller = HomePageController(Container.resolve(User), self.show_page)
    Container.add_existing_instance(HomePageController, self.home_page_controller)
    self.show_page('customer_home_page', self.home_page_controller)

  def show(self):
    self.view.show() 
    
    