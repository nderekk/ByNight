from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import QDate

class ValidateDate:
    @staticmethod
    def validate(from_date, to_date, parent_widget):
        today = QDate.currentDate()

        if from_date > today:
            QMessageBox.warning(parent_widget, "Invalid Date", "The 'From' date cannot be in the future.")
            return False

        if from_date > to_date:
            QMessageBox.warning(parent_widget, "Invalid Range", "The 'From' date must be before or equal to the 'To' date.")
            return False

        return True
