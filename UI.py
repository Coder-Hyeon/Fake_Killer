#UI modules
import sys

from functools import partial
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class QWidgetUI(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Fake Killer v_0.1")
        self.resize(1440,810)
        self.setWindowIcon(QIcon('icon.jpg'))

        gridLayout = QGridLayout(self)
        self.setLayout(gridLayout)

        self.IDinput = QLineEdit(self)
        gridLayout.addWidget(self.IDinput,0,0,1,2)

        self.URLtbl = QTableWidget(self)
        self.URLtbl.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.URLtblData()
        gridLayout.addWidget(self.URLtbl,0,3,2,1)

        self.progressBar = QProgressBar(self)
        self.progressBar.setProperty("value",0)
        gridLayout.addWidget(self.progressBar,2,3,1,1)

        self.IDtbl = QTableWidget(self)
        self.IDtbl.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.IDtblData()
        gridLayout.addWidget(self.IDtbl,1,0,1,3)

        self.searchBtn = QPushButton("🔍",self)
        gridLayout.addWidget(self.searchBtn,0,2,1,1)
        
        self.sendBtn = QPushButton("문의사항\n보내기",self)
        gridLayout.addWidget(self.sendBtn,2,0,1,1)

    def IDtblData(self):
        col_headers = ["ID","도용여부"]
        self.IDtbl.setColumnCount(len(col_headers))
        self.IDtbl.setHorizontalHeaderLabels(col_headers)

    def URLtblData(self):
        col_headers = ["검색한 URL","검색된 URL","검색결과 한눈에 보기"]
        self.URLtbl.setColumnCount(len(col_headers))
        self.URLtbl.setHorizontalHeaderLabels(col_headers)
        self.URLtbl.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def progressBar(self,val):
        self.progressBar.setValue(val)

    @pyqtSlot(str,int,int)
    def editURLtblData(self,URL,Row,Column):
        self.URLtbl.setRowCount(Row+1)
        self.URLtbl.setItem(Row,Column,QTableWidgetItem('{}'.format(URL)))
        self.URLtbl.resizeColumnsToContents()
        self.URLtbl.resizeRowsToContents()

    @pyqtSlot()
    def clearTbl(self):
        self.URLtbl.setRowCount(0)
