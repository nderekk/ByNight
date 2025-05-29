from app.utils.container import Container
from PySide6.QtCore import QObject, Signal
from app.models.user import User
from app.views.review_page import ReviewPage
from app.models import Reservation

class AddReviewController(QObject):
  # Signals for view updates
  # login_successful = Signal()
  # login_failed = Signal(str)
  # signup_successful = Signal()
  # signup_failed = Signal(str)
  
  def __init__(self,show_page: callable, res_id: int):
    super().__init__()
    # upcoming, past = self.get_dummy_data()
    self.show_page = show_page
    self.reservation = Reservation.get_res_from_id(res_id)
    self.view = ReviewPage((self.reservation.get_event_date(), self.reservation.get_event_name()))
    self.setup_connections()
  
  def setup_connections(self):
    self.view.back_btn.clicked.connect(self.handle_back)
    self.view.submit_btn.clicked.connect(self.submit_review)
    
  
  def handle_back(self):
    from app.controllers.view_res_controller import ViewReservationsController
    self.view_res_controller = ViewReservationsController(self.show_page)
    self.show_page('view_res_controller', self.view_res_controller)



  def submit_review(self):
    from PySide6.QtWidgets import QMessageBox

    music_rate = self.view.rating_widgets["Music"].current_rating
    atmosphere_rate = self.view.rating_widgets["Atmosphere"].current_rating
    service_rate = self.view.rating_widgets["Service"].current_rating
    overall_rate = self.view.rating_widgets["Overall Experience"].current_rating
    comment = self.view.comment_box.toPlainText()

       
    if music_rate == 0 or atmosphere_rate == 0 or service_rate == 0 or overall_rate == 0:
       
      QMessageBox.critical(
            self.view,
                "Missing Rating",
                "Please provide a rating (1-5 stars) for all categories."
            )
      return

         
    from app.models.review import Review
    Review.create_review(
      music_rating=music_rate,
      atmosphere_rating=atmosphere_rate,
      service_rating=service_rate,
      overall_experience=overall_rate,
      comment=comment,
      reservation_id=self.reservation.id
        )

    QMessageBox.information(self.view,"Success","Your review has been submitted successfully!")
    self.handle_back()




  def show(self):
    self.view.show() 