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
        self.show_state = "Both"
        self.show_plot = "month plot"
        self.__extend__()
        self.setUser(instance)
        self.typeSelectorData.valueChanged.connect(self.refresh)


    def setUser(self, init):
        if isinstance(init, Instance):
            self.instance = init
        elif isinstance(init, str):
            self.instance = Instance(user=init)
        else:
            print("provide a proper initialization")
        self.refresh()

    def get_type(self):
        temp = self.typeInputSelector.value()
        if temp == 0:
            return "Expense"
        elif temp == 1:
            return "Revenue"

    def insertdataclick(self):
        self.instance.add_data(date=self.inputDate.text(),
                               shop=self.inputShop.text(),
                               description=self.inputDescription.text(),
                               cost=self.inputCost.text(),
                               event=self.inputEvent.text(),
                               type=self.get_type())
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
        self.set_state()
        self.setData(data)
        self.refreshUser()
        self.refreshPlot()

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

    def set_state(self):
        temp = self.typeSelectorData.value()
        if temp == 0:
            self.show_state = "Expense"
        elif temp == 1:
            self.show_state = "Both"
        elif temp == 2:
            self.show_state = "Revenue"


    def data_to_show(self):
        if self.show_state == "Expense":
            return self.instance.data.loc[self.instance.data.Type == "Expense"]
        elif self.show_state == "Revenue":
            return self.instance.data.loc[self.instance.data.Type == "Revenue"]
        else:
            return self.instance.data

    def setData(self, data=None):
        if type(data) == DataFrame:
            model = PandasModel(data)
        else:
            model = PandasModel(self.data_to_show())
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
        self.show_plot = self.plotSelector.currentText()
        self.drawPlot()

    def drawPlot(self):
        self.plot(self.show_plot)

    def plot(self, plotType):
        for i in reversed(range(self.dynamicPlot.layout().count())):
            self.dynamicPlot.layout().itemAt(i).widget().setParent(None)
        self.instance.plot(plotType=plotType)
        self.instance._plot.generate(self.instance.data.copy())
        tempfig = self.instance._plot.fig
        tempax = self.instance._plot.ax
        temp = MatplotlibCanvas(fig=tempfig, ax=tempax)
        self.dynamicPlot.addWidget(temp)

    def __extend__(self):
        _translate = QtCore.QCoreApplication.translate
        self.window.setWindowTitle(_translate("MainWindow", "Expenditures Manager"))

        # tab 0
        self.userList.addItems(self.users.keys())
        self.labelUserSelected.setText(_translate("MainWindow", "User selected:"))
        self.labelPath.setText(_translate("MainWindow", "Path:"))
        self.path.setText(_translate("MainWindow", "path"))
        self.typeSelectorData.setValue(1)

        # ! tab 1
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("MainWindow", "Data"))
        self.insertDataButton.setText(_translate("MainWindow", "Send"))
        self.inputDate.setText(_translate("MainWindow", dt.today().date().__str__()))

        # !! tab 2
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("MainWindow", "Insert data"))

        # !!! tab 3
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), _translate("MainWindow", "Visualize"))
        self.plotSelector.addItems(self.plots)
