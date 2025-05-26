from PySide6.QtCore import QObject
from app.utils.container import Container
from app.views.club_stats_page import ClubStatsWindow
from app.services.statistics_validator import ValidateDate
from app.models.statistics import Statistics
from app.models import Club, User, Manager
from PySide6.QtCore import QDate



class ClubStatsController(QObject):
    def __init__(self, show_page: callable):
        super().__init__()
        self.show_page = show_page
        self.manager_club = Container.resolve(User)


        self.view = ClubStatsWindow(attendance=0)
        self.view.set_graph_attendace_callback(self.show_attendance_graph)
        self.view.set_graph_sales_callback(self.show_sales_graph)
        self.view.set_graph_drinks_callback(self.show_drinks_graph)
        self.view.set_graph_rating_callback(self.show_rating_graph)
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

        self.attendance = Statistics.get_attendance_percentage(fromdate, todate, self.manager_club.id)
        self.view.update_attendance(self.attendance)
        self.sales = Statistics.get_sale(fromdate,  todate, self.manager_club.id)
        self.view.update_sales(self.sales)
        self.percentage_larger_drinks = Statistics.get_drinks(fromdate,  todate, self.manager_club.id)
        self.view.update_drinks(self.percentage_larger_drinks)
        self.rating = Statistics.get_rating(fromdate, todate, self.manager_club.id)
        self.view.update_rating(self.rating)

    def show_attendance_graph(self):
        fromdate = self.view.from_date.date().toPython()
        todate = self.view.to_date.date().toPython()

        Statistics.plot_reservation_attendance(fromdate, todate, self.manager_club.id) 

    def show_sales_graph(self):
        fromdate = self.view.from_date.date().toPython()
        todate = self.view.to_date.date().toPython()

        Statistics.plot_daily_sales(fromdate, todate, self.manager_club.id)

    def show_drinks_graph(self):
        fromdate = self.view.from_date.date().toPython()
        todate = self.view.to_date.date().toPython()

        Statistics.plot_bottle_amounts(fromdate, todate, self.manager_club.id)

    def show_rating_graph(self):
        fromdate = self.view.from_date.date().toPython()
        todate = self.view.to_date.date().toPython()

        Statistics.plot_rating(fromdate, todate, self.manager_club.id)