import sys
from PySide6.QtWidgets import (
    QWidget, QLabel, QPushButton, QDateEdit,
    QVBoxLayout, QHBoxLayout, QScrollArea
)
from PySide6.QtGui import QFont, QPixmap, QIcon
from PySide6.QtCore import Qt, QDate
from datetime import timedelta

class DayEntry(QWidget):
    def __init__(self, date_obj, event_info=None, image_path=None):
        super().__init__()
        layout = QHBoxLayout()
        layout.setContentsMargins(10, 5, 10, 5)
        layout.setSpacing(15)
        
        day_text = date_obj.strftime("%a - %d/%m/%Y")

        # Day label
        day_label = QLabel(day_text)
        day_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        day_label.setFixedWidth(130)  # Set a consistent width
        day_label.setStyleSheet("font-weight: bold; font-size: 14px;")
        layout.addWidget(day_label, alignment=Qt.AlignmentFlag.AlignCenter)

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


class AddEventPage(QWidget):
    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(15, 15, 15, 15)
        main_layout.setSpacing(10)

        # Header
        header_layout = QHBoxLayout()
        self.back_btn = QPushButton("←")
        self.back_btn.setFixedSize(30, 30)
        self.back_btn.setStyleSheet("font-size: 18px; border: none; background: transparent;")
        self.back_btn.setCursor(Qt.PointingHandCursor)
        self.back_btn.clicked.connect(self.go_back)

        title = QLabel("Add Event")
        title.setFont(QFont("Arial", 20, QFont.Bold))

        header_layout.addWidget(self.back_btn)
        header_layout.addWidget(title)
        header_layout.addStretch()
        self.date_picker = QDateEdit()
        self.date_picker.setCalendarPopup(True)
        self.date_picker.setDate(QDate.currentDate())
        self.date_picker.setDisplayFormat("yyyy-MM-dd")
        header_layout.addWidget(self.date_picker)

        main_layout.addLayout(header_layout)

        # Scrollable day list
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)
        content_layout.setSpacing(20)
        self.content_layout = content_layout
        
        scroll.setWidget(content_widget)
        main_layout.addWidget(scroll)

    def go_back(self):
        print("Back button clicked")
        
    def update_week(self, start_date, events_by_date):
        # Clear existing day entries
        for i in reversed(range(self.content_layout.count())):
            widget = self.content_layout.itemAt(i).widget()
            if widget:
                widget.setParent(None)

        weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        for i in range(7):
            day_date = start_date + timedelta(days=i)
            day_name = weekdays[i]
            events = events_by_date.get(day_date)
            
            if events:
                # You could also support multiple events here
                event_info = f"Event: {events[0].title}\nOpen Doors: {events[0].time.strftime('%H:%M')}"
                self.content_layout.addWidget(DayEntry(day_date, event_info))
            else:
                self.content_layout.addWidget(DayEntry(day_date))

