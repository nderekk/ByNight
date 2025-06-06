from app.utils.container import Container
from PySide6.QtCore import QObject, Signal
from app.models import User
from app.views import CustomerViewReservations
from app.controllers.add_review_controller import AddReviewController
from app.utils.container import Container
from app.services.db_session import DatabaseSession

class ViewReservationsController(QObject): 
  def __init__(self, show_page: callable):
    super().__init__()
    self.show_page = show_page
    session = Container.resolve(DatabaseSession)
    user = Container.resolve(User)
    # Refresh the user object to get updated reservations
    session.refresh(user)
    self.upcoming, self.past = user.get_reservations()
    self.fomrat_for_card()
    self.view = CustomerViewReservations(self.upcoming, self.past)
    self.setup_connections()
  
  def setup_connections(self):
    self.view.review_button_clicked.connect(self.handle_view_review)
    self.view.back_btn.clicked.connect(self.handle_back)
    self.view.reservation_clicked.connect(self.handle_res_details)
      
  def fomrat_for_card(self):
    self.upcoming = [(r.club.name, r.date, r.id, r.event.title) for r in self.upcoming]
    self.past = [(r.club.name, r.date, r.id, r.event.title) for r in self.past]
  
  def handle_view_review(self, id:int):
    from app.models.review import Review
    from PySide6.QtWidgets import QMessageBox


    session = Container.resolve(DatabaseSession)

    existing_review = session.query(Review).filter_by(reservation_id=id).first()
    if existing_review:
      QMessageBox.warning(self.view, "Already Reviewed", "You have already submitted a review for this reservation.")
      return

    self.review_page_controller = AddReviewController(self.show_page, id)
    self.show_page('customer_view_button', self.review_page_controller)
      
  def handle_back(self):
    from app.controllers import HomePageController
        
    self.home_page_controller = Container.resolve(HomePageController)
    self.show_page('customer_home_page', self.home_page_controller)
    
  def handle_res_details(self, id: int):
    from app.controllers import ReservationDetailsController
    self.res_details_controller = ReservationDetailsController(id, self.show_page)
    self.show_page("res_details_page", self.res_details_controller)
    
  
  def show(self):
    self.view.show() 