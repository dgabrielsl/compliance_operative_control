import os
import sqlite3

from PyQt6.QtWidgets import *
from PyPDF2 import PdfReader, PdfWriter, PdfMerger
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

            if self.file_extension == '.pdf': self.pdf_object = PdfReader(self.full_path)
            else:
                self.img_object = Image.open(self.full_path)
                self.pdf_object = ''

            if self.pdf_object != '': self.bin_file = self.pdf_object
            else: self.bin_file = self.img_object


            con = sqlite3.connect('hub.db')
            cur = con.cursor()

            _size = round(os.path.getsize(self.full_path)/1024)

            try:
                cur.execute(f'INSERT INTO attached_files VALUES ("{timemark}", "{self.connected_user[-1]}", "{self.slot_1.text()}", "{self.file_name}", "{self.file_extension}", "{_size} MB", "{sqlite3.Binary(self.bin_file)}")')
                con.commit()
            except Exception as e: pass

            try:
                cur.execute(f'INSERT INTO attached_files_events_log VALUES ("{timemark}", "{self.connected_user[-1]}", "{self.slot_1.text()}", "{self.file_name}", "{self.file_extension}", "{_size} MB", "Adjuntar")')
                con.commit()
            except Exception as e: pass

            # path = f'C:/Users/gabriel.solano/Downloads/Save media/{self.file_name}{self.file_extension}'
            # _writer = PdfWriter()
            # for p in range(self.pdf_object.pages.__len__()):
            #     _writer.add_page(self.pdf_object.pages[p])
            #     with open(path, 'wb') as f:
            #         _writer.write(f)
            #         f.close()

            con.close()

            # con = sqlite3.connect('hub.db')
            # # con.text_factory = bytes
            # cur = con.cursor()

            # query = 'new_img'
            # cur.execute('SELECT bin_file FROM attached_files WHERE file_name = ?', (query,))
            # res = cur.fetchone()

            # path = f'C:/Users/gabriel.solano/Downloads/Save media/{self.file_name}{self.file_extension}'
            # print(res)

            # _writer = PdfWriter()

            # for p in range(res[0].pages.__len__()):
            #     _writer.add_page(res[0].pages[p])
            #     with open(path, 'wb') as f:
            #         _writer.write(f)
            #         f.close()

            # binary_file = cur
            # binary_file = open(path,'rb')

            # print(binary_file)

            # # _reader = PdfReader()
            # path = f'C:/Users/gabriel.solano/Downloads/Save media/{self.file_name}{self.file_extension}'

            # _pdf = PdfReader(binary_file)

            # _writer = PdfWriter()
            # for p in range(_pdf.pages.__len__()):
            #     _writer.add_page(_pdf.pages[p])
            #     with open(path, 'wb') as f:
            #         _writer.write(f)
            #         f.close()

            # con.close()