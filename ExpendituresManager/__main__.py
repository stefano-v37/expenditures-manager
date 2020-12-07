from PyQt5 import QtWidgets

from ExpendituresManager import Instance
from gui.extend import ExtendedMainWindow
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    instance = Instance()

    ui = ExtendedMainWindow(MainWindow, instance)

    MainWindow.show()
    sys.exit(app.exec_())