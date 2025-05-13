from typing import Dict, List, Callable, Any
from PySide6.QtCore import QObject, Signal

class EventBus(QObject):
  event_occurred = Signal(str, object)
  
  def __init__(self):
    super().__init__()
    self._subscriptions: Dict[str, List[Callable]] = {}
    
  def subscribe(self, event_type: str, callback: Callable):
    if event_type not in self._subscriptions:
      self._subscriptions[event_type] = []
    self._subscriptions[event_type].append(callback)
    
  def publish(self, event_type: str, data: Any = None):
    if event_type in self._subscriptions:
      for callback in self._subscriptions[event_type]:
        callback(data)
    self.event_occurred.emit(event_type, data)