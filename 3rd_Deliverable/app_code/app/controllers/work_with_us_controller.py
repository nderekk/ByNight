from app.views.work_with_us_page import WorkWithUsPage,FileUploadField
class WorkWithUsController():
    def __init__(self, show_page: callable):
        super().__init__()
        self.show_page=show_page
        self.view=WorkWithUsPage()

        

    def setup_connections(self):
    # Connect view signals to controller methods
        pass

        

