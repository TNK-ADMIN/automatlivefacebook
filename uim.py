# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(610, 422)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.start_btn = PushButton(self.frame)
        self.start_btn.setObjectName("start_btn")
        self.gridLayout_2.addWidget(self.start_btn, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.BodyLabel_2 = BodyLabel(self.frame)
        self.BodyLabel_2.setObjectName("BodyLabel_2")
        self.horizontalLayout.addWidget(self.BodyLabel_2)
        self.uidlive = LineEdit(self.frame)
        self.uidlive.setObjectName("uidlive")
        self.horizontalLayout.addWidget(self.uidlive)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        self.add_btn = PushButton(self.frame)
        self.add_btn.setObjectName("add_btn")
        self.gridLayout_2.addWidget(self.add_btn, 2, 1, 1, 1)
        self.horizontalLayout_2.addWidget(self.frame)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.BodyLabel = BodyLabel(self.tab)
        self.BodyLabel.setObjectName("BodyLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.BodyLabel)
        self.time_count = SpinBox(self.tab)
        self.time_count.setMaximum(999999999)
        self.time_count.setObjectName("time_count")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.time_count)
        self.BodyLabel_3 = BodyLabel(self.tab)
        self.BodyLabel_3.setObjectName("BodyLabel_3")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.BodyLabel_3)
        self.thread_count = SpinBox(self.tab)
        self.thread_count.setMaximum(999999999)
        self.thread_count.setObjectName("thread_count")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.thread_count)
        self.BodyLabel_4 = BodyLabel(self.tab)
        self.BodyLabel_4.setObjectName("BodyLabel_4")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.BodyLabel_4)
        self.delay_count = SpinBox(self.tab)
        self.delay_count.setMaximum(999999999)
        self.delay_count.setObjectName("delay_count")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.delay_count)
        self.horizontalLayout_2.addLayout(self.formLayout_2)
        self.frame1 = QtWidgets.QFrame(self.tab)
        self.frame1.setMinimumSize(QtCore.QSize(150, 0))
        self.frame1.setObjectName("frame1")
        self.label_4_success = QtWidgets.QLabel(self.frame1)
        self.label_4_success.setGeometry(QtCore.QRect(68, 43, 81, 20))
        self.label_4_success.setObjectName("label_4_success")
        self.label_5_fail = QtWidgets.QLabel(self.frame1)
        self.label_5_fail.setGeometry(QtCore.QRect(68, 76, 81, 20))
        self.label_5_fail.setObjectName("label_5_fail")
        self.label_3 = QtWidgets.QLabel(self.frame1)
        self.label_3.setGeometry(QtCore.QRect(9, 43, 44, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame1)
        self.label_4.setGeometry(QtCore.QRect(9, 76, 21, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame1)
        self.label_5.setGeometry(QtCore.QRect(9, 9, 28, 16))
        self.label_5.setObjectName("label_5")
        self.label_6_total = QtWidgets.QLabel(self.frame1)
        self.label_6_total.setGeometry(QtCore.QRect(68, 9, 81, 20))
        self.label_6_total.setObjectName("label_6_total")
        self.horizontalLayout_2.addWidget(self.frame1)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.view_accounts = TableWidget(self.tab)
        self.view_accounts.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.view_accounts.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.view_accounts.setObjectName("view_accounts")
        self.view_accounts.setColumnCount(2)
        self.view_accounts.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.view_accounts.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.view_accounts.setHorizontalHeaderItem(1, item)
        self.view_accounts.horizontalHeader().setSortIndicatorShown(False)
        self.view_accounts.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_5.addWidget(self.view_accounts)
        self.tabWidget.addTab(self.tab, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Auto Mắt Live Facebook"))
        self.start_btn.setText(_translate("MainWindow", "Start"))
        self.BodyLabel_2.setText(_translate("MainWindow", "ID:"))
        self.add_btn.setText(_translate("MainWindow", "Add Account"))
        self.BodyLabel.setText(_translate("MainWindow", "Time"))
        self.BodyLabel_3.setText(_translate("MainWindow", "Thread"))
        self.BodyLabel_4.setText(_translate("MainWindow", "Delay"))
        self.label_4_success.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#00ff00;\">0</span></p></body></html>"))
        self.label_5_fail.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#ff0000;\">0</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#00ff00;\">Success:</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#ff0000;\">Fail:</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Toltal</p></body></html>"))
        self.label_6_total.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">0</p></body></html>"))
        item = self.view_accounts.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "COOKIE"))
        item = self.view_accounts.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "STATUS"))
from qfluentwidgets import BodyLabel, LineEdit, PushButton, SpinBox, TableWidget
