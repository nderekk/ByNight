import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QVBoxLayout, QScrollArea, QFrame, QSizePolicy, QMessageBox
)
from PySide6.QtGui import QFont, QCursor
from PySide6.QtCore import Qt


class ReservationCard(QFrame):
    def __init__(self):
        super().__init__()

        # Hardcoded data
        self.table_no = 7
        self.reserved_by = "Alex Johnson"
        self.event = "Latin Night"
        self.ID = 101
        self.time = "9:00 PM"
        self.people = 4
        self.order = "Tacos and Margaritas"
        self.cost = 95.50

        self.setStyleSheet("""
            QFrame {
                background-color: #333333;
                color: white;
                border-radius: 10px;
            }
            QLabel {
                font-size: 14px;
            }
        """)

        layout = QVBoxLayout()
        layout.setContentsMargins(15, 10, 15, 10)
        layout.setSpacing(5)

        label1 = QLabel(f"<b>Table No: {self.table_no}</b>")
        label2 = QLabel(f"Reserved by: <b>{self.reserved_by}</b>")
        label3 = QLabel(f"Event: {self.event} | ID: {self.ID} | {self.time}")
        label4 = QLabel(f"People: {self.people} | Order: {self.order}")
        label5 = QLabel(f"<b>Cost: €{self.cost:.2f}</b>")

        for label in (label1, label2, label3, label4, label5):
            label.setWordWrap(True)
            layout.addWidget(label)

        self.setLayout(layout)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.setCursor(QCursor(Qt.PointingHandCursor))

    def mousePressEvent(self, event):
        message = (
            f"Table No: {self.table_no}\n"
            f"Reserved by: {self.reserved_by}\n"
            f"Event: {self.event}\n"
            f"ID: {self.ID}\n"
            f"Time: {self.time}\n"
            f"People: {self.people}\n"
            f"Order: {self.order}\n"
            f"Cost: €{self.cost:.2f}"
        )
        QMessageBox.information(self, "Reservation Details", message)


class ManagerHomePage(QWidget):
    def __init__(self, show_page: callable = None):
        super().__init__()
        self.show_page = show_page

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(15, 15, 15, 15)
        main_layout.setSpacing(15)

        # Header
        header_layout = QVBoxLayout()
        back_btn = QPushButton("←")
        back_btn.setFixedSize(30, 30)
        back_btn.setStyleSheet("font-size: 18px; background-color: #555; color: white; border: none;")
        back_btn.clicked.connect(self.on_back_clicked)

        title = QLabel("Manage Reservations")
        title.setFont(QFont("Arial", 18, QFont.Bold))

        subtitle = QLabel("Keep track of your club’s reservations. Tap them to see detailed info about them!")
        subtitle.setWordWrap(True)
        subtitle.setStyleSheet("color: gray;")

        header_layout.addWidget(back_btn, alignment=Qt.AlignLeft)
        header_layout.addWidget(title)
        header_layout.addWidget(subtitle)
        header_layout.setSpacing(10)

        main_layout.addLayout(header_layout)

        # Scrollable content
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)
        content_layout.setContentsMargins(10, 10, 10, 10)
        content_layout.setSpacing(20)

        # Add hardcoded reservation cards
        content_layout.addWidget(QLabel("<b>Sunday (Today)</b>"))
        for _ in range(2):
            content_layout.addWidget(ReservationCard())

        content_layout.addSpacing(20)
        content_layout.addWidget(QLabel("<b>Monday</b>"))
        for _ in range(2):
            content_layout.addWidget(ReservationCard())

        scroll.setWidget(content_widget)
        main_layout.addWidget(scroll)

    def on_back_clicked(self):
        if self.show_page:
            self.show_page("previous_page")  # Placeholder for navigation callback
        else:
            self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ManagerHomePage()
    window.resize(600, 800)
    window.setWindowTitle("Reservations")
    window.show()
    sys.exit(app.exec())
