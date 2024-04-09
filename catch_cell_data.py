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
        if self.insert == self.id_match_drop_rule: self.insert = ''
        else:
            pattern = re.search(r'R-',self.insert.upper())
            if not pattern: self.insert = ''
            else:
                pattern = re.search(r'\D',self.insert)
                if pattern or self.insert == 0 or self.insert == '0': self.insert = ''

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

        self.insert = self.insert.replace(',','.').replace('?','¢')

        pattern = re.search('(\s\d\d)$',self.insert)
        if pattern and self.insert != '': self.insert = self.insert.replace(pattern.group(),'')

    def ccd_customer_profile(self):
        pass

    def ccd_notif_type(self):
        pass

    def ccd_contact_type(self):
        pass
