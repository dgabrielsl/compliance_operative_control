import re
from datetime import datetime
from PyQt6.QtCore import QDate

class Dates():
    def contrast(self):
        # self.datetocheck = self.datetocheck.replace('-','/')
        datestamp = datetime.now().strftime('%Y-%m-%d')

        if self.datetocheck < datestamp: self.datetocheck = ''
        else:
            self.datetocheck = self.datetocheck.split('-')
            self.datetocheck = f'{self.datetocheck[2]}/{self.datetocheck[1]}/{self.datetocheck[0]}'
            print(self.datetocheck)