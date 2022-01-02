# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("""background-color: rgb(56, 56, 56);
        color: white;""")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 40, 751, 501))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.generated_text = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        self.generated_text.setFont(font)
        self.generated_text.setFocusPolicy(QtCore.Qt.NoFocus)
        self.generated_text.setStyleSheet("color: rgb(240, 223, 28);\n"
"border-color: rgb(255, 255, 255);\n"
"")
        self.generated_text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.generated_text.setWordWrap(True)
        self.generated_text.setObjectName("generated_text")
        self.verticalLayout.addWidget(self.generated_text)
        self.hint_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.hint_label.setMinimumSize(QtCore.QSize(0, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.hint_label.setFont(font)
        self.hint_label.setStyleSheet("color: rgb(161, 161, 161);")
        self.hint_label.setAlignment(QtCore.Qt.AlignCenter)
        self.hint_label.setObjectName("hint_label")
        self.verticalLayout.addWidget(self.hint_label)
        self.entered_text = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.entered_text.setFont(font)
        self.entered_text.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.entered_text.setStyleSheet("color: rgb(73, 220, 0);\n"
"border-color: rgb(255, 255, 0);")
        self.entered_text.setObjectName("entered_text")
        self.verticalLayout.addWidget(self.entered_text)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 3)
        self.stopwatch_label = QtWidgets.QLabel(self.centralwidget)
        self.stopwatch_label.setGeometry(QtCore.QRect(680, 0, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.stopwatch_label.setFont(font)
        self.stopwatch_label.setStyleSheet("color: rgb(240, 223, 28);")
        self.stopwatch_label.setAlignment(QtCore.Qt.AlignCenter)
        self.stopwatch_label.setObjectName("stopwatch_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setStyleSheet("color: white;\n"
"")
        self.menubar.setObjectName("menubar")
        self.settings_menu = QtWidgets.QMenu(self.menubar)
        self.settings_menu.setObjectName("settings_menu")
        self.theme_setting = QtWidgets.QMenu(self.settings_menu)
        self.theme_setting.setObjectName("theme_setting")
        self.difficulty_setting = QtWidgets.QMenu(self.settings_menu)
        self.difficulty_setting.setObjectName("difficulty_setting")
        self.user_setting = QtWidgets.QMenu(self.settings_menu)
        self.user_setting.setObjectName("user_setting")
        self.about_menu = QtWidgets.QMenu(self.menubar)
        self.about_menu.setObjectName("about_menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dark_theme = QtWidgets.QAction(MainWindow)
        self.dark_theme.setObjectName("dark_theme")
        self.light_theme = QtWidgets.QAction(MainWindow)
        self.light_theme.setObjectName("light_theme")
        self.easy_mode = QtWidgets.QAction(MainWindow)
        self.easy_mode.setObjectName("easy_mode")
        self.normal_mode = QtWidgets.QAction(MainWindow)
        self.normal_mode.setObjectName("normal_mode")
        self.hard_mode = QtWidgets.QAction(MainWindow)
        self.hard_mode.setObjectName("hard_mode")
        self.insane_mode = QtWidgets.QAction(MainWindow)
        self.insane_mode.setObjectName("insane_mode")
        self.register_user = QtWidgets.QAction(MainWindow)
        self.register_user.setObjectName("register_user")
        self.login_user = QtWidgets.QAction(MainWindow)
        self.login_user.setObjectName("login_user")
        self.theme_setting.addAction(self.dark_theme)
        self.theme_setting.addAction(self.light_theme)
        self.difficulty_setting.addAction(self.easy_mode)
        self.difficulty_setting.addAction(self.normal_mode)
        self.difficulty_setting.addAction(self.hard_mode)
        self.difficulty_setting.addAction(self.insane_mode)
        self.user_setting.addAction(self.register_user)
        self.user_setting.addAction(self.login_user)
        self.settings_menu.addAction(self.theme_setting.menuAction())
        self.settings_menu.addAction(self.difficulty_setting.menuAction())
        self.settings_menu.addAction(self.user_setting.menuAction())
        self.menubar.addAction(self.settings_menu.menuAction())
        self.menubar.addAction(self.about_menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.generated_text.setText(_translate("MainWindow", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequa"))
        self.hint_label.setText(_translate("MainWindow", "Нажмите Esc чтобы начать заново"))
        self.entered_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Calibri\'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequa</span></p></body></html>"))
        self.stopwatch_label.setText(_translate("MainWindow", "00:00"))
        self.settings_menu.setTitle(_translate("MainWindow", "Настройки"))
        self.theme_setting.setTitle(_translate("MainWindow", "Тема"))
        self.difficulty_setting.setTitle(_translate("MainWindow", "Сложность"))
        self.user_setting.setTitle(_translate("MainWindow", "Пользователь"))
        self.about_menu.setTitle(_translate("MainWindow", "О разработчиках"))
        self.dark_theme.setText(_translate("MainWindow", "Темная (по умолчанию)"))
        self.light_theme.setText(_translate("MainWindow", "Светлая"))
        self.easy_mode.setText(_translate("MainWindow", "Легкая"))
        self.normal_mode.setText(_translate("MainWindow", "Средняя"))
        self.hard_mode.setText(_translate("MainWindow", "Сложная"))
        self.insane_mode.setText(_translate("MainWindow", "Безумная (в планах)"))
        self.register_user.setText(_translate("MainWindow", "Регистрация"))
        self.login_user.setText(_translate("MainWindow", "Войти"))
