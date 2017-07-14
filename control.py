from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
import sys
import serial

class control_panel(QWidget):
    def __init__(self):
        super().__init__()
        self.Font = QFont('Roboto',16,QFont.Normal)
        self.lens1_status = False
        self.lens2_status = False
        self.lens3_status = False
        self.current_channel = 0
        self.initUI()

    def initUI(self):
        self.bt0 = QPushButton('Make Zero',self)
        self.bt0.clicked.connect(self.make_zero)
        self.bt0.setStyleSheet('background-color: #FFFFFF')
        self.bt0.setFont(self.Font)

        self.bt2 = QPushButton('Channel 1',self)
        self.bt2.clicked.connect(self.change_to_CH1)
        self.bt2.setStyleSheet('background-color: #FFFFFF')
        self.bt2.setFont(self.Font)

        self.bt3 = QPushButton('Channel 2',self)
        self.bt3.clicked.connect(self.change_to_CH2)
        self.bt3.setStyleSheet('background-color: #FFFFFF')
        self.bt3.setFont(self.Font)

        self.bt4 = QPushButton('Channel 3',self)
        self.bt4.clicked.connect(self.change_to_CH3)
        self.bt4.setStyleSheet('background-color: #FFFFFF')
        self.bt4.setFont(self.Font)

        self.bt5 = QPushButton('Channel 4',self)
        self.bt5.clicked.connect(self.change_to_CH4)
        self.bt5.setStyleSheet('background-color: #FFFFFF')
        self.bt5.setFont(self.Font)
        
        self.bt6 = QPushButton('Lens 1',self)
        self.bt6.clicked.connect(self.Lens1_event)
        self.bt6.setStyleSheet('background-color: #FFFFFF')
        self.bt6.setFont(self.Font)

        self.bt7 = QPushButton('Lens 2',self)
        self.bt7.clicked.connect(self.Lens2_event)
        self.bt7.setStyleSheet('background-color: #FFFFFF')
        self.bt7.setFont(self.Font)

        self.bt8 = QPushButton('Lens 3',self)
        self.bt8.clicked.connect(self.Lens3_event)
        self.bt8.setStyleSheet('background-color: #FFFFFF')
        self.bt8.setFont(self.Font)

        vbox1 = QVBoxLayout()
        vbox1.addWidget(self.bt2)
        vbox1.addWidget(self.bt3)
        vbox1.addWidget(self.bt4)
        vbox1.addWidget(self.bt5)

        vbox2 = QVBoxLayout()
        vbox2.addWidget(self.bt0)
        vbox2.addWidget(self.bt6)
        vbox2.addWidget(self.bt7)
        vbox2.addWidget(self.bt8)

        hbox = QHBoxLayout()
        hbox.addLayout(vbox1)
        hbox.addLayout(vbox2)

        self.setLayout(hbox)
        self.setGeometry(300,300,300,400)
        self.setWindowTitle('Control Panel')
        self.setStyleSheet('background-color: #CCCCCC')
        self.show()

    def connect_device(self):
        print('connect device')

    def change_to_CH1(self):
        print('change to channel 1')
        if self.current_channel == 1:
            self.current_channel = 0
            self.bt2.setStyleSheet('background-color: #FFFFFF')
        else:
            self.current_channel = 1
            self.bt2.setStyleSheet('background-color: #4CAF50')
            self.bt3.setStyleSheet('background-color: #FFFFFF')
            self.bt4.setStyleSheet('background-color: #FFFFFF')
            self.bt5.setStyleSheet('background-color: #FFFFFF')
            
    def change_to_CH2(self):
        print('change to channel 2')
        if self.current_channel == 2:
            self.current_channel = 0
            self.bt3.setStyleSheet('background-color: #FFFFFF')
        else:
            self.current_channel = 2
            self.bt2.setStyleSheet('background-color: #FFFFFF')
            self.bt3.setStyleSheet('background-color: #4CAF50')
            self.bt4.setStyleSheet('background-color: #FFFFFF')
            self.bt5.setStyleSheet('background-color: #FFFFFF')

    def change_to_CH3(self):
        print('change to channel 3')
        if self.current_channel == 3:
            self.current_channel = 0
            self.bt4.setStyleSheet('background-color: #FFFFFF')
        else:
            self.current_channel = 3
            self.bt2.setStyleSheet('background-color: #FFFFFF')
            self.bt3.setStyleSheet('background-color: #FFFFFF')
            self.bt4.setStyleSheet('background-color: #4CAF50')
            self.bt5.setStyleSheet('background-color: #FFFFFF')

    def change_to_CH4(self):
        print('change to channel 4')
        if self.current_channel == 4:
            self.current_channel = 0
            self.bt5.setStyleSheet('background-color: #FFFFFF')
        else:
            self.current_channel = 4
            self.bt2.setStyleSheet('background-color: #FFFFFF')
            self.bt3.setStyleSheet('background-color: #FFFFFF')
            self.bt4.setStyleSheet('background-color: #FFFFFF')
            self.bt5.setStyleSheet('background-color: #4CAF50')

    def make_zero(self):
        print('make zero')
        self.current_channel = 0
        self.bt2.setStyleSheet('background-color: #FFFFFF')
        self.bt3.setStyleSheet('background-color: #FFFFFF')
        self.bt4.setStyleSheet('background-color: #FFFFFF')
        self.bt5.setStyleSheet('background-color: #FFFFFF')

    def Lens1_event(self):
        print('lens 1 event')
        if self.lens1_status:
            self.lens1_status = False
            self.bt6.setStyleSheet('background-color: #FFFFFF')
        else:
            self.lens1_status = True
            self.bt6.setStyleSheet('background-color: #4CAF50')

    def Lens2_event(self):
        print('lens 2 event')
        if self.lens2_status:
            self.lens2_status = False
            self.bt7.setStyleSheet('background-color: #FFFFFF')
        else:
            self.lens2_status = True
            self.bt7.setStyleSheet('background-color: #4CAF50')

    def Lens3_event(self):
        print('lens 3 event')
        if self.lens3_status:
            self.lens3_status = False
            self.bt8.setStyleSheet('background-color: #FFFFFF')
        else:
            self.lens3_status = True
            self.bt8.setStyleSheet('background-color: #4CAF50')
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    cp = control_panel()
    sys.exit(app.exec_())
