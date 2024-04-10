import re

class Cell():
    # output = output.replace('\t','').replace('\n','').replace('\r','').replace('\f','').replace('\v','')

    def ccd_fname(self):
        output = self.insert.lower()

        for di in self.dict_instructions:
            output = output.replace(di,'')

        output = output.replace('\t','').replace('\n','').replace('\r','').replace('\f','').replace('\v','')

        output = output.split(' ')
        dropempties = []
        for op in output:
            if op != 'id' and op != '' and len(op) > 1: dropempties.append(op)
        output = ' '.join(dropempties)

        self.insert = output.upper()

    def ccd_full_name_titled(self):
        self.insert = self.insert.title()
        self.insert = self.insert.split(' ')

        dropempties = []
        for word in self.insert:
            if word != '': dropempties.append(word)
        self.insert = ' '.join(dropempties)

    def ccd_updated(self):
        self.insert = self.insert.split(' ')
        datestamp = self.insert[0]
        timestamp = self.insert[1]

        datestamp = datestamp.split('-')
        datestamp = f'{datestamp[2]}/{datestamp[1]}/{datestamp[0]}'

        timestamp = timestamp.split(':')
        timestamp = f'{timestamp[0]}:{timestamp[1]}H'

        self.insert = f'{datestamp} {timestamp}'

    def ccd_document(self):
        self.insert = self.insert.upper()
        self.insert = self.insert.replace('\xa0','').replace('\t','').replace('\n','').replace('\r','').replace('\f','').replace('\v','')

        if self.insert == self.id_match_drop_rule: self.insert = ''
        elif self.insert == 0 or self.insert == '0' or self.insert == None or self.insert == 'None': self.insert = ''

        if not self.insert.__contains__('R-'):
            pattern = re.search(r'\D',self.insert)
            if pattern: self.insert = ''

    def ccd_deadline(self):
        pattern = re.search(r'\d\d\d\d-\d\d-\d\d',self.insert)

        if not pattern: self.insert = ''
        else:
            try:
                self.insert = self.insert.split(' ')
                self.insert = self.insert[0].split('-')
                self.insert = f'{self.insert[2]}/{self.insert[1]}/{self.insert[0]}'
            except: pass

    def ccd_product(self):
        if self.insert == None or self.insert == 'None': self.insert = ''

    def ccd_result(self):
        if self.insert == None or self.insert == 'None': self.insert = ''

        pattern = re.search(r'\d. ',self.insert)
        if pattern:
            g = pattern.group()
            self.insert = self.insert.replace(g,'')

    def ccd_customer_answer(self):
        if self.insert == None or self.insert == 'None': self.insert = ''

        pattern = re.search(r'\d. ',self.insert)
        if pattern:
            g = pattern.group()
            self.insert = self.insert.replace(g,'')

        pattern = re.search(r'\d.',self.insert)
        if pattern:
            g = pattern.group()
            self.insert = self.insert.replace(g,'')

    def ccd_code(self):
        if self.insert == None or self.insert == 'None' or self.insert == 0 or self.insert == '0': self.insert = ''

        pattern = re.search(r'\D',self.insert)
        if pattern: self.insert = ''

    def ccd_income_source(self):
        if self.insert == None or self.insert == 'None' or self.insert.lower() == 'n/a': self.insert = ''

    def ccd_warning_amount(self):
        if self.insert == None or self.insert == 'None' or self.insert == 0 or self.insert == '0': self.insert = ''

        pattern = re.search(r'\d',self.insert)
        if not pattern: self.insert = ''

        self.insert = self.insert.replace('.',' ').replace(',',' ').replace('?','¢')

        pattern = re.search('(\s\d\d)$',self.insert)
        if pattern and self.insert != '': self.insert = self.insert.replace(pattern.group(),'')

        self.insert = self.insert.lower().replace('cripto','')

        self.insert = self.insert.split(' ')
        dropempties = []
        for char in self.insert:
            pattern = re.search(r'\d',char)
            if char: dropempties.append(char)
        self.insert = ''.join(dropempties)

        self.insert = self.insert.replace('\xa0','').replace('n','').replace('a','').replace('/','')

        pattern = re.search(r'[¢$]',self.insert)
        pattern2 = re.search(r'\d{0,50}',self.insert)
        if self.insert != '':
            if not pattern:
                if len(pattern2.group()) < 4: self.insert = ''
                elif pattern2.group() == self.id_match_drop_rule: self.insert = ''

        if self.insert.__contains__('¢') and self.insert.__contains__('$'):
            pattern = re.findall(r'\d',self.insert)
            pattern = ''.join(pattern)
            if int(pattern) <= 10000: self.insert = self.insert.replace('¢','')
            else: self.insert = self.insert.replace('$','')

        if not self.insert.__contains__('¢') and not self.insert.__contains__('$') and len(self.insert) > 0:
            n = self.insert
            n = int(n)
            if n > 10000: self.insert = f'¢{self.insert}'
            else: self.insert = f'¢{self.insert}'

        crc = False
        usd = False

        if self.insert.__contains__('¢'): crc = True
        else: usd = True

        self.insert = self.insert.replace('¢','').replace('$','')

        try:
            self.insert = int(self.insert)
            if crc: self.insert = f'{self.insert:0,.0f} CRC'.replace(',','.')
            else: self.insert = f'{self.insert:0,.0f} USD'.replace(',','.')
        except Exception as e: pass

    def ccd_customer_profile(self):
        if self.insert == None or self.insert == 'None' or self.insert.lower() == 'n/a': self.insert = ''

    def ccd_notif_type(self):
        if self.insert == None or self.insert == 'None' or self.insert.lower() == 'n/a': self.insert = ''
        else: self.insert = self.insert.lower().capitalize()

    def ccd_contact_type(self):
        if self.insert == None or self.insert == 'None' or self.insert.lower() == 'n/a': self.insert = ''
