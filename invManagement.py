
from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
from threading import Timer
import sys
import sqlite3
import second
import res
import post_emp_login
import Add_Product
from cv2 import cv2
from pyzbar import pyzbar
import update_Product
barcode_id = ""
selected_barcodeid = ""
check = True
Flag = True

class Ui_InvManagement(object):

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
        
    def setTextLabel(self, *text):
            string = ""
            for each in text:
                    string = string + each
            self.Error_Label.setText(string)

    def post_emp_login(self):
        global Flag 
        Flag = False                           
        self.window = QtWidgets.QMainWindow()
        self.ui = post_emp_login.Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()


    def Add_Product(self):                           
        self.window1 = QtWidgets.QMainWindow()
        self.ui = Add_Product.Ui_addProduct_Window()
        self.ui.setupUi(self.window1)
        self.window1.show()
    
    def filter_table(self,result): #can try with sql query too
        items = self.tableWidget.findItems(result, QtCore.Qt.MatchContains)
        if items:
                item = items[0]
                self.tableWidget.setCurrentItem(item)
        else:
                self.tableWidget.setCurrentItem(None)
                self.tableWidget.selectRow(-1)

    def deleteEntry(self):
        currRow = self.tableWidget.currentRow()
        item = self.tableWidget.item(currRow,0)
        try:
                product_id = item.text()
                connection = sqlite3.connect("db.db") 
                connection.execute("DELETE FROM product WHERE product_id = ?",[product_id])
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
                #error = Timer(0.0, self.setTextLabel, ("N","o"," ", "R", "o", "w", " ", "S", "e", 'l', "e", "c", "t", "e", "d"))
                error = Timer(0.0, self.setTextLabel, ("No Row Selected"))
                stop = Timer(4.0, self.setTextLabel, (""))
                error.start()
                stop.start()

    def loadData(self):
        connection = sqlite3.connect("db.db")
        sqlquery = "SELECT * FROM product"

        result = connection.execute(sqlquery)
        self.tableWidget.setRowCount(0)
        x=0
        for row_number,row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)  
                for x,data in enumerate(row_data):
                        self.tableWidget.setItem(row_number, x, QtWidgets.QTableWidgetItem(str(data)))
                        x+=1
        
        connection.close()

    def read_barcodes(self,frame):
        barcodes = pyzbar.decode(frame)
        for barcode in barcodes:
                x, y , w, h = barcode.rect
                barcode_info = barcode.data.decode('utf-8')
                cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 255, 0), 2)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, barcode_info, (x + 6, y - 6), font, 2.0, (255, 255, 255), 1)
                global barcode_id 
                #print(barcode_info)
                barcode_id = barcode_info
        return frame



    def setupUi(self, InvManagement):
        InvManagement.setObjectName("InvManagement")
        InvManagement.resize(1621, 899)
        InvManagement.setWindowFlags(QtCore.Qt.FramelessWindowHint)            
        InvManagement.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        InvManagement.setStyleSheet("QPushButton{\n"
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
        self.label = QtWidgets.QLabel(InvManagement)
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
        self.label_2 = QtWidgets.QLabel(InvManagement)
        self.label_2.setGeometry(QtCore.QRect(60, 40, 391, 821))
        self.label_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 98,112, 255), stop:1 rgba(255, 107, 107, 255));\n"
