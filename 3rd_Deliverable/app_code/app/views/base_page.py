# app/views/base_page.py
from PySide6.QtWidgets import QWidget
from typing import TYPE_CHECKING

if TYPE_CHECKING:
  from app.controllers.base_controller import BaseController

class BasePage(QWidget):
  """Base class for all pages with common functionality"""
  def __init__(self):
    super().__init__()
    self.controller: 'BaseController' = None
        
  def set_controller(self, controller: 'BaseController'):
    self.controller = controller