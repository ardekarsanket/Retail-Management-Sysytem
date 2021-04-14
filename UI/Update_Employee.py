from PyQt5 import QtCore, QtGui, QtWidgets
import empManagement
import addemp_res
import sys
import sqlite3
import time

check = True

#use variables of emp Management after empManagement(self) to avoid circular imports/dependencies
class Ui_UpdateEmp_Window(object):

    def empManagement(self):                             ##2
        self.window3 = QtWidgets.QMainWindow()
        self.ui = empManagement.Ui_ManageEmpWindow()
        self.ui.setupUi(self.window3)
        self.window3.show()

    def preloadData(self):
        connection = sqlite3.connect("db.db")
        result = connection.execute("""SELECT * FROM employee WHERE empId = ?""",(empManagement.empIdGlobal,))
        emplist = list(result.fetchall())
        self.empID_LE.setText(emplist[0][0])
        self.name_LE.setText(emplist[0][1])
        self.contactno_LE.setText(emplist[0][2])
        self.salary_LE.setText(emplist[0][3])
        self.password_LE.setText(emplist[0][4])
        self.role_LE.setText(emplist[0][5])
        self.address_LE.setText(emplist[0][6])
        connection.close()



    def allFieldsValidation(self):
        empid = self.empID_LE.text()
        name = self.name_LE.text()
        contact = self.contactno_LE.text()
        salary = self.salary_LE.text()
        password = self.password_LE.text()
        role = self.role_LE.text()
        address = self.address_LE.text()
        if ((empid != "" and  empid.isspace() == False) and (name != "" and  name.isspace() == False) and (contact != "" and  contact.isspace() == False) and (salary != "" and  salary.isspace() == False) and (password != "" and  password.isspace() == False) and (role != "" and  role.isspace() == False) and (address != "" and  address.isspace() == False)):
                return True
        else:
                self.label_5.setGeometry(QtCore.QRect(690, 680, 421, 91))
                self.label_5.setText("All fields are required ")
                return False

    def setupUi(self, UpdateEmp_Window):
        UpdateEmp_Window.setObjectName("UpdateEmp_Window")
        UpdateEmp_Window.resize(1350, 833)
        UpdateEmp_Window.setWindowFlags(QtCore.Qt.FramelessWindowHint)            
        UpdateEmp_Window.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        UpdateEmp_Window.setStyleSheet("QPushButton{\n"
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
        self.label = QtWidgets.QLabel(UpdateEmp_Window)
        self.label.setGeometry(QtCore.QRect(130, 30, 1131, 771))
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setStyleSheet("background-color:rgba(255,255,255,255);\n"
"border-bottom-right-radius:50px;\n"
"border-top-left-radius:50px;\n"
"border-top-right-radius:5px;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(UpdateEmp_Window)
        self.label_2.setGeometry(QtCore.QRect(130, 30, 381, 771))
        self.label_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 98,112, 255), stop:1 rgba(255, 107, 107, 255));\n"
