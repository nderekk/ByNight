from app.controllers.main_window import MainWindow
from datetime import datetime
from PySide6.QtWidgets import QApplication
import sys

if __name__ == "__main__":
    # upcoming = vr_controller.get_upcoming_reservations_for_display(xx)
     
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())