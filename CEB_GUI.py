# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\python_dell\Chemical_Equation_Balancer\GUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import utils



class Ui_Form(object):
    def setupUi(self, Form):
        #form
        Form.setObjectName("Form")
        Form.resize(840, 380)


        #label
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 15, 200, 30))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")

        #label2
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 210, 100, 30))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        #plainTestEdit
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(20, 50, 800, 100))
        font = QtGui.QFont()
        font.setFamily("Adobe Caslon Pro Bold")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setObjectName("plainTextEdit")

        #plainTestEdit_2
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(20, 250, 800, 100))
        font = QtGui.QFont()
        font.setFamily("Adobe Caslon Pro Bold")
        font.setPointSize(11)
        self.plainTextEdit_2.setFont(font)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.plainTextEdit_2.textChanged.connect(self.copy_plaintext2)
        
        #pushButton
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(230, 170, 100, 40))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.pushButtonClick)

        #pushButton_2
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(440, 170, 100, 40))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.copy_plaintext2)

        #pushButton_3
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(640, 170, 100, 40))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.pushButtonClick_3)
        # self.pushButton_3.clicked.connect(self.pushButtonClick)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)




    def pushButtonClick(self):
        cheq = self.plainTextEdit.toPlainText()
        res = utils.balancer(cheq)
        self.plainTextEdit_2.setPlainText(res)
        # print(res)

    def copy_plaintext2(self):
        clipbd = QApplication.clipboard()
        clipbd.setText(self.plainTextEdit_2.toPlainText())

    def pushButtonClick_3(self):
        clipbd = QApplication.clipboard()
        self.plainTextEdit.setPlainText(clipbd.text())

        cheq = self.plainTextEdit.toPlainText()
        print(cheq)
        res = utils.balancer(cheq)
        self.plainTextEdit_2.setPlainText(res)

        # self.pushButtonClick()


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Chemical Equation Balancer - 1.0"))
        Form.setWindowIcon(QtGui.QIcon('57.ico'))

        self.label.setText(_translate("Form", "请输入化学方程式"))
        self.label_2.setText(_translate("Form", "配平结果"))
        self.plainTextEdit.setPlainText(_translate("Form", "KMnO4+H2SO4+FeSO4=Fe2(SO4)3+MnSO4+K2SO4+H2O"))
        self.plainTextEdit_2.setPlainText(_translate("Form", ""))
        self.pushButton.setText(_translate("Form", "配 平"))
        self.pushButton_2.setText(_translate("Form", "复 制"))
        self.pushButton_3.setText(_translate("Form", "粘 贴"))


from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication
if __name__ == "__main__":
    import sys

    app=QApplication(sys.argv)
    widget=QWidget()
    form=Ui_Form()
    form.setupUi(widget)
    widget.show()
    app.exec_()
