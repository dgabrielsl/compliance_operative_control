import sqlite3

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

    def ccd_author(self):
        pass

    def ccd_assigned_to(self):
        pass

    def ccd_updated(self):
        pass

    def ccd_identification(self):
        pass

    def ccd_document(self):
        pass

    def ccd_class_case(self):
        pass

    def ccd_deadline(self):
        pass

    def ccd_product(self):
        pass

    def ccd_result(self):
        pass

    def ccd_customer_answer(self):
        pass

    def ccd_code(self):
        pass

    def ccd_income_source(self):
        pass

    def ccd_warning_amount(self):
        pass

    def ccd_customer_profile(self):
        pass

    def ccd_notif_type(self):
        pass

    def ccd_contact_type(self):
        pass
