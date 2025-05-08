# -*- coding: utf-8 -*-
################################################################################
## Form generated from reading UI file 'homepage.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QPushButton, QScrollArea, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_mainWidget(object):
    def setupUi(self, mainWidget):
        if not mainWidget.objectName():
            mainWidget.setObjectName(u"mainWidget")
        mainWidget.resize(518, 618)
        self.verticalLayout = QVBoxLayout(mainWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(1, -1, -1, -1)
        self.backButton = QPushButton(mainWidget)
        self.backButton.setObjectName(u"backButton")
        icon = QIcon()
        if QIcon.hasThemeIcon(QIcon.ThemeIcon.GoPrevious):
            icon = QIcon.fromTheme(QIcon.ThemeIcon.GoPrevious)
        else:
            icon.addFile(u".", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.backButton.setIcon(icon)

        self.horizontalLayout.addWidget(self.backButton)

        self.searchLineEdit = QLineEdit(mainWidget)
        self.searchLineEdit.setObjectName(u"searchLineEdit")

        self.horizontalLayout.addWidget(self.searchLineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.menuButton = QPushButton(mainWidget)
        self.menuButton.setObjectName(u"menuButton")
        font = QFont()
        font.setBold(True)
        self.menuButton.setFont(font)
        self.menuButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.menuButton)

        self.viewResButton = QPushButton(mainWidget)
        self.viewResButton.setObjectName(u"viewResButton")

        self.horizontalLayout_4.addWidget(self.viewResButton)

        self.profileButton = QPushButton(mainWidget)
        self.profileButton.setObjectName(u"profileButton")
        icon1 = QIcon()
        iconThemeName = u"user-available"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u".", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.profileButton.setIcon(icon1)
        self.profileButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.profileButton)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.locationLabel = QLabel(mainWidget)
        self.locationLabel.setObjectName(u"locationLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.locationLabel.sizePolicy().hasHeightForWidth())
        self.locationLabel.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.locationLabel)

        self.locationDropdown = QComboBox(mainWidget)
        self.locationDropdown.addItem("")
        self.locationDropdown.addItem("")
        self.locationDropdown.addItem("")
        self.locationDropdown.setObjectName(u"locationDropdown")

        self.verticalLayout_2.addWidget(self.locationDropdown)

        self.musicLabel = QLabel(mainWidget)
        self.musicLabel.setObjectName(u"musicLabel")

        self.verticalLayout_2.addWidget(self.musicLabel)

        self.musicDropdown = QComboBox(mainWidget)
        self.musicDropdown.addItem("")
        self.musicDropdown.addItem("")
        self.musicDropdown.addItem("")
        self.musicDropdown.addItem("")
        self.musicDropdown.setObjectName(u"musicDropdown")

        self.verticalLayout_2.addWidget(self.musicDropdown)

        self.eventLabel = QLabel(mainWidget)
        self.eventLabel.setObjectName(u"eventLabel")

        self.verticalLayout_2.addWidget(self.eventLabel)

        self.eventDropdown = QComboBox(mainWidget)
        self.eventDropdown.addItem("")
        self.eventDropdown.addItem("")
        self.eventDropdown.setObjectName(u"eventDropdown")

        self.verticalLayout_2.addWidget(self.eventDropdown)


        self.formLayout.setLayout(0, QFormLayout.ItemRole.LabelRole, self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.recClubsText = QLabel(mainWidget)
        self.recClubsText.setObjectName(u"recClubsText")
        font1 = QFont()
        font1.setBold(False)
        font1.setItalic(True)
        self.recClubsText.setFont(font1)
        self.recClubsText.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.recClubsText)

        self.scrollArea = QScrollArea(mainWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 378, 500))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.clubCard1 = QFrame(self.scrollAreaWidgetContents)
        self.clubCard1.setObjectName(u"clubCard1")
        self.clubCard1.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_6 = QHBoxLayout(self.clubCard1)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label = QLabel(self.clubCard1)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(100, 100))

        self.horizontalLayout_6.addWidget(self.label)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.makeResButton = QPushButton(self.clubCard1)
        self.makeResButton.setObjectName(u"makeResButton")

        self.verticalLayout_5.addWidget(self.makeResButton)

        self.moreDetailsPage = QPushButton(self.clubCard1)
        self.moreDetailsPage.setObjectName(u"moreDetailsPage")

        self.verticalLayout_5.addWidget(self.moreDetailsPage)


        self.horizontalLayout_6.addLayout(self.verticalLayout_5)


        self.verticalLayout_4.addWidget(self.clubCard1)

        self.clubCard1_2 = QFrame(self.scrollAreaWidgetContents)
        self.clubCard1_2.setObjectName(u"clubCard1_2")
        self.clubCard1_2.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_7 = QHBoxLayout(self.clubCard1_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_2 = QLabel(self.clubCard1_2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setMinimumSize(QSize(100, 100))

        self.horizontalLayout_7.addWidget(self.label_2)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.makeResButton_2 = QPushButton(self.clubCard1_2)
        self.makeResButton_2.setObjectName(u"makeResButton_2")

        self.verticalLayout_6.addWidget(self.makeResButton_2)

        self.moreDetails2 = QPushButton(self.clubCard1_2)
        self.moreDetails2.setObjectName(u"moreDetails2")

        self.verticalLayout_6.addWidget(self.moreDetails2)


        self.horizontalLayout_7.addLayout(self.verticalLayout_6)


        self.verticalLayout_4.addWidget(self.clubCard1_2)

        self.clubCard1_3 = QFrame(self.scrollAreaWidgetContents)
        self.clubCard1_3.setObjectName(u"clubCard1_3")
        self.clubCard1_3.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_8 = QHBoxLayout(self.clubCard1_3)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_3 = QLabel(self.clubCard1_3)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setMinimumSize(QSize(100, 100))

        self.horizontalLayout_8.addWidget(self.label_3)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.makeResButton_3 = QPushButton(self.clubCard1_3)
        self.makeResButton_3.setObjectName(u"makeResButton_3")

        self.verticalLayout_7.addWidget(self.makeResButton_3)

        self.moreDetails3 = QPushButton(self.clubCard1_3)
        self.moreDetails3.setObjectName(u"moreDetails3")

        self.verticalLayout_7.addWidget(self.moreDetails3)


        self.horizontalLayout_8.addLayout(self.verticalLayout_7)


        self.verticalLayout_4.addWidget(self.clubCard1_3)

        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_5 = QHBoxLayout(self.frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setMinimumSize(QSize(100, 100))

        self.horizontalLayout_5.addWidget(self.label_4)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_10.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_10.addWidget(self.pushButton_2)


        self.horizontalLayout_5.addLayout(self.verticalLayout_10)


        self.verticalLayout_4.addWidget(self.frame)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 4)

        self.formLayout.setLayout(0, QFormLayout.ItemRole.FieldRole, self.verticalLayout_3)


        self.verticalLayout.addLayout(self.formLayout)


        self.retranslateUi(mainWidget)

        QMetaObject.connectSlotsByName(mainWidget)
    # setupUi

    def retranslateUi(self, mainWidget):
        mainWidget.setWindowTitle(QCoreApplication.translate("mainWidget", u"Form", None))
        self.backButton.setText("")
        self.searchLineEdit.setPlaceholderText(QCoreApplication.translate("mainWidget", u"Search", None))
        self.menuButton.setText(QCoreApplication.translate("mainWidget", u"\u2261", None))
        self.viewResButton.setText(QCoreApplication.translate("mainWidget", u"View Reservations", None))
        self.profileButton.setText("")
        self.locationLabel.setText(QCoreApplication.translate("mainWidget", u"Location", None))
        self.locationDropdown.setItemText(0, QCoreApplication.translate("mainWidget", u"Athens", None))
        self.locationDropdown.setItemText(1, QCoreApplication.translate("mainWidget", u"Patra", None))
        self.locationDropdown.setItemText(2, QCoreApplication.translate("mainWidget", u"Thessaloniki", None))

        self.musicLabel.setText(QCoreApplication.translate("mainWidget", u"Music", None))
        self.musicDropdown.setItemText(0, QCoreApplication.translate("mainWidget", u"Rock", None))
        self.musicDropdown.setItemText(1, QCoreApplication.translate("mainWidget", u"Rap/Trap", None))
        self.musicDropdown.setItemText(2, QCoreApplication.translate("mainWidget", u"Pop", None))
        self.musicDropdown.setItemText(3, QCoreApplication.translate("mainWidget", u"Rnb", None))

        self.eventLabel.setText(QCoreApplication.translate("mainWidget", u"Event", None))
        self.eventDropdown.setItemText(0, QCoreApplication.translate("mainWidget", u"Kultura", None))
        self.eventDropdown.setItemText(1, QCoreApplication.translate("mainWidget", u"Lules Culpa", None))

        self.recClubsText.setText(QCoreApplication.translate("mainWidget", u"Recommended Clubs", None))
        self.label.setText(QCoreApplication.translate("mainWidget", u"ClubIMG", None))
        self.makeResButton.setText(QCoreApplication.translate("mainWidget", u"Make Reservation", None))
        self.moreDetailsPage.setText(QCoreApplication.translate("mainWidget", u"More Details", None))
        self.label_2.setText(QCoreApplication.translate("mainWidget", u"ClubIMG", None))
        self.makeResButton_2.setText(QCoreApplication.translate("mainWidget", u"Make Reservation", None))
        self.moreDetails2.setText(QCoreApplication.translate("mainWidget", u"More Details", None))
        self.label_3.setText(QCoreApplication.translate("mainWidget", u"ClubIMG", None))
        self.makeResButton_3.setText(QCoreApplication.translate("mainWidget", u"Make Reservation", None))
        self.moreDetails3.setText(QCoreApplication.translate("mainWidget", u"More Details", None))
        self.label_4.setText(QCoreApplication.translate("mainWidget", u"ClubIMG", None))
        self.pushButton.setText(QCoreApplication.translate("mainWidget", u"Make Reservation", None))
        self.pushButton_2.setText(QCoreApplication.translate("mainWidget", u"More Details", None))
    # retranslateUi

