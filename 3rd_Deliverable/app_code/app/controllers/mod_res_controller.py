from PySide6.QtCore import QObject, Signal
from app.utils.container import Container
from app.models import Reservation
from app.views import ModifyReservationPage, MessagePopup

class ModifyReservationController(QObject):
  def __init__(self, res_id: int, show_page: callable):
    super().__init__()
    self.res_id = res_id
    self.reservation = Reservation.get_res_from_id(res_id)
    self.show_page = show_page
    # if not Container.is_initialized(ModifyReservationPage):
    #   self.view = ModifyReservationPage(self.reservation.get_table_type(), self.reservation.num_of_people)
    #   Container.add_existing_instance(ModifyReservationPage, self.view)
    # else:
    #   self.view = Container.resolve(ModifyReservationPage)
    self.view = ModifyReservationPage(self.reservation.get_table_type(), self.reservation.num_of_people)
    self.setup_connections()

  def setup_connections(self):
    self.view.back_btn.clicked.connect(self.handle_back)
    self.view.save_btn.clicked.connect(self.handle_save_changes)
  
  def refresh_mod_fields(self, id: int):
    self.reservation = Reservation.get_res_from_id(id)
    print(f"RES_ID: {id}")
    current_table_type = self.reservation.get_table_type()
    current_num_of_people = self.reservation.num_of_people
    self.view.refresh_page(current_table_type, current_num_of_people)
    
  def handle_back(self):
    from app.controllers import ReservationDetailsController
        
    # self.controller = Container.resolve(ReservationDetailsController)
    
    self.controller = ReservationDetailsController(self.res_id, self.show_page)
    self.show_page('res_details_controller', self.controller)
    
  def handle_save_changes(self):
    from app.services import ReservationValidator
    
    self.club = self.reservation.get_club()
    self.table_type = self.view.table_type_combo.currentText()
    self.people = self.view.people_spin.text()
    response = ReservationValidator.check(self.table_type, self.people, 2, self.club)
    print(f"\nresponse: {response}\n")
    # result = ReservationValidator.check(self.table_type, self.people, self.bottles, self.club)
    if response[0]:
      # self.reservation.update_res(self.table_type, self.people, 2)
      # self.reservation.update_res(self.table_type, self.people, self.bottles)
      popup = MessagePopup(success=True, message="Your reservation has been updated successfully.")
      popup.exec()
    else:
      popup = MessagePopup(success=False, message=str(response[1]))
      popup.exec()
    