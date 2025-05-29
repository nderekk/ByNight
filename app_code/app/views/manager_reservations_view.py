from PySide6.QtWidgets import (
    QWidget, QLabel, QPushButton, QVBoxLayout, QScrollArea, QFrame,
    QSizePolicy, QMessageBox, QHBoxLayout
)
from PySide6.QtGui import QFont, QCursor, QMouseEvent
from PySide6.QtCore import Qt, Signal


class ClickableReservationCard(QFrame):
    clicked = Signal(object)  # Emits the reservation data (dict)

    def __init__(self, reservation_data, card_widget):
        super().__init__()
        self.reservation_data = reservation_data
        self.setLayout(card_widget.layout())
        self.setStyleSheet("background-color: #333333; color: white; border-radius: 10px;")
        self.setCursor(QCursor(Qt.PointingHandCursor))

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.clicked.emit(self.reservation_data)


class ManagerReservationPage(QWidget):
    reservation_clicked = Signal(dict)

    def __init__(self, show_page: callable = None):
        super().__init__()
        self.show_page = show_page
        self.sample_data = self.load_reservations()
        self.setup_ui()

    def setup_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(15, 15, 15, 15)
        main_layout.setSpacing(15)

        # Header
        header_layout = QHBoxLayout()
        self.back_btn = QPushButton("←")
        self.back_btn.setFixedSize(30, 30)
        self.back_btn.setStyleSheet("font-size: 18px; background-color: #555; color: white; border: none;")
        self.back_btn.clicked.connect(self.on_back_clicked)

        title = QLabel("Manage Reservations")
        title.setFont(QFont("Arial", 18, QFont.Bold))
        title.setStyleSheet("margin-left: 10px;")

        header_layout.addWidget(self.back_btn)
        header_layout.addWidget(title)
        header_layout.addStretch()

        main_layout.addLayout(header_layout)

        subtitle = QLabel("Keep track of your club’s reservations. Tap them to see detailed info about them!")
        subtitle.setWordWrap(True)
        subtitle.setStyleSheet("color: gray;")
        main_layout.addWidget(subtitle)

        # Scrollable content
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)

        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)
        content_layout.setContentsMargins(10, 10, 10, 10)
        content_layout.setSpacing(20)

        for day, reservations in self.sample_data.items():
            content_layout.addWidget(QLabel(f"<b>{day}</b>"))
            for res in reservations:
                card = self.create_reservation_card(res)
                content_layout.addWidget(card)

        scroll.setWidget(content_widget)
        main_layout.addWidget(scroll)

    def create_reservation_card(self, res):
        # Card layout
        card = QFrame()
        layout = QVBoxLayout()
        layout.setContentsMargins(15, 10, 15, 10)
        layout.setSpacing(5)

        label1 = QLabel(f"<b>Table No: {res['table_no']}</b>")
        label2 = QLabel(f"Reserved by: <b>{res['reserved_by']}</b>")
        label3 = QLabel(f"Event: {res['event']} | ID: {res['id']} | {res['time']}")
        label4 = QLabel(f"People: {res['people']} | Order: {res['order']}")
        label5 = QLabel(f"<b>Cost: {res['cost']}</b>")

        for label in (label1, label2, label3, label4, label5):
            label.setWordWrap(True)
            layout.addWidget(label)

        card.setLayout(layout)
        card.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)

        clickable = ClickableReservationCard(reservation_data=res, card_widget=card)
        clickable.clicked.connect(self.handle_card_click)
        return clickable

    def handle_card_click(self, reservation_data):
        msg = (
            f"Table No: {reservation_data['table_no']}\n"
            f"Reserved by: {reservation_data['reserved_by']}\n"
            f"Event: {reservation_data['event']}\n"
            f"ID: {reservation_data['id']}\n"
            f"Time: {reservation_data['time']}\n"
            f"People: {reservation_data['people']}\n"
            f"Order: {reservation_data['order']}\n"
            f"Cost: {reservation_data['cost']}"
        )
        QMessageBox.information(self, "Reservation Details", msg)
        self.reservation_clicked.emit(reservation_data)

    def load_reservations(self):
        return {
            "Sunday (Today)": [
                {"table_no": 1, "reserved_by": "Spyros Sioutas", "event": "Koultoura",
                 "id": 2, "time": "12:00", "people": 5, "order": 2, "cost": 120},
                {"table_no": 3, "reserved_by": "Alex Papadopoulos", "event": "Salsa Night",
                 "id": 3, "time": "14:00", "people": 3, "order": 1, "cost": 90}
            ],
            "Monday": [
                {"table_no": 4, "reserved_by": "Maria Georgiou", "event": "Jazz Night",
                 "id": 4, "time": "18:30", "people": 6, "order": 3, "cost": 160},
                {"table_no": 5, "reserved_by": "Kostas Theodorou", "event": "Tech Meetup",
                 "id": 5, "time": "20:00", "people": 2, "order": 1, "cost": 70}
            ]
        }

    def on_back_clicked(self):
        if self.show_page:
            self.show_page("previous_page")
        else:
            self.close()
