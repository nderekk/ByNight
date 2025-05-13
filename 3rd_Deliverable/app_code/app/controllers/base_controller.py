from typing import TYPE_CHECKING
from PySide6.QtCore import QObject

if TYPE_CHECKING:
    from app.models.app_model import AppModel
    from app.views.base_page import BasePage

class BaseController(QObject):
  """Base controller with common functionality"""
  def __init__(self, model: 'AppModel', view: 'BasePage'):
    super().__init__()
    self.model = model
    self.view = view
    self.view.set_controller(self)
    self._connect_signals()
        
  def _connect_signals(self):
    """Connect signals common to all controllers"""
    pass