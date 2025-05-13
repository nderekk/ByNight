from PySide6.QtCore import QObject, Signal
from app.views.customer_homepage import CustomerHomePage
from app.controllers.view_res_controller import ViewReservationController

class HomePageController(QObject):
  # Signals for view updates
  view_reservations_pushed = Signal()

  def __init__(self, show_page):
    super().__init__()
    self.show_page = show_page
    self.view = CustomerHomePage()
    self.setup_connections()

  def setup_connections(self):
    self.view.viewResButton.clicked.connect(self.handle_next_page)
    
  def handle_next_page(self):
    self.view_res_controller = ViewReservationController()
    self.show_page('customer_view_res_page', self.view_res_controller)