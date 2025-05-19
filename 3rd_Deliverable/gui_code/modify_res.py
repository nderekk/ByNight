import sys
from PySide6.QtWidgets import (
  QApplication, QWidget, QVBoxLayout, QHBoxLayout,
  QLabel, QPushButton, QComboBox, QSpinBox
)
from PySide6.QtCore import Qt
from enum import Enum
from datetime import datetime

# Assume TableType is already defined elsewhere:
class TableType(str, Enum):
  VIP = "VIP"
  PASS = "Pass"
  BAR = "bar"

class ModifyReservationPage(QWidget):
  def __init__(self, current_table_type, current_num_of_people):
    super().__init__()
    self.current_table_type = current_table_type
    self.current_num_of_people = current_num_of_people
    self.setup_ui()

  def setup_ui(self):
    layout = QVBoxLayout()

    # Header with back button
    header_layout = QHBoxLayout()
    self.back_btn = QPushButton("←")
    self.back_btn.setFixedSize(30, 30)
    self.back_btn.setStyleSheet("font-size: 14pt;")
    header_layout.addWidget(self.back_btn)
    header_layout.addStretch()
    layout.addLayout(header_layout)

    # Title
    title = QLabel("Modify Reservation")
    title.setStyleSheet("font-weight: bold; font-size: 18pt;")
    layout.addWidget(title)

    # Table type dropdown
    table_type_label = QLabel("Table Type")
    table_type_label.setStyleSheet("font-size: 10pt;")
    layout.addWidget(table_type_label)

    self.table_type_combo = QComboBox()
    self.table_type_combo.setStyleSheet("background-color: #333; color: white; padding: 5px;")
    for t in ["VIP", "Pass", "bar"]:
      self.table_type_combo.addItem(t)
    self.table_type_combo.setCurrentText(self.current_table_type)
    layout.addWidget(self.table_type_combo)

    # Number of people input
    num_label = QLabel("Number of People")
    num_label.setStyleSheet("font-size: 10pt; margin-top: 10px;")
    layout.addWidget(num_label)

    self.people_spin = QSpinBox()
    self.people_spin.setRange(1, 20)
    self.people_spin.setValue(self.current_num_of_people)
    self.people_spin.setStyleSheet("background-color: #333; color: white; padding: 15px;")
    layout.addWidget(self.people_spin)

    # Save button
    self.save_btn = QPushButton("Save Changes")
    self.save_btn.setCursor(Qt.PointingHandCursor)
    self.save_btn.setStyleSheet(
      "background-color: #666; color: white; border-radius: 5px; padding: 10px; font-size: 11pt;"
    )
    layout.addWidget(self.save_btn)

    self.setLayout(layout)

if __name__ == "__main__":
  app = QApplication(sys.argv)

  # Example values
  current_table_type = "VIP"
  current_num_of_people = 4

  window = ModifyReservationPage(current_table_type, current_num_of_people)
  window.setWindowTitle("Modify Reservation")
  window.resize(400, 300)
  window.show()

  sys.exit(app.exec())
