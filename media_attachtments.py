import os
import sqlite3

from PyQt6.QtWidgets import *
from PyPDF2 import PdfReader, PdfWriter
from PIL import Image
from datetime import datetime

class Attacthments():
    def __init__(self):
        super().__init__()

    def get_file(self):
        self.full_path = QFileDialog.getOpenFileName(filter=('*.pdf *.jpg *jpeg *.png'))
        self.full_path = self.full_path[0]

        if self.full_path != '':
            self.file_name = self.full_path.split('/')
            self.file_name = self.file_name[-1]
            self.file_extension = self.file_name.split('.')
            self.file_extension = f'.{self.file_extension[-1]}'
            self.file_name = self.file_name.split('.')
            self.file_name = self.file_name[0]

            timemark = datetime.now().strftime('%Y/%m/%d %H:%M:%SH')
            print(timemark)
            print(self.connected_user[-1])

            if self.file_extension == '.pdf':
                self.pdf_object = open(self.full_path,'rb')
                print(self.pdf_object)
            else:
                self.img_object = Image.open(self.full_path)
                print(self.img_object)
                # self.img_object.save('C:/Users/gabriel.solano/Downloads/new_img.png')

            self.slot_1.setText('554433')
            print(self.slot_1.text())
            print(self.file_name)
            print(self.file_extension)
            print(f'{round(os.path.getsize(self.full_path)/1024)} MB')

            # my_image.Image.save('C:/Users/gabriel.solano/Downloads/New folder/new_img.png')