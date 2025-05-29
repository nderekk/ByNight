import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton,
    QFrame, QSizePolicy
)
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt, QSize


class ManagerUI(QWidget):
    def __init__(self, club_registered):
        super().__init__()
        self.club_registered = club_registered
        self.setWindowTitle("Manager Homepage")
        self.resize(500, 650)

        main_layout = QVBoxLayout(self)

        # --- Manager Actions ---
        actions_bar = QHBoxLayout()
        self.urClubButton = QPushButton("Ur Club")
        actions_bar.addWidget(self.urClubButton)
        self.viewResButton = QPushButton("View Reservations")
        self.addEventButton = QPushButton("Add Event")
        self.viewStatsButton = QPushButton("View Stats")
        self.giveDiscountsButton = QPushButton("Give Discounts")
        actions_bar.addWidget(self.viewResButton)
        actions_bar.addWidget(self.addEventButton)
        actions_bar.addWidget(self.viewStatsButton)
        actions_bar.addWidget(self.giveDiscountsButton)
        main_layout.addLayout(actions_bar)
        if not self.club_registered:
            self.viewResButton.setDisabled(True)
            self.addEventButton.setDisabled(True)
            self.viewStatsButton.setDisabled(True)
            self.giveDiscountsButton.setDisabled(True)

        # --- Club Details Section ---
        club_details = QFrame()
        club_details_layout = QVBoxLayout(club_details)
        club_details_layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        # Club Image
        self.clubImage = QLabel("ClubIMG")
        self.clubImage.setFixedSize(300, 200)
        self.clubImage.setStyleSheet("background-color: lightgray; border: 1px solid #ccc;")
        self.clubImage.setAlignment(Qt.AlignCenter)
        club_details_layout.addWidget(self.clubImage)

        # Club Info
        self.clubName = QLabel("Club Name:")
        self.clubName.setFont(QFont("", 14, QFont.Bold))
        self.clubName.setAlignment(Qt.AlignCenter)

        self.clubDesc = QLabel("Club Details:")
        self.clubDesc.setWordWrap(True)
        self.clubDesc.setAlignment(Qt.AlignCenter)

        club_details_layout.addWidget(self.clubName)
        club_details_layout.addWidget(self.clubDesc)

        main_layout.addWidget(club_details)


 
