# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_screen.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from Login_Db import validate_user , create_user
from Dashboard import Ui_MainWindow
from PyQt5.QtWidgets import QMessageBox


class Ui_mainWindow(object):
  
    def login_screen(self):
      if self.stackedWidget.setCurrentIndex(0):
        pass
      else:
        pass
        email_text = self.email.toPlainText()
        password_text = self.password.toPlainText()
        # print(email_text+" "+password_text)
        if email_text == "" or password_text == "":
          msg = QMessageBox()
          msg.setIcon(QMessageBox.Warning)
          msg.setWindowTitle("ALERT")
          msg.setText('FILL ALL FIELDS FIRST !')
          msg.exec_()
        else:
          res = validate_user(email_text)
          print(res)
          if password_text == str(res):
            try:
              self.window = QtWidgets.QMainWindow()
              self.ui = Ui_MainWindow()
              self.ui.setupUi(self.window)
              self.ui.table_data()
              self.ui.dash_data()
              self.window.show()
              mainWindow.hide()
              print("Password Matched")
            except e:
               print("error")
          else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("ALERT")
            msg.setText('Password or Email may be Wrong !')
            msg.exec_()
  
    def signup_screen(self):
      if self.stackedWidget.setCurrentIndex(1):
        pass
      else:
        name = self.name.toPlainText()
        email = self.sig_email.toPlainText()
        password_text = self.sig_password.toPlainText()
        if name == "" or email == "" or password_text == "":
          msg = QMessageBox()
          msg.setIcon(QMessageBox.Warning)
          msg.setWindowTitle("ALERT")
          msg.setText('FILL ALL FIELDS FIRST !')
          msg.exec_()
        else:
          list = []
          list.append(name)
          list.append(email)
          list.append(password_text)
          res = create_user(list)
          try:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self.window)
            self.ui.table_data()
            self.ui.dash_data()
            self.window.show()
            mainWindow.hide()
          except e:
            print("error")

  
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(761, 481)
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(16)
        mainWindow.setFont(font)
        mainWindow.setAcceptDrops(False)
        mainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 120, 2, 2))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.functional_overview_heading_2 = QtWidgets.QLabel(self.centralwidget)
        self.functional_overview_heading_2.setGeometry(QtCore.QRect(10, 50, 751, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.functional_overview_heading_2.setFont(font)
        self.functional_overview_heading_2.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(0, 255, 0);")
        self.functional_overview_heading_2.setAlignment(QtCore.Qt.AlignCenter)
        self.functional_overview_heading_2.setWordWrap(True)
        self.functional_overview_heading_2.setObjectName("functional_overview_heading_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(80, 140, 351, 201))
        self.stackedWidget.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.stackedWidget.setObjectName("stackedWidget")
        self.login = QtWidgets.QWidget()
        self.login.setObjectName("login")
        self.functional_overview_heading = QtWidgets.QLabel(self.login)
        self.functional_overview_heading.setGeometry(QtCore.QRect(10, 50, 381, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.functional_overview_heading.setFont(font)
        self.functional_overview_heading.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(0, 255, 0);")
        self.functional_overview_heading.setObjectName("functional_overview_heading")
        self.password = QtWidgets.QPlainTextEdit(self.login)
        self.password.setGeometry(QtCore.QRect(10, 140, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(14)
        self.password.setFont(font)
        self.password.setStyleSheet("color: rgb(0, 255, 0);")
        self.password.setFrameShape(QtWidgets.QFrame.Box)
        self.password.setFrameShadow(QtWidgets.QFrame.Plain)
        self.password.setObjectName("password")
        
        self.email = QtWidgets.QPlainTextEdit(self.login)
        self.email.setGeometry(QtCore.QRect(10, 90, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(14)
        font.setKerning(False)
        self.email.setFont(font)
        self.email.setAcceptDrops(False)
        self.email.setToolTipDuration(1)
        self.email.setStyleSheet("color: rgb(0, 255, 0);")
        self.email.setFrameShape(QtWidgets.QFrame.Panel)
        self.email.setFrameShadow(QtWidgets.QFrame.Plain)
        self.email.setCenterOnScroll(True)
        self.email.setObjectName("email")
        self.stackedWidget.addWidget(self.login)
        self.signup = QtWidgets.QWidget()
        self.signup.setObjectName("signup")
        self.name = QtWidgets.QTextEdit(self.signup)
        self.name.setGeometry(QtCore.QRect(10, 40, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(14)
        self.name.setFont(font)
        self.name.setStyleSheet("color: rgb(0, 255, 0);")
        self.name.setFrameShadow(QtWidgets.QFrame.Plain)
        self.name.setObjectName("name")
        self.sig_email = QtWidgets.QTextEdit(self.signup)
        self.sig_email.setGeometry(QtCore.QRect(10, 90, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(14)
        self.sig_email.setFont(font)
        self.sig_email.setStyleSheet("color: rgb(0, 255, 0);")
        self.sig_email.setObjectName("sig_email")
        self.sig_password = QtWidgets.QTextEdit(self.signup)
        self.sig_password.setGeometry(QtCore.QRect(10, 140, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(14)
        self.sig_password.setFont(font)
        self.sig_password.setStyleSheet("color: rgb(0, 255, 0);")
        self.sig_password.setObjectName("sig_password")
        self.functional_overview_heading_3 = QtWidgets.QLabel(self.signup)
        self.functional_overview_heading_3.setGeometry(QtCore.QRect(10, 0, 381, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.functional_overview_heading_3.setFont(font)
        self.functional_overview_heading_3.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(0, 255, 0);")
        self.functional_overview_heading_3.setObjectName("functional_overview_heading_3")
        self.stackedWidget.addWidget(self.signup)
        self.signup1 = QtWidgets.QPushButton(self.centralwidget)
        self.signup1.setGeometry(QtCore.QRect(90, 400, 331, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.signup1.setFont(font)
        self.signup1.setStyleSheet("background-color:rgba(0,255,0);\n"
        "border:2px solid black;")
        self.signup1.setObjectName("signup1")
        self.login1 = QtWidgets.QPushButton(self.centralwidget)
        self.login1.setGeometry(QtCore.QRect(90, 340, 331, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.login1.setFont(font)
        self.login1.setStyleSheet("background-color:rgba(0,255,0);\n"
        "border:2px solid black;")
        self.login1.setObjectName("login1")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(470, 140, 271, 261))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../Project/Final Application/icons/speed-camera (1).png"))
        self.label.setObjectName("label")
        mainWindow.setCentralWidget(self.centralwidget)
        
        # login
        self.login1.clicked.connect(self.login_screen)

        # signup
        self.signup1.clicked.connect(self.signup_screen)


        self.retranslateUi(mainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)
      
      

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Automatic Licence Number Plate Detection And Recognition"))
        self.functional_overview_heading_2.setText(_translate("mainWindow", "<html><head/><body><p align=\"center\">AUTOMATIC LICENCE NUMBER PLATE DETECTION AND RECOGNITION</p><p align=\"center\">SOLUTION<br/></p></body></html>"))
        self.functional_overview_heading.setText(_translate("mainWindow", "PLEASE LOGIN !"))
        self.password.setPlaceholderText(_translate("mainWindow", "Password"))
        self.email.setPlaceholderText(_translate("mainWindow", "Username"))
        self.name.setPlaceholderText(_translate("mainWindow", "Name"))
        self.sig_email.setPlaceholderText(_translate("mainWindow", "Email"))
        self.sig_password.setPlaceholderText(_translate("mainWindow", "Password"))
        self.functional_overview_heading_3.setText(_translate("mainWindow", "PLEASE SIGNUP !"))
        self.signup1.setText(_translate("mainWindow", "SIGNUP"))
        self.login1.setText(_translate("mainWindow", "LOGIN"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
