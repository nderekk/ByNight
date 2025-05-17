from PySide6.QtWidgets import (
  QWidget, QLineEdit, QPushButton, QLabel, 
  QVBoxLayout, QHBoxLayout, QFrame, QMessageBox
)
from PySide6.QtGui import QFont, QIcon
from PySide6.QtCore import Qt, Signal

class LoginView(QWidget):
  # Signals for user actions
  login_attempted = Signal(str, str)  # email, password
  signup_attempted = Signal(str, str, str)  # email, password, user_type
  google_login_attempted = Signal()
  apple_login_attempted = Signal()
  continue_clicked = Signal()  # New signal for continue button click

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
    self.subtitle = QLabel("Create an account\nEnter your email to sign up for this app")
    self.subtitle.setAlignment(Qt.AlignCenter)
    self.subtitle.setStyleSheet("color: gray; font-size: 12px;")

    # Email input
    self.email_input = QLineEdit()
    self.email_input.setPlaceholderText("email@domain.com")
    self.email_input.setFixedHeight(40)
    self.email_input.setStyleSheet("padding: 8px; font-size: 14px;")
    self.email_input.returnPressed.connect(self.on_continue_clicked)  # Add Enter key handler

    # Password input (initially hidden)
    self.password_input = QLineEdit()
    self.password_input.setPlaceholderText("Password")
    self.password_input.setEchoMode(QLineEdit.Password)
    self.password_input.setFixedHeight(40)
    self.password_input.setStyleSheet("padding: 8px; font-size: 14px;")
    self.password_input.hide()
    self.password_input.returnPressed.connect(self.on_continue_clicked)  # Add Enter key handler

    # Continue/Login button
    self.continue_btn = QPushButton("Continue")
    self.continue_btn.setFixedHeight(40)
    self.continue_btn.setStyleSheet("background-color: black; color: white; font-size: 14px;")
    self.continue_btn.clicked.connect(self.on_continue_clicked)

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
    self.google_btn.clicked.connect(self.on_google_clicked)

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
    self.apple_btn.clicked.connect(self.on_apple_clicked)

    # Terms
    terms = QLabel("By clicking continue, you agree to our Terms of Service and Privacy Policy")
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
    layout.addWidget(self.continue_btn)
    layout.addLayout(divider_layout)
    layout.addWidget(self.google_btn)
    layout.addWidget(self.apple_btn)
    layout.addStretch()
    layout.addWidget(terms)

    self.setLayout(layout)

  def on_google_clicked(self):
    self.google_login_attempted.emit()

  def on_apple_clicked(self):
    self.apple_login_attempted.emit()

  def show_password_step(self):
    self.password_input.show()
    self.subtitle.setText("Enter your password")
    self.continue_btn.setText("Login")
    self.email_input.setEnabled(False)

  def show_error(self, message):
    QMessageBox.critical(self, "Error", message)

  def reset(self):
    self.email_input.clear()
    self.email_input.setEnabled(True)
    self.password_input.clear()
    self.password_input.hide()
    self.continue_btn.setText("Continue")
    self.subtitle.setText("Create an account\nEnter your email to sign up for this app")

  def on_continue_clicked(self):
    self.continue_clicked.emit() 