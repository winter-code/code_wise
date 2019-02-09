
import sys
import pandas as pd
import numpy as np
import csv
from PyQt5 import QtWidgets



class Window(QtWidgets.QWidget):
    df = pd.read_csv('Book1.csv')


    def __init__(self):
        df = pd.read_csv('Book1.csv')
        super().__init__()

        self.init_ui()

    def init_ui(self):
        df = pd.read_csv('Book1.csv')
        self.le = QtWidgets.QLineEdit()
        self.b1 = QtWidgets.QPushButton('Clear')
        self.b2 = QtWidgets.QPushButton('Search')
        self.l1 = QtWidgets.QLabel('In progress')



        v_box = QtWidgets.QVBoxLayout()

        v_box.addWidget(self.le)
        v_box.addWidget(self.b1)
        v_box.addWidget(self.b2)
        v_box.addWidget(self.l1)

        self.setLayout(v_box)
        self.setWindowTitle('Code_Wise')


        self.b1.clicked.connect(self.btn_clk)
        self.b2.clicked.connect(self.btn_clk)

        self.show()

    def btn_clk(self):
        df = pd.read_csv('Book1.csv')
        #print(self.le.text() == df['Item Name'])
        sender = self.sender()
        if sender.text() == 'Search':
            if self.le.text() == '':
                self.l1.setText("Enter something!")
            elif (df['Item Name'] == self.le.text()).any :
                v = df.loc[df['Item Name'] == self.le.text()]
                print(v)
            else:
                self.l1.setText('Not FOUND!')

        else:
            self.le.clear()


app = QtWidgets.QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())
