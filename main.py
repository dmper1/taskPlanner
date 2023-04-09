import sys
import random
import os.path
import pickle
from PySide6 import QtCore, QtWidgets, QtGui, QtMultimedia
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QMainWindow, QFrame
from ui_mainwindow import Ui_MainWindow
from PySide6.QtCore import QFile, Qt, QRectF, QDate, QSize, QUrl
from PySide6.QtGui import QColor, QPainter, QIcon
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput, QSoundEffect
import icons_rc
from itertools import groupby
from playsound import playsound
import winsound
import datetime
import math


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowTitle("Task Planner")
        appIcon = QIcon()
        appIcon.addFile(u":/icons/icons/appIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(appIcon)

        self.calendar = MyCalendar(self)
        self.ui.verticalLayout_6.addWidget(self.calendar)
        # self.ui.horizontalLayout_4.addWidget(self.ui.sidePanel)
        self.calendar.setStyleSheet("""
            QCalendarWidget QWidget#qt_calendar_navigationbar {
            background-color: #3c3f41;
            }

            QCalendarWidget QWidget{
            background-color: #3c3f41;
            color: white;
            }

            QCalendarWidget QAbstractItemView:enabled{
            background-color: #2b2b2b;
            color: white;
            font-weight: bold;
            }

            QCalendarWidget QAbstractItemView:disabled{
            background-color: #323232;
            color: #515151;
            }

            QAbstractItemView:item:selected { background-color: #515151; }

            QCalendarWidget QAbstractItemView:item:hover {
            border: 3px solid #515151; 
            }

            #qt_calendar_prevmonth, #qt_calendar_nextmonth {
                border: none;
                color: gray;
                font-weight: bold;
                qproperty-icon: none;    
                background-color: transparent;
            }

            #qt_calendar_prevmonth {
                qproperty-text: "<";      
            }

            #qt_calendar_nextmonth {
                qproperty-text: ">";
            }

            #qt_calendar_prevmonth:hover, #qt_calendar_nextmonth:hover {
                background-color: rgba(225, 225, 225, 100);
            }
            """)


        if os.path.exists(f'{os.getenv("APPDATA")}/TaskPlanner/tasks.txt'):
            with open(f'{os.getenv("APPDATA")}/TaskPlanner/tasks.txt', 'rb') as f:
                MainWindow.__init__.tasks = pickle.load(f)
                # print(self.tasks)
                # print(type(self.tasks))
        else:
            MainWindow.__init__.tasks = [] 

        if os.path.exists(f'{os.getenv("APPDATA")}/TaskPlanner/settings.txt'):
            with open(f'{os.getenv("APPDATA")}/TaskPlanner/settings.txt', 'rb') as f:
                self.settings = pickle.load(f)
                # print(self.tasks)
                # print(type(self.tasks))
        else:
            self.settings = {'enabledAS': True, 'timeoutAS': 5} 

        # self.id = 0
        if MainWindow.__init__.tasks == []:
            self.id = 0
        else:
            for i in MainWindow.__init__.tasks:
                self.id = i['id']


        # self.tasks = []

        self.isMaximized = False 
        
        self.current_id = 0
        self.lastClicked = 0
        self.color = '#ff0000'
        self.prevItem = 0
        self.c = 0
        self.is_Select = False
        MainWindow.__init__.isInit = True
        self.actions = []
        self.undoCount = 0
        self.cancels = []

        self.refresh()

        self.ui.top_panel.mouseMoveEvent = self.moveWindow
        self.ui.closeButton.clicked.connect(self.exitApp)
        self.ui.minusButton.clicked.connect(self.showMinimized)
        self.ui.minimizeButton.clicked.connect(self.changeMode)

        QtWidgets.QSizeGrip(self.ui.resize)

        self.fmt = self.calendar.headerTextFormat()
        self.fmt.setForeground(QtGui.QColor('white'))
        self.fmt.setBackground(QtGui.QColor('#3c3f41'))
        self.calendar.setHeaderTextFormat(self.fmt)

        self.file_toolbar = QtWidgets.QMenuBar(self.ui.bottom_panel)
        self.file_toolbar.setStyleSheet("""
            QMenuBar {
                background-color: #3c3f41;
                color: white;
            }

            QMenuBar::item:selected { /* when selected using mouse or keyboard */
                background: #515151;
            }

            QMenuBar::item:pressed {
                background: #515151;
            }

            QMenu { background-color: #3c3f41; color: white; }
            QMenu::item:selected { background-color: #515151; }

            """)
        self.file_toolbar.setMinimumWidth(300)
        self.saveAct = QtGui.QAction('Сохранить')
        self.saveAct.triggered.connect(self.saveFile)
        self.saveAct.setShortcut('Ctrl+S')
        self.deleteAllAct = QtGui.QAction('Удалить все')
        self.deleteAllAct.triggered.connect(self.deleteAll)
        self.fileMenu = self.file_toolbar.addMenu('Файл')
        self.fileMenu.addAction(self.saveAct)
        self.fileMenu.addAction(self.deleteAllAct)
        self.fileMenu.setStyleSheet("""
            #fileMenu:hover {
                background-color: black;
            }
            """)

        self.ui.taskList.setStyleSheet("""
            QlistWidget {
                background-color: black;
            }

            QListWidget::item:selected {
                background-color: rgb(128,128,255);
            }
            """)

        self.undoAct = QtGui.QAction('Отменить')
        self.undoAct.triggered.connect(self.undo)
        self.undoAct.setShortcut('Ctrl+Z')
        self.redoAct = QtGui.QAction('Вернуть')
        self.redoAct.triggered.connect(self.redo)
        self.redoAct.setShortcut('Ctrl+Y')
        self.editMenu = self.file_toolbar.addMenu('Правка')
        self.editMenu.addAction(self.undoAct)
        self.editMenu.addAction(self.redoAct)

        self.otherMenu = self.file_toolbar.addMenu('Прочее')
        self.settingsAct = QtGui.QAction('Настройки')
        self.otherMenu.addAction(self.settingsAct)
        self.settingsAct.triggered.connect(self.openSettings)

        self.ui.pushButton.clicked.connect(self.editTask)
        self.ui.selectColor.clicked.connect(self.selectColor)
        self.ui.delButton.clicked.connect(self.deleteItem)
        
        self.ui.addButton.clicked.connect(self.addTask)

        self.ui.taskList.itemClicked.connect(self.selectTask)
        self.ui.taskList.currentItemChanged.connect(self.selectionChanged)

        self.ui.pushButton_2.clicked.connect(self.testClick)

        self.calendar.selectionChanged.connect(self.dateChanged)
        self.calendar.currentPageChanged.connect(self.refreshNavBar)

        self.ui.checkBox.stateChanged.connect(self.changedAllDay)

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.updateTime)
        self.timer.start(1000) 

        self.timer1 = QtCore.QTimer(self)
        self.timer1.timeout.connect(self.bellActivate)
        self.timer1.start(50000) 

        # self.timerAS = QtCore.QTimer(self)
        # self.timerAS.timeout.connect(self.saveSettings)
        # self.timerAS.start(self.settings['timeoutAS']) 

        # self.ui.lineEdit.setVisible(False)
        # self.ui.pushButton.setVisible(False)
        # self.ui.checkBox.setVisible(False)
        # self.ui.timeEdit.setVisible(False)
        # self.ui.selectColor.setVisible(False)
        # self.ui.bellButton.setVisible(False)
        self.ui.delButton.setVisible(False)

        self.ui.editPanel.setVisible(False)

        self.ui.taskList.setAutoFillBackground(False)

        self.calendar.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendar.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.NoHorizontalHeader)
        self.calendar.setNavigationBarVisible(False)
        self.calendar.setGridVisible(False)

        self.icon3 = QIcon()
        self.icon3.addFile(u":/icons/icons/bell.png", QSize(), QIcon.Normal, QIcon.Off)

        self.refreshNavBar()

        self.ui.prevButton.clicked.connect(self.calendar.showPreviousMonth)
        self.ui.nextButton.clicked.connect(self.calendar.showNextMonth)
        self.ui.monthSelect.currentIndexChanged.connect(self.refreshMonth)
        self.ui.yearSelect.textChanged.connect(self.refreshYear)

        self.ui.tabWidget.currentChanged.connect(self.tabChanged)

        self.undoStack = QtGui.QUndoStack()

        self.player = QSoundEffect()
        url = QUrl.fromLocalFile(u":/icons/icons/sound.wav")
        self.player.setSource(url)
        self.player.setLoopCount(5)
        self.player.setVolume(0.2)

        self.ui.pushButton_2.setVisible(False)


    def mousePressEvent(self, event):                                 
        self.clickPosition = event.globalPosition()

    def moveWindow(self, e):
        if self.isMaximized == False:
            if e.buttons() == QtCore.Qt.LeftButton: 
                self.move(self.pos() + QtCore.QPointF.toPoint(e.globalPosition()) - QtCore.QPointF.toPoint(self.clickPosition))
                self.clickPosition = e.globalPosition()
                e.accept()

    def changeMode(self):
        if self.isMaximized == False:
            self.showMaximized()
            self.isMaximized = True
            self.screenShape = self.frameGeometry()
        elif self.isMaximized == True:
            self.isMaximized = False
            self.showNormal()
            self.move(self.screenShape.left(), self.screenShape.top())
            self.resize(self.screenShape.width(), self.screenShape.height())

    def addTask(self):

        self.id += 1

        self.taskCard = QtWidgets.QWidget()
        self.taskCard.resize(400, 50)
        self.taskCard.setStyleSheet("""
            QWidget:hover {
                background-color: #515151;
            }
            """)
        self.taskName = QtWidgets.QLabel()
        self.taskName.setText(f'Task {self.id}')
        self.taskName.setAutoFillBackground(True)
        self.taskName.setStyleSheet("""
            color: white;
            background:transparent;
            """)
        self.colorIndicator = QtWidgets.QPushButton()
        self.colorIndicator.resize(30, 30)
        self.colorIndicator.setStyleSheet(f"""
            background-color: #ff0000;
            """)
        self.timeLabel = QtWidgets.QLabel()
        # if self.ui.checkBox.isChecked():
        #     self.timeLabel.setText('Весь день')
        # else:
        #     self.timeLabel.setText(self.ui.timeEdit.time().toString())
        self.timeLabel.setText('Весь день')
        self.timeLabel.setStyleSheet("""
            color: gray;
            background:transparent;
            """)
        self.bellIcon = QtWidgets.QPushButton()
        self.bellIcon.resize(30, 30)
        self.bellIcon.setIcon(self.ui.icon5)
        self.main_layout = QtWidgets.QHBoxLayout()
        self.main_layout.addWidget(self.colorIndicator)
        self.main_layout.addWidget(self.taskName)
        self.main_layout.addWidget(self.timeLabel)
        self.main_layout.addStretch()
        self.taskCard.setLayout(self.main_layout)

        self.itemTask = QtWidgets.QListWidgetItem()
        self.ui.taskList.insertItem(self.ui.taskList.count(), self.itemTask)
        self.ui.taskList.setItemWidget(self.itemTask, self.taskCard)
        self.itemTask.setSizeHint(self.taskCard.sizeHint())
        self.itemTask.setData(0, self.id)


        MainWindow.__init__.tasks.append({'id': self.itemTask.data(0), 'date': self.calendar.selectedDate(), 'color': '#ff0000', 'text': self.taskName.text(), 'time': 0, 'bell': 0})

        # if self.ui.checkBox.isChecked():
        #     MainWindow.__init__.tasks.append({'id': self.itemTask.data(0), 'date': self.calendar.selectedDate(), 'color': '#ff0000', 'text': self.taskName.text(), 'time': 0, 'bell': 0})
        # else:
        #     MainWindow.__init__.tasks.append({'id': self.itemTask.data(0), 'date': self.calendar.selectedDate(), 'color': '#ff0000', 'text': self.taskName.text(), 'time': self.ui.timeEdit.time(), 'bell': 0})
        print(MainWindow.__init__.tasks)

        self.ui.taskList.setCurrentItem(self.itemTask)

        self.actions = ['new', {'id': self.itemTask.data(0), 'date': self.calendar.selectedDate(), 'color': '#ff0000', 'text': self.taskName.text(), 'time': 0, 'bell': 0}]


        self.calendar.updateCells()
        



    def selectColor(self):
        self.colorPicker = QtWidgets.QColorDialog()
        self.color = self.colorPicker.getColor().name()
        self.ui.selectColor.setStyleSheet(f"""
            background-color: {self.color};
            """)

    def selectTask(self, item):
        self.ui.taskList.setCurrentItem(item)

    def selectionChanged(self, curItem, prevItem):

        # cursor_position = QtGui.QWindow.mapFromGlobal(QtGui.QCursor.pos())
        # print(cursor_position)

        if self.ui.taskList.currentItem() == None:
            self.is_Select = False

            # self.ui.lineEdit.setVisible(False)
            # self.ui.lineEdit.setVisible(False)
            # self.ui.pushButton.setVisible(False)
            # self.ui.checkBox.setVisible(False)
            # self.ui.timeEdit.setVisible(False)
            # self.ui.selectColor.setVisible(False)
            # self.ui.bellButton.setVisible(False)
            self.ui.delButton.setVisible(False)

            self.ui.editPanel.setVisible(False)
        else:
            # self.ui.lineEdit.setVisible(True)
            # self.ui.pushButton.setVisible(True)
            # self.ui.checkBox.setVisible(True)
            # self.ui.timeEdit.setVisible(True)
            # self.ui.selectColor.setVisible(True)
            # self.ui.bellButton.setVisible(True)
            self.ui.delButton.setVisible(True)

            self.ui.editPanel.setVisible(True)

        self.is_Select = True
        sel_id = self.ui.taskList.currentItem().data(0)
        print(sel_id)
        for i in MainWindow.__init__.tasks:
            if i['id'] == sel_id:
                self.ui.lineEdit.setText(i['text'])
                self.ui.selectColor.setStyleSheet(f"""
                    background-color: {i['color']};
                    """)
                self.color = i['color']
                if i['time'] == 0:
                    self.ui.checkBox.setChecked(True)
                    self.ui.timeEdit.setStyleSheet("""
                        QTimeEdit {
                            background-color: #3c3f41;
                            border: none;
                            color: gray;
                        }

                        QTimeEdit:hover {
                            background-color: #515151;
                            border: none;
                            color: white;
                        }

                        QTimeEdit::down-button {
                            border: none;
                            image: url(:/icons/icons/down.png);
                        }

                        QTimeEdit::up-button {
                            border: none;
                            image: url(:/icons/icons/up.png);
                        }
                        """)
                else:
                    self.ui.checkBox.setChecked(False)
                    self.ui.timeEdit.setTime(i['time'])
                    self.ui.timeEdit.setStyleSheet("""
                        QTimeEdit {
                            background-color: #3c3f41;
                            border: none;
                            color: white;
                        }

                        QTimeEdit:hover {
                            background-color: #515151;
                            border: none;
                            color: white;
                        }

                        QTimeEdit::down-button {
                            border: none;
                            image: url(:/icons/icons/down.png);
                        }

                        QTimeEdit::up-button {
                            border: none;
                            image: url(:/icons/icons/up.png);
                        }
                        """)
                if i['bell'] == 0:
                    self.ui.bellButton.setChecked(False)
                else:
                    self.ui.bellButton.setChecked(True)
        task_widget = self.ui.taskList.itemWidget(self.ui.taskList.currentItem())
        task_widget.setStyleSheet("""
            QWidget {
            background-color: #515151;
            }

            QWidget:hover {
                background-color: #515151;
            }
            """)

        # if self.prevItem != 0 and self.ui.taskList.currentItem() != self.prevItem:
        #     # print(self.ui.taskList.currentItem(), self.prevItem)
        #     self.widget_prevItem = self.ui.taskList.itemWidget(self.prevItem)
        #     self.widget_prevItem.setStyleSheet("""
        #         QWidget {
        #         background-color: #3c3f41;
        #         }

        #         QWidget:hover {
        #         background-color: #515151;
        #         }
        #         """)

        widget_prevItem = self.ui.taskList.itemWidget(prevItem)
        widget_prevItem.setStyleSheet("""
                        QWidget {
                        background-color: #3c3f41;
                        }

                        QWidget:hover {
                        background-color: #515151;
                        }
                        """)


        if self.ui.checkBox.isChecked() == True:
            self.ui.bellButton.setChecked(False)
            self.ui.bellButton.setCheckable(False)
        else:
            self.ui.bellButton.setCheckable(True)


        self.prevItem = self.ui.taskList.currentItem()
        self.c += 1

        test_widget = self.ui.taskList.itemWidget(self.ui.taskList.currentItem())

        self.calendar.updateCells()

        



    def testClick(self):
        # winsound.PlaySound('SystemQuestion', winsound.SND_FILENAME)
        # print(self.ui.taskList.currentItem().data(0), self.prevItem.data(0))
        # print(self.calendar.frameGeometry().height())
        # print(self.ui.taskList.currentItem())

        # print(self.calendar.frameGeometry().height())
        # a = round((((self.calendar.frameGeometry().height() / 8) - 15) / 30 - 1))
        # print(a)

        # b = self.calendar.selectedDate().toString()
        # b = b.split(' ')
        # b = int(b[3] + b[2])

        # b = int(self.calendar.selectedDate().toString().split(' ')[3] + self.calendar.selectedDate().toString().split(' ')[2])
        # print(b)
        # print(math.floor((((self.calendar.frameGeometry().height() / 8) - 15) / 30)))

        # print(self.actions)
        # print(self.cancels)

        print(self.calendar.frameGeometry().width() / 4.65 / 10)


    def editTask(self):
        task_widget = self.ui.taskList.itemWidget(self.ui.taskList.currentItem())
        for i in MainWindow.__init__.tasks:
            if i['id'] == self.ui.taskList.currentItem().data(0):
                res = i.copy()
                i['text'] = self.ui.lineEdit.text()
                i['color'] = self.color
                if self.ui.checkBox.isChecked():
                    i['time'] = 0
                else:
                    i['time'] = self.ui.timeEdit.time()
                if self.ui.bellButton.isChecked():
                    i['bell'] = 1
                else:
                    i['bell'] = 0
                self.actions = [res, {'id': i['id'], 'date': i['date'], 'color': i['color'], 'text': i['text'], 'time': i['time'], 'bell': i['bell']}]
                self.refresh()
                self.calendar.updateCells()


    def dateChanged(self):
        self.refresh()
        self.ui.taskList.clearSelection()
        self.prevItem = 0

    def refresh(self):
        self.ui.taskList.clear()
        for i in MainWindow.__init__.tasks:
            if i['date'] == self.calendar.selectedDate():
                self.addTaskAutomatically(i['id'])

    def addTaskAutomatically(self, id):
        task = 0
        for i in MainWindow.__init__.tasks:
            if i['id'] == id:
                task = i

        self.taskCard = QtWidgets.QFrame()
        self.taskCard.resize(400, 50)
        self.taskCard.setStyleSheet("""
            QWidget:hover {
                background-color: #515151;
            }
            """)
        self.taskCard.setAutoFillBackground(False)
        self.taskName = QtWidgets.QLabel()
        self.taskName.setText(task['text'])
        self.taskName.setStyleSheet("""
            color: white;
            background:transparent
            """)
        
        self.colorIndicator = QtWidgets.QPushButton()
        self.colorIndicator.resize(30, 30)
        self.colorIndicator.setStyleSheet(f"""
            background-color: {task['color']};
            """)
        self.timeLabel = QtWidgets.QLabel()
        if task['time'] == 0:
            self.timeLabel.setText('Весь день')
        else:
            self.timeLabel.setText(task['time'].toString('hh:mm'))
        self.timeLabel.setStyleSheet("""
            color: gray;
            background:transparent;
            """)
        self.timeLabel.setAutoFillBackground(False)
        if task['bell'] == 1:
            self.bellIcon = QtWidgets.QPushButton()
            self.bellIcon.resize(30, 30)
            self.bellIcon.setIcon(self.ui.icon5)
            self.bellIcon.setStyleSheet("""
                background:transparent;
                """)
        self.main_layout = QtWidgets.QHBoxLayout()
        self.main_layout.addWidget(self.colorIndicator)
        self.main_layout.addWidget(self.taskName)
        self.main_layout.addWidget(self.timeLabel)
        if task['bell'] == 1:  
            self.main_layout.addWidget(self.bellIcon)
        self.main_layout.addStretch()
        self.taskCard.setLayout(self.main_layout)

        self.itemTask = QtWidgets.QListWidgetItem()
        self.ui.taskList.insertItem(self.ui.taskList.count(), self.itemTask)
        self.ui.taskList.setItemWidget(self.itemTask, self.taskCard)
        self.itemTask.setSizeHint(self.taskCard.sizeHint())
        self.itemTask.setData(0, id)

    def exitApp(self):
        folder_path = f'{os.getenv("APPDATA")}/TaskPlanner'
        save_path = f'{os.getenv("APPDATA")}/TaskPlanner/tasks.txt'
        if os.path.exists(folder_path):
            with open(save_path, 'wb') as f:
                # f.write(str(self.tasks))
                pickle.dump(MainWindow.__init__.tasks, f)
                print(f'EXIT ---- {MainWindow.__init__.tasks}')
        else:
            os.mkdir(folder_path)
            with open(save_path, 'wb') as f:
                # f.write(str(self.tasks))
                pickle.dump(MainWindow.__init__.tasks, f)

        QApplication.quit()

    def deleteItem(self):
        for i in MainWindow.__init__.tasks:
            if i['id'] == self.ui.taskList.currentItem().data(0):
                MainWindow.__init__.tasks.remove(i)
                print(f'delete {i["id"]} from file')
                self.actions = ['del', i]
        self.ui.taskList.takeItem(self.ui.taskList.currentRow())
        self.calendar.updateCells()

    def changedAllDay(self):
        if self.ui.checkBox.isChecked():
            self.ui.timeEdit.setReadOnly(True)
            self.ui.bellButton.setChecked(False)
            self.ui.bellButton.setCheckable(False)
            self.ui.timeEdit.setStyleSheet("""
                QTimeEdit {
                    background-color: #3c3f41;
                    border: none;
                    color: gray;
                }

                QTimeEdit:hover {
                    background-color: #515151;
                    border: none;
                    color: white;
                }

                QTimeEdit::down-button {
                    border: none;
                    image: url(:/icons/icons/down.png);
                }

                QTimeEdit::up-button {
                    border: none;
                    image: url(:/icons/icons/up.png);
                }
                """)
        else:
            self.ui.timeEdit.setReadOnly(False)
            self.ui.bellButton.setCheckable(True)
            self.ui.timeEdit.setStyleSheet("""
                QTimeEdit {
                    background-color: #3c3f41;
                    border: none;
                    color: white;
                }

                QTimeEdit:hover {
                    background-color: #515151;
                    border: none;
                    color: white;
                }

                QTimeEdit::down-button {
                    border: none;
                    image: url(:/icons/icons/down.png);
                }

                QTimeEdit::up-button {
                    border: none;
                    image: url(:/icons/icons/up.png);
                }
                """)

    def updateTime(self):
        self.ui.timeLabel.setText(QtCore.QTime.currentTime().toString("hh:mm"))

    def bellActivate(self):
        for i in MainWindow.__init__.tasks:
            if i['time'] != 0:
                if i['date'] == datetime.date.today():
                    if i['time'].toString('hh:mm') == self.ui.timeLabel.text():
                        self.player.play()

    def refreshNavBar(self):
        self.ui.yearSelect.setValue(self.calendar.yearShown())
        self.ui.monthSelect.setCurrentIndex(self.calendar.monthShown() - 1)

    def refreshCalendar(self):
        # self.calendar.setCurrentPage(self.ui.yearSelect.value(), self.ui.monthSelect.currentIndex() + 1)
        pass

    def refreshMonth(self):
        self.calendar.setCurrentPage(self.calendar.yearShown(), self.ui.monthSelect.currentIndex() + 1)

    def refreshYear(self):
        self.calendar.setCurrentPage(self.ui.yearSelect.value(), self.calendar.monthShown())

    def tabChanged(self, index):
        sortedTasks = sorted(MainWindow.__init__.tasks, key=lambda x: int(x['date'].toString().split(' ')[3] + x['date'].toString().split(' ')[2]))
        print(sortedTasks)
        self.ui.allTaskList.clear()
        if index == 1:
            for task in sortedTasks:
                self.taskCard = QtWidgets.QFrame()
                self.taskCard.resize(400, 50)
                self.taskCard.setStyleSheet("""
                    QWidget:hover {
                        background-color: #515151;
                    }
                    """)
                self.taskCard.setAutoFillBackground(False)
                self.taskName = QtWidgets.QLabel()
                self.taskName.setText(task['text'])
                self.taskName.setStyleSheet("""
                    color: white;
                    background:transparent
                    """)
                
                self.colorIndicator = QtWidgets.QPushButton()
                self.colorIndicator.resize(30, 30)
                self.colorIndicator.setStyleSheet(f"""
                    background-color: {task['color']};
                    """)
                self.timeLabel = QtWidgets.QLabel()
                if task['time'] == 0:
                    self.timeLabel.setText('Весь день')
                else:
                    self.timeLabel.setText(task['time'].toString('hh:mm'))
                self.timeLabel.setStyleSheet("""
                    color: gray;
                    background:transparent;
                    """)
                self.timeLabel.setAutoFillBackground(False)
                if task['bell'] == 1:
                    self.bellIcon = QtWidgets.QPushButton()
                    self.bellIcon.resize(30, 30)
                    self.bellIcon.setIcon(self.ui.icon5)
                    self.bellIcon.setStyleSheet("""
                        background:transparent;
                        """)
                self.main_layout = QtWidgets.QHBoxLayout()
                self.main_layout.addWidget(self.colorIndicator)
                self.main_layout.addWidget(self.taskName)
                self.main_layout.addWidget(self.timeLabel)
                if task['bell'] == 1:  
                    self.main_layout.addWidget(self.bellIcon)
                self.main_layout.addStretch()
                self.taskCard.setLayout(self.main_layout)

                self.itemTask = QtWidgets.QListWidgetItem()
                self.ui.allTaskList.insertItem(self.ui.allTaskList.count(), self.itemTask)
                self.ui.allTaskList.setItemWidget(self.itemTask, self.taskCard)
                self.itemTask.setSizeHint(self.taskCard.sizeHint())
                # self.itemTask.setData(0, id)

    def saveFile(self):
        folder_path = f'{os.getenv("APPDATA")}/TaskPlanner'
        save_path = f'{os.getenv("APPDATA")}/TaskPlanner/tasks.txt'
        if os.path.exists(folder_path):
            with open(save_path, 'wb') as f:
                # f.write(str(self.tasks))
                pickle.dump(MainWindow.__init__.tasks, f)
                print(f'SAVE ---- {MainWindow.__init__.tasks}')
        else:
            os.mkdir(folder_path)
            with open(save_path, 'wb') as f:
                # f.write(str(self.tasks))
                pickle.dump(MainWindow.__init__.tasks, f)

    def deleteAll(self):
        MainWindow.__init__.tasks = []

    def undo(self):
        # if self.undoCount < len(self.actions):
        #     if self.actions[self.undoCount][0] == 'new':
        #         print(self.actions[self.undoCount][1])
        #         # MainWindow.__init__.tasks.remove(self.actions[-(self.undoCount + 1)][1])
        #         for i in MainWindow.__init__.tasks:
        #             if i['id'] == self.actions[-(self.undoCount + 1)][1]['id']:
        #                 MainWindow.__init__.tasks.remove(i)
        #         self.undoCount += 1
        #         self.refresh()
        #         self.calendar.updateCells()
        #     else:
        #         for task in MainWindow.__init__.tasks:
        #             if task['id'] == self.actions[self.undoCount][1]['id']:
        #                 # task = self.actions[-(self.undoCount + 1)][0]
        #                 task['text'] = self.actions[-(self.undoCount + 1)][0]['text']
        #                 task['date'] = self.actions[-(self.undoCount + 1)][0]['date']
        #                 task['color'] = self.actions[-(self.undoCount + 1)][0]['color']
        #                 task['time'] = self.actions[-(self.undoCount + 1)][0]['time']
        #                 task['bell'] = self.actions[-(self.undoCount + 1)][0]['bell']
        #                 self.undoCount += 1
        #                 self.refresh()
        #                 self.calendar.updateCells()

        # else:
        #     self.undoAct.setEnabled(False)


        if self.actions == []:
            pass
        elif self.actions[0] == 'new':
            self.cancels = ['del', self.actions[1]]
            MainWindow.__init__.tasks.remove(self.actions[1])
            self.actions = []
            self.refresh()
            self.calendar.updateCells()
        elif self.actions[0] == 'del':
            self.cancels = ['new', self.actions[1]]
            MainWindow.__init__.tasks.append(self.actions[1])
            self.actions = []
            self.refresh()
            self.calendar.updateCells()
        else:
            for task in MainWindow.__init__.tasks:
                if task == self.actions[1]:
                    self.cancels = [self.actions[1], self.actions[0]]
                    MainWindow.__init__.tasks[MainWindow.__init__.tasks.index(task)] = self.actions[0]
                    self.actions = []
                    self.refresh()
                    self.calendar.updateCells()



    def redo(self):
        if self.cancels == []:
            pass
        elif self.cancels[0] == 'del':
            MainWindow.__init__.tasks.append(self.cancels[1])
        elif self.cancels[0] == 'new':
            MainWindow.__init__.tasks.remove(self.cancels[1])
        else:
            for task in MainWindow.__init__.tasks:
                if task == self.cancels[1]:
                    MainWindow.__init__.tasks[MainWindow.__init__.tasks.index(task)] = self.cancels[0]
        self.cancels = []
        self.refresh()
        self.calendar.updateCells()

    def openSettings(self):
        self.settingsDialog = QtWidgets.QDialog(self)
        self.baseLayout = QtWidgets.QGridLayout(self.settingsDialog)
        self.baseFrame = QtWidgets.QFrame(self.settingsDialog)
        self.baseLayout.addWidget(self.baseFrame, 0, 0)
        self.baseLayout.setColumnStretch(0, 1)
        self.baseLayout.setRowStretch(0, 1)
        self.baseLayout.setContentsMargins(0, 0, 0, 0)
        self.settingsList = QtWidgets.QListWidget()
        self.settingsList.setStyleSheet("""
            background-color: #3c3f41;
            """)
        self.bottomBar = QtWidgets.QFrame()
        self.bottomBar.setStyleSheet("""
            background-color: #3c3f41;
            """)
        self.bottomBar.setMinimumHeight(40)
        self.bottomBar.setMaximumHeight(40)
        self.cancelButton = QtWidgets.QPushButton()
        self.cancelButton.setText('Отменить')
        self.cancelButton.setStyleSheet("""
            color: white;
            """)
        self.cancelButton.clicked.connect(self.settingsDialog.close)
        self.applyButton = QtWidgets.QPushButton()
        self.applyButton.setText('Применить')
        self.applyButton.setStyleSheet("""
            color: white;
            """)
        self.applyButton.clicked.connect(self.saveSettings)
        self.emptyPlace = QtWidgets.QFrame()
        self.emptyPlace.setMaximumWidth(100000)
        self.bottomLayout = QtWidgets.QHBoxLayout()
        self.bottomLayout.addWidget(self.cancelButton, 0)
        self.bottomLayout.addWidget(self.emptyPlace, 1)
        self.bottomLayout.addWidget(self.applyButton, 0)
        self.bottomLayout.addStretch()
        self.bottomBar.setLayout(self.bottomLayout)
        self.mainSettingsLayout = QtWidgets.QVBoxLayout(self.baseFrame)
        self.mainSettingsLayout.addWidget(self.settingsList, 0)
        self.mainSettingsLayout.addWidget(self.bottomBar, 1)
        self.mainSettingsLayout.setContentsMargins(0, 0, 0, 0)
        self.mainSettingsLayout.setSpacing(0)
        self.baseFrame.setLayout(self.mainSettingsLayout)

        # Настройки автосохранения
        self.frameAutoSave = QtWidgets.QFrame()
        self.frameAutoSave.setStyleSheet("""
            QFrame {
                background-color: #3c3f41;
                border-bottom: 1px solid #323232;
            }
            """)

        self.layoutAutoSave = QtWidgets.QVBoxLayout()
        self.checkAutoSave = QtWidgets.QCheckBox()
        self.checkAutoSave.setText('Включить автосохранение')
        if self.settings['enabledAS'] == 1:
            self.checkAutoSave.setChecked(True)
        else:
            self.checkAutoSave.setChecked(False)

        self.checkAutoSave.setStyleSheet("""
            QCheckBox {
                color: white;
            }
            """)
        self.checkAutoSave.stateChanged.connect(self.changedAS)
        self.editAutoSave = QtWidgets.QLineEdit()
        self.editAutoSave.setText('5')
        if self.checkAutoSave.isChecked():
            self.editAutoSave.setStyleSheet("""
                QLineEdit {
                    background-color: #323232;
                    color: white;
                }
                """)
            self.editAutoSave.setEnabled(True)
        else:
            self.editAutoSave.setStyleSheet("""
                QLineEdit {
                    background-color: #323232;
                    color: gray;
                    opacity: 0.5;
                }
                """)
            self.editAutoSave.setEnabled(False)
        self.layoutAutoSave.addWidget(self.checkAutoSave, 0)
        self.layoutAutoSave.addWidget(self.editAutoSave, 1)
        self.layoutAutoSave.addStretch()
        self.frameAutoSave.setLayout(self.layoutAutoSave)
        self.itemAutoSave = QtWidgets.QListWidgetItem()
        self.settingsList.insertItem(0, self.itemAutoSave)
        self.settingsList.setItemWidget(self.itemAutoSave, self.frameAutoSave)
        self.itemAutoSave.setSizeHint(self.frameAutoSave.sizeHint())



        self.settingsDialog.resize(500, 300)
        self.settingsDialog.show()

    def changedAS(self):
        if self.checkAutoSave.isChecked():
            self.editAutoSave.setEnabled(True)
            self.editAutoSave.setStyleSheet("""
                QLineEdit {
                    background-color: #323232;
                    color: white;
                }
                """)
        else:
            self.editAutoSave.setEnabled(False)
            self.editAutoSave.setStyleSheet("""
                QLineEdit {
                    background-color: #3c3f41;
                    color: gray;
                    opacity: 0.5;
                }
                """)

    def saveSettings(self):
        self.settings['enabledAS'] =  self.checkAutoSave.isChecked()
        self.settings['timeoutAS'] = self.editAutoSave.text()
        self.settingsDialog.close()
        folder_path = f'{os.getenv("APPDATA")}/TaskPlanner'
        save_path = f'{os.getenv("APPDATA")}/TaskPlanner/settings.txt'
        if os.path.exists(folder_path):
            with open(save_path, 'wb') as f:
                pickle.dump(self.settings, f)
        else:
            os.mkdir(folder_path)
            with open(save_path, 'wb') as f:
                pickle.dump(self.settings, f)




