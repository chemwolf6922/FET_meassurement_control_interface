from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
import sys

class test(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.bt1 = QPushButton('button',self)
        self.bt1.resize(self.bt1.sizeHint())
        self.bt1.move(100,50)
        self.bt1.clicked.connect(self.ha)

        self.setFixedSize(300,200)
        self.move(300,300)
        self.setStyleSheet('background-color: #EEEEEE')
        self.setWindowTitle('haha')
        self.show()


    def ha(self):
        self.bt1.setStyleSheet('background-color: #666666; border: none')
        print('haha')


app = QApplication(sys.argv)
w = test()
sys.exit(app.exec_())

