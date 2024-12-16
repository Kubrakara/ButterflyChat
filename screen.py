from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(800, 600))
        self.centralwidget.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.stackedWidget.setMinimumSize(QtCore.QSize(800, 600))
        self.stackedWidget.setMaximumSize(QtCore.QSize(800, 600))
        self.stackedWidget.setStyleSheet("#page{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 160, 66, 255), stop:0.414773 rgba(235, 160, 84, 255), stop:0.98 rgba(243, 243, 243, 255), stop:1 rgba(0, 0, 0, 0));\n"
"}\n"
"")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setMaximumSize(QtCore.QSize(800, 600))
        self.page.setStyleSheet("")
        self.page.setObjectName("page")
        self.frame_3 = QtWidgets.QFrame(self.page)
        self.frame_3.setGeometry(QtCore.QRect(250, 170, 300, 311))
        self.frame_3.setStyleSheet("")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_2 = QtWidgets.QFrame(self.frame_3)
        self.frame_2.setGeometry(QtCore.QRect(25, 50, 250, 100))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(10, 10, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 10pt \"Sitka Small\";")
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 29, 221, 21))
        self.lineEdit_2.setStyleSheet("\n"
"    background-color: rgb(238, 238, 238);\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"\n"
"\n"
"")
        self.lineEdit_2.setPlaceholderText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(10, 53, 51, 16))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font: 10pt \"Sitka Small\";")
        self.label_2.setObjectName("label_2")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(10, 70, 221, 21))
        self.lineEdit_5.setStyleSheet("\n"
"    background-color: rgb(238, 238, 238);\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"\n"
"\n"
"")
        self.lineEdit_5.setPlaceholderText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.frame = QtWidgets.QFrame(self.frame_3)
        self.frame.setGeometry(QtCore.QRect(25, 180, 250, 43))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setStyleSheet("\n"
"#pushButton {\n"
"  padding: 5px;\n"
"  color: rgb(255, 255, 255);\n"
"  background: #111;\n"
"  border-radius: 10px;\n"
"}\n"
"\n"
"\n"
"#pushButton:focus {\n"
"background-color: rgb(255, 183, 0);\n"
"border: 1px solid orange;\n"
"color:black;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setStyleSheet("\n"
"#pushButton_2 {\n"
"  padding: 5px;\n"
"  color: rgb(255, 255, 255);\n"
"  background: #111;\n"
"  border-radius: 10px;\n"
"}\n"
"\n"
"\n"
"#pushButton_2:focus {\n"
"background-color: rgb(255, 183, 0);\n"
"border: 1px solid orange;\n"
"color:black;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.label_3 = QtWidgets.QLabel(self.page)
        self.label_3.setGeometry(QtCore.QRect(190, 70, 450, 41))
        self.label_3.setStyleSheet("font: 36pt \"Sitka Small\";")
        self.label_3.setObjectName("label_3")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setStyleSheet("#page_2{\n"
"        background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 160, 66, 255), stop:0.414773 rgba(235, 160, 84, 255), stop:0.98 rgba(243, 243, 243, 255), stop:1 rgba(0, 0, 0, 0));\n"
"\n"
"}\n"
"")
        self.page_2.setObjectName("page_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 10, 191, 21))
        self.lineEdit_3.setStyleSheet("\n"
"    \n"
"background-color: rgb(255, 255, 255);\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_3.setGeometry(QtCore.QRect(210, 10, 41, 23))
        self.pushButton_3.setStyleSheet("border:none;")
        self.pushButton_3.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/screen/search-interface-symbol.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_4.setGeometry(QtCore.QRect(714, 560, 71, 31))
        self.pushButton_4.setStyleSheet("\n"
"#pushButton_4 {\n"
"  padding: 5px;\n"
"  color: rgb(255, 255, 255);\n"
"  background: #ffa042;\n"
"  border-radius: 10px;\n"
"}\n"
"\n"
"\n"
"#pushButton_4:focus {\n"
"background-color: rgb(255, 183, 0);\n"
"border: 1px solid orange;\n"
"color:black;\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.listWidget = QtWidgets.QListWidget(self.page_2)
        self.listWidget.setGeometry(QtCore.QRect(20, 40, 761, 511))
        self.listWidget.setStyleSheet("background-color: rgb(252, 252, 252);\n"
"    border-radius:30px; \n"
"    border: 2px solid  grey;\n"
"")
        self.listWidget.setObjectName("listWidget")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(20, 560, 681, 31))
        self.lineEdit_4.setStyleSheet("\n"
"    \n"
"background-color: rgb(255, 255, 255);\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Kullanıcı Adı:"))
        self.label_2.setText(_translate("MainWindow", "Email:"))
        self.pushButton.setText(_translate("MainWindow", "Giriş Yap"))
        self.pushButton_2.setText(_translate("MainWindow", "Kaydol"))
        self.label_3.setText(_translate("MainWindow", "BUTTERFLY CHAT"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", " Kullanıcı adı ile arayın.."))
        self.pushButton_4.setText(_translate("MainWindow", "Gönder"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", " Mesajınızı buraya giriniz.."))

