from PySide6 import QStackedWidget, QMainWindow
from app.views.login_view import LoginView
from app.views.customer_view_res import CustomerViewReservations

class MainWindow(QMainWindow):
  def __init__(self):
    self.stack = QStackedWidget()
    self.pages = {
        'login': LoginView(),
        'customer_view_reservations': CustomerViewReservations()
    }
        
  def show_page(self, page_name: str):
    """Display requested page"""
    page = self.pages.get(page_name)
    if page:
      self.stack.setCurrentWidget(page)