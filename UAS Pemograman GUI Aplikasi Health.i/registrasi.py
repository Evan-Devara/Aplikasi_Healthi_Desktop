# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tubes3.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel
import mysql.connector as mc

class windowSukses(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Sukses')
        self.setFixedWidth(200)
        self.setStyleSheet("""
            
            QLabel{
                font-size: 20px
            }
            """)
        mainLayout = QVBoxLayout()
        self.Registrasi = Ui_Registrasi()
        
        self.nama = QLabel()
        self.ok = QPushButton('OK')
        mainLayout.addWidget(self.nama)
        mainLayout.addWidget(self.ok)
        self.nama.setText('Registrasi Berhasil')
        self.ok.clicked.connect(self.close)
        mainLayout.addWidget(self.ok)

        self.setLayout(mainLayout)

    def displayInfo(self):
        self.show()

class Ui_Registrasi(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(900, 747)
        self.windowOke = windowSukses()
        Dialog.setStyleSheet("*{\n"
"    font-family:SF UI Text;\n"
"    font-size:20px;\n"
"    color:#3575FE;\n"
"}\n"
"QFrame\n"
"{\n"
"    background:#F4F5F7;\n"
"}\n"
"QPushButton\n"
"{\n"
"    background:#FFFFFF;\n"
"    border-radius:10px;\n"
"}\n"
"QToolButton\n"
"{\n"
"    background:#3575FE;\n"
"    border-radius:60px;\n"
"}\n"
"QPushButton\n"
"{\n"
"    color:#3575FE;\n"
"}")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 901, 861))
        self.frame.setStyleSheet("QFrame\n"
"{\n"
"    background:#333;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(60, 0, 841, 51))
        self.frame_2.setStyleSheet("QFrame\n"
"{\n"
"    background:#FFFFFF;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(20, 10, 111, 31))
        self.label.setStyleSheet("*{\n"
"    font-family:aharoni;\n"
"    font-size:24px;\n"
"}")
        self.label.setObjectName("label")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 61, 51))
        self.frame_3.setStyleSheet("QFrame\n"
"{\n"
"    background:#3575FE;\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.toolButton = QtWidgets.QToolButton(self.frame_3)
        self.toolButton.setGeometry(QtCore.QRect(10, 0, 41, 51))
        self.toolButton.setStyleSheet("QToolButton\n"
"{\n"
"    \n"
"    image: url(:/images/logo.png);\n"
"    background:#3575FE;\n"
"    border-radius:60px;\n"
"}")
        self.toolButton.setText("")
        self.toolButton.setObjectName("toolButton")
        self.toolButton_3 = QtWidgets.QToolButton(self.frame)
        self.toolButton_3.setGeometry(QtCore.QRect(390, 100, 121, 121))
        self.toolButton_3.setStyleSheet("QToolButton\n"
"{\n"
"    background:#FFFFFF;\n"
"    border-radius:60px;\n"
"}\n"
"*\n"
"{\n"
"    font-family:SF UI Text bold;\n"
"    font-size:29px;\n"
"    color:#3575FE;\n"
"}")
        self.toolButton_3.setObjectName("toolButton_3")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setGeometry(QtCore.QRect(150, 170, 601, 471))
        self.frame_4.setStyleSheet("QFrame\n"
"{\n"
"    background:#3575FE;\n"
"    border-radius:10px;\n"
"}\n"
"")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        self.label_4.setGeometry(QtCore.QRect(60, 180, 131, 41))
        font = QtGui.QFont()
        font.setFamily("SF UI 57 12")
        font.setPointSize(-1)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("*\n"
"{\n"
"    font-family:SF UI Text Bold;\n"
"    font-size:16px;\n"
"    color:#FFFFFF;\n"
"}")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame_4)
        self.label_5.setGeometry(QtCore.QRect(60, 220, 141, 41))
        font = QtGui.QFont()
        font.setFamily("SF UI 57 12")
        font.setPointSize(-1)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("*\n"
"{\n"
"    font-family:SF UI Text Bold;\n"
"    font-size:16px;\n"
"    color:#FFFFFF;\n"
"}")
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setGeometry(QtCore.QRect(60, 140, 131, 41))
        font = QtGui.QFont()
        font.setFamily("SF UI 57 reguler")
        font.setPointSize(-1)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("*\n"
"{\n"
"    font-family:SF UI Text reguler;\n"
"    font-size:16px;\n"
"    color:#FFFFFF;\n"
"    background:transparent;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.label_13 = QtWidgets.QLabel(self.frame_4)
        self.label_13.setGeometry(QtCore.QRect(60, 300, 141, 31))
        font = QtGui.QFont()
        font.setFamily("SF UI 57 12")
        font.setPointSize(-1)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("*\n"
"{\n"
"    font-family:SF UI Text Bold;\n"
"    font-size:16px;\n"
"    color:#FFFFFF;\n"
"}")
        self.label_13.setObjectName("label_13")

        self.label2 = QtWidgets.QLabel(self.frame_4)
        self.label2.setGeometry(QtCore.QRect(60, 260, 141, 31))
        font = QtGui.QFont()
        font.setFamily("SF UI 57 12")
        font.setPointSize(-1)
        self.label2.setFont(font)
        self.label2.setStyleSheet("*\n"
"{\n"
"    font-family:SF UI Text Bold;\n"
"    font-size:16px;\n"
"    color:#FFFFFF;\n"
"}")
        self.label2.setObjectName("label2")

        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_3.setGeometry(QtCore.QRect(210, 230, 330, 22))
        self.lineEdit_3.setStyleSheet("*{\n"
"    font-family:SF UI Text;\n"
"    font-size:14px;\n"
"    color:#333;\n"
"}")
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.frame_4)
        self.dateTimeEdit.setGeometry(QtCore.QRect(210, 270, 330, 22))
        self.dateTimeEdit.setStyleSheet("*{\n"
"    font-family:SF UI Text;\n"
"    font-size:14px;\n"
"    color:#333;\n"
"}")
        self.dateTimeEdit.setObjectName("dateTimeEdit")

        self.lineEdit = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit.setGeometry(QtCore.QRect(210, 150, 331, 22))
        font = QtGui.QFont()
        font.setFamily("SF UI 57")
        font.setPointSize(-1)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("*{\n"
"    font-family:SF UI Text;\n"
"    font-size:14px;\n"
"    color:#333;\n"
"}")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_6.setGeometry(QtCore.QRect(210, 310, 330, 71))
        self.lineEdit_6.setStyleSheet("*{\n"
"    font-family:SF UI Text;\n"
"    font-size:14px;\n"
"    color:#333;\n"
"}")
        self.lineEdit_6.setInputMask("")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setFrame(True)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_14 = QtWidgets.QLabel(self.frame_4)
        self.label_14.setGeometry(QtCore.QRect(160, 60, 291, 31))
        font = QtGui.QFont()
        font.setFamily("SF UI 57 reguler")
        font.setPointSize(-1)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("*\n"
"{\n"
"    font-family:SF UI Text reguler;\n"
"    font-size:18px;\n"
"    color:#FFFFFF;\n"
"    background:transparent;\n"
"}")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.frame_4)
        self.label_15.setGeometry(QtCore.QRect(260, 100, 101, 21))
        font = QtGui.QFont()
        font.setFamily("SF UI 57 reguler")
        font.setPointSize(-1)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("*\n"
"{\n"
"    font-family:SF UI Text reguler;\n"
"    font-size:18px;\n"
"    color:#FFFFFF;\n"
"    background:transparent;\n"
"}")
        self.label_15.setObjectName("label_15")
        self.dateEdit = QtWidgets.QDateEdit(self.frame_4)
        self.dateEdit.setGeometry(QtCore.QRect(210, 190, 331, 22))
        self.dateEdit.setStyleSheet("*{\n"
"    font-family:SF UI Text;\n"
"    font-size:14px;\n"
"    color:#333;\n"
"}")
        self.dateEdit.setObjectName("dateEdit")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(350, 670, 211, 49))
        font = QtGui.QFont()
        font.setFamily("SF UI 57")
        font.setPointSize(-1)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton:hover\n"
