from PySide6.QtCore import QObject, Signal
from app.services.auth_service import AuthService
from app.views import LoginView
from app.controllers.manager_home_page_controller import ManagerHomePageController
from app.utils.container import Container
from app.models import User, Staff, Customer, Manager
from app.models import Role


class LoginController(QObject):
  # Signals for view updates
  login_successful = Signal(User)
  login_failed = Signal(str)

  def __init__(self, show_page):
    super().__init__()
    self.auth_service = Container.resolve(AuthService)
    self.show_page = show_page
    self.view = LoginView()
    self.setup_connections()

  def setup_connections(self):
    # Connect view signals to controller methods
    self.view.login_attempted.connect(self.handle_login)
    self.view.google_login_attempted.connect(self.handle_google_login)
    self.view.apple_login_attempted.connect(self.handle_apple_login)

    # Connect controller signals to view methods
    self.login_successful.connect(self.handle_next_page)
    self.login_failed.connect(self.view.show_error)

  def handle_login(self, email: str, password: str):
    """Authenticate user with email and password."""
    email = email.strip()
    if not self._validate_email(email):
      self.login_failed.emit("Please enter a valid email address")
      return
    if not password:
      self.login_failed.emit("Please enter your password")
      return

    try:
      success, user = self.auth_service.authenticate(email, password)
      if success:
        self.login_successful.emit(user)
      else:
        self.login_failed.emit("Invalid email or password")
    except Exception as e:
      self.login_failed.emit(str(e))

  def _validate_email(self, email: str) -> bool:
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

  def handle_google_login(self):
    self.login_failed.emit("Feature Not Yet Implimented")

  def handle_apple_login(self):
    self.login_failed.emit("Feature Not Yet Implimented")
    
  def handle_next_page(self, user: User):
    from app.models import Role
    from app.controllers import HomePageController, StaffHomePageController
    Container.add_existing_instance(User, user)
    
    if user.role == Role.CUSTOMER:
      self.home_page_controller = HomePageController(self.show_page)
      Container.add_existing_instance(HomePageController, self.home_page_controller)
      self.show_page('customer_home_page', self.home_page_controller)
    elif user.role == Role.MANAGER:
      self.manager_home_page_controller = ManagerHomePageController(self.show_page)
      Container.add_existing_instance(ManagerHomePageController, self.manager_home_page_controller)
      self.show_page('manager_home_page', self.manager_home_page_controller)
    elif user.role == Role.STAFF:
      self.staff_home_page_controller = StaffHomePageController(self.show_page)
      Container.add_existing_instance(StaffHomePageController, self.staff_home_page_controller)
      self.show_page('staff_home_page', self.staff_home_page_controller)        

  def show(self):
    self.view.show() 
    
    