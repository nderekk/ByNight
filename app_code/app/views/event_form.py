from PySide6.QtWidgets import (
  QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
  QLineEdit, QTimeEdit, QTextEdit, QApplication
)
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt, QDate, QTime
import sys

class EventForm(QWidget):
  def __init__(self, date_text):
    super().__init__()

    self.setStyleSheet("""
      QLabel { font-size: 16pt; }
      QLineEdit, QTimeEdit, QTextEdit {
        font-size: 12pt;
        padding: 6px;
        border-radius: 5px;
        border: 1px solid #ccc;
      }
      QTextEdit {
        min-height: 80px;
      }
    """)

    layout = QVBoxLayout(self)
    layout.setContentsMargins(20, 20, 20, 20)
    layout.setSpacing(16)

    # Header
    header_layout = QHBoxLayout()
    self.back_btn = QPushButton("←")
    self.back_btn.setFixedSize(30, 30)
    self.back_btn.setStyleSheet("font-size: 18px; border: none; background: transparent;")
    self.back_btn.setCursor(Qt.PointingHandCursor)

    title_label = QLabel("New Event")
    title_label.setFont(QFont("Arial", 20, QFont.Bold))

    date_display = QLabel(date_text)
    date_display.setStyleSheet("color: gray; font-size: 12pt; margin-left: 10px;")

    header_layout.addWidget(self.back_btn)
    header_layout.addWidget(title_label)
    header_layout.addStretch()
    header_layout.addWidget(date_display)
    header_layout.addStretch()

    layout.addLayout(header_layout)

    # Input fields
    self.title_input = QLineEdit()
    self.title_input.setPlaceholderText("Title*")
    layout.addWidget(self._labeled("Title:", self.title_input))

    self.description_input = QTextEdit()
    self.description_input.setPlaceholderText("Description")
    layout.addWidget(self._labeled("Description:", self.description_input))

    self.music_input = QLineEdit()
    self.music_input.setPlaceholderText("Music Type")
    layout.addWidget(self._labeled("Music:", self.music_input))

    self.time_input = QTimeEdit()
    self.time_input.setTime(QTime.currentTime())
    layout.addWidget(self._labeled("Time:", self.time_input))

    # Save button
    self.save_btn = QPushButton("Save")
    self.save_btn.setEnabled(False)
    self.save_btn.setStyleSheet("""
      QPushButton {
        font-size: 13pt;
        padding: 8px 16px;
        border-radius: 6px;
        background-color: #aaa;
        color: white;
      }
      QPushButton:disabled {
        background-color: #444;
        color: #ccc;
      }
    """)
    self.save_btn.setCursor(Qt.PointingHandCursor)
    layout.addWidget(self.save_btn)

    # Connect input changes to validation
    self._connect_validation()

  def _labeled(self, label_text, widget):
    wrapper = QVBoxLayout()
    label = QLabel(label_text)
    wrapper.addWidget(label)
    wrapper.addWidget(widget)
    container = QWidget()
    container.setLayout(wrapper)
    return container

  def _connect_validation(self):
    self.title_input.textChanged.connect(self._validate)
    self.time_input.timeChanged.connect(self._validate)

  def _validate(self):
    if all([
      self.title_input.text().strip(),
      self.time_input.time().isValid()
    ]):
      self.save_btn.setEnabled(True)
    else:
      self.save_btn.setEnabled(False)
