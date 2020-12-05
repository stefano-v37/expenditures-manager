from PyQt5.uic.properties import QtGui
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from pandas import DataFrame

from ExpendituresManager import Instance
from ExpendituresManager.utilities import get_configuration
from gui.matplotlibCanvas import MatplotlibCanvas
from gui.model import Ui_MainWindow
from PyQt5 import QtCore, QtWidgets

from datetime import datetime as dt

from gui.pandasModel import PandasModel


class ExtendedMainWindow(Ui_MainWindow):
    def __init__(self, MainWindow, instance):
        self.window = MainWindow
        self.setupUi(MainWindow)
        self.configuration = get_configuration()
        self.users = self.configuration['output_path']
        self.plots = self.configuration['plots']
        self.__extend__()
        self.setUser(instance)

    def setUser(self, init):
        if isinstance(init, Instance):
            self.instance = init
        elif isinstance(init, str):
            self.instance = Instance(user=init)
        else:
            print("provide a proper initialization")
        self.refresh()

    def insertdataclick(self):
        self.instance.add_data(date=self.inputDate.text(),
                               shop=self.inputShop.text(),
                               description=self.inputDescription.text(),
                               cost=self.inputCost.text(),
                               event=self.inputEvent.text(),
                               type="Expense")
        self.refresh()

    def deletedataclick(self):
        separationChar = [',', ', ', '↔ ']
        input = self.deleteRowInput.text()
        for sep in separationChar:
            input = input.replace(sep, '↔')
        if '↔' in input:
            rows = [int(x) for x in input.split('↔')]
        else:
            rows = int(input)
        self.instance.delete_row(rows)
        self.refresh()

    def changeUser(self):
        print("current user is: " + self.userList.currentText())
        self.setUser(self.userList.currentText())

    def refresh(self, data=None):
        self.setData(data)
        self.refreshUser()
        # self.refreshPlot()

    def refreshUser(self):
        _translate = QtCore.QCoreApplication.translate
        self.path.setText(_translate("MainWindow", self.instance.link))
        self.userList.setCurrentIndex(list(self.users).index(self.instance.user))

        try:
            self.disconnectActions()
            self.connectActions()

        except TypeError as te:
            print(te)
            self.connectActions()

    def setData(self, data=None):
        if type(data) == DataFrame:
            model = PandasModel(data)
        else:
            model = PandasModel(self.instance.data)
        self.tabWidget.setCurrentIndex(0)
        self.costView.setModel(model)
        self.costView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

    def disconnectActions(self):
        self.userList.disconnect()
        self.pushButtonDeleteRow.disconnect()
        self.pushButtonSaveData.disconnect()
        self.insertDataButton.disconnect()
        self.plotSelector.disconnect()

    def connectActions(self):
        self.userList.activated.connect(self.changeUser)
        self.pushButtonDeleteRow.clicked.connect(self.deletedataclick)
        self.pushButtonSaveData.clicked.connect(self.instance.save_df)
        self.insertDataButton.clicked.connect(self.insertdataclick)
        self.plotSelector.activated.connect(self.refreshPlot)

    def refreshPlot(self):
        plotType = self.plotSelector.currentText()
        self.plot(plotType)

    def plot(self, plotType):
        for i in reversed(range(self.dynamicPlot.layout().count())):
            self.dynamicPlot.layout().itemAt(i).widget().setParent(None)
        self.dynamicPlot.addWidget(MatplotlibCanvas(self.instance.data, plotType))

    def __extend__(self):
        _translate = QtCore.QCoreApplication.translate
        self.window.setWindowTitle(_translate("MainWindow", "Expenditures Manager"))

        # tab 0
        self.userList.addItems(self.users.keys())
        self.labelUserSelected.setText(_translate("MainWindow", "User selected:"))
        self.labelPath.setText(_translate("MainWindow", "Path:"))
        self.path.setText(_translate("MainWindow", "path"))

        # ! tab 1
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("MainWindow", "Data"))
        self.insertDataButton.setText(_translate("MainWindow", "Send"))
        self.inputDate.setText(_translate("MainWindow", dt.today().date().__str__()))

        # !! tab 2
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("MainWindow", "Insert data"))

        # !!! tab 3
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), _translate("MainWindow", "Visualize"))
        self.plotSelector.addItems(self.plots)
