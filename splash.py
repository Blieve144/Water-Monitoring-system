from PyQt6 import QtCore, QtGui, QtWidgets
class Ui_self(object):
    def setupUi_(self,SplashScreen):

        SplashScreen.setObjectName("self")
        SplashScreen.resize(640, 480)
        self.wid = QtWidgets.QFrame(SplashScreen)
        self.wid.setGeometry(QtCore.QRect(0, 0, 640, 480))
        self.wid.setStyleSheet("border-image:url('./src/images/19604.jpg')")
        id = QtGui.QFontDatabase.addApplicationFont("./src/fonts/Anurati-Regular.otf")
        fontstr = QtGui.QFontDatabase.applicationFontFamilies(id)[0]
        font1 = QtGui.QFont(fontstr)
        font = QtGui.QFont(fontstr)
        font1.setPointSize(20)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(5)
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label = QtWidgets.QLabel(self.wid)
        self.label.setGeometry(QtCore.QRect(250, 150, 901, 101))
        self.label.setObjectName("label")
        self.label.setStyleSheet("#label{border-image:none;color:white}")
        self.label.setText("B.Lieve")
        self.label.setFont(font1)
        self.shadow_label = QtWidgets.QGraphicsDropShadowEffect(self.label,blurRadius=20,xOffset=1,yOffset=1,color=QtGui.QColor(0, 0, 0))
        self.label.setGraphicsEffect(self.shadow_label)
        


        self.label_2 = QtWidgets.QLabel(self.wid)
        self.label_2.setGeometry(QtCore.QRect(230, 350, 921, 100))
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("#label_2{border-image:none;color:white}")
        self.label_2.setText("I  A M  T H E  F U T U R E")
        self.label_2.setFont(font)
        self.shadow_label_ = QtWidgets.QGraphicsDropShadowEffect(self.label_2,blurRadius=20,xOffset=1,yOffset=1,color=QtGui.QColor(0, 0, 0))
        self.label.setGraphicsEffect(self.shadow_label_)
        self.label_ = QtWidgets.QLabel(self.wid)
        self.label_.setGeometry(QtCore.QRect(205, 405, 200, 50))
        self.label_.setObjectName("lb1")
        self.label_.setStyleSheet("#lb1{border-image:none}")

        self.movie = QtGui.QMovie("./src/images/infinity.gif")
        self.label_.setMovie(self.movie)
        self.movie.start()
        SplashScreen.setCentralWidget(self.wid)