from PySide6.QtWidgets import (
  QWidget, QVBoxLayout, QHBoxLayout, QFormLayout,
  QLabel, QPushButton, QComboBox, QSpinBox
)
from PySide6.QtCore import Qt

class ModifyReservationPage(QWidget):
  def __init__(self, current_table_type, current_num_of_people):
    super().__init__()
    self.current_table_type = current_table_type
    self.current_num_of_people = current_num_of_people
    self.setup_ui()

  def setup_ui(self):
    main_layout = QVBoxLayout()

    header_layout = QHBoxLayout()
    self.back_btn = QPushButton("←")
    self.back_btn.setFixedSize(30, 30)
    self.back_btn.setStyleSheet("font-size: 14pt;")
    header_layout.addWidget(self.back_btn)
    header_layout.addStretch()
    main_layout.addLayout(header_layout)

    title = QLabel("Modify Reservation")
    title.setStyleSheet("font-weight: bold; font-size: 18pt; margin-top: 10px;")
    title.setAlignment(Qt.AlignCenter)
    main_layout.addWidget(title)

    form_layout = QFormLayout()
    form_layout.setLabelAlignment(Qt.AlignRight)
    form_layout.setFormAlignment(Qt.AlignTop)
    form_layout.setSpacing(12)

    spinbox_width = 80  # compact width for spinboxes

    self.table_type_combo = QComboBox()
    self.table_type_combo.setStyleSheet("background-color: #333; color: white; padding: 5px;")
    for t in ["VIP", "Pass", "bar"]:
      self.table_type_combo.addItem(t)
    self.table_type_combo.setCurrentText(self.current_table_type)
    self.table_type_combo.setFixedWidth(spinbox_width)
    form_layout.addRow("Table Type:", self.table_type_combo)

    self.people_spin = QSpinBox()
    self.people_spin.setRange(1, 10)
    self.people_spin.setValue(self.current_num_of_people)
    self.people_spin.setStyleSheet("background-color: #333; color: white; padding: 5px;")
    self.people_spin.setFixedWidth(spinbox_width)
    form_layout.addRow("Number of People:", self.people_spin)

    self.premium_spin = QSpinBox()
    self.premium_spin.setRange(0, 10)
    self.premium_spin.setStyleSheet("background-color: #333; color: white; padding: 5px;")
    self.premium_spin.setFixedWidth(spinbox_width)
    form_layout.addRow("Premium Bottles:", self.premium_spin)

    self.regular_spin = QSpinBox()
    self.regular_spin.setRange(0, 10)
    self.regular_spin.setStyleSheet("background-color: #333; color: white; padding: 5px;")
    self.regular_spin.setFixedWidth(spinbox_width)
    form_layout.addRow("Regular Bottles:", self.regular_spin)

    main_layout.addLayout(form_layout)

    self.save_btn = QPushButton("Save Changes")
    self.save_btn.setCursor(Qt.PointingHandCursor)
    self.save_btn.setStyleSheet(
      "background-color: #666; color: white; border-radius: 5px; padding: 10px; font-size: 11pt;"
    )
    main_layout.addWidget(self.save_btn)

    self.setLayout(main_layout)

  def refresh_page(self, current_table_type, current_num_of_people):
    print(f"\n {current_table_type} \n {current_num_of_people}")
    self.current_table_type = current_table_type
    self.current_num_of_people = current_num_of_people
    self.table_type_combo.setCurrentText(current_table_type)
    self.people_spin.setValue(current_num_of_people)
