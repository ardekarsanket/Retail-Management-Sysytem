from PyQt5 import QtCore, QtGui, QtWidgets
import sys                                       
import second 
import post_admin_login
import MySQLdb as mdb
import sqlite3

check = True
class Ui_Form(object):
        
    def messagebox(self,title,message):
            mess = QtWidgets.QMessageBox()
            mess.setWindowTitle(title)
            mess.setText(message)
            mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
            mess.exec_()
            
    def second(self):                           
        self.window2 = QtWidgets.QMainWindow()
        self.ui = second.Ui_Form2()
        self.ui.setupUi(self.window2)
        self.window2.show()

    def post_admin_login(self,x):                            
        self.window3 = QtWidgets.QMainWindow()
        self.ui = post_admin_login.Ui_Form3()
        self.ui.setupUi(self.window3)
        self.window3.show()
        x.hide()
        

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1039, 812)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)            
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground) 
      
        Form.setStyleSheet("QPushButton{\n"
"background-color:rgba(85,98,112,255);\n"
"color:rgba(255,255,255,200);\n"
"border-radius:25px\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgba(255,107,107,255);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(255,107,107,255):\n"
"backgound-position:calc(100% -10px)center:\n"
"}\n"
"")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(70, 40, 900, 700))
        self.label.setStyleSheet("background-color:rgba(255,255,255,255);\n"
"border-bottom-right-radius:50px;\n"
"border-top-left-radius:50px;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(70, 40, 450, 700))
        self.label_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 98,112, 255), stop:1 rgba(255, 107, 107, 255));\n"
"border-top-left-radius:50px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(630, 120, 241, 91))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(25)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:rgba(0,0,0,200);")
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(590, 250, 321, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(590, 350, 321, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(590, 470, 321, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.passage)

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(590, 570, 321, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("")
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_2.clicked.connect(self.second)               
        self.pushButton_2.clicked.connect(Form.close)

        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(80, 430, 441, 401))
        font = QtGui.QFont()
        font.setFamily("Mountain")
        font.setPointSize(210)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgba(255,107,107,255);")
        self.label_4.setObjectName("label_4")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(940, 40, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(Form.close)                                   
        self.messageLabel = QtWidgets.QLabel(Form)
        self.messageLabel.setGeometry(QtCore.QRect(560, 640, 371, 91))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.messageLabel.setFont(font)
        self.messageLabel.setStyleSheet("color: #6B6B6B;")
        self.messageLabel.setText("")
        self.messageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.messageLabel.setWordWrap(False)
        self.messageLabel.setObjectName("messageLabel")

        self.label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25,xOffset=0,yOffset=0))
        self.label_3.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25,xOffset=0,yOffset=0))
        self.pushButton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25,xOffset=3,yOffset=3))
        self.pushButton_2.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25,xOffset=3,yOffset=3))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "TextLabel"))
        self.label_3.setText(_translate("Form", "Admin Login"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Username"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Password"))
        self.pushButton.setText(_translate("Form", "Log In"))
        self.pushButton_2.setText(_translate("Form", "Log In as Employee"))
        self.label_4.setText(_translate("Form", "-"))
        self.pushButton_3.setText(_translate("Form", "X"))

        global check
        check = True
        if(check):
                global x
                x = Form
                check = False
    
    def passage(self):
            self.admin_logincheck(x)
            
    def admin_logincheck(self,x):
        usern = self.lineEdit.text()
        pass11 = self.lineEdit_2.text()
        check = False
        if(usern != "" and pass11 != ""):
                check = True
        connection = sqlite3.connect("db.db")
        #result1 = connection.execute("SELECT * FROM admin WHERE username = ? and password = ?",(usern,pass11))

        result_user = connection.execute(f"SELECT username FROM admin WHERE username = '{usern}'")
        result_pass = connection.execute(f"SELECT password FROM admin WHERE password = '{pass11}'")
        
        usern = result_user.fetchone()
        pass11 = result_pass.fetchone()
        #result1 = result1.fetchall()

        if(usern != None and pass11 != None):
                self.window3 = QtWidgets.QMainWindow()
                self.ui = post_admin_login.Ui_Form3()
                self.ui.setupUi(self.window3)
                self.window3.show()
                x.close()
        else:
                if((usern == None) and (pass11 == None) and (check == False)):
                        self.messageLabel.setText("Please Enter Credentials")
                elif((usern == None) and (pass11 == None) and (check == True)):
                        self.messageLabel.setStyleSheet("font-size:29px;\n"
                        "color: #6B6B6B;")
                        self.messageLabel.setText("Invalid Username and Password")
                elif(usern == None):
                        self.messageLabel.setText("Invalid Username")
                else:
                        self.messageLabel.setText("Invalid Password")  
        connection.close()            
        
if __name__ == "__main__":                                   
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
 
 