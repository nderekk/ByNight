import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout,
    QDateEdit, QTimeEdit, QFrame, QPushButton
)
from PySide6.QtCore import Qt, QDate, QTime
from PySide6.QtGui import QFont


class StatCard(QWidget):
    def __init__(self, title, value):
        super().__init__()
        self.setStyleSheet("background-color: #2f2f2f; border-radius: 8px;")
        self.setFixedHeight(100)

        layout = QVBoxLayout()
        layout.setContentsMargins(12, 8, 12, 8)

        # Title
        title_label = QLabel(title)
        title_label.setStyleSheet("color: white; font-weight: bold; font-size: 14px;")

        # Value and Placeholder Chart
        value_label = QLabel(f"{value}%")
        value_label.setStyleSheet("color: white; font-size: 20px; font-weight: bold;")

        placeholder_chart = QLabel("📈")  # Placeholder for real chart
        placeholder_chart.setAlignment(Qt.AlignRight)
        placeholder_chart.setStyleSheet("font-size: 20px; color: #007bff;")

        top = QHBoxLayout()
        top.addWidget(value_label)
        top.addStretch()
        top.addWidget(placeholder_chart)

        layout.addWidget(title_label)
        layout.addLayout(top)

        self.setLayout(layout)


class ClubStatsWindow(QWidget):
    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(16, 16, 16, 16)
        main_layout.setSpacing(16)

        # Header with back button
        header_layout = QHBoxLayout()
        self.back_button = QPushButton("←")
        self.back_button.setFixedSize(30, 30)
        self.back_button.setStyleSheet("font-size: 18px; border: none; background: transparent;")
        self.back_button.setCursor(Qt.PointingHandCursor)
        self.back_button.clicked.connect(self.go_back)

        header_layout.addWidget(self.back_button)
        header_layout.addStretch()
        main_layout.addLayout(header_layout)

        # Title and subtitle
        title = QLabel("Club Statistics")
        title.setFont(QFont("Arial", 16, QFont.Bold))
        title.setAlignment(Qt.AlignLeft)
        main_layout.addWidget(title)

        subtitle = QLabel("Select a time period to view statistics.")
        subtitle.setStyleSheet("color: gray; font-size: 12px;")
        main_layout.addWidget(subtitle)

        # Date pickers
        today = QDate.currentDate()

        from_label = QLabel("From:")
        to_label = QLabel("To:")

        self.from_date = QDateEdit(today)
        self.to_date = QDateEdit(today)

        for widget in [self.from_date, self.to_date]:
            widget.setCalendarPopup(True)
            widget.setStyleSheet("""
                QDateEdit {
                    padding: 6px;
                    font-size: 12px;
                    background-color: #f0f0f0;
                    color: black;
                    border: 1px solid #ccc;
                    border-radius: 4px;
                }
            """)

        date_layout = QHBoxLayout()
        date_layout.addWidget(from_label)
        date_layout.addWidget(self.from_date)
        date_layout.addSpacing(16)
        date_layout.addWidget(to_label)
        date_layout.addWidget(self.to_date)

        main_layout.addLayout(date_layout)

        # Load button
        self.load_button = QPushButton("Load")
        self.load_button.setStyleSheet("""
            QPushButton {
                background-color: #007bff;
                color: white;
                font-weight: bold;
                padding: 6px 12px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
        """)
        self.load_button.setCursor(Qt.PointingHandCursor)
        main_layout.addWidget(self.load_button, alignment=Qt.AlignLeft)

        # Statistic cards
        main_layout.addWidget(self.create_divider())
        main_layout.addWidget(StatCard("Attendance", 82))
        main_layout.addWidget(self.create_divider())
        main_layout.addWidget(StatCard("Sales", 95))
        main_layout.addWidget(self.create_divider())
        main_layout.addWidget(StatCard("Drink Distribution", 14))
        main_layout.addWidget(self.create_divider())
        main_layout.addWidget(StatCard("Rating", 14))

        self.setLayout(main_layout)

    def create_divider(self):
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setStyleSheet("color: lightgray;")
        return line

    def go_back(self):
        print("Back button clicked")


