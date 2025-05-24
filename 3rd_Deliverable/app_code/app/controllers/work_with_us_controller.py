from app.utils.container import Container
from PySide6.QtCore import QObject, Signal
from app.models.user import User
from app.utils.container import Container
from app.views.work_with_us_page import WorkWithUsPage
from app.services.business_registry import BusinessRegistry

class WorkWithUsController(QObject):
  
  def __init__(self, show_page: callable):
    super().__init__()
    self.show_page = show_page
    self.view = WorkWithUsPage()
    self.setup_connections()
  
  def setup_connections(self):
    self.view.back_btn.clicked.connect(self.handle_back)
    self.view.submit_btn.clicked.connect(self.handle_upload)
    

          
  def handle_back(self):
    from app.controllers.home_page_controller import HomePageController
        
    self.home_page_controller = Container.resolve(HomePageController)
    self.show_page('customer_home_page', self.home_page_controller)
  
  def handle_upload(self):
    file_paths = self.view.get_uploaded_files()

    if len(file_paths) < 4:  
            self.view.show_error("U should upload all the files")
            return

    registry = BusinessRegistry()
    if registry.validate_documents(file_paths):
       from app.controllers.home_page_controller import HomePageController
       home_controller = Container.resolve(HomePageController)
       home_controller.update()
       
    else:
        self.view.show_error("Η εγγραφή απέτυχε. Ελέγξτε τα αρχεία σας.")

  def show(self):
    self.view.show() 
