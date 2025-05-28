from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import QDate

class ValidateDate:
    @staticmethod
    def validate(from_date, to_date, parent_widget):
        today = QDate.currentDate()

        if from_date > today:
            QMessageBox.warning(parent_widget, "Not Valid Period")
            return False

        if from_date > to_date:
            QMessageBox.warning(parent_widget, "Not Valid Period")
            return False
        if to_date > today :
            QMessageBox.warning(parent_widget, "Not Valid Period")

        return True
