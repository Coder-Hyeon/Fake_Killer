#https://wikidocs.net/book/2165
#https://wiki.qt.io/Signals_and_Slots_in_PySide/ko
#그 외 많은 html파싱 자료들(from google)
#우리동네약사
#IML

#UI modules
import inside
import sys
import UI
import webbrowser

from functools import partial
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Window(QObject):

    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.gui = UI.QWidgetUI()

        self.worker = inside.Worker()
        self.workerThread = QThread()
        self.worker.moveToThread(self.workerThread)
        self.workerThread.start()

        self.connectSignal()

        self.gui.show()

    def connectSignal(self):
        self.gui.searchBtn.clicked.connect(self.launchTask)
        self.gui.searchBtn.clicked.connect(self.gui.clearTbl)
        self.gui.URLtbl.clicked.connect(self.openURL)
        self.worker.sig_class.connect(self.gui.editURLtblData)

    def openURL(self):
        webbrowser.open('{}'.format(self.gui.URLtbl.currentItem().text()),1)

    def launchTask(self):
        wrapper = partial(self.worker.conductCrolling,self.gui.IDinput.text())
        QTimer.singleShot(0,wrapper)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Window()
    sys.exit(app.exec_())
