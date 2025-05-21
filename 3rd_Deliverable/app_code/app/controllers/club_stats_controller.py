from app.utils.container import Container
from PySide6.QtCore import QObject, Signal
from app.utils.container import Container
from app.views.club_stats_page import ClubStatsWindow

class ClubStatsController(QObject):
  
  def __init__(self, show_page: callable):
    super().__init__()
    self.show_page = show_page
    self.view = ClubStatsWindow()
    self.setup_connections()
    
  
  def setup_connections(self):
    # Connect view signals to controller methods
    self.view.back_button.clicked.connect(self.handle_back)
    self.view.load_button.clicked.connect(self.handle_input)

          
  def handle_back(self):
    from app.controllers.manager_home_page_controller import ManagerHomePageController
        
    self.manager_home_page_controller = Container.resolve(ManagerHomePageController)
    self.show_page('manager_home_page_controller', self.manager_home_page_controller)
  
  def show(self):
    self.view.show() 

  def handle_input(self):
    fromdate = self.view.from_date.date()
    todate = self.view.to_date.date()
    print(fromdate, todate)

    