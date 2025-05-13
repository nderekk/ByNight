from PySide6.QtCore import QObject, Signal
from app.views.customer_homepage import CustomerHomePage

class HomePageController(QObject):
  # Signals for view updates
  view_reservations_pushed = Signal()

  def __init__(self, show_customer_view_reservations):
    super().__init__()
    self.show_customer_view_reservations = show_customer_view_reservations
    self.view = CustomerHomePage()
    self.setup_connections()

  def setup_connections(self):
    self.view.viewResButton.clicked.connect(self.show_customer_view_reservations)