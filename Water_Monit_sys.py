import sys
from PyQt6 import QtWidgets, uic
from splash import *
from PyQt6.QtWidgets import QMainWindow, QApplication
from dbconnection import adaptor
from PyQt6.QtCore import Qt
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtWidgets import QLineEdit, QSizeGrip,QFrame
from PyQt6 import QtCore, QtGui
from PyQt6.QtCore import QPropertyAnimation, QEasingCurve


class Ui(QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi("watersystem.ui", self)
        self.show()

        ####shadow effect
        # self.shadow=QGraphicsDropShadowEffect(self)
        # self.shadow.setBlurRadius(50)
        # self.shadow.setXOffset(0)
        # self.shadow.setYOffset(0)
        # self.shadow.setColor(QColor(0,92,157,550))
        # self.centralWidget.setGrapicsEffect(self.shadow)
        
        
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

        self.setWindowTitle("Water Monitoring System")
        self.setWindowIcon(QtGui.QIcon("icons/activity.svg"))

        QSizeGrip(self.size_grip)

        self.minimize_button.clicked.connect(lambda: self.showMinimized())
        self.close.clicked.connect(lambda: self.close())
        self.max.clicked.connect(lambda: self.Rest_or_max())
        self.open_close.clicked.connect(lambda: self.SideMenu())
        self.pushButton_6.clicked.connect(lambda: self.close())

        self.pushButton_10.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.page_1)
        )
        self.pushButton_11.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.page_4)
        )
        self.pushButton_7.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.page_6)
        )
        self.pushButton_8.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.page_3)
        )
        self.pushButton_9.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.page_5)
        )
        self.pushButton.clicked.connect(lambda: self.submit_complaint())
        self.pushButton_12.clicked.connect(lambda: self.login())
        self.pushButton_3.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_5))
        self.pushButton_5.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_5))

        # Image relaod
        self.open_close.setIcon(QtGui.QIcon("icons/align-left.svg"))
        self.pushButton_7.setIcon(QtGui.QIcon("icons/anchor.svg"))
        self.pushButton_8.setIcon(QtGui.QIcon("icons/user.svg"))
        self.pushButton_9.setIcon(QtGui.QIcon("icons/settings.svg"))
        self.pushButton_6.setIcon(QtGui.QIcon("icons/external-link.svg"))
        self.pushButton_4.setIcon(QtGui.QIcon("icons/box.svg"))
        self.pushButton_10.setIcon(QtGui.QIcon("icons/home.svg"))
        self.pushButton_11.setIcon(QtGui.QIcon("icons/alert-triangle.svg"))
        
        self.close.setIcon(QtGui.QIcon("icons/x.svg"))
        self.max.setIcon(QtGui.QIcon("icons/maximize-2.svg"))
        self.minimize_button.setIcon(QtGui.QIcon("icons/arrow-down.svg"))

        self.label_3.setPixmap(QPixmap("icons/droplet.svg"))

        # set start page******************************************************
        self.stackedWidget.setCurrentWidget(self.page_1)

        # get water source info
        information = []
        information = adaptor.retrive_all()
        userinfo=[]
        #hide a button
        if not userinfo:  
            pass
            self.pushButton_11.hide()
            self.pushButton_7.hide()
            self.pushButton_2.hide()
        else:
            pass

        # load Mainpage frame###############################################################################################################################33
        for i in range((len(information)-1)):
            main_comp = QFrame(self.frame_12)
            main_comp.setObjectName(u"main_comp")
            main_comp.setStyleSheet(u"background-color: rgb(0, 255, 255);")
            main_comp.setFrameShape(QFrame.Shape.StyledPanel)
            main_comp.setFrameShadow(QFrame.Shadow.Raised)
            horizontalLayout_21 = QHBoxLayout(main_comp)
            horizontalLayout_21.setObjectName(u"horizontalLayout_21")
            
            sub_comp = QFrame(main_comp)
            sub_comp.setObjectName(u"sub_comp")
            sub_comp.setFrameShape(QFrame.Shape.StyledPanel)
            sub_comp.setFrameShadow(QFrame.Shadow.Raised)
            verticalLayout_10 = QVBoxLayout(sub_comp)
            verticalLayout_10.setObjectName(u"verticalLayout_10")
        
            label_17 = QLabel(sub_comp)
            label_17.setObjectName(u"label_17")
            label_17.setText(str(information[i][3]))

            verticalLayout_10.addWidget(label_17)

            label_18 = QLabel(sub_comp)
            label_18.setObjectName(u"label_18")
            label_18.setText(str(information[i][1]))

            verticalLayout_10.addWidget(label_18)

            label_19 = QLabel(sub_comp)
            label_19.setObjectName(u"label_19")
            label_19.setText(str(information[i][2]))

            verticalLayout_10.addWidget(label_19)

            label_20 = QLabel(sub_comp)
            label_20.setObjectName(u"label_20")
            label_20.setText(str(information[i][4]))

            verticalLayout_10.addWidget(label_20)


            horizontalLayout_21.addWidget(sub_comp, 0, Qt.AlignmentFlag.AlignTop)

            side_comp = QFrame(main_comp)
            side_comp.setObjectName(u"side_comp")
            side_comp.setFrameShape(QFrame.Shape.StyledPanel)
            side_comp.setFrameShadow(QFrame.Shadow.Raised)
            horizontalLayout_22 = QHBoxLayout(side_comp)
            horizontalLayout_22.setObjectName(u"horizontalLayout_22")
            label_21 = QLabel(side_comp)
            label_21.setObjectName(u"label_21")
            label_21.setText(str(information[i][5]))
            label_21.setFont(QFont('Arial', 20))
            if(int(information[i][5])>5):
                label_21.setStyleSheet("color: green")
            else:
                label_21.setStyleSheet("color: red")
            

            horizontalLayout_22.addWidget(label_21)


            horizontalLayout_21.addWidget(side_comp, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


            self.verticalLayout_11.addWidget(main_comp, 0, Qt.AlignmentFlag.AlignTop)

        # load QcomboBox
        for i in range((len(information)-1)):
            self.comboBox.addItem(str(information[i][0]))
            self.comboBox_2.addItem(information[i][1])
        for i in range(11):
            self.comboBox_3.addItem(str(i))

    # Slots
    def SideMenu(self):
        width = self.side_menu_container.width()
        if width == 0:
            newwidth = 250
            self.open_close.setIcon(QtGui.QIcon("icons/chevron-left.svg"))
        else:
            newwidth = 0
            self.open_close.setIcon(QtGui.QIcon("icons/align-left.svg"))

        self.animation = QPropertyAnimation(self.side_menu_container, b"maximumwidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newwidth)
        self.animation.setEasingCurve(QEasingCurve.InOutQuad)
        self.animation.start()
        
        
    def login(self):
        print("test")
        name=self.lineEdit_2.text()
        password=self.lineEdit_3.text()
        userinfo=adaptor.search(name,password)
        if not userinfo:  
               
            # Stores the return value for the button pressed
            self.pushButton_11.hide()
            self.pushButton_7.hide()
            self.pushButton_2.hide()
        else:
            self.pushButton_11.show()
            self.pushButton_7.show()
            self.pushButton_2.show()
            self.label_10.setText(userinfo[0][1])
            self.label_12.setText(userinfo[0][4])
            self.label_14.setText(userinfo[0][3])
            self.label_16.setText(userinfo[0][2])
            

    def submit_complaint(self):
        userid = 252
        wID = self.comboBox.currentText()
        wName = self.comboBox_2.currentText()
        DComp = self.textEdit.toPlainText()
        approx = self.comboBox_3.currentText()
        adaptor.storecomplaint(userid, wID, wName, DComp, approx)

    def Rest_or_max(self):
        if self.isMaximized():
            self.showNormal()
            self.max.setIcon(QtGui.QIcon("icons/maximize-2.svg"))

        else:
            self.showMaximized()
            self.max.setIcon(QtGui.QIcon("icons/minimize-2.svg"))
            self.max


counter = 0


class SplashScreen(QtWidgets.QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui_ = Ui_self()
        self.ui_.setupUi_(self)
        # self.setWindowFlag(Qt.FramelessWindowHint)
        # self.setAttribute(Qt.WA_TranslucentBackground)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(35)
        self.show()
        self.center()

    def center(self):
        geo_frame = self.frameGeometry()
        # cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        # geo_frame.moveCenter(cp)
        self.move(geo_frame.topLeft())

    def progress(self):
        global counter
        if counter > 20:
            self.timer.stop()
            self.main = Ui()
            self.main.show()
            self.close()
        counter += 1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(True)
    window = SplashScreen()
    window.show()
    sys.exit(app.exec())