"border-top-left-radius:50px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(UpdateEmp_Window)
        self.label_3.setGeometry(QtCore.QRect(640, 40, 481, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: #000;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(False)
        self.label_3.setObjectName("label_3")
        self.empID_LE = QtWidgets.QLineEdit(UpdateEmp_Window)
        self.empID_LE.setGeometry(QtCore.QRect(560, 190, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.empID_LE.setFont(font)
        self.empID_LE.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.empID_LE.setText("")
        self.empID_LE.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.empID_LE.setObjectName("empID_LE")
        self.password_LE = QtWidgets.QLineEdit(UpdateEmp_Window)
        self.password_LE.setGeometry(QtCore.QRect(560, 290, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.password_LE.setFont(font)
        self.password_LE.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.password_LE.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_LE.setObjectName("password_LE")
        self.pushButton = QtWidgets.QPushButton(UpdateEmp_Window)
        self.pushButton.setGeometry(QtCore.QRect(810, 600, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setMouseTracking(False)
        self.pushButton.setTabletTracking(False)
        self.pushButton.setStyleSheet("border-radius:15px;")
        self.pushButton.setObjectName("pushButton")


        self.pushButton.clicked.connect(self.passage)

        self.label_4 = QtWidgets.QLabel(UpdateEmp_Window)
        self.label_4.setGeometry(QtCore.QRect(130, 400, 381, 541))
        font = QtGui.QFont()
        font.setFamily("Mountain")
        font.setPointSize(210)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgba(255,107,107,255);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.address_LE = QtWidgets.QLineEdit(UpdateEmp_Window)
        self.address_LE.setGeometry(QtCore.QRect(560, 490, 661, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.address_LE.setFont(font)
        self.address_LE.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.address_LE.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.address_LE.setObjectName("address_LE")
        self.role_LE = QtWidgets.QLineEdit(UpdateEmp_Window)
        self.role_LE.setGeometry(QtCore.QRect(910, 290, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.role_LE.setFont(font)
        self.role_LE.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.role_LE.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.role_LE.setObjectName("role_LE")
        self.name_LE = QtWidgets.QLineEdit(UpdateEmp_Window)
        self.name_LE.setGeometry(QtCore.QRect(910, 190, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.name_LE.setFont(font)
        self.name_LE.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.name_LE.setText("")
        self.name_LE.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.name_LE.setObjectName("name_LE")
        self.salary_LE = QtWidgets.QLineEdit(UpdateEmp_Window)
        self.salary_LE.setGeometry(QtCore.QRect(910, 390, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.salary_LE.setFont(font)
        self.salary_LE.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.salary_LE.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.salary_LE.setObjectName("salary_LE")
        self.contactno_LE = QtWidgets.QLineEdit(UpdateEmp_Window)
        self.contactno_LE.setGeometry(QtCore.QRect(560, 390, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.contactno_LE.setFont(font)
        self.contactno_LE.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.contactno_LE.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.contactno_LE.setObjectName("contactno_LE")
        self.pushButton_2 = QtWidgets.QPushButton(UpdateEmp_Window)
        self.pushButton_2.setGeometry(QtCore.QRect(1200, 30, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("font-size:20px;\n"
"image: url(:/img/back2.png);\n"
"text-align: center;\n"
"border-radius:5px;")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_5 = QtWidgets.QLabel(UpdateEmp_Window)
        self.label_5.setGeometry(QtCore.QRect(740, 680, 421, 91))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: #6B6B6B;")
        self.label_5.setText("")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setWordWrap(False)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(UpdateEmp_Window)
        self.label_6.setGeometry(QtCore.QRect(670, 690, 91, 71))
        self.label_6.setStyleSheet("")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.empID_LE.setEnabled(False)

        self.pushButton_2.clicked.connect(self.empManagement)
        self.pushButton_2.clicked.connect(UpdateEmp_Window.close)
        self.preloadData()

        self.label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25,xOffset=0,yOffset=0))
        self.label_3.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25,xOffset=0,yOffset=0))
        self.pushButton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25,xOffset=3,yOffset=3))
        

        self.retranslateUi(UpdateEmp_Window)
        QtCore.QMetaObject.connectSlotsByName(UpdateEmp_Window)

    def retranslateUi(self, UpdateEmp_Window):
        _translate = QtCore.QCoreApplication.translate
        UpdateEmp_Window.setWindowTitle(_translate("UpdateEmp_Window", "Form"))
        self.label.setText(_translate("UpdateEmp_Window", "TextLabel"))
        self.label_3.setText(_translate("UpdateEmp_Window", "UPDATE EMPLOYEE"))
        self.empID_LE.setPlaceholderText(_translate("UpdateEmp_Window", "Employee ID"))
        self.password_LE.setPlaceholderText(_translate("UpdateEmp_Window", "Password"))
        self.pushButton.setText(_translate("UpdateEmp_Window", "Update"))
        self.label_4.setText(_translate("UpdateEmp_Window", "-"))
        self.address_LE.setPlaceholderText(_translate("UpdateEmp_Window", "Address"))
        self.role_LE.setPlaceholderText(_translate("UpdateEmp_Window", "Role/Position"))
        self.name_LE.setPlaceholderText(_translate("UpdateEmp_Window", "Name"))
        self.salary_LE.setPlaceholderText(_translate("UpdateEmp_Window", "Salary"))
        self.contactno_LE.setPlaceholderText(_translate("UpdateEmp_Window", "Contact No."))
        global check
        check = True
        if(check):
                global x
                x = UpdateEmp_Window
                check = False
       
    def passage(self):
        self.updEmp(x)

    def updEmp(self,x):
        empid = self.empID_LE.text()
        name = self.name_LE.text()
        contact = self.contactno_LE.text()
        salary = self.salary_LE.text()
        password = self.password_LE.text()
        role = self.role_LE.text()
        address = self.address_LE.text()

        connection = sqlite3.connect("db.db")

        if (self.allFieldsValidation()):
                contact = str(contact)
                salary = str(salary)
                if(empid.startswith('EMP') == False):
                        self.label_5.setGeometry(QtCore.QRect(690, 680, 421, 91))
                        self.label_5.setText("Enter Valid ID")
                elif name.isdigit():
                        self.label_5.setGeometry(QtCore.QRect(690, 680, 421, 91))
                        self.label_5.setText("Enter valid Name")

                elif (len(contact)!= 10 or contact.isdigit() == False):
                        self.label_5.setGeometry(QtCore.QRect(690, 680, 421, 91))
                        self.label_5.setText("Enter Valid Contact No.")
                
                elif (salary.isdigit() == False):
                        self.label_5.setGeometry(QtCore.QRect(690, 680, 421, 91))
                        self.label_5.setText("Enter Valid Salary")
                
                elif any(chr.isdigit() for chr in role):
                        self.label_5.setGeometry(QtCore.QRect(690, 680, 421, 91))
                        self.label_5.setText("Enter Valid Role/Position")
             
                else:
                        connection.execute("""UPDATE employee SET  name = ?, contact = ?, salary = ?, password = ?, role = ?, address =? WHERE empId = ?""",(name,contact,salary,password,role,address,empManagement.empIdGlobal))
                        connection.commit()
                        self.label_5.setGeometry(QtCore.QRect(690, 680, 421, 91))
                        self.label_5.setText("Update Successful")
                        self.label_6.setStyleSheet("image: url(:/img/success-icon-23194.png);")
                        #self.pushButton.setEnabled(False)
                        #time.sleep(5)
                        #x.close()
        
        connection.close()

if __name__ == "__main__":                                    ##6
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_UpdateEmp_Window()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())