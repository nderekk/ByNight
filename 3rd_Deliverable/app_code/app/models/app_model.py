from typing import Dict, List
from PySide6 import AppState

class AppModel:
  def __init__(self):
    """Central data model that maintains application state"""
    self.state = AppState()
    self._page_graph = {}  # Navigation rules
        
  # Defines legal page transitions as {current_page: [allowed_pages]}
  def define_navigation(self, page_graph: Dict[str, List[str]]):
    """Define possible navigation paths between pages"""
    self._page_graph = page_graph
    
  # Validates and executes page transition, updates history
  def navigate_to(self, page_name: str):
    """Transition to new page"""
    if self.can_navigate_to(page_name):
      self.state.page_history.append(page_name)
      self.state.current_page = page_name

  # Returns to previous page while maintaining history
  def navigate_back(self):
    """Return to previous page"""
    if len(self.state.page_history) > 1:
      self.state.page_history.pop()
      self.state.current_page = self.state.page_history[-1]
      return True
    return False
        
  # Checks if requested transition is permitted by navigation rules
  def can_navigate_to(self, page_name: str) -> bool:
    current = self.get_current_page_name()
    return page_name in self._page_graph.get(current, [])