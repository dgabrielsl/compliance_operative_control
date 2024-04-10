import re
import datetime

class Dates():
    def contrast(self):
        self.insert = self.insert.split(' ')
        self.insert = self.insert[0].split('-')
        datetocheck = '/'.join(self.insert)
        self.insert = f'{self.insert[2]}/{self.insert[1]}/{self.insert[0]}'

        datestamp = datetime.now().strftime('%Y/%m/%d')

        if datetocheck < datestamp: self.insert = ''