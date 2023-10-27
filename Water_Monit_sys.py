import sys
from PyQt6 import QtWidgets, uic
from splash import *
from PyQt6.QtWidgets import QMainWindow, QApplication

from PyQt6.QtCore import Qt
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6 import QtCore, QtGui


class Ui(QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('watersystem.ui', self)
        self.show()
        
        self.label.setText('test')




counter=0

class SplashScreen(QtWidgets.QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui_ = Ui_self()
        self.ui_.setupUi_(self)
        #self.setWindowFlag(Qt.FramelessWindowHint)
        #self.setAttribute(Qt.WA_TranslucentBackground)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(35)
        self.show()
        self.center()
    def center(self):
        geo_frame = self.frameGeometry()
        #cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        #geo_frame.moveCenter(cp)
        self.move(geo_frame.topLeft())
    def progress(self):

        global counter
        if counter > 50:

            self.timer.stop()
            print('here1')
            self.main = Ui()
            print('here2')
            self.main.show()
            self.close()
        counter += 1


if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(True)
    window = SplashScreen()
    window.show()
    sys.exit(app.exec())