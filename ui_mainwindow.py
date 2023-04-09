# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QSizePolicy,
    QSpinBox, QTabWidget, QTimeEdit, QVBoxLayout,
    QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#centralWidget \n"
"{\n"
"	border-style: solid;\n"
"	border-color: gray;\n"
"	border-width: 10px;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame{\n"
"	border: none;\n"
"}\n"
"\n"
"#frame {\n"
"	border: 2px solid #515151;	\n"
"}\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(0)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.toolbar = QFrame(self.frame)
        self.toolbar.setObjectName(u"toolbar")
        self.toolbar.setMinimumSize(QSize(0, 60))
        self.toolbar.setMaximumSize(QSize(16777215, 60))
        self.toolbar.setStyleSheet(u"\n"
"#toolbar {\n"
"	border-bottom: 1px solid #323232;\n"
"	background-color: #3c3f41;\n"
"}")
        self.toolbar.setFrameShape(QFrame.StyledPanel)
        self.toolbar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.toolbar)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.top_panel = QFrame(self.toolbar)
        self.top_panel.setObjectName(u"top_panel")
        self.top_panel.setMaximumSize(QSize(16777215, 40))
        self.top_panel.setLayoutDirection(Qt.LeftToRight)
        self.top_panel.setStyleSheet(u"#top_panel\n"
"{\n"
"	border-bottom: 1px solid #515151;\n"
"}")
        self.top_panel.setFrameShape(QFrame.StyledPanel)
        self.top_panel.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.top_panel)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.appInfo = QFrame(self.top_panel)
        self.appInfo.setObjectName(u"appInfo")
        self.appInfo.setFrameShape(QFrame.StyledPanel)
        self.appInfo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.appInfo)
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 0, 0)
        self.appIcon = QFrame(self.appInfo)
        self.appIcon.setObjectName(u"appIcon")
        self.appIcon.setMinimumSize(QSize(20, 20))
        self.appIcon.setMaximumSize(QSize(20, 20))
        self.appIcon.setStyleSheet(u"image: url(:/icons/icons/appIcon.png);\n"
"background-repeat: no-repeat;")
        self.appIcon.setFrameShape(QFrame.StyledPanel)
        self.appIcon.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_7.addWidget(self.appIcon)

        self.appName = QLabel(self.appInfo)
        self.appName.setObjectName(u"appName")
        self.appName.setStyleSheet(u"color: white;")

        self.horizontalLayout_7.addWidget(self.appName)


        self.horizontalLayout.addWidget(self.appInfo)

        self.system_buttons = QFrame(self.top_panel)
        self.system_buttons.setObjectName(u"system_buttons")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.system_buttons.sizePolicy().hasHeightForWidth())
        self.system_buttons.setSizePolicy(sizePolicy)
        self.system_buttons.setMaximumSize(QSize(140, 16777215))
        self.system_buttons.setStyleSheet(u"border: none")
        self.system_buttons.setFrameShape(QFrame.StyledPanel)
        self.system_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.system_buttons)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.minusButton = QPushButton(self.system_buttons)
        self.minusButton.setObjectName(u"minusButton")
        self.minusButton.setMaximumSize(QSize(70, 50))
        self.minusButton.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"   background-color: #4f5254;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/icons/minus1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minusButton.setIcon(icon)
        self.minusButton.setIconSize(QSize(10, 10))

        self.horizontalLayout_2.addWidget(self.minusButton)

        self.minimizeButton = QPushButton(self.system_buttons)
        self.minimizeButton.setObjectName(u"minimizeButton")
        self.minimizeButton.setMaximumSize(QSize(70, 50))
        self.minimizeButton.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"   background-color: #4f5254;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/minimize1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeButton.setIcon(icon1)
        self.minimizeButton.setIconSize(QSize(10, 10))
        self.minimizeButton.setFlat(False)

        self.horizontalLayout_2.addWidget(self.minimizeButton)

        self.closeButton = QPushButton(self.system_buttons)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setMaximumSize(QSize(70, 50))
        self.closeButton.setStyleSheet(u"#closeButton:hover\n"
"{\n"
"	background-color: red;\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/close1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeButton.setIcon(icon2)
        self.closeButton.setIconSize(QSize(10, 10))

        self.horizontalLayout_2.addWidget(self.closeButton)


        self.horizontalLayout.addWidget(self.system_buttons)


        self.verticalLayout_2.addWidget(self.top_panel)

        self.bottom_panel = QFrame(self.toolbar)
        self.bottom_panel.setObjectName(u"bottom_panel")
        self.bottom_panel.setMaximumSize(QSize(16777215, 20))
        self.bottom_panel.setLayoutDirection(Qt.LeftToRight)
        self.bottom_panel.setFrameShape(QFrame.StyledPanel)
        self.bottom_panel.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottom_panel)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_2.addWidget(self.bottom_panel)


        self.verticalLayout_3.addWidget(self.toolbar)

        self.base = QFrame(self.frame)
        self.base.setObjectName(u"base")
        self.base.setStyleSheet(u"#base {\n"
"	background-color: #2b2b2b;\n"
"}")
        self.base.setFrameShape(QFrame.StyledPanel)
        self.base.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.base)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.actualBase = QFrame(self.base)
        self.actualBase.setObjectName(u"actualBase")
        self.actualBase.setFrameShape(QFrame.StyledPanel)
        self.actualBase.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.actualBase)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.leftSide = QFrame(self.actualBase)
        self.leftSide.setObjectName(u"leftSide")
        self.leftSide.setFrameShape(QFrame.StyledPanel)
        self.leftSide.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.leftSide)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.calendarNavBar = QFrame(self.leftSide)
        self.calendarNavBar.setObjectName(u"calendarNavBar")
        self.calendarNavBar.setMinimumSize(QSize(0, 25))
        self.calendarNavBar.setMaximumSize(QSize(16777215, 30))
        self.calendarNavBar.setStyleSheet(u"QFrame {\n"
"	background-color: #3c3f41;\n"
"}")
        self.calendarNavBar.setFrameShape(QFrame.StyledPanel)
        self.calendarNavBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.calendarNavBar)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.prevButton = QPushButton(self.calendarNavBar)
        self.prevButton.setObjectName(u"prevButton")
        self.prevButton.setMinimumSize(QSize(25, 25))
        self.prevButton.setMaximumSize(QSize(25, 25))
        self.prevButton.setFocusPolicy(Qt.StrongFocus)
        self.prevButton.setStyleSheet(u"QPushButton {\n"
"	background-color: #3c3f41;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #515151;\n"
"	border: none;\n"
"}\n"
"\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/prev.png", QSize(), QIcon.Normal, QIcon.Off)
        self.prevButton.setIcon(icon3)

        self.horizontalLayout_10.addWidget(self.prevButton)

        self.frame_2 = QFrame(self.calendarNavBar)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.frame_2)

        self.monthSelect = QComboBox(self.calendarNavBar)
        self.monthSelect.addItem("")
        self.monthSelect.addItem("")
        self.monthSelect.addItem("")
        self.monthSelect.addItem("")
        self.monthSelect.addItem("")
        self.monthSelect.addItem("")
        self.monthSelect.addItem("")
        self.monthSelect.addItem("")
        self.monthSelect.addItem("")
        self.monthSelect.addItem("")
        self.monthSelect.addItem("")
        self.monthSelect.addItem("")
        self.monthSelect.setObjectName(u"monthSelect")
        self.monthSelect.setMaximumSize(QSize(70, 16777215))
        self.monthSelect.setStyleSheet(u"QComboBox {\n"
"margin-right: 3px;\n"
"background-color: #3c3f41;\n"
"border: none;\n"
"color: white;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"	background-color: #515151;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"	image: url(:/icons/icons/down.png);\n"
"	width: 10px;\n"
"}\n"
"\n"
"QComboBox::drop-down{border: none;}\n"
"\n"
"")
        self.monthSelect.setMaxVisibleItems(12)

        self.horizontalLayout_10.addWidget(self.monthSelect)

        self.yearSelect = QSpinBox(self.calendarNavBar)
        self.yearSelect.setObjectName(u"yearSelect")
        self.yearSelect.setMaximumSize(QSize(50, 16777215))
        self.yearSelect.setStyleSheet(u"QSpinBox {\n"
"	background-color: #3c3f41;\n"
"	border: none;\n"
"	color: white;\n"
"}\n"
"\n"
"QSpinBox:hover {\n"
"	background-color: #515151;\n"
"	border: none;\n"
"	color: white;\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"	border: none;\n"
"	image: url(:/icons/icons/down.png);\n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"	border: none;\n"
"	image: url(:/icons/icons/up.png);\n"
"}")
        self.yearSelect.setMinimum(2000)
        self.yearSelect.setMaximum(2100)

        self.horizontalLayout_10.addWidget(self.yearSelect)

        self.frame_3 = QFrame(self.calendarNavBar)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.frame_3)

        self.nextButton = QPushButton(self.calendarNavBar)
        self.nextButton.setObjectName(u"nextButton")
        self.nextButton.setMinimumSize(QSize(25, 25))
        self.nextButton.setMaximumSize(QSize(25, 25))
        self.nextButton.setStyleSheet(u"QPushButton {\n"
"	background-color: #3c3f41;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #515151;\n"
"	border: none;\n"
"}\n"
"\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/next.png", QSize(), QIcon.Normal, QIcon.Off)
        self.nextButton.setIcon(icon4)

        self.horizontalLayout_10.addWidget(self.nextButton)


        self.verticalLayout_6.addWidget(self.calendarNavBar)

        self.calendarDays = QFrame(self.leftSide)
        self.calendarDays.setObjectName(u"calendarDays")
        self.calendarDays.setMinimumSize(QSize(0, 30))
        self.calendarDays.setMaximumSize(QSize(16777215, 30))
        self.calendarDays.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"	font-weight: bold;\n"
