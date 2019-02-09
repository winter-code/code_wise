
import sys
from PyQt5 import QtWidgets


class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.le = QtWidgets.QLineEdit()
        self.b1 = QtWidgets.QPushButton('Clear')
        self.b2 = QtWidgets.QPushButton('Search')
        self.l1 = QtWidgets.QLabel('What do you want?')



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
        sender = self.sender()
        if sender.text() == 'Search':
            if self.le.text() == '':
                self.l1.setText("Enter something!")
            else:
                self.l1.setText('Not Found!')
        else:
            self.le.clear()


app = QtWidgets.QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())
