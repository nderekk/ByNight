from app.utils.container import Container
from PySide6.QtCore import QObject, Signal
from app.models.user import User
from app.utils.container import Container
from app.views.add_event_view import AddEventPage
from datetime import timedelta, datetime

class AddEventController(QObject):
  
  def __init__(self, club, show_page: callable):
    super().__init__()
    self.show_page = show_page
    self.view = AddEventPage()
    self.club = club
    self.handle_date_change(self.view.date_picker.date())
    self.setup_connections()
  
  def setup_connections(self):
    self.view.back_btn.clicked.connect(self.handle_back)
    self.view.date_picker.dateChanged.connect(self.handle_date_change)
    self.view.add_button_clicked.connect(self.handle_add_event)
    self.view.edit_button_clicked.connect(self.handle_edit_event)
          
  def handle_back(self):
    from app.controllers.manager_home_page_controller import ManagerHomePageController
        
    self.manager_home_page_controller = Container.resolve(ManagerHomePageController)
    self.show_page('manager_home_page_controller', self.manager_home_page_controller)
    
  def handle_date_change(self, qdate):
    from app.models import Club
    
    date = qdate.toPython()
    start_of_week = date - timedelta(days=date.weekday())  # monday
    
    events = self.club.get_weeks_events(start_of_week)
    events_by_date = {}
    for event in events:
      events_by_date.setdefault(event.date, event)

    self.view.update_week(start_of_week, events_by_date)
    
  def handle_add_event(self, date_obj: datetime):
    from app.controllers import EventCreatorController
    self.event_creator_controller = EventCreatorController(date_obj, self.club, self.show_page)
    self.show_page("event_form_page", self.event_creator_controller)
    
  def handle_edit_event(self):
    pass
  
  def show(self):
    self.view.show() 