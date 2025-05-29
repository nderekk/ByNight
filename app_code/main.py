from app.controllers.main_window import MainWindow
from PySide6.QtWidgets import QApplication
from app.data.database import SessionLocal
import sys

if __name__ == "__main__":     
  app = QApplication(sys.argv)
  window = MainWindow()
  window.show()
  sys.exit(app.exec())