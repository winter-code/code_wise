import sys
from PyQt4 import QtGui, QtCore
from random import shuffle
import pyaudio
import wave


class Window(QtGui.QMainWindow):
     #window is just a variable and we make a class

    def __init__(self):
        super(Window,self).__init__()
        self.setGeometry(50,50,700,400)
        self.setWindowTitle('Engame')
        self.setWindowIcon(QtGui.QIcon('playlogo.png'))

        self.home()

    def cEvent(self, event): #to add functionality in close button
        event.ignore()
        self.close_app()


    def home(self):

        image = QtGui.QLabel(self)
        image.setGeometry(5,5, 150, 30)
        pixmap = QtGui.QPixmap("logo Engame.png")
        pixmap = pixmap.scaledToWidth(150)
        image.setPixmap(pixmap)
        image.show()



        exit_btn=QtGui.QPushButton('X', self)
        exit_btn.clicked.connect(self.close_app)
        exit_btn.setStyleSheet('background-color: red')
        exit_btn.resize(20,20)
        exit_btn.move(680,10)

        beginner_btn=QtGui.QPushButton('Beginner Level', self)
        beginner_btn.clicked.connect(self.callbeginnerWindow)
        beginner_btn.setStyleSheet('background-color: #fad123')
        beginner_btn.resize(150,70)
        beginner_btn.move(50,100)

        intermidiate_btn=QtGui.QPushButton('Intermidiate Level', self)
        intermidiate_btn.clicked.connect(self.callintermidiateWindow)
        intermidiate_btn.setStyleSheet('background-color: cyan')
        intermidiate_btn.resize(150,70)
        intermidiate_btn.move(275,100)

        expert_btn=QtGui.QPushButton('Expert Level', self)
        expert_btn.clicked.connect(self.callexpertWindow)
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
    def callbeginnerWindow(self):
        self.hide()
        self.Window_Begin = BeginnerWindow()
        self.Window_Begin.show()
        self.Window_Begin.raise_()
    def callintermidiateWindow(self):
        self.hide()
        self.Window_inter = IntermidiateWindow()
        self.Window_inter.show()
        self.Window_inter.raise_()
    def callexpertWindow(self):
        self.hide()
        self.Window_expert = ExpertWindow()
        self.Window_expert.show()
        self.Window_expert.raise_()
class BeginnerWindow(QtGui.QMainWindow):
    def __init__(self):
        super(BeginnerWindow,self).__init__()
        self.setGeometry(50,50,700,400)
        self.setWindowTitle('Engame')
        self.setWindowIcon(QtGui.QIcon('playlogo.png'))

        self.buttons_Beginner()


    def cEvent(self, event): #to add functionality in close button
        event.ignore()
        self.close_app()

    def buttons_Beginner(self):


        image_button = QtGui.QPushButton('', self)
        image_button.clicked.connect(self.callmainWindow)
        image_button.setIcon(QtGui.QIcon('logo Engame.png'))
        image_button.resize(160,40)
        image_button.setIconSize(QtCore.QSize(150,30))


        exit_btn=QtGui.QPushButton('X', self)
        exit_btn.clicked.connect(self.close_app)
        exit_btn.setStyleSheet('background-color: red')
        exit_btn.resize(20,20)
        exit_btn.move(680,10)

        speak_btn=QtGui.QPushButton('speak', self)
        speak_btn.clicked.connect(self.speak_button)
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

    def speak_button(self):

        
        for i in range(1,2):
            FORMAT = pyaudio.paInt16
            CHANNELS = 1
            RATE = 24000
            CHUNK = 1024
            RECORD_SECONDS = 3
            
            WAVE_OUTPUT_FILENAME = "audiofiles/file"+str(i)+".wav"
             
            audio = pyaudio.PyAudio()
             
            
            stream = audio.open(format=FORMAT, channels=CHANNELS,
                            rate=RATE, input=True,
                            frames_per_buffer=CHUNK)
            
            frames = []
             
            for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
                data = stream.read(CHUNK)
                frames.append(data)
            
            stream.stop_stream()
            stream.close()
            audio.terminate()
             
            waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
            waveFile.setnchannels(CHANNELS)
            waveFile.setsampwidth(audio.get_sample_size(FORMAT))
            waveFile.setframerate(RATE)
            waveFile.writeframes(b''.join(frames))
            waveFile.close()



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
    def callmainWindow(self):
        self.hide()
        self.Window_main = Window()
        self.Window_main.show()
        self.Window_main.raise_()
class IntermidiateWindow(QtGui.QMainWindow):
    def __init__(self):
        super(IntermidiateWindow,self).__init__()
        self.setGeometry(50,50,700,400)
        self.setWindowTitle('Engame')
        self.setWindowIcon(QtGui.QIcon('playlogo.png'))

        self.buttons_Intermidiate()


    def cEvent(self, event): #to add functionality in close button
        event.ignore()
        self.close_app()

    def buttons_Intermidiate(self):

        image_button = QtGui.QPushButton('', self)
        image_button.clicked.connect(self.callmainWindow)
        image_button.setIcon(QtGui.QIcon('logo Engame.png'))
        image_button.resize(160,40)
        image_button.setIconSize(QtCore.QSize(150,30))


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



        self.words=['decoration', 'amused', 'humus', 'acknowledge', 'property']
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

    def callmainWindow(self):
        self.hide()
        self.Window_main = Window()
        self.Window_main.show()
        self.Window_main.raise_()

        
class ExpertWindow(QtGui.QMainWindow):
    def __init__(self):
        super(ExpertWindow,self).__init__()
        self.setGeometry(50,50,700,400)
        self.setWindowTitle('Engame')
        self.setWindowIcon(QtGui.QIcon('playlogo.png'))

        self.buttons_Expert()


    def cEvent(self, event): #to add functionality in close button
        event.ignore()
        self.close_app()

    def buttons_Expert(self):

        image_button = QtGui.QPushButton('', self)
        image_button.clicked.connect(self.callmainWindow)
        image_button.setIcon(QtGui.QIcon('logo Engame.png'))
        image_button.resize(160,40)
        image_button.setIconSize(QtCore.QSize(150,30))


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



        self.words=['mischievous', 'asterisk', 'prerogative', 'frequently', 'nuclear']
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

    def callmainWindow(self):
        self.hide()
        self.Window_main = Window()
        self.Window_main.show()
        self.Window_main.raise_()


def run():
    app=QtGui.QApplication(sys.argv)
    GUI= Window()
    sys.exit(app.exec_())

run()