"border-top-left-radius:75px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.updateproduct = QtWidgets.QPushButton(InvManagement)
        self.updateproduct.setGeometry(QtCore.QRect(110, 480, 281, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.updateproduct.setFont(font)
        self.updateproduct.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.updateproduct.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.updateproduct.setStyleSheet("")
        self.updateproduct.setObjectName("updateproduct")
        

        self.backbutton = QtWidgets.QPushButton(InvManagement)
        self.backbutton.setGeometry(QtCore.QRect(1510, 40, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.backbutton.setFont(font)
        self.backbutton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backbutton.setStyleSheet("image: url(:/images/back2.png);\n"
"border-radius:5px;")
        self.backbutton.setText("")
        self.backbutton.setObjectName("backbutton")
        self.label_3 = QtWidgets.QLabel(InvManagement)
        self.label_3.setGeometry(QtCore.QRect(780, 50, 481, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:rgba(0,0,0,200);")
        self.label_3.setObjectName("label_3")
        self.tableWidget = QtWidgets.QTableWidget(InvManagement)
        self.tableWidget.setGeometry(QtCore.QRect(485, 191, 1051, 631))
        self.tableWidget.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.tableWidget.setStyleSheet("border: 1px solid black;\n"
"\n"
"\n"
"")
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
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
        self.addproduct = QtWidgets.QPushButton(InvManagement)
        self.addproduct.setGeometry(QtCore.QRect(110, 400, 281, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.addproduct.setFont(font)
        self.addproduct.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addproduct.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.addproduct.setStyleSheet("")
        self.addproduct.setObjectName("addproduct")
        self.deleteproduct = QtWidgets.QPushButton(InvManagement)
        self.deleteproduct.setGeometry(QtCore.QRect(110, 560, 281, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.deleteproduct.setFont(font)
        self.deleteproduct.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.deleteproduct.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.deleteproduct.setStyleSheet("")
        self.deleteproduct.setObjectName("deleteproduct")
        
        self.deleteproduct.clicked.connect(self.deleteEntry)

        self.search_LE = QtWidgets.QLineEdit(InvManagement)
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
        self.label_4 = QtWidgets.QLabel(InvManagement)
        self.label_4.setGeometry(QtCore.QRect(80, 60, 71, 51))
        self.label_4.setStyleSheet("image: url(:/images/profile.png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")

        self.Error_Label = QtWidgets.QLabel(InvManagement)
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

        self.currEmpLabel = QtWidgets.QLabel(InvManagement)
        self.currEmpLabel.setGeometry(QtCore.QRect(150, 70, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.currEmpLabel.setFont(font)
        self.currEmpLabel.setAutoFillBackground(False)
        self.currEmpLabel.setStyleSheet("color:white;")
        self.currEmpLabel.setText("")
        self.currEmpLabel.setObjectName("currEmpLabel")
        self.currEmpLabel.setText(second.currentEmpName)
        
        self.day = QtWidgets.QLabel(InvManagement)
        self.day.setGeometry(QtCore.QRect(1380, 40, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Kozuka Mincho Pro M")
        font.setPointSize(14)
        self.day.setFont(font)
        self.day.setText("")
        self.day.setObjectName("day")
        self.time = QtWidgets.QLabel(InvManagement)
        self.time.setGeometry(QtCore.QRect(1370, 70, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Kozuka Mincho Pro M")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.time.setFont(font)
        self.time.setText("")
        self.time.setObjectName("time")
        self.label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25,xOffset=0,yOffset=0))
        self.label_3.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25,xOffset=0,yOffset=0))
        self.addproduct.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25,xOffset=3,yOffset=3))
        self.updateproduct.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25,xOffset=3,yOffset=3))
        self.deleteproduct.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25,xOffset=3,yOffset=3))

        self.tableWidget.setColumnWidth(0,180)
        self.tableWidget.setColumnWidth(1,270)
        self.tableWidget.setColumnWidth(2,170)
        self.tableWidget.setColumnWidth(3,129)
        self.tableWidget.setColumnWidth(4,150)
        self.tableWidget.setColumnWidth(5,150)
        self.tableWidget.setColumnWidth(6,250)

        self.backbutton.clicked.connect(self.post_emp_login)
        self.backbutton.clicked.connect(InvManagement.close)

        #self.addproduct.clicked.connect(InvManagement.close)
        self.addproduct.clicked.connect(self.passage)
        self.updateproduct.clicked.connect(self.passage2)
        
        self.label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25,xOffset=0,yOffset=0))
        self.label_3.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25,xOffset=0,yOffset=0))
        self.addproduct.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25,xOffset=3,yOffset=3))
        self.deleteproduct.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25,xOffset=3,yOffset=3))
        self.updateproduct.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25,xOffset=3,yOffset=3))

        self.tableWidget.setColumnWidth(0,180)
        self.tableWidget.setColumnWidth(1,200)
        self.tableWidget.setColumnWidth(2,200)
        self.tableWidget.setColumnWidth(3,150)
        self.tableWidget.setColumnWidth(4,150)
        self.tableWidget.setColumnWidth(5,150)
        self.tableWidget.setColumnWidth(6,400)
        self.loadData()


        self.time.setGeometry(QtCore.QRect(460, 70, 151, 41))
        self.day.setGeometry(QtCore.QRect(460, 40, 141, 41))

        self.search_LE.textChanged.connect(self.filter_table)

        self.timer=QtCore.QTimer()
        self.timer.timeout.connect(self.showTime)
        self.timer.start(10)

        self.retranslateUi(InvManagement)
        QtCore.QMetaObject.connectSlotsByName(InvManagement)


    def retranslateUi(self, InvManagement):
        _translate = QtCore.QCoreApplication.translate
        InvManagement.setWindowTitle(_translate("InvManagement", "Form"))
        self.updateproduct.setText(_translate("InvManagement", "Update Product"))
        self.label_3.setText(_translate("InvManagement", "Inventory Management"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("InvManagement", "Product ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("InvManagement", "Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("InvManagement", "Category"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("InvManagement", "In Stock"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("InvManagement", "Cost Price"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("InvManagement", "MRP"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("InvManagement", "Description"))
        self.addproduct.setText(_translate("InvManagement", "Add Product"))
        self.deleteproduct.setText(_translate("InvManagement", "Delete Product"))
        self.search_LE.setPlaceholderText(_translate("InvManagement", "Search                  "))
        global check
        check = True
        if(check):
                global x
                x = InvManagement
                check = False

    def passage(self):
            self.startScan(x)
    
    def passage2(self):
            self.updateProduct(x)

    def updateProduct(self,x):
        try:
                clear = Timer(0.0, self.setTextLabel, (""))
                clear.start()
                currRow = self.tableWidget.currentRow()
                item = self.tableWidget.item(currRow,0)
                global selected_barcodeid
                selected_barcodeid = item.text()
                #print(selected_barcodeid)
                self.window5 = QtWidgets.QMainWindow()
                self.ui = update_Product.Ui_updateProduct_Window()
                self.ui.setupUi(self.window5)
                self.window5.show()
                x.close()
                
        except:
                error = Timer(0.0, self.setTextLabel, ("No Row Selected"))
                stop = Timer(4.0, self.setTextLabel, (""))
                error.start()
                stop.start()

    def startScan(self,x):
        camera = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        ret, frame = camera.read()
        while ret:
                ret, frame = camera.read()
                frame = self.read_barcodes(frame)
                cv2.imshow('Barcode scanner', frame)
                global barcode_id
                if cv2.waitKey(1) & 0xFF == 27 or barcode_id!= "": 
                        break
        
        self.Add_Product()
        barcode_id = ""
        camera.release()
        cv2.destroyAllWindows()
        x.close()


if __name__ == "__main__":                                    
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_InvManagement()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())