from PySide6.QtWidgets import (
    QWidget, QLineEdit, QPushButton, QLabel, 
    QVBoxLayout, QHBoxLayout, QFrame, QMessageBox
)
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt, Signal

class LoginView(QWidget):
    # Signals for user actions
    login_attempted = Signal(str, str)  # email, password
    signup_attempted = Signal(str, str, str)  # email, password, user_type
    google_login_attempted = Signal()
    apple_login_attempted = Signal()

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)
        layout.setContentsMargins(20, 20, 20, 20)

        # Title
        title = QLabel("ByNight")
        title.setFont(QFont("Old English Text MT", 24))
        title.setAlignment(Qt.AlignCenter)

        # Subtitle
        self.subtitle = QLabel("Enter your email and password to login")
        self.subtitle.setAlignment(Qt.AlignCenter)
        self.subtitle.setStyleSheet("color: gray; font-size: 12px;")

        # Email input
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("email@domain.com")
        self.email_input.setFixedHeight(40)
        self.email_input.setStyleSheet("padding: 8px; font-size: 14px;")
        self.email_input.returnPressed.connect(self.on_login_clicked)

        # Password input (always visible)
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setFixedHeight(40)
        self.password_input.setStyleSheet("padding: 8px; font-size: 14px;")
        self.password_input.returnPressed.connect(self.on_login_clicked)

        # Login button
        self.login_btn = QPushButton("Login")
        self.login_btn.setFixedHeight(40)
        self.login_btn.setStyleSheet("background-color: black; color: white; font-size: 14px;")
        self.login_btn.clicked.connect(self.on_login_clicked)

        # Divider
        divider_layout = QHBoxLayout()
        divider_layout.setContentsMargins(0, 20, 0, 10)

        line1 = QFrame()
        line1.setFrameShape(QFrame.HLine)
        line1.setFrameShadow(QFrame.Sunken)
        line1.setStyleSheet("color: lightgray;")

        or_label = QLabel("or")
        or_label.setStyleSheet("color: gray; padding: 0 10px; font-size: 12px;")
        or_label.setAlignment(Qt.AlignCenter)

        line2 = QFrame()
        line2.setFrameShape(QFrame.HLine)
        line2.setFrameShadow(QFrame.Sunken)
        line2.setStyleSheet("color: lightgray;")

        divider_layout.addWidget(line1)
        divider_layout.addWidget(or_label)
        divider_layout.addWidget(line2)

        # Social login buttons
        self.google_btn = QPushButton("  Continue with Google")
        self.google_btn.setFixedHeight(40)
        self.google_btn.setStyleSheet("""
          QPushButton {
            background-color: white;
            color: #202124;
            font-size: 13px;
            border: 1px solid #dadce0;
          }
          QPushButton:hover {
            background-color: #f1f3f4;
          }
        """)
        self.google_btn.clicked.connect(self.google_login_attempted.emit)

        self.apple_btn = QPushButton("  Continue with Apple")
        self.apple_btn.setFixedHeight(40)
        self.apple_btn.setStyleSheet("""
          QPushButton {
            background-color: white;
            color: black;
            font-size: 13px;
            border: 1px solid #dadce0;
          }
          QPushButton:hover {
            background-color: #f1f3f4;
          }
        """)
        self.apple_btn.clicked.connect(self.apple_login_attempted.emit)

        # Terms
        terms = QLabel("By clicking login, you agree to our Terms of Service and Privacy Policy")
        terms.setStyleSheet("font-size: 10px; color: gray;")
        terms.setWordWrap(True)
        terms.setAlignment(Qt.AlignCenter)

        # Assemble layout
        layout.addWidget(title)
        layout.addSpacing(10)
        layout.addWidget(self.subtitle)
        layout.addSpacing(20)
        layout.addWidget(self.email_input)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_btn)
        layout.addLayout(divider_layout)
        layout.addWidget(self.google_btn)
        layout.addWidget(self.apple_btn)
        layout.addStretch()
        layout.addWidget(terms)

        self.setLayout(layout)

    def show_error(self, message):
        QMessageBox.critical(self, "Error", message)

    def reset(self):
        self.email_input.clear()
        self.password_input.clear()

    def on_login_clicked(self):
        email = self.email_input.text()
        password = self.password_input.text()
        self.login_attempted.emit(email, password)
