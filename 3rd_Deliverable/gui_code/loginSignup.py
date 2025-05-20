from PySide6.QtWidgets import (
    QApplication, QWidget, QLineEdit, QPushButton,
    QLabel, QVBoxLayout, QHBoxLayout, QFrame
)
from PySide6.QtGui import QFont, QIcon
from PySide6.QtCore import Qt
import sys

class LoginSignupWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ByNight - Login/Signup")
        self.setFixedSize(360, 480)
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
        subtitle = QLabel("Create an account\nEnter your email to sign up for this app")
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setStyleSheet("color: gray; font-size: 12px;")

        # Email input
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("email@domain.com")
        self.email_input.setFixedHeight(40)
        self.email_input.setStyleSheet("padding: 8px; font-size: 14px;")

        # Continue button
        continue_btn = QPushButton("Continue")
        continue_btn.setFixedHeight(40)
        continue_btn.setStyleSheet("background-color: black; color: white; font-size: 14px;")

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

        # Google Button
        google_btn = QPushButton("  Continue with Google")
        google_btn.setFixedHeight(40)
        google_btn.setStyleSheet("""
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
        google_btn.setIcon(QIcon.fromTheme("google"))  # Replace if needed

        # Apple Button
        apple_btn = QPushButton("  Continue with Apple")
        apple_btn.setFixedHeight(40)
        apple_btn.setStyleSheet("""
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
        apple_btn.setIcon(QIcon.fromTheme("apple")) 

        # Terms
        terms = QLabel("By clicking continue, you agree to our Terms of Service and Privacy Policy")
        terms.setStyleSheet("font-size: 10px; color: gray;")
        terms.setWordWrap(True)
        terms.setAlignment(Qt.AlignCenter)

        # Assemble layout
        layout.addWidget(title)
        layout.addSpacing(10)
        layout.addWidget(subtitle)
        layout.addSpacing(20)
        layout.addWidget(self.email_input)
        layout.addWidget(continue_btn)
        layout.addLayout(divider_layout)
        layout.addWidget(google_btn)
        layout.addWidget(apple_btn)
        layout.addStretch()
        layout.addWidget(terms)

        self.setLayout(layout)

# Run the app
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginSignupWindow()
    window.show()
    sys.exit(app.exec())
