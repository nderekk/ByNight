import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QScrollArea,
    QCheckBox, QSizePolicy, QFrame, QPushButton
)
from PySide6.QtGui import QFont, QColor, QPainter, QBrush
from PySide6.QtCore import Qt


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


class DiscountPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Discount Page")
        self.resize(400, 600)

        main_layout = QVBoxLayout(self)
        self.setLayout(main_layout)

        # --- Header ---
        header = QHBoxLayout()
        self.back_button = QPushButton("←")
        self.back_button.setFixedWidth(30)
        self.back_button.setStyleSheet("font-size: 14pt;")
        self.back_button.clicked.connect(self.go_back)

        title = QLabel("Discount Tab")
        title.setAlignment(Qt.AlignCenter)
        title.setFont(QFont("", 14, QFont.Bold))

        date_label = QLabel("13/5/2025")
        date_label.setStyleSheet("background-color: #; border-radius: 10px; padding: 5px;")

        header.addWidget(self.back_button)
        header.addStretch()
        header.addWidget(title)
        header.addStretch()
        header.addWidget(date_label)
        main_layout.addLayout(header)

        # --- Divider ---
        divider = QLabel()
        divider.setFixedHeight(2)
        divider.setStyleSheet("background-color: black; margin: 8px;")
        main_layout.addWidget(divider)

        # --- Scrollable List ---
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        list_widget = QWidget()
        list_layout = QVBoxLayout(list_widget)

        # Drink items
        drinks = [
            ("V", "Serkova", "50%"),
            ("V", "Absolute", "12%"),
            ("V", "Ciroc", "17%"),
            ("W", "Johny Black", "25%"),
            ("W", "Johny Red", "20%"),
            ("W", "Johny Gold", "20%"),
            ("G", "Gordons", "20%"),
            ("G", "Bombay", "20%"),
        ]

        for icon, name, discount in drinks:
            row = QHBoxLayout()

            avatar = CircleAvatar(icon)
            name_label = QLabel(name)
            name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
            discount_label = QLabel(discount)
            checkbox = QCheckBox()
            checkbox.setChecked(True)

            row.addWidget(avatar)
            row.addSpacing(10)
            row.addWidget(name_label)
            row.addWidget(discount_label)
            row.addWidget(checkbox)

            container = QFrame()
            container.setLayout(row)
            list_layout.addWidget(container)

        scroll_area.setWidget(list_widget)
        main_layout.addWidget(scroll_area)

    def go_back(self):
        # Implement back navigation here
        print("Back button clicked")

