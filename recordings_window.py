# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'recordings_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(558, 300)
        Form.setStyleSheet("")
        self.recordings_table = QtWidgets.QTableWidget(Form)
        self.recordings_table.setGeometry(QtCore.QRect(10, 10, 331, 281))
        self.recordings_table.setStyleSheet("color: black;\n"
"background-color: white;")
        self.recordings_table.setObjectName("recordings_table")
        self.recordings_table.setColumnCount(0)
        self.recordings_table.setRowCount(0)
        self.username_label = QtWidgets.QLabel(Form)
        self.username_label.setGeometry(QtCore.QRect(350, 10, 201, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.username_label.setFont(font)
        self.username_label.setStyleSheet("")
        self.username_label.setAlignment(QtCore.Qt.AlignCenter)
        self.username_label.setWordWrap(True)
        self.username_label.setObjectName("username_label")
        self.delete_btn = QtWidgets.QPushButton(Form)
        self.delete_btn.setGeometry(QtCore.QRect(350, 110, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.delete_btn.setFont(font)
        self.delete_btn.setStyleSheet("")
        self.delete_btn.setObjectName("delete_btn")
        self.convert_btn = QtWidgets.QPushButton(Form)
        self.convert_btn.setGeometry(QtCore.QRect(350, 170, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.convert_btn.setFont(font)
        self.convert_btn.setObjectName("convert_btn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Просмотр записей"))
        self.username_label.setText(_translate("Form", "Пользователь"))
        self.delete_btn.setText(_translate("Form", "Удалить запись"))
        self.convert_btn.setText(_translate("Form", "Конвертировать в csv"))