class MyCalendar(QtWidgets.QCalendarWidget):
    def __init__(self, parent=None):
        QtWidgets.QCalendarWidget.__init__(self, parent)



    def paintCell(self, painter, rect, date):
        QtWidgets.QCalendarWidget.paintCell(self, painter, rect, date)

        # painter.setBrush(QColor(58, 58, 58, 255))
        # painter.drawRect(rect)
        # painter.setPen(Qt.black)
        # painter.setFont(self.font())
        # text_rect = QRectF(rect.x(), rect.y(), rect.width(), rect.height() - 70)
        # painter.drawText(text_rect, Qt.AlignCenter, str(date.day()))
        # painter.restore()

        if date == date.currentDate():
            painter.setBrush(QtGui.QColor(68, 72, 74, 100))
            pen1 = QtGui.QPen()
            pen1.setBrush(QtGui.QColor(81, 81, 81, 255))
            pen1.setWidth(1)
            pen1.setStyle(QtCore.Qt.DashLine)

            # painter.setPen(QtGui.QColor(81, 81, 81, 255))
            painter.setPen(pen1)
            painter.drawRect(rect)
            painter.restore()

        # for i in MainWindow.__init__.tasks:
        #     if date == i['date']:
        #         rgb_color = i['color'].lstrip('#')
        #         rgb_color = tuple(int(rgb_color[i:i+2], 16) for i in (0, 2, 4))
        #         rgb_color.append(255)
        #         painter.setBrush(QtGui.QColor(rgb_color))


        # if MainWindow.__init__.isInit == True:
        #     tasks_sorted = sorted(MainWindow.__init__.tasks, key=lambda x: x['date'])
        #     tasks_grouped = [list(group) for key, group in groupby(tasks_sorted, lambda x: x['date'])]
        #     for i in tasks_grouped:
        #         if len(i) == 2:
        #             if date == i[0]['date']:
        #                 painter.save()
        #                 font = QtGui.QFont()
        #                 font.setPixelSize(10)
        #                 painter.setFont(font)
        #                 painter.drawText(rect.topLeft() + QtCore.QPoint(10, 10), i[0]['text'],)
        #                 painter.restore()


        c = self.frameGeometry().height() / 13

        # for task in MainWindow.__init__.tasks:
        #     if task['date'] == date:
        #         c += 20
        #         task_rect = QRectF(rect.x(), rect.y() + c, rect.width(), 15)
        #         painter.setPen(Qt.NoPen)
        #         painter.setBrush(QColor(task['color']))
        #         painter.setRenderHint(QPainter.Antialiasing)
        #         painter.drawRoundedRect(task_rect, 5, 5)

        #         r, g, b = tuple(int(task['color'][i:i+2], 16) for i in (1, 3, 5))
        #         r_lum = 0.2126 * r
        #         g_lum = 0.7152 * g
        #         b_lum = 0.0722 * b
        #         result = (r_lum + g_lum + b_lum) / 255
        #         text_color = 0
        #         if result < 0.5:
        #             text_color = '#ffffff'
        #         else:
        #             text_color = '#000000'

        #         painter.setPen(text_color)
        #         painter.drawText(task_rect, Qt.AlignCenter, task['text'])

        tasks_sorted = sorted(MainWindow.__init__.tasks, key=lambda x: x['date'])
        tasks_grouped = [list(group) for key, group in groupby(tasks_sorted, lambda x: x['date'])]
        limit = round((((self.frameGeometry().height() / 8) - 15) / 30))
        wordLimit = math.floor(self.frameGeometry().width() / 4.75 / 13)
        for i in tasks_grouped:
            if len(i) < limit:
                c = self.frameGeometry().height() / 13
                for task in i:
                    if task['date'] == date:
                        c += 20
                        task_rect = QRectF(rect.x(), rect.y() + c, rect.width(), 15)
                        painter.setPen(Qt.NoPen)
                        painter.setBrush(QColor(task['color']))
                        painter.setRenderHint(QPainter.Antialiasing)
                        painter.drawRoundedRect(task_rect, 5, 5)

                        r, g, b = tuple(int(task['color'][i:i+2], 16) for i in (1, 3, 5))
                        r_lum = 0.2126 * r
                        g_lum = 0.7152 * g
                        b_lum = 0.0722 * b
                        result = (r_lum + g_lum + b_lum) / 255
                        text_color = 0
                        if result < 0.5:
                            text_color = '#ffffff'
                        else:
                            text_color = '#000000'

                        painter.setPen(text_color)
                        if len(task['text']) > wordLimit:
                            painter.drawText(task_rect, Qt.AlignCenter, f'{task["text"][:wordLimit]}...')
                            print(task["text"][:wordLimit])
                        else:
                            painter.drawText(task_rect, Qt.AlignCenter, task['text'])
            else:
                c = self.frameGeometry().height() / 13
                c1 = 0
                for task in i[:limit]:
                    if task['date'] == date:
                        c1 += 1
                        c += 20
                        if c1 != limit:
                            task_rect = QRectF(rect.x(), rect.y() + c, rect.width(), 15)
                            painter.setPen(Qt.NoPen)
                            painter.setBrush(QColor(task['color']))
                            painter.setRenderHint(QPainter.Antialiasing)
                        
                            painter.drawRoundedRect(task_rect, 5, 5)

                            r, g, b = tuple(int(task['color'][i:i+2], 16) for i in (1, 3, 5))
                            r_lum = 0.2126 * r
                            g_lum = 0.7152 * g
                            b_lum = 0.0722 * b
                            result = (r_lum + g_lum + b_lum) / 255
                            text_color = 0
                            if result < 0.5:
                                text_color = '#ffffff'
                            else:
                                text_color = '#000000'

                            painter.setPen(text_color)
                            if len(task['text']) > wordLimit:
                                painter.drawText(task_rect, Qt.AlignCenter, f'{task["text"][:wordLimit]}...')
                                print(task["text"][:wordLimit])
                            else:
                                painter.drawText(task_rect, Qt.AlignCenter, task['text'])
                            painter.restore()
                        else:
                            task_rect = QRectF(rect.x(), rect.y() + c, rect.width(), 15)
                            painter.setPen(Qt.NoPen)
                            painter.setBrush(QColor(255, 255, 255, 0))
                            painter.setPen(QtGui.QColor(255, 255, 255))
                            painter.drawText(task_rect, Qt.AlignCenter, f'+ еще {len(i) - (limit-1)}')



    # def taskRect(self, task):
    #     date = task['date']
    #     rect = self.rectForDate(date)
    #     task_rect = QRectF(rect.x(), rect.y() + 5, rect.width(), 10)
    #     return task_rect








    # def addTask(self):

    #     self.id += 1

    #     self.color = 'red'

    #     self.taskCard = QtWidgets.QWidget()
    #     self.taskCard.resize(400, 50)
    #     self.taskCard.setStyleSheet("""
    #         QWidget:hover {
    #             background-color: #515151;
    #         }
    #         """)
    #     self.taskName = QtWidgets.QLineEdit()
    #     self.taskName.setText('Задача')
    #     self.taskName.setStyleSheet("""
    #         background-color: #3c3f41;
    #         color: white;
    #         border: none;
    #         """)
    #     self.taskName.setStyleSheet("""
    #         color: white;
    #         """)
    #     self.colorPickerButton = QtWidgets.QPushButton()
    #     self.colorPickerButton.resize(30, 30)
    #     self.colorPickerButton.setStyleSheet(f"""
    #         background-color: {self.color};
    #         """)

    #     self.colorPickerButton.clicked.connect(self.pickColor)

    #     self.main_layout = QtWidgets.QHBoxLayout()
    #     self.main_layout.addWidget(self.colorPickerButton)
    #     self.main_layout.addWidget(self.taskName)
    #     self.main_layout.addStretch()
    #     self.taskCard.setLayout(self.main_layout)

    #     self.itemTask = QtWidgets.QListWidgetItem()
    #     self.ui.taskList.insertItem(self.ui.taskList.count(), self.itemTask)
    #     self.ui.taskList.setItemWidget(self.itemTask, self.taskCard)
    #     self.itemTask.setSizeHint(self.taskCard.sizeHint())
    #     self.itemTask.setData(0, self.id)

    #     print(self.ui.calendarWidget.selectedDate())

    #     self.tasks.append({'id': self.itemTask.data(0), 'date': self.ui.calendarWidget.selectedDate(), 'color': self.color, 'text': self.taskName.text()})
    #     print(self.tasks)

    # def pickColor(self):
    #     self.colorPicker = QtWidgets.QColorDialog()
    #     self.color = self.colorPicker.getColor().name()
    #     self.colorPickerButton.setStyleSheet(f"""
    #         background-color: {self.color};
    #         """)

    # def changedItem(self, item):
    #     print(item.data(0))

        

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    app.setStyle(QtWidgets.QStyleFactory.create("fusion"))


    widget = MainWindow()
    widget.resize(1200, 1000)
    widget.show()

    sys.exit(app.exec())
