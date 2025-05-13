import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout, QScrollArea
)
from PySide6.QtGui import QFont, QPixmap, QIcon
from PySide6.QtCore import Qt


class DayEntry(QWidget):
    def __init__(self, day, event_info=None, image_path=None):
        super().__init__()
        layout = QHBoxLayout()
        layout.setContentsMargins(10, 5, 10, 5)
        layout.setSpacing(15)

        # Day label
        day_label = QLabel(day)
        day_label.setFont(QFont("Arial", 12, QFont.Bold))
        day_label.setFixedWidth(90)
        layout.addWidget(day_label)

        # Optional image
        if image_path:
            image_label = QLabel()
            pixmap = QPixmap(image_path).scaled(50, 50, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            image_label.setPixmap(pixmap)
            layout.addWidget(image_label)

        # Event or "No Events" label
        if event_info:
            event_label = QLabel(event_info)
            event_label.setWordWrap(True)
            layout.addWidget(event_label)
        else:
            no_event_label = QLabel("No Events")
            no_event_label.setStyleSheet("color: gray")
            layout.addWidget(no_event_label)

        layout.addStretch()

        # Optional edit icon for events
        if event_info:
            edit_icon = QLabel()
            edit_icon.setPixmap(QPixmap.fromImage(QIcon.fromTheme("document-edit").pixmap(24, 24).toImage()))
            layout.addWidget(edit_icon)

        # Plus button (always present)
        plus_btn = QPushButton("➕")
        plus_btn.setFixedSize(30, 30)
        plus_btn.setStyleSheet("font-size: 18px; border: none; background: transparent;")
        plus_btn.setCursor(Qt.PointingHandCursor)
        plus_btn.clicked.connect(lambda: print(f"Add event for {day}"))
        layout.addWidget(plus_btn)

        self.setLayout(layout)


class AddEventWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Event")
        self.setMinimumSize(500, 600)

        central = QWidget()
        main_layout = QVBoxLayout(central)
        main_layout.setContentsMargins(15, 15, 15, 15)
        main_layout.setSpacing(10)

        # Header
        header_layout = QHBoxLayout()
        back_btn = QPushButton("←")
        back_btn.setFixedSize(30, 30)
        back_btn.setStyleSheet("font-size: 18px; border: none; background: transparent;")
        back_btn.setCursor(Qt.PointingHandCursor)
        back_btn.clicked.connect(self.go_back)

        title = QLabel("Add Event")
        title.setFont(QFont("Arial", 20, QFont.Bold))

        header_layout.addWidget(back_btn)
        header_layout.addWidget(title)
        header_layout.addStretch()
        date_label = QLabel("Date: Current Week")
        header_layout.addWidget(date_label)

        main_layout.addLayout(header_layout)

        # Scrollable day list
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)
        content_layout.setSpacing(20)

        # Sample week layout
        content_layout.addWidget(DayEntry("Monday"))
        content_layout.addWidget(DayEntry("Tuesday"))
        content_layout.addWidget(DayEntry("Wednesday", "Event: Kultura   Open Doors: 12:00", "event1.jpg"))
        content_layout.addWidget(DayEntry("Thursday", "Event: Lunes Colpa   Open Doors: 12:00", "event2.jpg"))
        content_layout.addWidget(DayEntry("Friday", "Supporting line text lorem ipsum dolor sit amet, consectetur."))
        content_layout.addWidget(DayEntry("Saturday", "Supporting line text lorem ipsum dolor sit amet, consectetur."))
        content_layout.addWidget(DayEntry("Sunday", "Supporting line text lorem ipsum dolor sit amet, consectetur."))

        scroll.setWidget(content_widget)
        main_layout.addWidget(scroll)

        self.setCentralWidget(central)

    def go_back(self):
        print("Back button clicked")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AddEventWindow()
    window.show()
    sys.exit(app.exec())