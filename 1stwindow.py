import sys
from PyQt4 import QtGui, QtCore
from random import shuffle

class Window(QtGui.QMainWindow):
     #window is just a variable and we make a class

    def __init__(self):
        super(Window,self).__init__()
        self.setGeometry(50,50,700,400)
        self.setWindowTitle('Engame')
        self.setWindowIcon(QtGui.QIcon('logo.png'))

        self.home()

    def cEvent(self, event): #to add functionality in close button
        event.ignore()
        self.close_app()


    def home(self):
        exit_btn=QtGui.QPushButton('X', self)
        exit_btn.clicked.connect(self.close_app)
        exit_btn.setStyleSheet('background-color: red')
        exit_btn.resize(20,20)
        exit_btn.move(680,10)

        beginner_btn=QtGui.QPushButton('Beginner Level', self)
        beginner_btn.clicked.connect(self.callAnotherQMainWindow)
        beginner_btn.setStyleSheet('background-color: #fad123')
        beginner_btn.resize(150,70)
        beginner_btn.move(50,100)

        intermidiate_btn=QtGui.QPushButton('Intermidiate Level', self)
        #beginner_btn.clicked.connect(self.close_app)
        intermidiate_btn.setStyleSheet('background-color: cyan')
        intermidiate_btn.resize(150,70)
        intermidiate_btn.move(275,100)

        expert_btn=QtGui.QPushButton('Expert Level', self)
        #beginner_btn.clicked.connect(self.close_app)
        expert_btn.setStyleSheet('background-color: green')
        expert_btn.resize(150,70)
        expert_btn.move(500,100)

        self.show()


    def close_app(self): #printing the line after quiting the app
        #print('closed...')
        choice=QtGui.QMessageBox.question(self, 'Extract!', 'Do you want to quit?',QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)

        if choice==QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            pass
    def callAnotherQMainWindow(self):
        self.hide()
        self.Window_Begin = BeginnerWindow()
        self.Window_Begin.show()
        self.Window_Begin.raise_()
class BeginnerWindow(QtGui.QMainWindow): #window is just a variable and we make a class
    def __init__(self):
        super(BeginnerWindow,self).__init__()
        self.setGeometry(50,50,700,400)
        self.setWindowTitle('Engame')
        self.setWindowIcon(QtGui.QIcon('logo.png'))

        self.buttons_Beginner()


    def cEvent(self, event): #to add functionality in close button
        event.ignore()
        self.close_app()

    def buttons_Beginner(self):


        exit_btn=QtGui.QPushButton('X', self)
        exit_btn.clicked.connect(self.close_app)
        exit_btn.setStyleSheet('background-color: red')
        exit_btn.resize(20,20)
        exit_btn.move(680,10)

        speak_btn=QtGui.QPushButton('speak', self)
        #speak_btn.clicked.connect(self.close_app)
        speak_btn.setStyleSheet('background-color: pink')
        speak_btn.resize(100,30)
        speak_btn.move(150,300)

        self.styleChoice=QtGui.QLabel(self)

        next_btn=QtGui.QPushButton('Next Word', self)
        next_btn.clicked.connect(self.randomized_bwords)
        next_btn.setStyleSheet('background-color: cyan')
        next_btn.resize(100,30)
        next_btn.move(450,300)



        self.words=['Hello', 'Buy', 'Chair', 'cash', 'money']
        shuffle(self.words)

        self.styleChoice.move(100,50)
        self.styleChoice.resize(500,150)
        self.styleChoice.setText(self.words[0])
        self.styleChoice.setFont(QtGui.QFont("Times", 50, QtGui.QFont.Bold))
        self.styleChoice.setStyleSheet('background-color: #fad123')
        self.styleChoice.setAlignment(QtCore.Qt.AlignCenter)
        self.show()


    def randomized_bwords(self):
        if len(self.words)>0:
            self.styleChoice.setText(self.words.pop(1))
            self.styleChoice.move(100,50)
            self.styleChoice.resize(500,150)
            self.styleChoice.setFont(QtGui.QFont("Times", 50, QtGui.QFont.Bold))
            self.styleChoice.setStyleSheet('background-color: #fad123')
            self.styleChoice.setAlignment(QtCore.Qt.AlignCenter)



    def close_app(self):
        choice=QtGui.QMessageBox.question(self, 'Extract!', 'Do you want to quit?',QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)

        if choice==QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            pass


def run():
    app=QtGui.QApplication(sys.argv)
    GUI= Window()
    sys.exit(app.exec_())

run()
