# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'model.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(668, 641)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.labelPath = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelPath.sizePolicy().hasHeightForWidth())
        self.labelPath.setSizePolicy(sizePolicy)
        self.labelPath.setObjectName("labelPath")
        self.gridLayout_4.addWidget(self.labelPath, 1, 0, 1, 1)
        self.userList = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.userList.sizePolicy().hasHeightForWidth())
        self.userList.setSizePolicy(sizePolicy)
        self.userList.setObjectName("userList")
        self.gridLayout_4.addWidget(self.userList, 0, 1, 1, 1)
        self.path = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.path.sizePolicy().hasHeightForWidth())
        self.path.setSizePolicy(sizePolicy)
        self.path.setObjectName("path")
        self.gridLayout_4.addWidget(self.path, 1, 1, 1, 1)
        self.labelUserSelected = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelUserSelected.sizePolicy().hasHeightForWidth())
        self.labelUserSelected.setSizePolicy(sizePolicy)
        self.labelUserSelected.setObjectName("labelUserSelected")
        self.gridLayout_4.addWidget(self.labelUserSelected, 0, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.tab1)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.costView = QtWidgets.QTableView(self.tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.costView.sizePolicy().hasHeightForWidth())
        self.costView.setSizePolicy(sizePolicy)
        self.costView.setMinimumSize(QtCore.QSize(0, 300))
        self.costView.setObjectName("costView")
        self.gridLayout_7.addWidget(self.costView, 0, 0, 1, 2)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.labelRevenues = QtWidgets.QLabel(self.tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelRevenues.sizePolicy().hasHeightForWidth())
        self.labelRevenues.setSizePolicy(sizePolicy)
        self.labelRevenues.setMinimumSize(QtCore.QSize(50, 0))
        self.labelRevenues.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelRevenues.setAlignment(QtCore.Qt.AlignCenter)
        self.labelRevenues.setObjectName("labelRevenues")
        self.gridLayout_5.addWidget(self.labelRevenues, 2, 2, 1, 1)
        self.labelExpenses = QtWidgets.QLabel(self.tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelExpenses.sizePolicy().hasHeightForWidth())
        self.labelExpenses.setSizePolicy(sizePolicy)
        self.labelExpenses.setMinimumSize(QtCore.QSize(50, 0))
        self.labelExpenses.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelExpenses.setAlignment(QtCore.Qt.AlignCenter)
        self.labelExpenses.setObjectName("labelExpenses")
        self.gridLayout_5.addWidget(self.labelExpenses, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem, 3, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem1, 0, 2, 1, 1)
        self.typeSelectorData = QtWidgets.QSlider(self.tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.typeSelectorData.sizePolicy().hasHeightForWidth())
        self.typeSelectorData.setSizePolicy(sizePolicy)
        self.typeSelectorData.setMinimumSize(QtCore.QSize(150, 0))
        self.typeSelectorData.setMaximum(2)
        self.typeSelectorData.setPageStep(1)
        self.typeSelectorData.setOrientation(QtCore.Qt.Horizontal)
        self.typeSelectorData.setObjectName("typeSelectorData")
        self.gridLayout_5.addWidget(self.typeSelectorData, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem2, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(50, 0))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 2, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout_7.addLayout(self.gridLayout_5, 2, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_7.addItem(spacerItem3, 1, 0, 1, 2)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.deleteRowInput = QtWidgets.QLineEdit(self.tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deleteRowInput.sizePolicy().hasHeightForWidth())
        self.deleteRowInput.setSizePolicy(sizePolicy)
        self.deleteRowInput.setObjectName("deleteRowInput")
        self.gridLayout_6.addWidget(self.deleteRowInput, 0, 2, 1, 1)
        self.pushButtonDeleteRow = QtWidgets.QPushButton(self.tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonDeleteRow.sizePolicy().hasHeightForWidth())
        self.pushButtonDeleteRow.setSizePolicy(sizePolicy)
        self.pushButtonDeleteRow.setObjectName("pushButtonDeleteRow")
        self.gridLayout_6.addWidget(self.pushButtonDeleteRow, 0, 3, 1, 1)
        self.pushButtonSaveData = QtWidgets.QPushButton(self.tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonSaveData.sizePolicy().hasHeightForWidth())
        self.pushButtonSaveData.setSizePolicy(sizePolicy)
        self.pushButtonSaveData.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButtonSaveData.setObjectName("pushButtonSaveData")
        self.gridLayout_6.addWidget(self.pushButtonSaveData, 2, 2, 1, 2)
        self.labelDeleteRow = QtWidgets.QLabel(self.tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelDeleteRow.sizePolicy().hasHeightForWidth())
        self.labelDeleteRow.setSizePolicy(sizePolicy)
        self.labelDeleteRow.setObjectName("labelDeleteRow")
        self.gridLayout_6.addWidget(self.labelDeleteRow, 0, 0, 1, 2, QtCore.Qt.AlignRight)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem4, 1, 0, 2, 2)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout_6.addItem(spacerItem5, 1, 2, 1, 2)
        self.gridLayout_7.addLayout(self.gridLayout_6, 2, 1, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_7, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab1, "")
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.tab2)
        self.gridLayout_10.setObjectName("gridLayout_10")
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_10.addItem(spacerItem6, 3, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem7 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.typeInputSelector = QtWidgets.QSlider(self.tab2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.typeInputSelector.sizePolicy().hasHeightForWidth())
        self.typeInputSelector.setSizePolicy(sizePolicy)
        self.typeInputSelector.setMaximum(1)
        self.typeInputSelector.setPageStep(1)
        self.typeInputSelector.setOrientation(QtCore.Qt.Horizontal)
        self.typeInputSelector.setObjectName("typeInputSelector")
        self.horizontalLayout_5.addWidget(self.typeInputSelector)
        spacerItem8 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem8)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labelExpensesInput = QtWidgets.QLabel(self.tab2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelExpensesInput.sizePolicy().hasHeightForWidth())
        self.labelExpensesInput.setSizePolicy(sizePolicy)
        self.labelExpensesInput.setAlignment(QtCore.Qt.AlignCenter)
        self.labelExpensesInput.setObjectName("labelExpensesInput")
        self.horizontalLayout_3.addWidget(self.labelExpensesInput)
        self.labelRevenuesInput = QtWidgets.QLabel(self.tab2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelRevenuesInput.sizePolicy().hasHeightForWidth())
        self.labelRevenuesInput.setSizePolicy(sizePolicy)
        self.labelRevenuesInput.setAlignment(QtCore.Qt.AlignCenter)
        self.labelRevenuesInput.setObjectName("labelRevenuesInput")
        self.horizontalLayout_3.addWidget(self.labelRevenuesInput)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.gridLayout_8.addLayout(self.verticalLayout_3, 5, 1, 1, 1)
        self.inputDate = QtWidgets.QLineEdit(self.tab2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputDate.sizePolicy().hasHeightForWidth())
        self.inputDate.setSizePolicy(sizePolicy)
        self.inputDate.setMinimumSize(QtCore.QSize(300, 0))
        self.inputDate.setObjectName("inputDate")
        self.gridLayout_8.addWidget(self.inputDate, 1, 1, 1, 1)
        self.labelDate = QtWidgets.QLabel(self.tab2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelDate.sizePolicy().hasHeightForWidth())
        self.labelDate.setSizePolicy(sizePolicy)
        self.labelDate.setObjectName("labelDate")
        self.gridLayout_8.addWidget(self.labelDate, 1, 0, 1, 1)
        self.labelShop = QtWidgets.QLabel(self.tab2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelShop.sizePolicy().hasHeightForWidth())
        self.labelShop.setSizePolicy(sizePolicy)
        self.labelShop.setObjectName("labelShop")
        self.gridLayout_8.addWidget(self.labelShop, 2, 0, 1, 1)
        self.inputDescription = QtWidgets.QLineEdit(self.tab2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputDescription.sizePolicy().hasHeightForWidth())
        self.inputDescription.setSizePolicy(sizePolicy)
        self.inputDescription.setMinimumSize(QtCore.QSize(300, 0))
        self.inputDescription.setObjectName("inputDescription")
        self.gridLayout_8.addWidget(self.inputDescription, 3, 1, 1, 1)
        self.inputShop = QtWidgets.QLineEdit(self.tab2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputShop.sizePolicy().hasHeightForWidth())
        self.inputShop.setSizePolicy(sizePolicy)
        self.inputShop.setMinimumSize(QtCore.QSize(300, 0))
        self.inputShop.setObjectName("inputShop")
        self.gridLayout_8.addWidget(self.inputShop, 2, 1, 1, 1)
        self.labelCost = QtWidgets.QLabel(self.tab2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelCost.sizePolicy().hasHeightForWidth())
        self.labelCost.setSizePolicy(sizePolicy)
        self.labelCost.setObjectName("labelCost")
        self.gridLayout_8.addWidget(self.labelCost, 4, 0, 1, 1)
        self.inputCost = QtWidgets.QLineEdit(self.tab2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputCost.sizePolicy().hasHeightForWidth())
        self.inputCost.setSizePolicy(sizePolicy)
        self.inputCost.setMinimumSize(QtCore.QSize(300, 0))
        self.inputCost.setObjectName("inputCost")
        self.gridLayout_8.addWidget(self.inputCost, 4, 1, 1, 1)
        self.labelStar1 = QtWidgets.QLabel(self.tab2)
        self.labelStar1.setObjectName("labelStar1")
        self.gridLayout_8.addWidget(self.labelStar1, 2, 2, 1, 1)
        self.labelDescriptio = QtWidgets.QLabel(self.tab2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelDescriptio.sizePolicy().hasHeightForWidth())
        self.labelDescriptio.setSizePolicy(sizePolicy)
        self.labelDescriptio.setObjectName("labelDescriptio")
        self.gridLayout_8.addWidget(self.labelDescriptio, 3, 0, 1, 1)
        self.labelEvent = QtWidgets.QLabel(self.tab2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelEvent.sizePolicy().hasHeightForWidth())
        self.labelEvent.setSizePolicy(sizePolicy)
        self.labelEvent.setObjectName("labelEvent")
        self.gridLayout_8.addWidget(self.labelEvent, 6, 0, 1, 1)
        self.inputEvent = QtWidgets.QLineEdit(self.tab2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputEvent.sizePolicy().hasHeightForWidth())
        self.inputEvent.setSizePolicy(sizePolicy)
        self.inputEvent.setMinimumSize(QtCore.QSize(300, 0))
        self.inputEvent.setObjectName("inputEvent")
        self.gridLayout_8.addWidget(self.inputEvent, 6, 1, 1, 1)
        self.labelStar2 = QtWidgets.QLabel(self.tab2)
        self.labelStar2.setObjectName("labelStar2")
        self.gridLayout_8.addWidget(self.labelStar2, 4, 2, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(10, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_8.addItem(spacerItem9, 0, 1, 1, 1)
        self.horizontalLayout_4.addLayout(self.gridLayout_8)
        self.gridLayout_10.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem10 = QtWidgets.QSpacerItem(0, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_2.addItem(spacerItem10)
        self.insertDataButton = QtWidgets.QPushButton(self.tab2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.insertDataButton.sizePolicy().hasHeightForWidth())
        self.insertDataButton.setSizePolicy(sizePolicy)
        self.insertDataButton.setObjectName("insertDataButton")
        self.verticalLayout_2.addWidget(self.insertDataButton)
        self.labelStar = QtWidgets.QLabel(self.tab2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelStar.sizePolicy().hasHeightForWidth())
        self.labelStar.setSizePolicy(sizePolicy)
        self.labelStar.setObjectName("labelStar")
        self.verticalLayout_2.addWidget(self.labelStar)
        self.gridLayout_11.addLayout(self.verticalLayout_2, 1, 2, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem11, 0, 0, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem12, 0, 2, 1, 1)
        self.gridLayout_10.addLayout(self.gridLayout_11, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab2, "")
        self.tab3 = QtWidgets.QWidget()
        self.tab3.setObjectName("tab3")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab3)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 70, 601, 311))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.dynamicPlot = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.dynamicPlot.setContentsMargins(0, 0, 0, 0)
        self.dynamicPlot.setObjectName("dynamicPlot")
        self.plotSelector = QtWidgets.QComboBox(self.tab3)
        self.plotSelector.setGeometry(QtCore.QRect(10, 20, 191, 22))
        self.plotSelector.setObjectName("plotSelector")
        self.tabWidget.addTab(self.tab3, "")
        self.gridLayout_4.addWidget(self.tabWidget, 2, 0, 1, 3)
        spacerItem13 = QtWidgets.QSpacerItem(497, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem13, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 668, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.userList, self.tabWidget)
        MainWindow.setTabOrder(self.tabWidget, self.costView)
        MainWindow.setTabOrder(self.costView, self.typeSelectorData)
        MainWindow.setTabOrder(self.typeSelectorData, self.deleteRowInput)
        MainWindow.setTabOrder(self.deleteRowInput, self.pushButtonDeleteRow)
        MainWindow.setTabOrder(self.pushButtonDeleteRow, self.pushButtonSaveData)
        MainWindow.setTabOrder(self.pushButtonSaveData, self.inputDate)
        MainWindow.setTabOrder(self.inputDate, self.inputShop)
        MainWindow.setTabOrder(self.inputShop, self.inputDescription)
        MainWindow.setTabOrder(self.inputDescription, self.inputCost)
        MainWindow.setTabOrder(self.inputCost, self.typeInputSelector)
        MainWindow.setTabOrder(self.typeInputSelector, self.inputEvent)
        MainWindow.setTabOrder(self.inputEvent, self.insertDataButton)
        MainWindow.setTabOrder(self.insertDataButton, self.plotSelector)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelPath.setText(_translate("MainWindow", "Path:"))
        self.path.setText(_translate("MainWindow", "path"))
        self.labelUserSelected.setText(_translate("MainWindow", "User selected:"))
        self.labelRevenues.setText(_translate("MainWindow", "revenues"))
        self.labelExpenses.setText(_translate("MainWindow", "expenses"))
        self.label.setText(_translate("MainWindow", "both"))
        self.pushButtonDeleteRow.setText(_translate("MainWindow", "Ok"))
        self.pushButtonSaveData.setText(_translate("MainWindow", "Save changes"))
        self.labelDeleteRow.setText(_translate("MainWindow", "Delete row number:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("MainWindow", "Tab 1"))
        self.labelExpensesInput.setText(_translate("MainWindow", "expense"))
        self.labelRevenuesInput.setText(_translate("MainWindow", "revenue"))
        self.inputDate.setText(_translate("MainWindow", "Today"))
        self.labelDate.setText(_translate("MainWindow", "Date:"))
        self.labelShop.setText(_translate("MainWindow", "Shop:"))
        self.labelCost.setText(_translate("MainWindow", "Value:"))
        self.labelStar1.setText(_translate("MainWindow", "*"))
        self.labelDescriptio.setText(_translate("MainWindow", "Description:"))
        self.labelEvent.setText(_translate("MainWindow", "Event:"))
        self.labelStar2.setText(_translate("MainWindow", "*"))
        self.insertDataButton.setText(_translate("MainWindow", "PushButton"))
        self.labelStar.setText(_translate("MainWindow", "* Mandatory field"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("MainWindow", "Tab 2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), _translate("MainWindow", "Page"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

