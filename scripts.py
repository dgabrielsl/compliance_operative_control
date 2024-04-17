import sqlite3

from datetime import datetime

class Scripts():
    def __init__(self):
        super().__init__()

    def make_new(self):
        self.new_script_record = f'INSERT INTO scripts VALUES ("{self.pre_created}", "{self.pre_created}", "{self.pre_creator}", "{self.pre_header}", "{self.pre_description}", "{self.pre_body}", "{self.pre_status}")'

        self.new_script_record_log = f'INSERT INTO log_for_scripts VALUES ("{self.pre_created}", "N/A", "{self.pre_creator}", "{self.pre_header}", "N/A", "{self.pre_description}", "N/A", "{self.pre_body}", "N/A", "{self.pre_status}", "N/A", "Nuevo registro")'

    def make_update(self):
        print(f'pull_int_dat:  {self.pull_int_dat}')
        print(f'pull_dbo_log: {self.pull_dbo_log}')

        print()
        for i in range(len(self.pull_int_dat)):
            print(f'{self.pull_int_dat[i]} /// {self.pull_dbo_log[i]}')

        self.new_script_record_log = f'INSERT INTO log_for_scripts VALUES ("{self.pre_created}", "N/A", "{self.pre_creator}", "{self.pre_header}", "N/A", "{self.pre_description}", "N/A", "{self.pre_body}", "N/A", "{self.pre_status}", "N/A", "Nuevo registro")'

    def make_del(self):
        print(f'pre_grouped:  {self.pre_grouped}')
