from PyQt5 import QtWidgets

from gui.extend import ExtendedMainWindow

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ExtendedMainWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())