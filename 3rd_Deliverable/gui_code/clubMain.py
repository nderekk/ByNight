from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout, QFrame, QMessageBox
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import sys


class ClubPageApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Club Page")
        self.setMinimumSize(400, 700)
        self.setup_ui()

    def setup_ui(self):
        main_layout = QVBoxLayout()

        # Back Button & Header
        header_layout = QHBoxLayout()
        back_btn = QPushButton("←")
        back_btn.setFixedSize(30, 30)
        back_btn.setStyleSheet("font-size: 14pt;")
        header_layout.addWidget(back_btn)
        header_layout.addStretch()
        main_layout.addLayout(header_layout)

        # Club Image
        club_image = QLabel()
        header_pixmap = QPixmap(400, 200)
        header_pixmap.fill(Qt.darkMagenta)
        club_image.setPixmap(header_pixmap)
        club_image.setScaledContents(True)
        club_image.setFixedHeight(200)
        main_layout.addWidget(club_image)

        # Club Name
        name = QLabel("Kanakari 99")
        name.setStyleSheet("padding: 10px; font-size: 10pt;")
        main_layout.addWidget(name)

        # Tabs
        tab_layout = QHBoxLayout()
        upcoming_btn = QPushButton("Upcoming Events")
        photos_btn = QPushButton("Photos")
        for btn in [upcoming_btn, photos_btn]:
            btn.setFlat(True)
            btn.setStyleSheet("font-weight: bold; font-size: 10pt;")
        tab_layout.addWidget(upcoming_btn)
        tab_layout.addWidget(photos_btn)
        main_layout.addLayout(tab_layout)

        # Line separator
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        main_layout.addWidget(line)

        # Tonight's Event
        main_layout.addSpacing(10)
        main_layout.addWidget(QLabel("<b>Tonight's Event:</b>"))

        event_image = QLabel()
        event_pixmap = QPixmap(150, 150)
        event_pixmap.fill(Qt.red)
        event_image.setPixmap(event_pixmap)
        event_image.setScaledContents(True)
        event_image.setFixedSize(150, 150)
        event_image.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(event_image, alignment=Qt.AlignHCenter)

        # Event Info Button
        btn_event_info = QPushButton("Event Info")
        btn_event_info.setStyleSheet("""
            padding: 8px; font-size: 11pt;
            background-color: #333; color: white;
            border-radius: 8px;
        """)
        btn_event_info.setFixedWidth(120)
        btn_event_info.clicked.connect(self.show_event_info)
        main_layout.addWidget(btn_event_info, alignment=Qt.AlignHCenter)

        # Reservation Button
        btn_reserve = QPushButton("Reservation")
        btn_reserve.setStyleSheet("""
            padding: 10px; font-size: 12pt;
            background-color: #111; color: white;
            border-radius: 8px;
        """)
        btn_reserve.setFixedWidth(180)
        btn_reserve.clicked.connect(self.make_reservation)
        main_layout.addSpacing(5)
        main_layout.addWidget(btn_reserve, alignment=Qt.AlignHCenter)

        # Spacer
        main_layout.addStretch()

        # Contact Us
        contact = QLabel('<a href="#">Contact us</a>')
        contact.setOpenExternalLinks(True)
        contact.setStyleSheet("font-size: 9pt; color: gray;")
        contact.setAlignment(Qt.AlignRight)
        main_layout.addWidget(contact)

        self.setLayout(main_layout)

    def show_event_info(self):
        QMessageBox.information(self, "Event Info", "Details about tonight's event will be shown here.")

    def make_reservation(self):
        QMessageBox.information(self, "Reservation", "Reservation process starts here.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ClubPageApp()
    window.show()
    sys.exit(app.exec())