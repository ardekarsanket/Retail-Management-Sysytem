from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import sqlite3
import datetime
import add_employee
import post_admin_login
import Update_Employee
import empManag_res
from threading import Timer

empIdGlobal = ""
Flag = True

class Ui_ManageEmpWindow(object):
    
    def showTime(self):
        global Flag
        try:
                while Flag:
                        QtWidgets.QApplication.processEvents()
                        #currTime = QtCore.QTime.currentTime()
                        now = datetime.datetime.now()
                        self.day.setText(now.strftime("%A"))
                        self.time.setText(now.strftime("%I:%M:%S %p"))
                        #self.time.setText(currTime.toString('hh:mm:ss'))
        except Exception as e:
                print(e)

    def filter_table(self,result): #can try with sql query too
        items = self.tableWidget.findItems(result, QtCore.Qt.MatchContains)
        if items:
                item = items[0]
                self.tableWidget.setCurrentItem(item)
        else:
                self.tableWidget.setCurrentItem(None)
                self.tableWidget.selectRow(-1)

    def setTextLabel(self, *text):
            string = ""
            for each in text:
                    string = string + each
            self.Error_Label.setText(string)

    def deleteEntry(self):
        currRow = self.tableWidget.currentRow()
        item = self.tableWidget.item(currRow,0)
        try:
                empid = item.text()
                connection = sqlite3.connect("db.db") 
                connection.execute("DELETE FROM employee WHERE empId = ?",[empid])
                connection.commit() 
                self.loadData() 
                connection.close()
                clear = Timer(0.0, self.setTextLabel, (""))
                sucess = Timer(0.3, self.setTextLabel, ("Deleted Sucessfully"))
                stop = Timer(4.0, self.setTextLabel, (""))
                clear.start()
                sucess.start()
                stop.start()
        except:
                error = Timer(0.0, self.setTextLabel, ("No Row Selected"))
                stop = Timer(4.0, self.setTextLabel, (""))
                error.start()
                stop.start()

    def loadData(self):
        connection = sqlite3.connect("db.db")
        sqlquery = "SELECT * FROM employee"

        result = connection.execute(sqlquery)
        self.tableWidget.setRowCount(0)
        x=0
        for row_number,row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)  
                for x,data in enumerate(row_data):
                        self.tableWidget.setItem(row_number, x, QtWidgets.QTableWidgetItem(str(data)))
                        x+=1
        
        connection.close()
                

        '''

        tablerow = 0
        self.tableWidget.setRowCount(0)

        for row in cur.execute(sqlquery):
                self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
                self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
                self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
                self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
                self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[4]))
                self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(row[5]))
                self.tableWidget.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(row[6]))

                tablerow+=1 '''

    def post_admin_login(self,x):
        global Flag 
        Flag = False                             ##2
        self.window3 = QtWidgets.QMainWindow()
        self.ui = post_admin_login.Ui_Form3()
        self.ui.setupUi(self.window3)
        self.window3.show()

    def add_employee(self,x):                             ##2
        self.window4 = QtWidgets.QMainWindow()
        self.ui = add_employee.Ui_addEmp_Window()
        self.ui.setupUi(self.window4)
        self.window4.show()
        global empIdGlobal
        empIdGlobal = "abc"



    '''def Update_Employee(self,x):
        try:
                currRow = self.tableWidget.currentRow()
                item = self.tableWidget.item(currRow,0)
                global empIdGlobal
                empIdGlobal = item.text()
                print(empIdGlobal)
                self.window5 = QtWidgets.QMainWindow()
                self.ui = Update_Employee.Ui_UpdateEmp_Window()
                self.ui.setupUi(self.window5)
                self.window5.show()
                x.close()
        except:
                print("No Row Selected")'''
        

    def setupUi(self, ManageEmpWindow):
        ManageEmpWindow.setObjectName("ManageEmpWindow")
        ManageEmpWindow.resize(1621, 899)
        ManageEmpWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)            
        ManageEmpWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        ManageEmpWindow.setStyleSheet("QPushButton{\n"
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
"\n"
"")
        self.label = QtWidgets.QLabel(ManageEmpWindow)
        self.label.setGeometry(QtCore.QRect(60, 40, 1511, 821))
        self.label.setStyleSheet("background-color:rgba(255,255,255,255);\n"
"border-bottom-right-radius:75px;\n"
"border-top-left-radius:75px;\n"
"border-top-right-radius:5px;\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(ManageEmpWindow)
        self.label_2.setGeometry(QtCore.QRect(60, 40, 391, 821))
        self.label_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 98,112, 255), stop:1 rgba(255, 107, 107, 255));\n"
