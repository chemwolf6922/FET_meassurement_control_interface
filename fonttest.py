from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFontDatabase,QFont
import sys

class font_test(QWidget):
    def __init__(self):
        super().__init__()
        self.font = QFont('Roboto-Light',20,QFont.Normal)
        self.initUI()

    def initUI(self):
        self.bt1 = QPushButton('test',self)
        self.bt1.setGeometry(100,50,100,50)
        self.bt1.setFont(self.font)

        self.setGeometry(300,300,300,300)
        self.setWindowTitle('fonttestha')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    test = font_test()
    sys.exit(app.exec_())
