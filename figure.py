import pylab as pl
import math
import time
from PyQt5.QtWidgets import QWidget,QPushButton,QApplication
from PyQt5.QtCore import QThread
import sys

graphstatus = True

class graphthread(QThread):
    def __init__(self):
        super(graphthread,self).__init__()
        self.data = []
        self.i = 0

    def run(self):
        global graphstatus
        while graphstatus:
            self.data.append(math.sin(self.i/20*math.pi))
            if len(self.data)>50:
                self.data = self.data[1:]
            pl.cla()
            pl.plot(self.data)
            pl.pause(0.02)
            self.i += 1 
        pl.close()
        self.exec_()


class switch(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        bt1 = QPushButton('button',self)
        bt1.setGeometry(100,50,100,50)
        bt1.clicked.connect(self.setstatus)

        self.setGeometry(300,300,300,300)
        self.show()

    def setstatus(self):
        global graphstatus
        graphstatus = False
        
app = QApplication(sys.argv)
a = graphthread()
a.start()
b = switch()
app.exit(app.exec_())