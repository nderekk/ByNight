from app.controllers.main_window import MainWindow
from PySide6.QtWidgets import QApplication
from app.data.database import SessionLocal
from app.services.db_session import DatabaseSession
from app.utils.container import Container
import sys

if __name__ == "__main__":
  Container.register(DatabaseSession, DatabaseSession(SessionLocal).get_session)
     
  app = QApplication(sys.argv)
  window = MainWindow()
  window.show()
  sys.exit(app.exec())