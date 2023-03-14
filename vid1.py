from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 800, 600))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.label.setPalette(palette)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("treebackground.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(333, 60, 170, 165))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../wolf-removebg-preview.png"))  
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_2.setGraphicsEffect(QtWidgets.QGraphicsOpacityEffect(opacity=0.8))
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(310, 250, 211, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setGraphicsEffect(QtWidgets.QGraphicsOpacityEffect(opacity=0.4))
        self.lineEdit.setStyleSheet("QLineEdit { color: red; border-radius: 15px; border: 5px solid lightblue; }")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(350, 257, 71, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(199, 199, 199))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(199, 199, 199))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.label_3.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(327, 258, 16, 16))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("usericon.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(310, 310, 211, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setGraphicsEffect(QtWidgets.QGraphicsOpacityEffect(opacity=0.4))
        self.lineEdit_2.setStyleSheet("QLineEdit { color: red; border-radius: 15px; border: 5px solid lightblue; }")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(350, 317, 61, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(327, 317, 16, 16))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("lock.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 370, 211, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setGraphicsEffect(QtWidgets.QGraphicsOpacityEffect(opacity=0.7))
        self.pushButton.setStyleSheet("QPushButton { border-radius: 18px; border: 2px solid darkorange; background-color: darkorange; }")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(310, 445, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_7.setGraphicsEffect(QtWidgets.QGraphicsOpacityEffect(opacity=0.8))
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(432, 448, 101, 16))
        self.label_8.setGraphicsEffect(QtWidgets.QGraphicsOpacityEffect(opacity=0.8))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(60, 560, 18, 18))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("face.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.label_9.setGraphicsEffect(QtWidgets.QGraphicsOpacityEffect(opacity=0.5))
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(90, 558, 23, 23))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("okinsta.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.label_10.setGraphicsEffect(QtWidgets.QGraphicsOpacityEffect(opacity=0.5))
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(120, 552, 35, 35))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("twitter.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.label_11.setGraphicsEffect(QtWidgets.QGraphicsOpacityEffect(opacity=0.5))
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(165, 560, 20, 20))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("Youtube.png"))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName("label_12")
        self.label_12.setGraphicsEffect(QtWidgets.QGraphicsOpacityEffect(opacity=0.5))
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(540, 559, 281, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_13.setGraphicsEffect(QtWidgets.QGraphicsOpacityEffect(opacity=0.5))
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(520, 561, 13, 13))
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap("copy.png"))
        self.label_14.setScaledContents(True)
        self.label_14.setObjectName("label_14")
        self.label_14.setGraphicsEffect(QtWidgets.QGraphicsOpacityEffect(opacity=0.5))
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(20, 8, 60, 55))
        self.label_15.setText("")
        self.label_15.setPixmap(QtGui.QPixmap("logwolf-modified.png"))
        self.label_15.setScaledContents(True)
        self.label_15.setObjectName("label_15")
        self.label_15.setGraphicsEffect(QtWidgets.QGraphicsOpacityEffect(opacity=0.7))
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(605, 24, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setGraphicsEffect(QtWidgets.QGraphicsOpacityEffect(opacity=0.7))
        self.pushButton_2.setStyleSheet("QPushButton { border-radius: 10px; border: 2px solid darkorange; background-color: darkorange; }")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(690, 24, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setGraphicsEffect(QtWidgets.QGraphicsOpacityEffect(opacity=0.7))
        self.pushButton_3.setStyleSheet("QPushButton { border-radius: 10px; border: 2px solid darkorange; background-color: darkorange; }")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Username"))
        self.label_5.setText(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWindow", "GET STARTED"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">FORGOT PASSWORD?</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">CREATE ACCOUNT</span></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">2023 All Rights Reserved | Design By RizyG</span></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Login"))
        self.pushButton_3.setText(_translate("MainWindow", "Register"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
