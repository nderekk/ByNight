from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from app.models.club import Club
from app.models.user import User
from app.services.db_session import DatabaseSession
from app.utils.container import Container

class ClubCreator:
    def __init__(self, show_page: callable, club_details: callable):
        self.show_page = show_page
        self.club_details=club_details
        self.user = Container.resolve(User)

    def ur_club(self):
        self.window = QWidget()
        self.window.setWindowTitle("Create Your Club")
        layout = QVBoxLayout(self.window)

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Club Name")
        self.addr_input = QLineEdit()
        self.addr_input.setPlaceholderText("Address")
        self.loc_input = QLineEdit()
        self.loc_input.setPlaceholderText("Location")

        submit_btn = QPushButton("Create Club")
        submit_btn.clicked.connect(self.create_club)

        layout.addWidget(QLabel("Enter Your Club Info:"))
        layout.addWidget(self.name_input)
        layout.addWidget(self.addr_input)
        layout.addWidget(self.loc_input)
        layout.addWidget(submit_btn)

        self.window.show()

    def create_club(self):
        name = self.name_input.text().strip()
        address = self.addr_input.text().strip()
        location = self.loc_input.text().strip()

        if not name or not address or not location:
            QMessageBox.warning(self.window, "Validation Error", "All fields are required.")
            return

        session = Container.resolve(DatabaseSession)

        if session.query(Club).filter_by(name=name).first():
            QMessageBox.critical(self.window, "Error", "Club with this name already exists.")
            return

        new_club = Club(
            name=name,
            address=address,
            location=location,
            manager_id=self.user.id
        )
        session.add(new_club)
        session.commit()

        self.club_details({
            "name": name,
            "address": address,
            "location": location
        })

        QMessageBox.information(self.window, "Success", f"Club '{name}' created successfully!")
        self.window.close()
