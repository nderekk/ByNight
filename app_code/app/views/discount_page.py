import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QScrollArea,
    QCheckBox, QSizePolicy, QFrame, QPushButton, QDateEdit, QLineEdit
)
from PySide6.QtGui import QFont, QColor, QPainter, QBrush, QIntValidator
from PySide6.QtCore import Qt, QDate
from app.models.discount import Discount


class CircleAvatar(QLabel):
    def __init__(self, letter, color=QColor("#D6C6F5")):
        super().__init__()
        self.letter = letter.upper()
        self.color = color
        self.setFixedSize(40, 40)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QBrush(self.color))
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(0, 0, self.width(), self.height())
        painter.setPen(Qt.black)
        font = QFont("Arial", 14, QFont.Bold)
        painter.setFont(font)
        painter.drawText(self.rect(), Qt.AlignCenter, self.letter)


class PercentageInput(QWidget):
    def __init__(self, value="0"):
        super().__init__()
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        self.line_edit = QLineEdit()
        self.line_edit.setValidator(QIntValidator(0, 100))
        self.line_edit.setFixedWidth(40)
        self.line_edit.setAlignment(Qt.AlignRight)
        self.line_edit.setText(str(value).replace('%', ''))

        percent_label = QLabel("%")
        percent_label.setFixedWidth(15)
        percent_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        layout.addWidget(self.line_edit)
        layout.addWidget(percent_label)

    def value(self):
        try:
            return float(self.line_edit.text()) / 100
        except ValueError:
            return 0.0

    def setEnabled(self, enabled):
        self.line_edit.setEnabled(enabled)

    def text(self):
        return self.line_edit.text() + "%"


class DiscountPage(QWidget):
    def __init__(self):
        super().__init__()
        main_layout = QVBoxLayout(self)
        self.setLayout(main_layout)

        # Header
        header = QHBoxLayout()
        self.back_button = QPushButton("←")
        self.back_button.setFixedWidth(30)
        self.back_button.setStyleSheet("font-size: 14pt;")
        

        title = QLabel("Discount Tab")
        title.setAlignment(Qt.AlignCenter)
        title.setFont(QFont("", 14, QFont.Bold))

        self.date_edit = QDateEdit() 
        self.date_edit.setDate(QDate.currentDate())
        self.date_edit.setCalendarPopup(True)
        self.date_edit.dateChanged.connect(self.handle_date_change)
        

        header.addWidget(self.back_button)
        header.addStretch()
        header.addWidget(title)
        header.addStretch()
        header.addWidget(self.date_edit)
        main_layout.addLayout(header)

        # Divider
        divider = QLabel()
        divider.setFixedHeight(2)
        divider.setStyleSheet("background-color: black; margin: 8px;")
        main_layout.addWidget(divider)

        # Scrollable List
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        self.list_widget = QWidget()
        self.list_layout = QVBoxLayout(self.list_widget)

        self.drinks = [
            ("V", "Regular", "50%"),
            ("V", "Premium", "12%"),
        ]

        self.discount_fields = []

        for icon, name, discount in self.drinks:
            row = QHBoxLayout()

            avatar = CircleAvatar(icon)
            name_label = QLabel(name)
            name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

            discount_edit = PercentageInput(discount)

            checkbox = QCheckBox()
            checkbox.setChecked(True)
            self.connect_checkbox_to_lineedit(checkbox, discount_edit)

            row.addWidget(avatar)
            row.addSpacing(10)
            row.addWidget(name_label)
            row.addWidget(discount_edit)
            row.addWidget(checkbox)

            container = QFrame()
            container.setLayout(row)
            self.list_layout.addWidget(container)
            self.discount_fields.append((name, discount_edit, checkbox))

        self.handle_date_change() 

        scroll_area.setWidget(self.list_widget)
        main_layout.addWidget(scroll_area)

        # Footer (No Enter button)
        footer = QHBoxLayout()
        self.load_button = QPushButton("Save")
        self.load_button.clicked.connect(self.load_discounts)

        footer.addStretch()
        footer.addWidget(self.load_button)
        main_layout.addLayout(footer)

    def handle_date_change(self):
        from app.utils.container import Container
        from app.models import User
        qdate = self.date_edit.date()
        selected_date = qdate.toPython()  
        self.manager_club = Container.resolve(User)


        discounts = Discount.get_discounts_by_date(selected_date, self.manager_club.id)  

        for name, lineedit, checkbox in self.discount_fields:
            value = 0.0
            if name == "Regular":
                value = discounts.get("regular", 0.0)
            elif name == "Premium":
                value = discounts.get("premium", 0.0)

            # Set value (in percent)
            lineedit.line_edit.setText(str(int(value * 100)))
            lineedit.setEnabled(True)
            checkbox.setChecked(True)

    def load_discounts(self):
        for name, lineedit, checkbox in self.discount_fields:
            lineedit.setEnabled(checkbox.isChecked())

    def connect_checkbox_to_lineedit(self, checkbox, lineedit):
        checkbox.stateChanged.connect(
            lambda state: lineedit.setEnabled(state == Qt.Checked)
        )

    def get_selected_date(self):
        return self.date_edit.date()

    def get_discount_values(self):
        discounts = {}
        for name, lineedit, checkbox in self.discount_fields:
            if checkbox.isChecked():
                discounts[name] = lineedit.value()  # returns decimal
        return discounts


