from app.utils.container import Container
from PySide6.QtCore import QObject, Signal
from app.utils.container import Container
from app.views.discount_page import DiscountPage

class DiscountController(QObject):
  
  def __init__(self, show_page: callable):
    super().__init__()
    self.show_page = show_page
    self.view = DiscountPage()
    self.setup_connections()
  
  def setup_connections(self):
    # Connect view signals to controller methods
    self.view.back_button.clicked.connect(self.handle_back)
          
  def handle_back(self):
    from app.controllers.manager_home_page_controller import ManagerHomePageController
        
    self.manager_home_page_controller = Container.resolve(ManagerHomePageController)
    self.show_page('manager_home_page_controller', self.manager_home_page_controller)
  
  def show(self):
    self.view.show() 