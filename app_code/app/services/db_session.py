from sqlalchemy.orm import Session
from typing import Optional, Callable

class DatabaseSession:
  def __init__(self, session_factory: Callable[[], Session]):
    self._session_factory = session_factory
    self._session: Optional[Session] = None

  def get_session(self) -> Session:
    if self._session is None:
      self._session = self._session_factory()
    return self._session

  def close(self):
    if self._session:
      self._session.close()
      self._session = None
