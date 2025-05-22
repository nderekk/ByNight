from PySide6.QtCore import QObject
from app.views import EventForm, MessagePopup
from datetime import datetime, timedelta 

class EventCreatorController(QObject):
  def __init__(self, date_obj: datetime, club, show_page: callable):
    super().__init__()
    self.date_obj = date_obj
    self.club = club
    self.view = EventForm(date_obj.strftime("%A - %d/%m/%Y"))
    self.show_page = show_page
    self.setup_connections()
      
  def setup_connections(self):
    self.view.save_btn.clicked.connect(self.save_event)
    self.view.back_btn.clicked.connect(self.handle_back)
    
  def save_event(self):
    from app.models import Event
    music = self.view.music_input.text()
    title = self.view.title_input.text()
    desc = self.view.description_input.toPlainText()
    date = self.date_obj
    time = self.view.time_input.time().toPython()
    ok = Event.create_event(title, desc, music, date, time, self.club) 
    if ok:
      MessagePopup(True, "Event Added!").exec()
      # TODO notification
    else:
      MessagePopup(False, "There was an Internal Error")
    self.handle_back()
     
  def handle_back(self):
    from app.controllers import AddEventController
        
    self.add_event_controller = AddEventController(self.club, self.show_page)
    self.show_page('add_event_page', self.add_event_controller)

