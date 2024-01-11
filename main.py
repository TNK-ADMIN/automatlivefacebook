import random, sys
from PyQt5.QtCore import QObject, Qt
from PyQt5.QtWidgets import QWidget
from uim import Ui_MainWindow
from apifb import FacebookMain
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QObject, Qt, QThread, pyqtSignal
import time
from PyQt5.QtWidgets import QMessageBox
class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.list_Thread = {}
        self.main = Ui_MainWindow()
        self.main.setupUi(self)
        #self.setFixedSize(self.size())
        self.main.add_btn.clicked.connect(self.openFile)
        self.main.start_btn.clicked.connect(self.let_start)
        self.success = 0
        self.fail_count = 0
    def showMessageBox(self, title, text):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(text)
        msg_box.setIcon(QMessageBox.Warning)
        font = msg_box.font()
        font.setPointSize(14)
        msg_box.setFont(font)
        msg_box.setStyleSheet("QMessageBox{min-width: 300px;}")
        
        msg_box.exec_()
    def Delay(self, s):
        loop = QtCore.QEventLoop()
        QtCore.QTimer.singleShot(int(s*1000), loop.quit)
        loop.exec_()
    def openFile(self):
        filename,_ = QFileDialog.getOpenFileName(self)
        if filename:
            self.loadData(filename)
    def addItem(self,row:int = 0,col:int = 2,text:str = ''):
        self.main.view_accounts.setItem(row,col,QTableWidgetItem(text))
    def loadData(self, filename):
        data = open(filename, 'r', encoding='utf-8').read().strip().splitlines()
        index = self.main.view_accounts.rowCount()

        for x in data:
            self.main.view_accounts.insertRow(index)
            parts = x.split("|")
            if len(parts) >= 2:
                self.addItem(index, 0, parts[1])
            else:
                if parts:
                    self.addItem(index, 0, parts[0])
                else:
                    self.addItem(index, 0, "")
            index += 1

        total_rows = len(data)
        self.main.label_6_total.setText(str(total_rows))


    def let_start(self):
        timetotal = self.main.time_count.value()
        uidlive = self.main.uidlive.text()
        index = self.main.view_accounts.rowCount()

        start_time = time.time()

        while True:
            elapsed_time = time.time() - start_time
            if elapsed_time >= timetotal * 60:
                print("Dừng")
                for x in range(0, int(index)):
                    self.addItem(x, 1, "Đã Dừng")
                self.showMessageBox("Thông Báo", f"Đã Hết {timetotal} Phút")
                break

            for x in range(0, int(index)):
                cookie = self.main.view_accounts.item(x, 0).text()
                self.list_Thread[x] = ThreadMAIN(uidlive, cookie, x)
                self.list_Thread[x].show.connect(self.addItem)
                self.list_Thread[x].result.connect(self.handleResult)
                self.list_Thread[x].start()
                self.Delay(1)
            self.Delay(20)

    def handleResult(self, result):
        if result:
            self.success += 1
            self.main.label_4_success.setText(str(self.success))
            self.main.label_4_success.setStyleSheet("color: green;")
        else:
            self.fail_count += 1
            self.main.label_5_fail.setText(str(self.fail_count))
            self.main.label_5_fail.setStyleSheet("color: red;")

class ThreadMAIN(QThread):
    show = pyqtSignal(int,int,str)
    result = pyqtSignal(bool)
    def __init__(self, uidlive, cookie, x) -> None:
        super().__init__()
        self.uidlive = uidlive
        self.cookie = cookie
        self.row = x
    def run(self):
        fb = FacebookMain()
        if fb.addCookie(self.cookie)[0] == True:
            result = fb.view_live(self.uidlive)
            result = result[0] if isinstance(result, tuple) else result
        else:
            result = False
        self.show.emit(self.row, 1, str(result))
        self.result.emit(result)
if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
