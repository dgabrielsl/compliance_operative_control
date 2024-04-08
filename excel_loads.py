import os
import sqlite3

from PyQt6.QtWidgets import *

import openpyxl

import re
from datetime import datetime

class Excel(QWidget):
    def __init__(self):
        super().__init__()

    def load_sysde(self):
        path = QFileDialog.getOpenFileName(filter=('*.xlsx'))
        path = path[0]

        if path != '':
            wb = openpyxl.load_workbook(path)
            ws = wb.worksheets[0]

            ws.delete_rows(1,4)

            char_1 = char_2 = char_3 = ''

            for i in range(ws.max_column):
                i += 1
                if ws.cell(1,i).value == 'Identificación' or ws.cell(1,i).value == 'Identificacion': char_1 = ws.cell(1,i).column_letter
                if ws.cell(1,i).value == 'Email': char_2 = ws.cell(1,i).column_letter
                if ws.cell(1,i).value == 'Teléfono celular' or ws.cell(1,i).value == 'Telefono celular': char_3 = ws.cell(1,i).column_letter

            self.records_from_sysde = []

            for i in range(int(ws.max_row) + 1):
                if i > 1:
                    line = []
                    insert = f'{ws[char_1+str(i)].value}'
                    insert = insert.replace('-','')
                    line.append(str(insert))
                    line.append(f'{ws[char_2+str(i)].value}'.lower())
                    line.append(str(f'{ws[char_3+str(i)].value}'))
                    self.records_from_sysde.append(line)

    def save_sysde(self):
        print('save_sysde')

        # con = sqlite3.connect('hub.db')
        # cur = con.cursor()

        # for record in self.records_from_sysde:
        #     r = f'INSERT INTO sysde VALUES ("{record[0]}", "{record[1]}", "{record[2]}")'
        #     try: cur.execute(r)
        #     except Exception as e:
        #         print(e)
        #         break

        # con.commit()
        # con.close()

    def load_hds(self):
        path = QFileDialog.getOpenFileName(filter=('*.xlsx'))
        path = path[0]

    def save_hdsreport(self):
        print('save_hdsreport')