from app.views.work_with_us_page import WorkWithUsPage,FileUploadField
from app.utils.container import Container
class WorkWithUsController():
    def __init__(self, show_page: callable):
        super().__init__()
        if not Container.is_initialized(WorkWithUsPage):
            self.view = WorkWithUsPage()
            Container.add_existing_instance(WorkWithUsPage, self.view)
        else:
            self.view = Container.resolve(WorkWithUsPage)
            
        self.show_page=show_page
        self.setup_connections()



    def setup_connections(self):
        self.view.back_btn.clicked.connect(self.handle_back)


    def handle_back(self):
        from app.controllers.home_page_controller import HomePageController
        self.home_page_controller = Container.resolve(HomePageController)
        self.show_page('customer_home_page', self.home_page_controller)
    


     
    
    

        

