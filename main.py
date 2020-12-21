from windows.window import BaseWindow
from PyQt5 import QtWidgets
import sys


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = BaseWindow()

    sys.exit(app.exec_())


