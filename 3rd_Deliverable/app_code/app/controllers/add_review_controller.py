from app.utils.container import Container
from PySide6.QtCore import QObject, Signal
from app.views.review_view import AddReviewApp
from app.models.user import User

class AddReviewController(QObject):
  # Signals for view updates
  # login_successful = Signal()
  # login_failed = Signal(str)
  # signup_successful = Signal()
  # signup_failed = Signal(str)
  
  def __init__(self,show_page: callable):
    super().__init__()
    # upcoming, past = self.get_dummy_data()
    self.show_page = show_page
    self.view = AddReviewApp()
    self.setup_connections()
  
  def setup_connections(self):
    self.view.back_btn.clicked.connect(self.handle_back)
    pass
  
  def handle_back(self):
    from app.controllers.view_res_controller import ViewReservationsController
    
    self.view_res_controller = Container.resolve(ViewReservationsController)
    self.show_page('view_res_controller', self.view_res_controller)
   
  def show(self):
    self.view.show() 