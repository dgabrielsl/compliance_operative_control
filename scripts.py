import sqlite3

from datetime import datetime

class Scripts():
    def __init__(self):
        super().__init__()

    def make_new(self):
        _created = datetime.now().strftime('%d/%m/%Y %H:%M:%SH')
        _creator = self.connected_user[-1]
        _header = self.scripts_tool_title.text()
        _description = self.scripts_tool_description.text()
        _body = self.scripts_tool_body.toPlainText()
        if self.scripts_tool_disable.isChecked(): _status = 0
        else: _status = 1

        self.new_script_record = f'INSERT INTO scripts VALUES ("{_created}", "{_created}", "{_creator}", "{_header}", "{_description}", "{_body}", "{_status}")'