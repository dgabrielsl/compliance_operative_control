import sqlite3

from datetime import datetime

class Scripts():
    def __init__(self):
        super().__init__()

    def make_new(self):
        self.new_script_record = f'INSERT INTO scripts VALUES ("{self.pre_created}", "{self.pre_created}", "{self.pre_creator}", "{self.pre_header}", "{self.pre_description}", "{self.pre_body}", "{self.pre_status}")'
        self.new_script_record_log = f'INSERT INTO log_for_scripts VALUES ("{self.pre_created}", "N/A", "{self.pre_creator}", "{self.pre_header}", "N/A", "{self.pre_description}", "N/A", "{self.pre_body}", "N/A", "{self.pre_status}", "N/A", "Nuevo registro")'

    def make_update(self):
        to_insert = []
        for i in range(len(self.pull_int_dat)):
            if f'{self.pull_int_dat[i]}' != f'{self.pull_dbo_log[i]}':
                if i < 3: to_insert.append(f'{self.pull_int_dat[i]}')
                else:
                    if f'{self.pull_int_dat[i]}' == '0': to_insert.append('Deshabilitado')
                    else: to_insert.append('Habilitado')

            else: to_insert.append('N/A')

        timemark = datetime.now().strftime('%Y/%m/%d %H:%M:%SH')

        if self.pull_dbo_log[3] == '0': self.pull_dbo_log[0] = 'Habilitado'
        else: self.pull_dbo_log[3] = 'Deshabilitado'

        self.new_script_record_log = f'INSERT INTO log_for_scripts VALUES ("{self.pre_created}", "{timemark}", "{self.pre_creator}", "{self.pull_dbo_log[0]}", "{to_insert[0]}", "{self.pull_dbo_log[1]}", "{to_insert[1]}", "{self.pull_dbo_log[2]}", "{to_insert[2]}", "{self.pull_dbo_log[3]}", "{to_insert[3]}", "Actualizado")'

        con = sqlite3.connect('hub.db')
        cur = con.cursor()
        cur.execute(self.new_script_record_log)
        con.commit()

        push_script_update = f'UPDATE scripts SET modified = "{timemark}", creator = "{self.pre_creator}", description = "{self.pre_description}", body = "{self.pre_body}", status = "{self.pre_status}" WHERE header = "{self.pre_header}"'
        cur.execute(push_script_update)
        con.commit()
        con.close()

    def make_del(self):
        timemark = datetime.now().strftime('%Y/%m/%d %H:%M:%SH')

        if self.pull_int_dat[3] == '0': self.pull_int_dat[3] = 'Habilitado'
        else: self.pull_int_dat[3] = 'Deshabilitado'

        self.new_script_record_log = f'INSERT INTO log_for_scripts VALUES ("{self.pre_created}", "{timemark}", "{self.pre_creator}", "{self.pull_int_dat[0]}", "N/A", "{self.pull_int_dat[1]}", "N/A", "{self.pull_int_dat[2]}", "N/A", "{self.pull_int_dat[3]}", "N/A", "Eliminado")'

        con = sqlite3.connect('hub.db')
        cur = con.cursor()
        cur.execute(self.new_script_record_log)
        con.commit()
        con.close()

    def make_events_log_file(self):
        print(self.sender().text())

        # Fn to create a new Excel's book with the whole data from dbo.HUB[log_for_scripts]