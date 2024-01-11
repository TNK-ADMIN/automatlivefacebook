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
        MainWindow.resize(606, 422)
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
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.view_accounts = QtWidgets.QTableWidget(self.tab)
        self.view_accounts.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.view_accounts.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.view_accounts.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.view_accounts.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.EditKeyPressed|QtWidgets.QAbstractItemView.SelectedClicked)
        self.view_accounts.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.view_accounts.setWordWrap(False)
        self.view_accounts.setObjectName("view_accounts")
        self.view_accounts.setColumnCount(2)
        self.view_accounts.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.view_accounts.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.view_accounts.setHorizontalHeaderItem(1, item)
        self.view_accounts.horizontalHeader().setStretchLastSection(True)
        self.view_accounts.verticalHeader().setVisible(False)
        self.gridLayout_6.addWidget(self.view_accounts, 1, 0, 1, 1)
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
        self.start_btn = QtWidgets.QPushButton(self.frame)
        self.start_btn.setObjectName("start_btn")
        self.gridLayout_2.addWidget(self.start_btn, 1, 0, 1, 1)
        self.add_btn = QtWidgets.QPushButton(self.frame)
        self.add_btn.setObjectName("add_btn")
        self.gridLayout_2.addWidget(self.add_btn, 1, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.uidlive = QtWidgets.QLineEdit(self.frame)
        self.uidlive.setPlaceholderText("")
        self.uidlive.setObjectName("uidlive")
        self.horizontalLayout.addWidget(self.uidlive)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        self.horizontalLayout_2.addWidget(self.frame)
        self.frame1 = QtWidgets.QFrame(self.tab)
        self.frame1.setMinimumSize(QtCore.QSize(150, 0))
        self.frame1.setObjectName("frame1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_4_success = QtWidgets.QLabel(self.frame1)
        self.label_4_success.setObjectName("label_4_success")
        self.gridLayout_3.addWidget(self.label_4_success, 2, 1, 1, 1)
        self.label_5_fail = QtWidgets.QLabel(self.frame1)
        self.label_5_fail.setObjectName("label_5_fail")
        self.gridLayout_3.addWidget(self.label_5_fail, 3, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame1)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame1)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 3, 0, 1, 1)
        self.time_count = QtWidgets.QSpinBox(self.frame1)
        self.time_count.setMaximum(999999999)
        self.time_count.setObjectName("time_count")
        self.gridLayout_3.addWidget(self.time_count, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame1)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 1, 0, 1, 1)
        self.label_6_total = QtWidgets.QLabel(self.frame1)
        self.label_6_total.setObjectName("label_6_total")
        self.gridLayout_3.addWidget(self.label_6_total, 1, 1, 1, 1)
        self.horizontalLayout_2.addWidget(self.frame1)
        self.gridLayout_6.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Auto Mắt Live Facebook"))
        item = self.view_accounts.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "COOKIE"))
        item = self.view_accounts.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "STATUS"))
        self.start_btn.setText(_translate("MainWindow", "Start"))
        self.add_btn.setText(_translate("MainWindow", "Add Account"))
        self.label.setText(_translate("MainWindow", "ID:"))
        self.label_4_success.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#00ff00;\">0</span></p></body></html>"))
        self.label_5_fail.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#ff0000;\">0</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Time"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#00ff00;\">Success:</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#ff0000;\">Fail:</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Toltal</p></body></html>"))
        self.label_6_total.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">0</p></body></html>"))