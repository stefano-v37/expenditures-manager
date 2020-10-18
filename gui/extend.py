from ExpendituresManager.utilities import get_configuration
from gui.model import Ui_MainWindow
from PyQt5 import QtCore


class ExtendedMainWindow(Ui_MainWindow):
    def __init__(self, MainWindow, instance):
        self.setupUi(MainWindow)
        self.__extend__(MainWindow)

        self.instance = instance
        self.users = get_configuration()['output_path']

        self.refreshUser()

    def refreshUser(self):
        _translate = QtCore.QCoreApplication.translate
        self.path.setText(_translate("MainWindow", self.instance.path))
        self.userList.setCurrentIndex(list(self.users).index(self.instance.user))

    def __extend__(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Expenditures Manager"))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("MainWindow", "Resoconto"))
        self.insertDataButton.setText(_translate("MainWindow", "Send"))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("MainWindow", "Insert data"))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), _translate("MainWindow", "Page"))
        self.labelUserSelected.setText(_translate("MainWindow", "User selected:"))
        self.labelPath.setText(_translate("MainWindow", "Path:"))
        self.path.setText(_translate("MainWindow", "path"))