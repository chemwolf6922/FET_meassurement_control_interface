from PyQt5.QtWidgets import QMainWindow,QPushButton,QApplication
import sys
import time

class test_panel(QMainWindow):
    def __init__(self):
        super().__init__()
        self.lasttime = time.time()
        self.initUI()

    def initUI(self):
        self.bt0 = QPushButton('Push me',self)
        #self.bt0.clicked.connect(self.pressed)
        self.bt0.setStyleSheet('background-color: #00FF00')
        self.bt0.setGeometry(50,100,200,100)

        self.setGeometry(300,300,400,300)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    a = test_panel()
    sys.exit(app.exec_())
