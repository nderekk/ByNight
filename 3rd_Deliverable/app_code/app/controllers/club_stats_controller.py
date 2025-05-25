from PySide6.QtCore import QObject
from app.utils.container import Container
from app.views.club_stats_page import ClubStatsWindow
from app.services.statistics_validator import ValidateDate
from app.models.statistics import Statistics
from app.models import Club
from PySide6.QtCore import QDate



class ClubStatsController(QObject):
    def __init__(self, show_page: callable):
        super().__init__()
        self.show_page = show_page

        self.view = ClubStatsWindow(attendance=0)
        self.view.set_graph_callback(self.show_attendance_graph)
        self.setup_connections()
        

    def setup_connections(self):
        self.view.back_button.clicked.connect(self.handle_back)
        self.view.load_button.clicked.connect(self.handle_input)

    def handle_back(self):
        from app.controllers.manager_home_page_controller import ManagerHomePageController
        self.manager_home_page_controller = Container.resolve(ManagerHomePageController)
        self.show_page('manager_home_page_controller', self.manager_home_page_controller)

    def show(self):
        self.view.show()

    def handle_input(self):
        fromdate = self.view.from_date.date().toPython()
        todate = self.view.to_date.date().toPython()
        ValidateDate.validate(fromdate, todate, self.view)

        self.attendance = Statistics.get_attendance_percentage(fromdate, todate, 4)
        self.view.update_attendance(self.attendance)
        self.sales = Statistics.get_sale(fromdate,  todate, 4)
        self.view.update_sales(self.sales)
        
    def show_attendance_graph(self):
        fromdate = self.view.from_date.date().toPython()
        todate = self.view.to_date.date().toPython()

        Statistics.plot_reservation_attendance(fromdate, todate, 4) 

  