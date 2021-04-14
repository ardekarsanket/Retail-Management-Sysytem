from PyQt5 import QtCore, QtGui, QtWidgets
import sys                                  #1
import first1    
import post_emp_login       
import sqlite3              


currentEmp = ""
currentEmpName = ""


class Ui_Form2(object):

    def first(self):                             ##2
        self.window2 = QtWidgets.QMainWindow()
        self.ui = first1.Ui_Form()
        self.ui.setupUi(self.window2)
        self.window2.show()    
    def post_emp_login(self,x):                             ##2
        self.window3 = QtWidgets.QMainWindow()
        self.ui = post_emp_login.Ui_Form()
        self.ui.setupUi(self.window3)
        self.window3.show()
        x.hide()
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1039, 812)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)               ##3
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
        self.label_3.setGeometry(QtCore.QRect(600, 110, 291, 91))
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
        self.pushButton_2.clicked.connect(self.first)                ##4
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

        self.pushButton_3.clicked.connect(Form.close)                        ##5
        self.label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25,xOffset=0,yOffset=0))
        self.label_3.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25,xOffset=0,yOffset=0))
        self.pushButton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25,xOffset=3,yOffset=3))
        self.pushButton.clicked.connect(self.passage)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "TextLabel"))
        self.label_3.setText(_translate("Form", "Employee Login"))
        self.lineEdit.setPlaceholderText(_translate("Form", "EMP ID"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Password"))
        self.pushButton.setText(_translate("Form", "Log In"))
        self.pushButton_2.setText(_translate("Form", "Back"))
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
        empId = self.lineEdit.text()
        empPass = self.lineEdit_2.text()
        check = False
        if(empId != "" and empPass != ""):
                check = True
        connection = sqlite3.connect("db.db")
        #result1 = connection.execute("SELECT * FROM admin WHERE username = ? and password = ?",(empId,empPass))

        result_user = connection.execute(f"SELECT empId FROM employee WHERE empId = '{empId}'")
        result_pass = connection.execute(f"SELECT password FROM employee WHERE password = '{empPass}'")
        
        empId = result_user.fetchone()
        empPass = result_pass.fetchone()        
        #result1 = result1.fetchall()

        if(empId != None and empPass != None):
                global currentEmp
                global currentEmpName
                currentEmp = self.lineEdit.text()
                result1 = connection.execute("SELECT name FROM employee WHERE empId = ?",(currentEmp,))
                result = list(result1.fetchall())
                currentEmpName = result[0][0]
                self.window3 = QtWidgets.QMainWindow()
                self.ui = post_emp_login.Ui_Form()
                self.ui.setupUi(self.window3)
                self.window3.show()
                x.close()
        else:
                if((empId == None) and (empPass == None) and (check == False)):
                        self.messageLabel.setText("Please Enter Credentials")
                elif((empId == None) and (empPass == None) and (check == True)):
                        self.messageLabel.setText("Invalid ID and Password")
                elif(empId == None):
                        self.messageLabel.setText("Invalid ID")
                else:
                        self.messageLabel.setText("Invalid Password")   
        connection.close()  

if __name__ == "__main__":                                    ##6
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form2()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
