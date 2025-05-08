import sys
from PySide6.QtWidgets import QApplication, QWidget
from HomePage import Ui_mainWidget  # Make sure the filename matches

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QWidget()
    ui = Ui_mainWidget()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec())
