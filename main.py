#!/usr/bin/env python3
import sys, os
from pytube import YouTube
from multiprocessing import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from Download_int2 import Ui_MainWindow


# Создаём необходимые параметры
directory = os.getcwd()

    

# Инициализируем функции кнопок
def d144p():
    global i
    i = 160

def d360p():
    global i
    i = 18

def d720p():
    global i
    i = 22

def awt():
    global i
    i = ""

def audio():
    global i
    i = 33



# Инициализируем интерфейс
class ui_init(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.button_144p.clicked.connect(d144p)
        self.button_360p.clicked.connect(d360p)
        self.button_720p.clicked.connect(d720p)
        self.button_audio.clicked.connect(audio)
        self.button_audio_2.clicked.connect(awt)
        self.pushButton.clicked.connect(self.download_start)
        self.pushButton_2.clicked.connect(self.text)
        self.pushButton_3.clicked.connect(self.dir)
        self.setFixedSize(self.size())

    def text(self):
        self.URL = self.plainTextEdit.toPlainText()

    def download_start(self, b):
        try:
            p1 = Process(target=self.download, name="downloading", args=(self, URL, i))
            p1.start()
        except:
        	pass

    def dir(self):
        try:
            directory = QFileDialog.getExistingDirectory(self, "Directory", "/home")
        except:
        	os.chdir(directory)

    def download(*args):
        try:
            yt = YouTube(args[1])
        except:
        	sys.exit()
        try:
            if args[2] == 160: # 144
                video = yt.streams.filter(res="144p").first()
                video.download()
            elif args[2] == 18: # 360
                video = yt.streams.filter(res="360p").first()
                video.download()
            elif args[2] == 22: # 720
                video = yt.streams.filter(res="720p").first()
                video.download()
            elif args[2] == "": # awt
                video = yt.streams.filter(res="1080p").first()
                video.download()
            elif args[2] == 33: # audio
                video = yt.streams.filter(type=audio).first()
                video.download()
            del video
        except:
            pass


def main():
    app = QApplication([])
    app.setWindowIcon(QIcon("test.jpg"))
    ui = ui_init()
    ui.show()
    app.exec_()


if __name__ == "__main__":
    main()
    sys.exit()
