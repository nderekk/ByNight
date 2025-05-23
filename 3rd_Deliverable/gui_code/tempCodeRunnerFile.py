import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton,
    QComboBox, QScrollArea, QFrame, QSizePolicy
)
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt, QSize


class MainUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Club Finder")
        self.resize(500, 650)

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
        self.menuButton = QPushButton("≡")
        self.menuButton.setFont(QFont("", weight=QFont.Bold))
        self.viewResButton = QPushButton("View Reservations")
        self.profileButton = QPushButton("👤")
        menu_bar.addWidget(self.menuButton)
        menu_bar.addWidget(self.viewResButton)
        menu_bar.addWidget(self.profileButton)
        main_layout.addLayout(menu_bar)

        # --- Dropdowns ---
        filter_layout = QVBoxLayout()
        self.locationLabel = QLabel("Location")
        self.locationDropdown = QComboBox()
        self.locationDropdown.addItems(["Athens", "Patras"])
        filter_layout.addWidget(self.locationLabel)
        filter_layout.addWidget(self.locationDropdown)

        self.musicLabel = QLabel("Music")
        self.musicDropdown = QComboBox()
        self.musicDropdown.addItems(["Rock", "Rap/Trap", "Pop", "Rnb"])
        filter_layout.addWidget(self.musicLabel)
        filter_layout.addWidget(self.musicDropdown)

        self.eventLabel = QLabel("Event")
        self.eventDropdown = QComboBox()
        self.eventDropdown.addItems(["Kultura", "Lules Culpa"])
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
        scroll_layout = QVBoxLayout(scroll_content)

        # Add 3 club cards
        for i in range(3):
            card = self.create_club_card(f"Club {i+1}")
            scroll_layout.addWidget(card)

        scroll_area.setWidget(scroll_content)
        main_layout.addWidget(scroll_area)

    def create_club_card(self, club_name):
        card = QFrame()
        card.setFrameShape(QFrame.NoFrame)
        layout = QHBoxLayout(card)

        # Placeholder for club image
        image = QLabel("ClubIMG")
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

        return card


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainUI()
    window.show()
    sys.exit(app.exec())
