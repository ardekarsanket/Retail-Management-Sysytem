from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import billingsystem_res
import datetime
import second
import post_emp_login
import sqlite3
import pdfgen
from cv2 import cv2
from pyzbar import pyzbar
from reportlab.pdfgen import canvas
import webbrowser,os

Flag = True
Flag2 = False
scannedbarcode_id = ""
current_bill = ""
currRow = -1
customer_Name = ""
Customer_contact = ""

try:
	os.mkdir("C:\\InvoiceGenerator")
except:
	pass
class product:
	def __init__(self,name,category,quantity,rate,amount):
		self.name = name
		self.category =category
		self.quantity =  quantity
		self.rate= rate
		self.amount = amount
class Ui_ManageBilllWindow(object):


    def generateBill(self):
             global customer_Name
             customer_Name =  self.customername_LE.text()
             global Customer_contact 
             Customer_contact=  self.contactnumber_LE.text()
             if(self.customerValidations()):
                        global current_bill
                        #self.getDetailsToPrint()
                        pdf= canvas.Canvas("C:\\InvoiceGenerator\\" + str(current_bill) + ".pdf")
                        pdfgen.header(pdf)
                        pdfgen.middle(pdf)
                        ycooridinate=650
                        x=1
                        Products=[]
                        global Total
                        Total = 0

                        connection = sqlite3.connect("db.db")
                        result = connection.execute("SELECT * from bill WHERE bill_id = (?)",(current_bill,))
                        result_list = list(result.fetchall())
                        print(result_list)
                        
                        i = 0
                        while  i < len(result_list):
                                #print("Inside While")
                                #print(result_list[i][1],result_list[i][2], result_list[i][3], result_list[i][4],result_list[i][5])
                                currproduct  = product(result_list[i][1],result_list[i][2], result_list[i][3], result_list[i][4],result_list[i][5] )
                                
                                Total = Total + int(result_list[i][5])
                                pdf.drawString(35,ycooridinate,str(x))
                                x=x+1
                                pdf.setFont("Courier-Bold",9)
                                ycooridinate=pdfgen.additem(currproduct,pdf,ycooridinate) 
                                i += 1

                        pdf.setFont("Courier-Bold",11)
                        pdfgen.footer(pdf,Products)
                        pdf.save()
                        webbrowser.open("C:\\InvoiceGenerator\\" + str(current_bill) + ".pdf")

                        quantity = connection.execute("""SELECT name,quantity FROM bill WHERE bill_id = ?""",(current_bill,))
                        quantity_list = list(quantity.fetchall())
                        #print(len(resultlist))
                        for x in quantity_list:
                                a = int(x[1])
                                b = x[0]
                                try:
                                        connection.execute("UPDATE product SET in_stock = in_stock - (?) WHERE name = (?) ",(a,b,))
                                        connection.commit()
                                except Exception as e:
                                        print(e)

                        self.carttable.clear()

                        last_bill = "SELECT MAX(bill_id) from bill"
                        result_lastbill = connection.execute(last_bill)
                        final_result = list(result_lastbill.fetchall())
                        current_bill = int(final_result[0][0]) + 1
                        
                        if current_bill<10:
                                current_bill = '0' + str(current_bill)
                        self.billno_LE.setText(str(current_bill))
                        self.billno_LE.setDisabled(True)
                        self.customername_LE.setText("")
                        self.contactnumber_LE.setText("")
                        self.loadData()
                        connection.close()
                
    def customerValidations(self):
             global customer_Name
             if(customer_Name == "" or customer_Name.isspace()):
                     self.errorlabel2.setText("Enter Customer Name")
                     return False
             if any(chr.isdigit() for chr in customer_Name):
                        self.errorlabel2.setText("Enter valid Name")
                        return False
             global Customer_contact 
             if(Customer_contact == "" or Customer_contact.isspace()):
                     self.errorlabel2.setText("Enter Customer Contact")
                     return False
             if (not Customer_contact.isdigit() or len(Customer_contact)!=10):
                        self.errorlabel2.setText("Enter valid Contact ")
                        return False
             return True
    def clearAll(self):
        self.customername_LE.setText("")
        self.contactnumber_LE.setText("")
        self.search_LE.setText("")
        self.quantity_LE.setText("")
        self.currentProduct_lE.setText("")
        self.errorlabel1.setText("")
        self.errorlabel2.setText("")
        #use flag to clear table after generating and incrementing bill number otherwise delete from db as well
        #self.carttable.clear()

    def selectedProduct(self):
        currentRow = self.producttable.currentRow()
        prod = self.producttable.item(currentRow,1)
        try:
                self.currentProduct_lE.setText(prod.text())
                self.errorlabel1.setText("")
        except Exception:
                pass
        
        

    def removeProduct(self):
        currRow = self.carttable.currentRow()
        item = self.carttable.item(currRow,0)
        try:
                selectedProduct = item.text()
                connection = sqlite3.connect("db.db") 
                connection.execute("DELETE FROM bill WHERE name = ?",[selectedProduct])
                connection.commit() 
                self.loadBillData() 
        except Exception as e:
                print(e)
               

    def insertIntoCart(self):
        global scannedbarcode_id
        global currRow
        connection = sqlite3.connect("db.db")
        
        try:
                currRow = self.producttable.currentRow()
                #print(currRow)
                item = self.producttable.item(currRow,0)
                #print(item)
                if item!= None:
                        scannedbarcode_id = item.text()
                        self.producttable.setCurrentCell(-1,-1)

                result = connection.execute("""SELECT * FROM product WHERE product_id = ?""",(scannedbarcode_id,))
                #print(scannedbarcode_id)
                resultlist = list(result.fetchall())
                name = resultlist[0][1]
                category = resultlist[0][2]
                quantity = self.quantity_LE.text()
                rate = resultlist[0][5]
                amount = int(quantity)*int(rate)
                connection.execute("""INSERT into bill VALUES (?,?,?,?,?,?)""",(current_bill,name,category,quantity,rate,amount))
                scannedbarcode_id = ""
                #print(scannedbarcode_id)
                self.currentProduct_lE.setText("")
                self.quantity_LE.setText("")
                connection.commit()
                self.producttable.setCurrentCell(-1,-1)
                self.errorlabel1.setText("")
            
        except Exception as e:
                if item == None and scannedbarcode_id == "":
                        self.errorlabel1.setText("No Row Selected")
                elif self.quantity_LE.text() == "":
                        self.errorlabel1.setText("Please Enter Quantity")
                else:
                        self.errorlabel1.setText("Product Already In Cart")
                        self.producttable.setCurrentCell(-1,-1)
                print(e)
        connection.close()

    def setProductName(self):
        self.errorlabel1.setText("")
        global scannedbarcode_id
        connection = sqlite3.connect("db.db")
        result = connection.execute("""SELECT name from product WHERE product_id = ?""",(scannedbarcode_id,))
        result_list = list(result.fetchall())
        result1 = connection.execute("SELECT MAX(bill_id) from bill")
        
        result1_list = result1.fetchone()
        try:
                if(result1_list[0] == current_bill):
                        print("WOrking")
                        result2 = connection.execute("""SELECT name from bill WHERE name =? AND bill_id =?""",(result_list[0][0],current_bill,))
                        result2_list = list(result2.fetchall())
                        if result2_list[0][0] != result_list[0][0]:
                                self.currentProduct_lE.setText(result_list[0][0])
                                in_stock = connection.execute("""SELECT in_stock from  product WHERE product_id = ?""",(scannedbarcode_id,))
                                in_stock = in_stock.fetchone()
                                self.errorlabel1.setText(f"In Stock : {in_stock[0]}")
                        else:
                                self.errorlabel1.setText("Product Already In Cart")
                                scannedbarcode_id = ""
                else:
                        result2 = connection.execute("""SELECT name from bill WHERE name =? AND bill_id =?""",(result_list[0][0],current_bill,))
                        result2_list = list(result2.fetchall())
                        self.currentProduct_lE.setText(result_list[0][0])
                        in_stock = connection.execute("""SELECT in_stock from  product WHERE product_id = ?""",(scannedbarcode_id,))
                        in_stock = in_stock.fetchone()
                        self.errorlabel1.setText(f"In Stock : {in_stock[0]}")
        except:
                result2 = connection.execute("""SELECT name from bill WHERE name =? AND bill_id =?""",(result_list[0][0],current_bill,))
                result2_list = list(result2.fetchall())
                self.currentProduct_lE.setText(result_list[0][0])
                in_stock = connection.execute("""SELECT in_stock from  product WHERE product_id = ?""",(scannedbarcode_id,))
                in_stock = in_stock.fetchone()
                self.errorlabel1.setText(f"In Stock : {in_stock[0]}")
        connection.close()
                
    def filter_table(self,result): #can try with sql query too
        items = self.producttable.findItems(result, QtCore.Qt.MatchContains)
        if items:
                item = items[0]
                self.producttable.setCurrentItem(item)
        else:
                self.producttable.setCurrentItem(None)
                self.producttable.selectRow(-1)

    def loadData(self):
        connection = sqlite3.connect("db.db")
        sqlquery = "SELECT product_id,name,category,in_stock,mrp FROM product WHERE in_stock > 0"
        last_bill = "SELECT MAX(bill_id) from bill"
        result_lastbill = connection.execute(last_bill)
        final_result = list(result_lastbill.fetchall())
        #print(final_result[0][0])
        global current_bill
        current_bill = int(final_result[0][0]) + 1
        #print(current_bill)
        if current_bill<10:
                current_bill = '0' + str(current_bill)
        self.billno_LE.setText(str(current_bill))
        self.billno_LE.setDisabled(True)


        result = connection.execute(sqlquery)
        self.producttable.setRowCount(0)
        x=0
        for row_number,row_data in enumerate(result):
                self.producttable.insertRow(row_number)  
                for x,data in enumerate(row_data):
                        self.producttable.setItem(row_number, x, QtWidgets.QTableWidgetItem(str(data)))
                        x+=1
        
        connection.close()

    def loadBillData(self):
        val = current_bill
        connection = sqlite3.connect("db.db") 

        try:
                result = connection.execute("""SELECT name,category,quantity,rate,amount FROM bill WHERE bill_id=?""",(val,))
                self.carttable.setRowCount(0)
                x=0
                for row_number,row_data in enumerate(result):
                        self.carttable.insertRow(row_number)  
                        for x,data in enumerate(row_data):
                                self.carttable.setItem(row_number, x, QtWidgets.QTableWidgetItem(str(data)))
                                x+=1
        except Exception as e:
                print(e)
        connection.close()
        

    def read_barcodes(self,frame):
        barcodes = pyzbar.decode(frame)
        for barcode in barcodes:
                x, y , w, h = barcode.rect
                barcode_info = barcode.data.decode('utf-8')
                cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 255, 0), 2)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, barcode_info, (x + 6, y - 6), font, 2.0, (255, 255, 255), 1)
                global scannedbarcode_id 
                #print(barcode_info)
                scannedbarcode_id = barcode_info
        return frame

    def showTime(self):
        global Flag
        try:
                while Flag:
                        QtWidgets.QApplication.processEvents()
                        #currTime = QtCore.QTime.currentTime()
                        now = datetime.datetime.now()
                        self.day.setText(now.strftime("%A"))
                        self.time.setText(now.strftime("%I:%M:%S %p"))
                        self.selectedProduct()
                        #self.time.setText(currTime.toString('hh:mm:ss'))
        except Exception as e:
                print(e)


    def post_emp_login(self):
        global Flag 
        Flag = False                                                     
        self.window1 = QtWidgets.QMainWindow()
        self.ui = post_emp_login.Ui_Form()
        self.ui.setupUi(self.window1)   
        self.window1.show()


    def setupUi(self, ManageEmpWindow):
        ManageEmpWindow.setObjectName("ManageEmpWindow")
        ManageEmpWindow.setGeometry(70,90,1885, 949)
        #ManageEmpWindow.resize(1885, 949)
        ManageEmpWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)            
        ManageEmpWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        ManageEmpWindow.setStyleSheet("QPushButton{\n"
"background-color:rgba(85,98,112,255);\n"
"color:rgba(255,255,255,200);\n"
"border-radius:25px;\n"
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
        self.label.setGeometry(QtCore.QRect(60, 10, 1711, 871))
        self.label.setStyleSheet("background-color:rgba(255,255,255,255);\n"
"border-bottom-right-radius:75px;\n"
"border-top-left-radius:75px;\n"
"border-top-right-radius:10px;\n"
"border:6px solid rgba(46,82,101,200);\n"
"\n"
"\n"
"\n"
"\n"
"\n"
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
        self.back_btn = QtWidgets.QPushButton(ManageEmpWindow)
        self.back_btn.setGeometry(QtCore.QRect(1710, 10, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.back_btn.setFont(font)
        self.back_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.back_btn.setStyleSheet("image: url(:/images/back2.png);\n"
"border-radius:5px;")
        self.back_btn.setText("")
        self.back_btn.setObjectName("back_btn")
        self.label_3 = QtWidgets.QLabel(ManageEmpWindow)
        self.label_3.setGeometry(QtCore.QRect(780, 10, 361, 100))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(31)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:rgba(0,0,0,200);\n"
"")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(ManageEmpWindow)
        self.label_4.setGeometry(QtCore.QRect(70, 30, 71, 51))
        self.label_4.setStyleSheet("image: url(:/images/profile.png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.currentEmp_LE = QtWidgets.QLabel(ManageEmpWindow)
        self.currentEmp_LE.setGeometry(QtCore.QRect(130, 40, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.currentEmp_LE.setFont(font)
        self.currentEmp_LE.setAutoFillBackground(False)
        self.currentEmp_LE.setStyleSheet("color:black;")
        self.currentEmp_LE.setText(second.currentEmpName)
        self.currentEmp_LE.setObjectName("currentEmp_LE")
        self.label_6 = QtWidgets.QLabel(ManageEmpWindow)
        self.label_6.setGeometry(QtCore.QRect(80, 130, 1671, 81))
        self.label_6.setStyleSheet("")
        self.label_6.setFrameShape(QtWidgets.QFrame.Box)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(ManageEmpWindow)
        self.label_5.setGeometry(QtCore.QRect(120, 150, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:rgba(0,0,0,200);\n"
"")
        self.label_5.setObjectName("label_5")
        self.billno_LE = QtWidgets.QLineEdit(ManageEmpWindow)
        self.billno_LE.setGeometry(QtCore.QRect(290, 160, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.billno_LE.setFont(font)
        self.billno_LE.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"")
        self.billno_LE.setText("")
        self.billno_LE.setObjectName("billno_LE")
        self.label_7 = QtWidgets.QLabel(ManageEmpWindow)
        self.label_7.setGeometry(QtCore.QRect(640, 150, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:rgba(0,0,0,200);\n"
"")
        self.label_7.setObjectName("label_7")
        self.customername_LE = QtWidgets.QLineEdit(ManageEmpWindow)
        self.customername_LE.setGeometry(QtCore.QRect(860, 160, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.customername_LE.setFont(font)
        self.customername_LE.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"")
        self.customername_LE.setObjectName("customername_LE")
        self.label_8 = QtWidgets.QLabel(ManageEmpWindow)
        self.label_8.setGeometry(QtCore.QRect(1200, 149, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:rgba(0,0,0,200);\n"
"")
        self.label_8.setObjectName("label_8")
        self.contactnumber_LE = QtWidgets.QLineEdit(ManageEmpWindow)
        self.contactnumber_LE.setGeometry(QtCore.QRect(1420, 160, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.contactnumber_LE.setFont(font)
        self.contactnumber_LE.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"")
        self.contactnumber_LE.setObjectName("contactnumber_LE")
        self.label_9 = QtWidgets.QLabel(ManageEmpWindow)
        self.label_9.setGeometry(QtCore.QRect(80, 220, 801, 621))
        self.label_9.setStyleSheet("")
        self.label_9.setFrameShape(QtWidgets.QFrame.Box)
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(ManageEmpWindow)
        self.label_10.setGeometry(QtCore.QRect(890, 220, 861, 621))
        self.label_10.setStyleSheet("")
        self.label_10.setFrameShape(QtWidgets.QFrame.Box)
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.search_LE = QtWidgets.QLineEdit(ManageEmpWindow)
        self.search_LE.setGeometry(QtCore.QRect(120, 240, 281, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.search_LE.setFont(font)
        self.search_LE.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"padding-bottom: -10px;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:black;\n"
"\n"
"")
        self.search_LE.setText("")
        self.search_LE.setObjectName("search_LE")
        self.producttable = QtWidgets.QTableWidget(ManageEmpWindow)
        self.producttable.setGeometry(QtCore.QRect(110, 310, 751, 361))
        self.producttable.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.producttable.setStyleSheet("border: 1px solid black;\n"
"\n"
"\n"
"")
        self.producttable.setFrameShape(QtWidgets.QFrame.Box)
        self.producttable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.producttable.setAlternatingRowColors(False)
        self.producttable.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.producttable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.producttable.setGridStyle(QtCore.Qt.SolidLine)
        self.producttable.setObjectName("producttable")
        self.producttable.setColumnCount(5)
        self.producttable.setRowCount(0)
        self.producttable.verticalHeader().setVisible(False)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        item.setFont(font)
        self.producttable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        item.setFont(font)
        self.producttable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        item.setFont(font)
        self.producttable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        item.setFont(font)
        self.producttable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        item.setFont(font)
        self.producttable.setHorizontalHeaderItem(4, item)
        self.barcode_btn = QtWidgets.QPushButton(ManageEmpWindow)
        self.barcode_btn.setGeometry(QtCore.QRect(770, 250, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.barcode_btn.setFont(font)
        self.barcode_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.barcode_btn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.barcode_btn.setStyleSheet("text-align: left;\n"
"image: url(:/images/bar_code.png);\n"
"")
        self.barcode_btn.setText("")
        self.barcode_btn.setObjectName("barcode_btn")
        self.label_11 = QtWidgets.QLabel(ManageEmpWindow)
        self.label_11.setGeometry(QtCore.QRect(600, 240, 161, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color:rgba(0,0,0,200);\n"
"")
        self.label_11.setObjectName("label_11")
        self.addtocart_btn = QtWidgets.QPushButton(ManageEmpWindow)
        self.addtocart_btn.setGeometry(QtCore.QRect(640, 760, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.addtocart_btn.setFont(font)
        self.addtocart_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addtocart_btn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.addtocart_btn.setStyleSheet("")
        self.addtocart_btn.setObjectName("addtocart_btn")
        self.clear_btn = QtWidgets.QPushButton(ManageEmpWindow)
        self.clear_btn.setGeometry(QtCore.QRect(120, 760, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.clear_btn.setFont(font)
        self.clear_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clear_btn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.clear_btn.setStyleSheet("")
        self.clear_btn.setObjectName("clear_btn")
        self.carttable = QtWidgets.QTableWidget(ManageEmpWindow)
        self.carttable.setGeometry(QtCore.QRect(920, 250, 801, 491))
        self.carttable.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.carttable.setStyleSheet("border: 1px solid black;\n"
"\n"
"\n"
"")
        self.carttable.setFrameShape(QtWidgets.QFrame.Box)
        self.carttable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.carttable.setAlternatingRowColors(False)
        self.carttable.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.carttable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.carttable.setShowGrid(False)
        self.carttable.setGridStyle(QtCore.Qt.SolidLine)
        self.carttable.setObjectName("carttable")
        self.carttable.setColumnCount(5)
        self.carttable.setRowCount(0)
        self.carttable.verticalHeader().setVisible(False)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        item.setFont(font)
        self.carttable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        item.setFont(font)
        self.carttable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        item.setFont(font)
        self.carttable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        item.setFont(font)
        self.carttable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        item.setFont(font)
        self.carttable.setHorizontalHeaderItem(4, item)
        self.carttable.verticalHeader().setVisible(False)
        self.remove_btn = QtWidgets.QPushButton(ManageEmpWindow)
        self.remove_btn.setGeometry(QtCore.QRect(950, 760, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.remove_btn.setFont(font)
        self.remove_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.remove_btn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.remove_btn.setStyleSheet("")
        self.remove_btn.setObjectName("remove_btn")
        self.generatebill_btn = QtWidgets.QPushButton(ManageEmpWindow)
        self.generatebill_btn.setGeometry(QtCore.QRect(1490, 760, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.generatebill_btn.setFont(font)
        self.generatebill_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.generatebill_btn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.generatebill_btn.setStyleSheet("")
        self.generatebill_btn.setObjectName("generatebill_btn")
        self.errorlabel1 = QtWidgets.QLabel(ManageEmpWindow)
        self.errorlabel1.setGeometry(QtCore.QRect(340, 760, 281, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.errorlabel1.setFont(font)
        self.errorlabel1.setStyleSheet("color: #6B6B6B;")
        self.errorlabel1.setText("")
        self.errorlabel1.setAlignment(QtCore.Qt.AlignCenter)
        self.errorlabel1.setWordWrap(False)
        self.errorlabel1.setObjectName("errorlabel1")
        self.errorlabel2 = QtWidgets.QLabel(ManageEmpWindow)
        self.errorlabel2.setGeometry(QtCore.QRect(1160, 760, 321, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.errorlabel2.setFont(font)
        self.errorlabel2.setStyleSheet("color: #6B6B6B;")
        self.errorlabel2.setText("")
        self.errorlabel2.setAlignment(QtCore.Qt.AlignCenter)
        self.errorlabel2.setWordWrap(False)
        self.errorlabel2.setObjectName("errorlabel2")
        self.day = QtWidgets.QLabel(ManageEmpWindow)
        self.day.setGeometry(QtCore.QRect(1540, 10, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Kozuka Mincho Pro M")
        font.setPointSize(14)
        self.day.setFont(font)
        self.day.setText("")
        self.day.setObjectName("day")
        self.time = QtWidgets.QLabel(ManageEmpWindow)
        self.time.setGeometry(QtCore.QRect(1540, 40, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Kozuka Mincho Pro M")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.time.setFont(font)
        self.time.setText("")
        self.time.setObjectName("time")
        self.label_12 = QtWidgets.QLabel(ManageEmpWindow)
        self.label_12.setGeometry(QtCore.QRect(640, 680, 101, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color:rgba(0,0,0,200);\n"
"")
        self.label_12.setObjectName("label_12")
        self.quantity_LE = QtWidgets.QLineEdit(ManageEmpWindow)
        self.quantity_LE.setGeometry(QtCore.QRect(740, 696, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.quantity_LE.setFont(font)
        self.quantity_LE.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"")
        self.quantity_LE.setAlignment(QtCore.Qt.AlignCenter)
        self.quantity_LE.setObjectName("quantity_LE")
        self.currentProduct_lE = QtWidgets.QLineEdit(ManageEmpWindow)
        self.currentProduct_lE.setGeometry(QtCore.QRect(210, 700, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.currentProduct_lE.setFont(font)
        self.currentProduct_lE.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"color:rgba(0,0,0,240);\n"
"")
        self.currentProduct_lE.setObjectName("currentProduct_lE")
        self.label_13 = QtWidgets.QLabel(ManageEmpWindow)
        self.label_13.setGeometry(QtCore.QRect(120, 680, 91, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color:rgba(0,0,0,200);\n"
"")
        self.label_13.setObjectName("label_13")

        self.search_LE.textChanged.connect(self.filter_table)

        self.back_btn.clicked.connect(self.post_emp_login)
        self.back_btn.clicked.connect(ManageEmpWindow.close)
        self.barcode_btn.clicked.connect(self.passage)

        self.timer=QtCore.QTimer()
        self.timer.timeout.connect(self.showTime)
        self.timer.start(10)
        self.loadData()
        self.currentProduct_lE.setDisabled(True)
        self.addtocart_btn.clicked.connect(self.insertIntoCart)
        self.addtocart_btn.clicked.connect(self.loadBillData)
        self.remove_btn.clicked.connect(self.removeProduct)
        self.clear_btn.clicked.connect(self.clearAll)
        #self.generatebill_btn.clicked.connect(self.deductQuantity)
        self.generatebill_btn.clicked.connect(self.generateBill)


        self.label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25,xOffset=0,yOffset=0))
        self.label_3.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25,xOffset=0,yOffset=0))
        self.addtocart_btn.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25,xOffset=3,yOffset=3))
        self.clear_btn.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25,xOffset=3,yOffset=3))
        self.remove_btn.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25,xOffset=3,yOffset=3))
        self.generatebill_btn.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25,xOffset=3,yOffset=3))
        

        self.producttable.setColumnWidth(0,150)
        self.producttable.setColumnWidth(1,200)
        self.producttable.setColumnWidth(2,150)
        self.producttable.setColumnWidth(3,100)
        self.producttable.setColumnWidth(4,149)


        self.carttable.setColumnWidth(0,200)
        self.carttable.setColumnWidth(1,150)
        self.carttable.setColumnWidth(2,150)
        self.carttable.setColumnWidth(3,150)
        self.carttable.setColumnWidth(4,149)

        self.retranslateUi(ManageEmpWindow)
        QtCore.QMetaObject.connectSlotsByName(ManageEmpWindow)

    def retranslateUi(self, ManageEmpWindow):
        _translate = QtCore.QCoreApplication.translate
        ManageEmpWindow.setWindowTitle(_translate("ManageEmpWindow", "Form"))
        self.label_3.setText(_translate("ManageEmpWindow", "Billing System"))
        self.label_5.setText(_translate("ManageEmpWindow", "Bill Number"))
        self.label_7.setText(_translate("ManageEmpWindow", "Customer Name"))
        self.label_8.setText(_translate("ManageEmpWindow", "Contact Number"))
        self.search_LE.setPlaceholderText(_translate("ManageEmpWindow", "Search                       "))
        self.producttable.setSortingEnabled(True)
        item = self.producttable.horizontalHeaderItem(0)
        item.setText(_translate("ManageEmpWindow", "Product ID"))
        item = self.producttable.horizontalHeaderItem(1)
        item.setText(_translate("ManageEmpWindow", "Name"))
        item = self.producttable.horizontalHeaderItem(2)
        item.setText(_translate("ManageEmpWindow", "Category"))
        item = self.producttable.horizontalHeaderItem(3)
        item.setText(_translate("ManageEmpWindow", "In Stock"))
        item = self.producttable.horizontalHeaderItem(4)
        item.setText(_translate("ManageEmpWindow", "MRP"))
        self.label_11.setText(_translate("ManageEmpWindow", "Scan Barcode"))
        self.addtocart_btn.setText(_translate("ManageEmpWindow", "Add To Cart"))
        self.clear_btn.setText(_translate("ManageEmpWindow", "Clear"))
        self.carttable.setSortingEnabled(True)
        item = self.carttable.horizontalHeaderItem(0)
        item.setText(_translate("ManageEmpWindow", "Name"))
        item = self.carttable.horizontalHeaderItem(1)
        item.setText(_translate("ManageEmpWindow", "Category"))
        item = self.carttable.horizontalHeaderItem(2)
        item.setText(_translate("ManageEmpWindow", "Quantity"))
        item = self.carttable.horizontalHeaderItem(3)
        item.setText(_translate("ManageEmpWindow", "Rate"))
        item = self.carttable.horizontalHeaderItem(4)
        item.setText(_translate("ManageEmpWindow", "Amount"))
        self.remove_btn.setText(_translate("ManageEmpWindow", "Remove"))
        self.generatebill_btn.setText(_translate("ManageEmpWindow", "Generate Bill"))
        self.label_12.setText(_translate("ManageEmpWindow", "Quantity:"))
        self.label_13.setText(_translate("ManageEmpWindow", "Product:"))
        global check
        check = True
        if(check):
                global x
                x = ManageEmpWindow
                check = False

    def passage(self):
            self.startScan(x)
            self.producttable.setCurrentCell(-1,-1)


    def startScan(self,x):
        global scannedbarcode_id
        scannedbarcode_id = ""
        self.errorlabel1.setText("")
        camera = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        ret, frame = camera.read()
        while ret:
                ret, frame = camera.read()
                frame = self.read_barcodes(frame)
                cv2.imshow('Barcode scanner', frame)
                if scannedbarcode_id!= "": 
                        self.setProductName()
                        break
                elif cv2.waitKey(1) & 0xFF == 27 :
                        break
        
        #scannedbarcode_id = ""
        camera.release()
        cv2.destroyAllWindows()
        #x.close()


if __name__ == "__main__":                                   
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_ManageBilllWindow()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
 