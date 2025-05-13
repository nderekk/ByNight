from app.controllers.main_window import MainWindow
from PySide6.QtWidgets import QApplication
from app.data.repositories.init_repos import InitRepos
import sys

if __name__ == "__main__":
    # upcoming = vr_controller.get_upcoming_reservations_for_display(xx)
    InitRepos()
     
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())