"}")
        self.calendarDays.setFrameShape(QFrame.StyledPanel)
        self.calendarDays.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.calendarDays)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label = QLabel(self.calendarDays)
        self.label.setObjectName(u"label")

        self.horizontalLayout_11.addWidget(self.label)

        self.label_2 = QLabel(self.calendarDays)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_11.addWidget(self.label_2)

        self.label_3 = QLabel(self.calendarDays)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_11.addWidget(self.label_3)

        self.label_4 = QLabel(self.calendarDays)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_11.addWidget(self.label_4)

        self.label_5 = QLabel(self.calendarDays)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_11.addWidget(self.label_5)

        self.label_6 = QLabel(self.calendarDays)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"color: red;")

        self.horizontalLayout_11.addWidget(self.label_6)

        self.label_7 = QLabel(self.calendarDays)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"color: red;")

        self.horizontalLayout_11.addWidget(self.label_7)


        self.verticalLayout_6.addWidget(self.calendarDays)


        self.horizontalLayout_4.addWidget(self.leftSide)

        self.sidePanel = QFrame(self.actualBase)
        self.sidePanel.setObjectName(u"sidePanel")
        self.sidePanel.setMinimumSize(QSize(400, 0))
        self.sidePanel.setMaximumSize(QSize(400, 16777215))
        self.sidePanel.setStyleSheet(u"QFrame\n"
"{\n"
"background-color: #3c3f41;\n"
"}\n"
"\n"
"#sidePanel\n"
"{\n"
"	border-left: 1px solid #323232;\n"
"	background-color: #323232;\n"
"}")
        self.sidePanel.setFrameShape(QFrame.StyledPanel)
        self.sidePanel.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.sidePanel)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.sidePanel)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(0, 0))
        self.tabWidget.setStyleSheet(u"#tabWidget {\n"
"	border: none\n"
"}\n"
"\n"
" QTabBar::tab {\n"
"     background-color: #313335;\n"
"	color: gray;\n"
"	border-bottom-color: #C2C7CB; \n"
"     border-top-left-radius: 4px;\n"
"     border-top-right-radius: 4px;\n"
"     min-width: 8ex;\n"
"     padding: 2px;\n"
"	height: 25px;\n"
"	width: 80px;\n"
" }\n"
"\n"
"QTabBar::tab:hover {\n"
"     background-color: #515151;\n"
" }\n"
"\n"
" QTabBar::tab:selected {\n"
"     border-color: #3c3f41;\n"
"     border-bottom-color: #3c3f41; \n"
"	background-color: #3c3f41;\n"
"	color: white;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"\n"
"	border-bottom: 1px solid #323232; \n"
"}")
        self.tabWidget.setTabBarAutoHide(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(2)
        sizePolicy1.setHeightForWidth(self.tab.sizePolicy().hasHeightForWidth())
        self.tab.setSizePolicy(sizePolicy1)
        self.tab.setMaximumSize(QSize(399, 100000))
        self.tab.setStyleSheet(u"background-color: #3c3f41;\n"
"border:  none;")
        self.horizontalLayout_8 = QHBoxLayout(self.tab)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.taskList = QListWidget(self.tab)
        self.taskList.setObjectName(u"taskList")
        self.taskList.setStyleSheet(u"QListWidget::item\n"
"{\n"
"    background: rgb(255,255,255); \n"
"}\n"
"QListWidget::item:selected\n"
"{\n"
"    background: rgb(128,128,255);\n"
"}")
        self.taskList.setSelectionRectVisible(True)

        self.horizontalLayout_8.addWidget(self.taskList)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        sizePolicy1.setHeightForWidth(self.tab_2.sizePolicy().hasHeightForWidth())
        self.tab_2.setSizePolicy(sizePolicy1)
        self.tab_2.setStyleSheet(u"border: none;\n"
"background-color: #3c3f41;")
        self.allTaskList = QListWidget(self.tab_2)
        self.allTaskList.setObjectName(u"allTaskList")
        self.allTaskList.setGeometry(QRect(0, 0, 401, 9999))
        sizePolicy1.setHeightForWidth(self.allTaskList.sizePolicy().hasHeightForWidth())
        self.allTaskList.setSizePolicy(sizePolicy1)
        self.allTaskList.setMaximumSize(QSize(401, 99999))
        self.allTaskList.setStyleSheet(u"QListWidget {\n"
"	background-color: #3c3f41;\n"
"}")
        self.allTaskList.setSelectionRectVisible(True)
        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_5.addWidget(self.tabWidget)

        self.editPanel = QFrame(self.sidePanel)
        self.editPanel.setObjectName(u"editPanel")
        self.editPanel.setMinimumSize(QSize(0, 30))
        self.editPanel.setStyleSheet(u"#editPanel {\n"
"	border-top: 1px solid #515151;\n"
"}")
        self.editPanel.setFrameShape(QFrame.StyledPanel)
        self.editPanel.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.editPanel)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.selectColor = QPushButton(self.editPanel)
        self.selectColor.setObjectName(u"selectColor")
        self.selectColor.setMinimumSize(QSize(30, 30))
        self.selectColor.setMaximumSize(QSize(30, 30))
        self.selectColor.setStyleSheet(u"background-color: red;")
        self.selectColor.setFlat(False)

        self.horizontalLayout_12.addWidget(self.selectColor)

        self.lineEdit = QLineEdit(self.editPanel)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(999999, 16777215))
        self.lineEdit.setStyleSheet(u"background-color: #323232;\n"
"border: 1px solid #323232;\n"
"color: white;\n"
"margin-right: 5px;\n"
"margin-left: 5px;")

        self.horizontalLayout_12.addWidget(self.lineEdit)

        self.frame_4 = QFrame(self.editPanel)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_4)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.checkBox = QCheckBox(self.frame_4)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setStyleSheet(u"color: white;")
        self.checkBox.setChecked(True)

        self.verticalLayout_7.addWidget(self.checkBox)

        self.timeEdit = QTimeEdit(self.frame_4)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setStyleSheet(u"QTimeEdit {\n"
"	background-color: #3c3f41;\n"
"	border: none;\n"
"	color: white;\n"
"}\n"
"\n"
"QTimeEdit:hover {\n"
"	background-color: #515151;\n"
"	border: none;\n"
"	color: white;\n"
"}\n"
"\n"
"QTimeEdit::down-button {\n"
"	border: none;\n"
"	image: url(:/icons/icons/down.png);\n"
"}\n"
"\n"
"QTimeEdit::up-button {\n"
"	border: none;\n"
"	image: url(:/icons/icons/up.png);\n"
"}")
        self.timeEdit.setReadOnly(True)

        self.verticalLayout_7.addWidget(self.timeEdit)


        self.horizontalLayout_12.addWidget(self.frame_4)

        self.bellButton = QPushButton(self.editPanel)
        self.bellButton.setObjectName(u"bellButton")
        self.bellButton.setMinimumSize(QSize(30, 30))
        self.bellButton.setMaximumSize(QSize(30, 30))
        self.bellButton.setStyleSheet(u"QPushButton {\n"
"	background-color: #3c3f41;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:checked { \n"
"background-color: #515151; \n"
"} \n"
"\n"
"QPushButton:hover {\n"
"                            background-color: #515151;\n"
"                        }")
        self.icon5 = QIcon()
        self.icon5.addFile(u":/icons/icons/bell.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bellButton.setIcon(self.icon5)
        self.bellButton.setCheckable(True)

        self.horizontalLayout_12.addWidget(self.bellButton)

        self.pushButton = QPushButton(self.editPanel)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(30, 30))
        self.pushButton.setMaximumSize(QSize(30, 30))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	background-color: #3c3f41;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #515151;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/tick.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon6)

        self.horizontalLayout_12.addWidget(self.pushButton)


        self.verticalLayout_5.addWidget(self.editPanel)

        self.sidePanelTop = QFrame(self.sidePanel)
        self.sidePanelTop.setObjectName(u"sidePanelTop")
        self.sidePanelTop.setMinimumSize(QSize(0, 30))
        self.sidePanelTop.setMaximumSize(QSize(16777215, 30))
        self.sidePanelTop.setFocusPolicy(Qt.NoFocus)
        self.sidePanelTop.setAutoFillBackground(False)
        self.sidePanelTop.setStyleSheet(u"#sidePanelTop {	\n"
"	border-bottom: 1px solid #323232;\n"
"	border-top: 1px solid #515151;\n"
"}")
        self.sidePanelTop.setFrameShape(QFrame.StyledPanel)
        self.sidePanelTop.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.sidePanelTop)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.addButton = QPushButton(self.sidePanelTop)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setMinimumSize(QSize(30, 30))
        self.addButton.setMaximumSize(QSize(30, 30))
        self.addButton.setStyleSheet(u"#addButton {\n"
"	background-color: #3c3f41;\n"
"	border: none;\n"
"}\n"
"\n"
"#addButton:hover\n"
"{\n"
"   background-color: #4f5254;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addButton.setIcon(icon7)
        self.addButton.setFlat(True)

        self.horizontalLayout_6.addWidget(self.addButton)

        self.delButton = QPushButton(self.sidePanelTop)
        self.delButton.setObjectName(u"delButton")
        self.delButton.setMinimumSize(QSize(30, 30))
        self.delButton.setMaximumSize(QSize(30, 30))
        self.delButton.setStyleSheet(u"#delButton {\n"
"	background-color: #3c3f41;\n"
"	border: none;\n"
"}\n"
"\n"
"#delButton:hover\n"
"{\n"
"   background-color: #4f5254;\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/bin.png", QSize(), QIcon.Normal, QIcon.Off)
        self.delButton.setIcon(icon8)
        self.delButton.setFlat(True)

        self.horizontalLayout_6.addWidget(self.delButton)


        self.verticalLayout_5.addWidget(self.sidePanelTop)


        self.horizontalLayout_4.addWidget(self.sidePanel)


        self.verticalLayout_4.addWidget(self.actualBase)

        self.statusBar = QFrame(self.base)
        self.statusBar.setObjectName(u"statusBar")
        self.statusBar.setMinimumSize(QSize(0, 20))
        self.statusBar.setMaximumSize(QSize(16777215, 20))
        self.statusBar.setStyleSheet(u"#statusBar\n"
"{\n"
"\n"
"border-top: 1px solid #515151;\n"
"}\n"
"\n"
"QFrame\n"
"{\n"
"background-color: #3c3f41;\n"
"}")
        self.statusBar.setFrameShape(QFrame.StyledPanel)
        self.statusBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.statusBar)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.baseStatusBar = QFrame(self.statusBar)
        self.baseStatusBar.setObjectName(u"baseStatusBar")
        self.baseStatusBar.setFrameShape(QFrame.StyledPanel)
        self.baseStatusBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.baseStatusBar)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.timeLabel = QLabel(self.baseStatusBar)
        self.timeLabel.setObjectName(u"timeLabel")
        self.timeLabel.setStyleSheet(u"color: gray;\n"
"margin-left: 5px;")

        self.horizontalLayout_9.addWidget(self.timeLabel)

        self.pushButton_2 = QPushButton(self.baseStatusBar)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_9.addWidget(self.pushButton_2)


        self.horizontalLayout_3.addWidget(self.baseStatusBar)

        self.resize = QFrame(self.statusBar)
        self.resize.setObjectName(u"resize")
        self.resize.setMaximumSize(QSize(20, 16777215))
        self.resize.setFrameShape(QFrame.StyledPanel)
        self.resize.setFrameShadow(QFrame.Raised)
        self.resize.setLineWidth(1)

        self.horizontalLayout_3.addWidget(self.resize)


        self.verticalLayout_4.addWidget(self.statusBar)


        self.verticalLayout_3.addWidget(self.base)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.appName.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0449\u0438\u043a \u0437\u0430\u0434\u0430\u0447 v1.0", None))
        self.minusButton.setText("")
        self.minimizeButton.setText("")
        self.closeButton.setText("")
        self.prevButton.setText("")
        self.monthSelect.setItemText(0, QCoreApplication.translate("MainWindow", u"\u042f\u043d\u0432\u0430\u0440\u044c", None))
        self.monthSelect.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0424\u0435\u0432\u0440\u0430\u043b\u044c", None))
        self.monthSelect.setItemText(2, QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0440\u0442", None))
        self.monthSelect.setItemText(3, QCoreApplication.translate("MainWindow", u"\u0410\u043f\u0440\u0435\u043b\u044c", None))
        self.monthSelect.setItemText(4, QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0439", None))
        self.monthSelect.setItemText(5, QCoreApplication.translate("MainWindow", u"\u0418\u044e\u043d\u044c", None))
        self.monthSelect.setItemText(6, QCoreApplication.translate("MainWindow", u"\u0418\u044e\u043b\u044c", None))
        self.monthSelect.setItemText(7, QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0433\u0443\u0441\u0442", None))
        self.monthSelect.setItemText(8, QCoreApplication.translate("MainWindow", u"\u0421\u0435\u043d\u0442\u044f\u0431\u0440\u044c", None))
        self.monthSelect.setItemText(9, QCoreApplication.translate("MainWindow", u"\u041e\u043a\u0442\u044f\u0431\u0440\u044c", None))
        self.monthSelect.setItemText(10, QCoreApplication.translate("MainWindow", u"\u041d\u043e\u044f\u0431\u0440\u044c", None))
        self.monthSelect.setItemText(11, QCoreApplication.translate("MainWindow", u"\u0414\u0435\u043a\u0430\u0431\u0440\u044c", None))

        self.nextButton.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043d", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0442", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0442", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0442", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0431\u044b\u0442\u0438\u044f \u0434\u043d\u044f", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435 \u0441\u043e\u0431\u044b\u0442\u0438\u044f", None))
        self.selectColor.setText("")
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"Task", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0435\u0441\u044c \u0434\u0435\u043d\u044c", None))
        self.bellButton.setText("")
        self.pushButton.setText("")
        self.addButton.setText("")
        self.delButton.setText("")
        self.timeLabel.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi

