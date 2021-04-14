from PyQt5 import QtCore, QtGui, QtWidgets
import invManagement
import addemp_res
import sys
import sqlite3


class Ui_updateProduct_Window(object):

    def invManagement(self):                           
        self.window = QtWidgets.QMainWindow()
        self.ui = invManagement.Ui_InvManagement()
        self.ui.setupUi(self.window)
        self.window.show()

    def preloadData(self):
        connection = sqlite3.connect("db.db")
        result = connection.execute("""SELECT * FROM product WHERE product_id = ?""",(invManagement.selected_barcodeid,))
        emplist = list(result.fetchall())
        self.productId_LE.setText(emplist[0][0])
        self.name_LE.setText(emplist[0][1])
        self.category_LE.setText(emplist[0][2])
        self.inStock_LE.setText(str(emplist[0][3]))
        self.costPrice_LE.setText(str(emplist[0][4]))
        self.mrp_LE.setText(str(emplist[0][5]))
        self.description_LE.setText(emplist[0][6])
        connection.close()

    def setupUi(self, updateProduct_Window):
        updateProduct_Window.setObjectName("updateProduct_Window")
        updateProduct_Window.resize(1350, 833)
        updateProduct_Window.setWindowFlags(QtCore.Qt.FramelessWindowHint)            
        updateProduct_Window.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        updateProduct_Window.setStyleSheet("QPushButton{\n"
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
        self.label = QtWidgets.QLabel(updateProduct_Window)
        self.label.setGeometry(QtCore.QRect(130, 30, 1131, 771))
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setStyleSheet("background-color:rgba(255,255,255,255);\n"
"border-bottom-right-radius:50px;\n"
"border-top-left-radius:50px;\n"
"border-top-right-radius:5px;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(updateProduct_Window)
        self.label_2.setGeometry(QtCore.QRect(130, 30, 381, 771))
        self.label_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 98,112, 255), stop:1 rgba(255, 107, 107, 255));\n"
