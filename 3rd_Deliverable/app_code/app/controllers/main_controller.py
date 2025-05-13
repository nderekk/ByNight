from PySide6 import AppModel
from app.views.main_window import MainWindow
from app.utils.container import Container
from app.utils.event_bus import EventBus
from app.views.base_page import BasePage
from app.utils.page_registry import PageRegistry
from typing import List

class MainController:
  def __init__(self, model: AppModel, view: MainWindow):
    self.model = model
    self.view = view
    self.event_bus = Container.resolve(EventBus)
    self.pages: List[BasePage] = []
    
    # Initialize pages from registry
    for view_class, controller_class in PageRegistry.get_page_classes():
      page_view = view_class()
      page_controller = controller_class(model, page_view)
      self.pages.append(page_view)
      self.view.add_page(page_view)
    
    self._setup_navigation()

  def _setup_navigation(self):
    """Initialize navigation handlers"""
    self.view.back_button.clicked.connect(self.handle_back)
    self.event_bus.subscribe("navigation_request", self.handle_navigation)

  def handle_back(self):
    """Handle backward navigation"""
    if self.model.navigate_back():
      self._update_view()

  def handle_navigation(self, request):
    """Handle programmatic navigation requests"""
    if self.model.can_navigate_to(request.destination):
      self.model.navigate_to(request.destination)
      self._update_view()

  def _update_view(self):
    """Refresh UI state"""
    self.view.show_page(self.model.current_page)
    self._update_button_states()

  def _update_button_states(self):
    """Control navigation button availability"""
    current = self.model.current_page
    self.view.back_button.setEnabled(len(self.model.history) > 1)
    self.view.forward_button.setEnabled(bool(self.model.page_graph.get(current)))