from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton,
    QComboBox, QScrollArea, QFrame, QSizePolicy
)
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt, QSize, Signal
from app.models import Club,User


class CustomerHomePage(QWidget):
    more_button_clicked=Signal(Club)
    make_reservation_clicked=Signal(Club)
    
    
    def __init__(self, clubs: list[Club], filters: dict[str: list[str]]):
        super().__init__()
        self.clubs = clubs
        main_layout = QVBoxLayout(self)

        # --- Top Bar ---
        top_bar = QHBoxLayout()
        self.backButton = QPushButton("←")
        self.searchLineEdit = QLineEdit()
        self.searchLineEdit.setPlaceholderText("Search")
        top_bar.addWidget(self.backButton)
        top_bar.addWidget(self.searchLineEdit)
        main_layout.addLayout(top_bar)


        # --- Menu Buttons ---
        menu_bar = QHBoxLayout()
        self.menuButton = QPushButton("Work With Us")
        self.menuButton.setFont(QFont("", weight=QFont.Bold))
        self.viewResButton = QPushButton("View Reservations")
        self.profileButton = QPushButton("👤")
        menu_bar.addWidget(self.menuButton)
        menu_bar.addWidget(self.viewResButton)
        menu_bar.addWidget(self.profileButton)
        main_layout.addLayout(menu_bar)

        

        # --- Dropdowns ---
        filter_layout = QVBoxLayout()
        self.addressLabel = QLabel("address")
        self.addressDropdown = QComboBox()
        self.addressDropdown.addItem("Any")
        self.addressDropdown.addItems(filters["location"])
        filter_layout.addWidget(self.addressLabel)
        filter_layout.addWidget(self.addressDropdown)

        self.musicLabel = QLabel("Music")
        self.musicDropdown = QComboBox()
        self.musicDropdown.addItem("Any")
        self.musicDropdown.addItems(filters["music"])
        filter_layout.addWidget(self.musicLabel)
        filter_layout.addWidget(self.musicDropdown)

        self.eventLabel = QLabel("Event")
        self.eventDropdown = QComboBox()
        self.eventDropdown.addItem("Any")
        self.eventDropdown.addItems(filters["event"])
        filter_layout.addWidget(self.eventLabel)
        filter_layout.addWidget(self.eventDropdown)

        main_layout.addLayout(filter_layout)

        # --- Recommended Clubs Label ---
        self.recClubsText = QLabel("Recommended Clubs")
        self.recClubsText.setFont(QFont("", italic=True))
        self.recClubsText.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.recClubsText)

        # --- Scroll Area with Club Cards ---
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_content = QWidget()
        self.scroll_layout = QVBoxLayout(scroll_content)
            
        # Add club cards
        for club in self.clubs:
            self.scroll_layout.addWidget(self.create_club_card(club.name, club))

        scroll_area.setWidget(scroll_content)
        main_layout.addWidget(scroll_area)

    def create_club_card(self, club_name,club):
        card = QFrame()
        card.setFrameShape(QFrame.NoFrame)
        layout = QHBoxLayout(card)

        # Placeholder for club image
        image = QLabel(club_name)
        image.setMinimumSize(QSize(100, 100))
        image.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        layout.addWidget(image)

        # Buttons
        buttons_layout = QVBoxLayout()
        res_button = QPushButton("Make Reservation")
        more_button = QPushButton("More Details")
        buttons_layout.addWidget(res_button)
        buttons_layout.addWidget(more_button)
        layout.addLayout(buttons_layout)
        more_button.clicked.connect(lambda _, c=club: self.more_button_clicked.emit(c))
        res_button.clicked.connect(lambda _, c=club: self.make_reservation_clicked.emit(c))


        return card
    
    def update_club_display(self, filtered_clubs):
        # Clear existing club cards
        for i in reversed(range(self.scroll_layout.count())): 
            widget = self.scroll_layout.takeAt(i).widget()
            if widget:
                widget.setParent(None)

        if not filtered_clubs:
            # Show a message if no clubs match
            no_result_label = QLabel("No clubs matching your filters")
            no_result_label.setAlignment(Qt.AlignCenter)
            no_result_label.setStyleSheet("color: gray; font-style: italic; padding: 10px;")
            self.scroll_layout.addWidget(no_result_label)
            return
        
        # Add filtered club cards
        for club in filtered_clubs:
            self.scroll_layout.addWidget(self.create_club_card(club.name, club))
