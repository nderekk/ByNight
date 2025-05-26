from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from app.models.club import Club
from app.models.user import User
from app.services.db_session import DatabaseSession
from app.utils.container import Container

class ClubCreator:
    def __init__(self, show_page: callable, club_details: callable):
        self.show_page = show_page
        self.club_details = club_details
        self.user = Container.resolve(User)
        self.session = Container.resolve(DatabaseSession)

    def ur_club(self):
        self.window = QWidget()
        self.window.setWindowTitle("Create or Edit Your Club")
        layout = QVBoxLayout(self.window)

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Club Name")
        self.addr_input = QLineEdit()
        self.addr_input.setPlaceholderText("Address")
        self.loc_input = QLineEdit()
        self.loc_input.setPlaceholderText("Location")

        self.submit_btn = QPushButton("Save Club")
        self.submit_btn.clicked.connect(self.save_or_update_club)

        layout.addWidget(QLabel("Enter or Update Your Club Info:"))
        layout.addWidget(self.name_input)
        layout.addWidget(self.addr_input)
        layout.addWidget(self.loc_input)
        layout.addWidget(self.submit_btn)

        
        existing_club = self.session.query(Club).filter_by(manager_id=self.user.id).first()
        self.existing_club = existing_club

        if existing_club:
            self.name_input.setText(existing_club.name)
            self.addr_input.setText(existing_club.address)
            self.loc_input.setText(existing_club.location)

        self.window.show()

    def save_or_update_club(self):
        name = self.name_input.text().strip()
        address = self.addr_input.text().strip()
        location = self.loc_input.text().strip()

        if not name or not address or not location:
            QMessageBox.warning(self.window, "Validation Error", "All fields are required.")
            return

         
        if self.existing_club:
            self.existing_club.name = name
            self.existing_club.address = address
            self.existing_club.location = location
            self.session.commit()
            QMessageBox.information(self.window, "Success", "Club updated successfully!")
        else:
             
            if self.session.query(Club).filter_by(name=name).first():
                QMessageBox.critical(self.window, "Error", "Club with this name already exists.")
                return

            new_club = Club(
                name=name,
                address=address,
                location=location,
                manager_id=self.user.id
            )
            self.session.add(new_club)
            self.session.commit()
            QMessageBox.information(self.window, "Success", f"Club '{name}' created successfully!")

        self.club_details({
            "name": name,
            "address": address,
            "location": location
        })

        self.window.close()
