from pandas import DataFrame

from ExpendituresManager import Instance
from ExpendituresManager.utilities import get_configuration
from gui.model import Ui_MainWindow
from PyQt5 import QtCore

from datetime import datetime as dt

from gui.pandasModel import PandasModel


class ExtendedMainWindow(Ui_MainWindow):
    def __init__(self, MainWindow, instance):
        self.window = MainWindow;
        self.setupUi(MainWindow)
        self.users = get_configuration()['output_path']
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
                               event=self.inputEvent.text())
        self.refresh()

    def deletedataclick(self):
        input = self.deleteRowInput.text()
        if ", " in input:
            rows = input.split(", ")
            rows = [int(x) for x in rows]
        if "," in input:
            rows = input.split(",")
            rows = [int(x) for x in rows]
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

    def disconnectActions(self):
        self.userList.disconnect()
        self.pushButtonDeleteRow.disconnect()
        self.pushButtonSaveData.disconnect()
        self.insertDataButton.disconnect()

    def connectActions(self):
        self.userList.activated.connect(self.changeUser)
        self.pushButtonDeleteRow.clicked.connect(self.deletedataclick)
        self.pushButtonSaveData.clicked.connect(self.instance.save_df)
        self.insertDataButton.clicked.connect(self.insertdataclick)

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

        # !! tab 2
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("MainWindow", "Insert data"))

        # !!! tab 3
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), _translate("MainWindow", "Visualize"))