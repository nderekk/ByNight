from app.views.work_with_us_page import WorkWithUsPage,FileUploadField
from app.utils.container import Container
class WorkWithUsController():
    def __init__(self, show_page: callable):
        super().__init__()
        self.show_page=show_page
        self.view=WorkWithUsPage()
        self.setup_connections()



    def setup_connections(self):
        self.view.back_btn.clicked.connect(self.handle_back)


    def handle_back(self):
        from app.controllers.home_page_controller import HomePageController
        self.home_page_controller = Container.resolve(HomePageController)
        self.show_page('customer_home_page', self.home_page_controller)
    


     
    
    

        