"border-top-left-radius:75px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.manageEmp = QtWidgets.QPushButton(ManageEmpWindow)
        self.manageEmp.setGeometry(QtCore.QRect(110, 480, 281, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.manageEmp.setFont(font)
        self.manageEmp.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.manageEmp.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.manageEmp.setStyleSheet("")
        self.manageEmp.setObjectName("manageEmp")

        
        #self.manageEmp.clicked.connect(self.changeTxt)
        self.manageEmp.clicked.connect(self.passage)
        #self.manageEmp.clicked.connect(ManageEmpWindow.close)



        self.pushButton_3 = QtWidgets.QPushButton(ManageEmpWindow)
        self.pushButton_3.setGeometry(QtCore.QRect(1510, 40, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("image: url(:/images/back2.png);\n"
"border-radius:5px;")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_3.clicked.connect(self.post_admin_login)
        self.pushButton_3.clicked.connect(ManageEmpWindow.close)


        self.label_3 = QtWidgets.QLabel(ManageEmpWindow)
        self.label_3.setGeometry(QtCore.QRect(780, 50, 481, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:rgba(0,0,0,200);")
        self.label_3.setObjectName("label_3")
        self.tableWidget = QtWidgets.QTableWidget(ManageEmpWindow)
        self.tableWidget.setGeometry(QtCore.QRect(485, 191, 1051, 631))
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setStyleSheet("border: 0px solid black;\n"
"font:Fake Receipt\n"
"\n"
"\n"
"")

        self.day = QtWidgets.QLabel(ManageEmpWindow)
        self.day.setGeometry(QtCore.QRect(460, 40, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Kozuka Mincho Pro M")
        font.setPointSize(14)
        self.day.setFont(font)
        self.day.setText("")
        self.day.setObjectName("day")
        self.time = QtWidgets.QLabel(ManageEmpWindow)
        self.time.setGeometry(QtCore.QRect(460, 70, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Kozuka Mincho Pro M")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.time.setFont(font)
        self.time.setText("")
        self.time.setObjectName("time")

        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.manageEmp_2 = QtWidgets.QPushButton(ManageEmpWindow)
        self.manageEmp_2.setGeometry(QtCore.QRect(110, 400, 281, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.manageEmp_2.setFont(font)
        self.manageEmp_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.manageEmp_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.manageEmp_2.setStyleSheet("")
        self.manageEmp_2.setObjectName("manageEmp_2")

        self.manageEmp_2.clicked.connect(self.add_employee)
        self.manageEmp_2.clicked.connect(ManageEmpWindow.close)



        self.manageEmp_3 = QtWidgets.QPushButton(ManageEmpWindow)
        self.manageEmp_3.setGeometry(QtCore.QRect(110, 560, 281, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.manageEmp_3.setFont(font)
        self.manageEmp_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.manageEmp_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.manageEmp_3.setStyleSheet("")
        self.manageEmp_3.setObjectName("manageEmp_3")

        self.manageEmp_3.clicked.connect(self.deleteEntry)

        self.search_LE = QtWidgets.QLineEdit(ManageEmpWindow)
        self.search_LE.setGeometry(QtCore.QRect(120, 280, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.search_LE.setFont(font)
        self.search_LE.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:white;\n"
"padding-bottom:4px;\n"
"")
        self.search_LE.setText("")
        self.search_LE.setObjectName("search_LE")
        self.label_4 = QtWidgets.QLabel(ManageEmpWindow)
        self.label_4.setGeometry(QtCore.QRect(80, 60, 71, 51))
        self.label_4.setStyleSheet("image: url(:/images/profile.png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(ManageEmpWindow)
        self.label_5.setGeometry(QtCore.QRect(150, 70, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setStyleSheet("color:white;")
        self.label_5.setObjectName("label_5")

        self.Error_Label = QtWidgets.QLabel(ManageEmpWindow)
        self.Error_Label.setGeometry(QtCore.QRect(140,640, 215, 51))
        self.Error_Label.setText("")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.Error_Label.setFont(font)
        self.Error_Label.setAutoFillBackground(False)
        self.Error_Label.setStyleSheet("color:white;\n"
        "text-align: center;")
        self.Error_Label.setObjectName("Error_Label")

        self.label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25,xOffset=0,yOffset=0))
        self.label_3.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25,xOffset=0,yOffset=0))
        self.manageEmp.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25,xOffset=3,yOffset=3))
        self.manageEmp_2.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25,xOffset=3,yOffset=3))
        self.manageEmp_3.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25,xOffset=3,yOffset=3))

        self.tableWidget.setColumnWidth(0,180)
        self.tableWidget.setColumnWidth(1,200)
        self.tableWidget.setColumnWidth(2,200)
        self.tableWidget.setColumnWidth(3,150)
        self.tableWidget.setColumnWidth(4,150)
        self.tableWidget.setColumnWidth(5,150)
        self.tableWidget.setColumnWidth(6,400)
        self.loadData()

        '''filter_proxy_model = QtCore.QSortFilterProxyModel()
        self.model = TableModel
        filter_proxy_model.setSourceModel(tableWidget)'''

        self.search_LE.textChanged.connect(self.filter_table)

        self.timer=QtCore.QTimer()
        self.timer.timeout.connect(self.showTime)
        self.timer.start(10)

        self.retranslateUi(ManageEmpWindow)
        QtCore.QMetaObject.connectSlotsByName(ManageEmpWindow)

    def retranslateUi(self, ManageEmpWindow):
        _translate = QtCore.QCoreApplication.translate
        ManageEmpWindow.setWindowTitle(_translate("ManageEmpWindow", "Form"))
        self.manageEmp.setText(_translate("ManageEmpWindow", "Update Employee"))
        self.label_3.setText(_translate("ManageEmpWindow", "Employee Management"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ManageEmpWindow", "Employee ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ManageEmpWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("ManageEmpWindow", "Contact No."))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("ManageEmpWindow", "Salary"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("ManageEmpWindow", "Password"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("ManageEmpWindow", "Role/Position"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("ManageEmpWindow", "Address"))
        self.manageEmp_2.setText(_translate("ManageEmpWindow", "Add Employee"))
        self.manageEmp_3.setText(_translate("ManageEmpWindow", "Delete Employee"))
        self.search_LE.setPlaceholderText(_translate("ManageEmpWindow", "Search                  "))
        self.label_5.setText(_translate("ManageEmpWindow", "Admin"))
        global check
        check = True
        if(check):
                global x
                x = ManageEmpWindow
                check = False

    def changeTxt(self):
            currRow = self.tableWidget.currentRow()
            item = self.tableWidget.item(currRow,0)
            global empIdGlobal 
            empIdGlobal = item.text()
            #print(empIdGlobal)
            

    def passage(self):
            self.Update_Employee(x)   

    def Update_Employee(self,x):
        try:
                clear = Timer(0.0, self.setTextLabel, (""))
                clear.start()
                currRow = self.tableWidget.currentRow()
                item = self.tableWidget.item(currRow,0)
                global empIdGlobal
                empIdGlobal = item.text()
                #print(empIdGlobal)
                self.window5 = QtWidgets.QMainWindow()
                self.ui = Update_Employee.Ui_UpdateEmp_Window()
                self.ui.setupUi(self.window5)
                self.window5.show()
                x.close()
        except:
                error = Timer(0.0, self.setTextLabel, ("No Row Selected"))
                stop = Timer(4.0, self.setTextLabel, (""))
                error.start()
                stop.start()

if __name__ == "__main__":                                    ##6
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_ManageEmpWindow()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())