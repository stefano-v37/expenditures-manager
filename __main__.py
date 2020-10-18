import os
from PyQt5 import QtWidgets

from ExpendituresManager import Instance
from gui.extend import ExtendedMainWindow

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    print(os.environ['expmanStefano'])
    instance = Instance(user='Stefano')
    ui = ExtendedMainWindow(MainWindow, instance)
    MainWindow.show()
    sys.exit(app.exec_())