import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit,
    QPushButton, QFrame, QSizePolicy, QSpacerItem, QComboBox
    QPushButton, QFrame, QSizePolicy, QSpacerItem, QComboBox
)
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtCore import Qt


class ReservationUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Make a Reservation")
        self.setFixedSize(390, 720)
        self.setStyleSheet("background-color: #121212;")
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)

        # Header
        header_layout = QHBoxLayout()
        back_button = QPushButton("←")
        back_button.setFont(QFont("Arial", 16))  # Smaller font size
        back_button.setStyleSheet("color: white;")
        back_button.setFixedSize(30, 30)  # Make the button smaller
        back_button.clicked.connect(self.on_back_clicked)
        back_button = QPushButton("←")
        back_button.setFont(QFont("Arial", 16))  # Smaller font size
        back_button.setStyleSheet("color: white;")
        back_button.setFixedSize(30, 30)  # Make the button smaller
        back_button.clicked.connect(self.on_back_clicked)

        title = QLabel("Make a reservation")
        title.setFont(QFont("Arial", 12, QFont.Bold))
        title.setStyleSheet("color: white;")
        title.setAlignment(Qt.AlignCenter)

        header_layout.addWidget(back_button)
        header_layout.addWidget(back_button)
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
        venue_label = QLabel("Saint")
        venue_label.setFont(QFont("Arial", 24, QFont.Bold))
        venue_label.setStyleSheet("color: white;")
        venue_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(venue_label)

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

        # Guests
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
        # Table Section - Dropdown
        table_title = QLabel("☰  Select a table")
        table_title.setFont(QFont("Arial", 11))
        table_title.setStyleSheet("color: white;")
        
        table_dropdown = QComboBox()
        table_dropdown.addItems(["Table 1", "Table 2", "Table 3", "Table 4"])
        
        
        table_dropdown = QComboBox()
        table_dropdown.addItems(["Table 1", "Table 2", "Table 3", "Table 4"])
        
        card_layout.addWidget(table_title)
        card_layout.addWidget(table_dropdown)
        card_layout.addWidget(table_dropdown)

        # Drink Section - Dropdown
        # Drink Section - Dropdown
        drinks_title = QLabel("☰  Select drinks")
        drinks_title.setFont(QFont("Arial", 11))
        drinks_title.setStyleSheet("color: white;")
        
        drinks_dropdown = QComboBox()
        drinks_dropdown.addItems(["Drink 1", "Drink 2", "Drink 3", "Drink 4"])
        
        
        drinks_dropdown = QComboBox()
        drinks_dropdown.addItems(["Drink 1", "Drink 2", "Drink 3", "Drink 4"])
        
        card_layout.addWidget(drinks_title)
        card_layout.addWidget(drinks_dropdown)
        card_layout.addWidget(drinks_dropdown)

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

    def on_back_clicked(self):
        self.close()  # Close the current window when back is clicked


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ReservationUI()
    window.show()
    sys.exit(app.exec())