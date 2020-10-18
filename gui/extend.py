from gui.model import Ui_MainWindow
from PyQt5 import QtCore


class ExtendedMainWindow(Ui_MainWindow):
    def __init__(self, MainWindow):
        self.setupUi(MainWindow)
        self.__extend__(MainWindow)

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