"{\n"
"    color:#FFFFFF;\n"
"    border-radius:10px;\n"
"    background:#7CA5FF;\n"
"}\n"
"*{\n"
"    font-size:18px;\n"
"}\n"
"QPushButton\n"
"{\n"
"    color:#FFFFFF;\n"
"    background:#3575FE;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.simpanData)
        self.frame_4.raise_()
        self.frame_2.raise_()
        self.frame_3.raise_()
        self.toolButton_3.raise_()
        self.pushButton_3.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Health.i"))
        self.toolButton_3.setText(_translate("Dialog", "Regist"))
        self.label_4.setText(_translate("Dialog", "Tanggal Lahir"))
        self.label2.setText(_translate("Dialog", "Waktu Berobat"))
        self.label_5.setText(_translate("Dialog", "Alamat"))
        self.label_2.setText(_translate("Dialog", "Nama Lengkap"))
        self.label_13.setText(_translate("Dialog", "Keluhan"))
        self.label_14.setText(_translate("Dialog", "Inputkan data registrasi dengan baik"))
        self.label_15.setText(_translate("Dialog", "dan benar"))
        self.pushButton_3.setText(_translate("Dialog", "Daftar"))

    def simpanData(self):
        try:
                nama = self.lineEdit.text()
                tgl_lahir = self.dateEdit.text()
                alamat = self.lineEdit_3.text()
                waktu_berobat = self.dateTimeEdit.text()
                keluhan = self.lineEdit_6.text()
                mydb = mc.connect(
                        host="localhost",
                        user="root",
                        password="",
                        database="rumah_sakit"

                    )

                mycursor = mydb.cursor()
                query = "INSERT INTO pasien (nama,tgl_lahir,alamat,waktu_berobat,keluhan) VALUES (%s,%s,%s,%s,%s)"
                value = (nama,tgl_lahir,alamat,waktu_berobat,keluhan)
                mycursor.execute(query,value)
                mydb.commit()
                print(nama,tgl_lahir,alamat,waktu_berobat,keluhan)
                
                self.windowOke.displayInfo()
        except mc.Error as e:
                print('gagal')



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Registrasi()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
