import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout, QScrollArea, QFrame, QSizePolicy, QMessageBox
)
from PySide6.QtGui import QFont, QCursor
from PySide6.QtCore import Qt


class ReservationCard(QFrame):
    def __init__(self):  #, table_no, reserved_by, event, ID, time, people, order, cost):
        super().__init__()
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
        # self.table_no = table_no
        # self.reserved_by = reserved_by
        # self.event = event
        # self.ID = ID
        # self.time = time
        # self.people = people
        # self.order = order
        # self.cost = cost

        layout = QVBoxLayout()
        layout.setContentsMargins(15, 10, 15, 10)
        layout.setSpacing(5)

        # Create labels with word wrap
        label1 = QLabel(f"<b>Table No: {1}</b>")
        label2 = QLabel(f"Reserved by: <b>{'Spyros Sioutas'}</b>")
        label3 = QLabel(f"Event: {'Koultoura'} | ID: {2} | {12}")
        label4 = QLabel(f"People: {5} | Order: {2}")
        label5 = QLabel(f"<b>Cost: {120}</b>")

        for label in (label1, label2, label3, label4, label5):
            label.setWordWrap(True)
            layout.addWidget(label)

        self.setLayout(layout)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        
        # Set cursor to pointer to indicate it's clickable
        self.setCursor(QCursor(Qt.PointingHandCursor))

    def mousePressEvent(self, event):
        # Show a popup with the reservation details
        message = f"Table No: {self.table_no}\nReserved by: {self.reserved_by}\nEvent: {self.event}\n" \
                  f"ID: {self.ID}\nTime: {self.time}\nPeople: {self.people}\nOrder: {self.order}\nCost: {self.cost}"
        
        QMessageBox.information(self, "Reservation Details", message)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Club Manager - Reservations")
        self.setMinimumSize(500, 600)

        main_widget = QWidget()
        main_layout = QVBoxLayout(main_widget)
        main_layout.setContentsMargins(15, 15, 15, 15)
        main_layout.setSpacing(15)

        # Header section
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

        # Scroll area for reservations
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)

        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)
        content_layout.setContentsMargins(10, 10, 10, 10)
        content_layout.setSpacing(20)

        # Sample sections and cards
        content_layout.addWidget(QLabel("<b>Sunday (Today)</b>"))
        for _ in range(2):
            content_layout.addWidget(ReservationCard())

        content_layout.addSpacing(20)
        content_layout.addWidget(QLabel("<b>Monday</b>"))
        for _ in range(2):
            content_layout.addWidget(ReservationCard())

        scroll.setWidget(content_widget)
        main_layout.addWidget(scroll)

        self.setCentralWidget(main_widget)

    def on_back_clicked(self):
        # Here, you can either close the window or switch to a previous window
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