"border-top-left-radius:50px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(updateProduct_Window)
        self.label_3.setGeometry(QtCore.QRect(670, 50, 441, 81))
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
        self.productId_LE = QtWidgets.QLineEdit(updateProduct_Window)
        self.productId_LE.setGeometry(QtCore.QRect(560, 190, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.productId_LE.setFont(font)
        self.productId_LE.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.productId_LE.setText("")
        self.productId_LE.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.productId_LE.setObjectName("productId_LE")
        self.category_LE = QtWidgets.QLineEdit(updateProduct_Window)
        self.category_LE.setGeometry(QtCore.QRect(560, 290, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.category_LE.setFont(font)
        self.category_LE.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.category_LE.setText("")
        self.category_LE.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.category_LE.setObjectName("category_LE")
        self.submit_btn = QtWidgets.QPushButton(updateProduct_Window)
        self.submit_btn.setGeometry(QtCore.QRect(810, 600, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.submit_btn.setFont(font)
        self.submit_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.submit_btn.setMouseTracking(False)
        self.submit_btn.setTabletTracking(False)
        self.submit_btn.setStyleSheet("border-radius:15px;")
        self.submit_btn.setObjectName("submit_btn")
        self.label_4 = QtWidgets.QLabel(updateProduct_Window)
        self.label_4.setGeometry(QtCore.QRect(130, 400, 381, 541))
        font = QtGui.QFont()
        font.setFamily("Mountain")
        font.setPointSize(210)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgba(255,107,107,255);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.description_LE = QtWidgets.QLineEdit(updateProduct_Window)
        self.description_LE.setGeometry(QtCore.QRect(560, 490, 661, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.description_LE.setFont(font)
        self.description_LE.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.description_LE.setText("")
        self.description_LE.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.description_LE.setObjectName("description_LE")
        self.inStock_LE = QtWidgets.QLineEdit(updateProduct_Window)
        self.inStock_LE.setGeometry(QtCore.QRect(910, 290, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.inStock_LE.setFont(font)
        self.inStock_LE.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.inStock_LE.setText("")
        self.inStock_LE.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.inStock_LE.setObjectName("inStock_LE")
        self.name_LE = QtWidgets.QLineEdit(updateProduct_Window)
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
        self.mrp_LE = QtWidgets.QLineEdit(updateProduct_Window)
        self.mrp_LE.setGeometry(QtCore.QRect(910, 390, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.mrp_LE.setFont(font)
        self.mrp_LE.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.mrp_LE.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.mrp_LE.setObjectName("mrp_LE")
        self.costPrice_LE = QtWidgets.QLineEdit(updateProduct_Window)
        self.costPrice_LE.setGeometry(QtCore.QRect(560, 390, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.costPrice_LE.setFont(font)
        self.costPrice_LE.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.costPrice_LE.setText("")
        self.costPrice_LE.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.costPrice_LE.setObjectName("costPrice_LE")
        self.pushButton_2 = QtWidgets.QPushButton(updateProduct_Window)
        self.pushButton_2.setGeometry(QtCore.QRect(1200, 30, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("font-size:20px;\n"
"image: url(:/images/back2.png);\n"
"text-align: center;\n"
"border-radius:5px;")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_5 = QtWidgets.QLabel(updateProduct_Window)
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
        self.label_6 = QtWidgets.QLabel(updateProduct_Window)
        self.label_6.setGeometry(QtCore.QRect(670, 690, 91, 71))
        self.label_6.setStyleSheet("")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.submit_btn.clicked.connect(self.updateProduct)
        self.pushButton_2.clicked.connect(self.invManagement)
        self.pushButton_2.clicked.connect(updateProduct_Window.close)

        self.productId_LE.setEnabled(False)
        self.preloadData()
        self.retranslateUi(updateProduct_Window)
        QtCore.QMetaObject.connectSlotsByName(updateProduct_Window)

    def retranslateUi(self, updateProduct_Window):
        _translate = QtCore.QCoreApplication.translate
        updateProduct_Window.setWindowTitle(_translate("updateProduct_Window", "Form"))
        self.label.setText(_translate("updateProduct_Window", "TextLabel"))
        self.label_3.setText(_translate("updateProduct_Window", "UPDATE PRODUCT"))
        self.productId_LE.setPlaceholderText(_translate("updateProduct_Window", "Product ID"))
        self.category_LE.setPlaceholderText(_translate("updateProduct_Window", "Category"))
        self.submit_btn.setText(_translate("updateProduct_Window", "Submit"))
        self.label_4.setText(_translate("updateProduct_Window", "-"))
        self.description_LE.setPlaceholderText(_translate("updateProduct_Window", "Description (Optional)"))
        self.inStock_LE.setPlaceholderText(_translate("updateProduct_Window", "In Stock"))
        self.name_LE.setPlaceholderText(_translate("updateProduct_Window", "Name"))
        self.mrp_LE.setPlaceholderText(_translate("updateProduct_Window", "MRP"))
        self.costPrice_LE.setPlaceholderText(_translate("updateProduct_Window", "Cost Price"))
        global check
        check = True
        if(check):
                global x
                x = updateProduct_Window
                check = False
    
    def passage(self):
        self.updateProduct(x)
    
    def updateProduct(self, x):
        #product_id = self.productId_LE.text()
        name = self.name_LE.text()
        category = self.category_LE.text()
        stock = self.inStock_LE.text()
        cost_price = self.costPrice_LE.text()
        mrp = self.mrp_LE.text()
        description = self.description_LE.text()

        connection = sqlite3.connect("db.db")

        if (self.allFieldsValidation()):
                if any(chr.isdigit() for chr in name):
                        self.label_5.setGeometry(QtCore.QRect(690, 680, 421, 91))
                        self.label_5.setText("Enter valid Name")
                        self.label_6.setStyleSheet("")
                elif stock.isdigit() == False:
                        self.label_5.setGeometry(QtCore.QRect(690, 680, 421, 91))
                        self.label_5.setText("Enter valid Stock")
                        self.label_6.setStyleSheet("")
                
                elif cost_price.isdigit() == False:
                        self.label_5.setGeometry(QtCore.QRect(690, 680, 421, 91))
                        self.label_5.setText("Enter valid Cost Price")
                        self.label_6.setStyleSheet("")

                elif mrp.isdigit() == False:
                        self.label_5.setGeometry(QtCore.QRect(690, 680, 421, 91))
                        self.label_5.setText("Enter valid MRP")
                        self.label_6.setStyleSheet("")
                
                elif(description.isspace()):
                        self.label_5.setGeometry(QtCore.QRect(690, 680, 421, 91))
                        self.label_5.setText("Enter Valid Description")
                        self.label_6.setStyleSheet("")
                else:
                        connection.execute("""UPDATE product SET  name = ?, category = ?, in_stock = ?, cost_price = ?, mrp = ?, description =? WHERE product_id = ?""",(name,category,stock,cost_price,mrp,description,invManagement.selected_barcodeid))
                        connection.commit()
                        self.label_5.setGeometry(QtCore.QRect(690, 680, 421, 91))
                        self.label_5.setText("Update Successful")
                        self.label_6.setStyleSheet("image: url(:/img/success-icon-23194.png);")
                        connection.close()
    
    def allFieldsValidation(self):
        product_id = self.productId_LE.text()
        name = self.name_LE.text()
        category = self.category_LE.text()
        stock = self.inStock_LE.text()
        cost_price = self.costPrice_LE.text()
        mrp = self.mrp_LE.text()

        if ((product_id != "" and  product_id.isspace() == False) and (name != "" and  name.isspace() == False) and (cost_price != "" and  cost_price.isspace() == False) and (mrp != "" and  mrp.isspace() == False) and (category != "" and  category.isspace() == False) and (stock != "" and  stock.isspace() == False)):
                return True
        else:
                self.label_5.setGeometry(QtCore.QRect(690, 680, 421, 91))
                self.label_5.setText("All fields are required ")
                self.label_6.setStyleSheet("")
                return False
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    updateProduct_Window = QtWidgets.QWidget()
    ui = Ui_updateProduct_Window()
    ui.setupUi(updateProduct_Window)
    updateProduct_Window.show()
    sys.exit(app.exec_())
