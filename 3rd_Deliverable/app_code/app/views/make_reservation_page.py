from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit,
    QPushButton, QFrame, QSizePolicy, QSpacerItem, QComboBox, QSpinBox
)
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtCore import Qt
from app.models.club import Club
from app.utils.container import Container                
from app.services.db_session import DatabaseSession      
import app.models                                        


class MakeReservationPage(QWidget):
     def __init__(self, club: Club):
        super().__init__()
        self.club=club
        self.venue_label = QLabel()
        self.init_ui()

     
     def init_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)

        # Header
        header_layout = QHBoxLayout()
        self.back_button = QPushButton("←")
        self.back_button.setFont(QFont("Arial", 16))   
        self.back_button.setStyleSheet("color: white;")
        self.back_button.setFixedSize(30, 30)  

        title = QLabel("Make a reservation")
        title.setFont(QFont("Arial", 12, QFont.Bold))
        title.setStyleSheet("color: white;")
        title.setAlignment(Qt.AlignCenter)

        header_layout.addWidget(self.back_button)
        header_layout.addStretch()
        header_layout.addWidget(title)
        header_layout.addStretch()
        header_layout.addSpacerItem(QSpacerItem(30, 0))  # Spacer to balance back arrow
        main_layout.addLayout(header_layout)

        # Logo
        logo_label = QLabel()
        pixmap = QPixmap("saint_logo.png").scaled(80, 80, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        logo_label.setPixmap(pixmap)
        logo_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(logo_label)

        # Venue Name
        
        self.venue_label.setFont(QFont("Arial", 24, QFont.Bold))
        self.venue_label.setStyleSheet("color: white;")
        self.venue_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.venue_label)

        # Card
        card = QFrame()
        card.setStyleSheet("""
            QFrame {
                background-color: #1E1E1E;
                border-radius: 12px;
                border: 1px solid #333;
            }
        """)
        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(16, 16, 16, 16)
        card_layout.setSpacing(12)

        section_title = QLabel("Reservation")
        section_title.setFont(QFont("Arial", 10, QFont.Bold))
        section_title.setStyleSheet("color: white;")
        card_layout.addWidget(section_title)

        # Guests (Removed the checkbox)
        guests_layout = QVBoxLayout()
        guest_input = QLineEdit()
        guest_input.setPlaceholderText("Insert Number of Guests")
        guest_input.setStyleSheet("""
            QLineEdit {
                background-color: #2A2A2A;
                color: white;
                border: 1px solid #444;
                border-radius: 6px;
                padding: 6px;
            }
            QLineEdit::placeholder {
                color: #888;
            }
        """)
        guests_layout.addWidget(guest_input)
        card_layout.addLayout(guests_layout)

        # Table Section - Dropdown
        table_title = QLabel("☰  Select a table")
        table_title.setFont(QFont("Arial", 11))
        table_title.setStyleSheet("color: white;")
        
        table_dropdown = QComboBox()
        table_dropdown.addItems(["VIP", "Pass", "bar"])
        
        card_layout.addWidget(table_title)
        card_layout.addWidget(table_dropdown)

        # Drink Section - Dropdown
        bottles_layout = QHBoxLayout()

 
        premium_label = QLabel("Premium bottle")
        premium_label.setStyleSheet("color: white;")
        premium_spinbox = QSpinBox()
        premium_spinbox.setMinimum(0)
        premium_spinbox.setMaximum(20)
        premium_spinbox.setStyleSheet("""
            QSpinBox {
            background-color: #2A2A2A;
            color: white;
            border: 1px solid #444;
            border-radius: 6px;
            padding: 4px;
                }
            """)

 
        regular_label = QLabel("Regular bottle")
        regular_label.setStyleSheet("color: white;")
        regular_spinbox = QSpinBox()
        regular_spinbox.setMinimum(0)
        regular_spinbox.setMaximum(20)
        regular_spinbox.setStyleSheet("""
    QSpinBox {
        background-color: #2A2A2A;
        color: white;
        border: 1px solid #444;
        border-radius: 6px;
        padding: 4px;
    }
""")

 
        bottles_layout.addWidget(premium_label)
        bottles_layout.addWidget(premium_spinbox)
        bottles_layout.addSpacing(40)   
        bottles_layout.addWidget(regular_label)
        bottles_layout.addWidget(regular_spinbox)

 
        drinks_title = QLabel("Select type of bottles")
        drinks_title.setFont(QFont("Arial", 11))
        drinks_title.setStyleSheet("color: white;")

        card_layout.addWidget(drinks_title)
        card_layout.addLayout(bottles_layout)

                
        event_title = QLabel("☰  Select event")
        event_title.setFont(QFont("Arial", 11))
        event_title.setStyleSheet("color: white;")

        self.event_dropdown = QComboBox()
        self.load_events()

        card_layout.addWidget(event_title)
        card_layout.addWidget(self.event_dropdown)


        main_layout.addWidget(card)

        # Confirm Button
        confirm_btn = QPushButton("Confirm Reservation")
        confirm_btn.setStyleSheet("""
            QPushButton {
                background-color: #333;
                color: white;
                padding: 14px;
                border-radius: 10px;
                font-weight: bold;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #444;
            }
        """)
        confirm_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        main_layout.addStretch()
        main_layout.addWidget(confirm_btn)

     def set_name(self, club: Club):
      self.venue_label.setText(club.name)

     def load_events(self):
  
        session = Container.resolve(DatabaseSession)

        self.event_dropdown.clear()

        events = session.query(app.models.Event)\
                        .filter(app.models.Event.club_id == self.club.id)\
                        .order_by(app.models.Event.date.asc())\
                        .all()

        for event in events:
            label = f"{event.title} - {event.date.strftime('%d/%m/%Y')}"
            self.event_dropdown.addItem(label, event.id)


     