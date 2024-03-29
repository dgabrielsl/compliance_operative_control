import sqlite3

from PyQt6.QtWidgets import QHBoxLayout, QLabel, QComboBox
from PyQt6.QtCore import Qt
from datetime import datetime

from text import *

class Queries():
    def __init__(self):
        super().__init__()

    def get_users(self):
        self.existent_users.clear()

        con = sqlite3.connect('hub.db')
        cur = con.cursor()
        cur.execute('SELECT * FROM users')
        res = cur.fetchall()

        for i in res:
            self.existent_users.addItem(i[3])

        con.close()

    def check_username(self):
        def cleanup():
            self.input_username.setText('')
            self.input_fullname.setText('')
            self.input_password.setText('')
            self.input_password_confirm.setText('')

            self.metadata_1.setText('-')
            self.metadata_2.setText('-')
            self.metadata_3.setText('-')

            self.permission_1.setChecked(False)
            self.permission_2.setChecked(False)
            self.permission_3.setChecked(False)
            self.permission_4.setChecked(False)
            self.permission_5.setChecked(False)
            self.permission_6.setChecked(False)
            self.permission_7.setChecked(False)
            self.permission_8.setChecked(False)
            self.permission_9.setChecked(False)

            if self.onoff_echo_2.isChecked(): self.onoff_echo_2.click()

        _sender = self.sender().text()

        con = sqlite3.connect('hub.db')
        cur = con.cursor()

        username = self.input_username.text()

        cur.execute('SELECT * FROM users WHERE username = ?', (username,))
        res = cur.fetchone()

        Text.check_inputs(self)

        time_mark = datetime.now().strftime('%d/%m/%Y %H:%M:%SH')
        __creator = self.connected_user[0]
        __username = self.input_username.text().lower()
        __fullname = self.input_fullname.text().title()
        __password = self.input_password.text()

        if not res == None:
            if _sender == 'Guardar/Actualizar':
                    time_mark = datetime.now().strftime('%d/%m/%Y %H:%M:%SH')
                    rec = f'UPDATE users SET last_modified = "{time_mark}", created_by = "{__creator}", username = "{__username}", fullname = "{__fullname}", password = "{__password}", disabled_user = {self.permission_1.isChecked()}, requests_processing = {self.permission_2.isChecked()}, create_new_logs = {self.permission_3.isChecked()}, edit_all_fields = {self.permission_4.isChecked()}, data_load = {self.permission_5.isChecked()}, make_assignments = {self.permission_6.isChecked()}, make_reports = {self.permission_7.isChecked()}, admin_users = {self.permission_8.isChecked()}, edit_dict = {self.permission_9.isChecked()} WHERE username = ?'
                    cur.execute(rec,(username,))
                    con.commit()

            elif _sender == 'Eliminar':
                cur.execute(f'DELETE FROM users WHERE username = ?', (username,))
                self.statusbar.showMessage(f'Se ha eliminado el usuario «{username}» correctamente.')

            cleanup()

        else:
            if self.input_username.text().strip() == '' or self.input_fullname.text().strip() == '' or self.input_password.text().strip() == '' or self.input_password_confirm.text().strip() == '':
                QMessageBox.warning(self, 'DeskPyL', '\nHay campos sin completar, todos los campos son obligatorios.\t\t\n', QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok)
            else:
                if len(self.output_errors_message) == 0:
                    rec = f'INSERT INTO users VALUES ("{time_mark}", "{time_mark}", "{__creator}", "{__username}", "{__fullname}", "{__password}", {self.permission_1.isChecked()}, {self.permission_2.isChecked()}, {self.permission_3.isChecked()}, {self.permission_4.isChecked()}, {self.permission_5.isChecked()}, {self.permission_6.isChecked()}, {self.permission_7.isChecked()}, {self.permission_8.isChecked()}, {self.permission_9.isChecked()})'
                    cur.execute(rec)
                    cleanup()

                else: print(self.output_errors_message)

        con.commit()
        con.close()

    def clean_table_list(self):
        if self.action_table.count() > 0:
            while self.action_table.count():
                child = self.action_table.takeAt(0)
                if child.widget(): child.widget().deleteLater()

        hbox = QHBoxLayout()

        def lbl_1(lbl):
            l = QLabel(lbl)
            l.setStyleSheet('padding: 3px 30px; background: #e1efe1; color: #495; border-bottom: 3px solid #495; border-radius: 3px;')
            l.setFixedHeight(25)
            l.setFixedWidth(200)
            l.setAlignment(Qt.AlignmentFlag.AlignHCenter)
            hbox.addWidget(l)

        lbl_1('Solicitud')
        lbl_1('Identificación')
        lbl_1('Tipo de caso')
        lbl_1('Producto')
        lbl_1('Asignado a')
        lbl_1('Acción')

        hbox.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.action_table.addLayout(hbox)

    def action_table_list(self):
        con = sqlite3.connect('hub.db')
        cur = con.cursor()

        cur.execute('SELECT fullname FROM users')
        fname_users = cur.fetchall()
        self.fname_users = []

        for item in fname_users:
            for i in item:
                self.fname_users.append(i)

        cur.execute('SELECT helpdesk, id, class_case, product, assigned_to FROM core WHERE system_assigned_to = ?', ('Pendiente',))

        res = cur.fetchall()

        for rs in res:
            hbox = QHBoxLayout()

            for r in rs:
                object = QLabel(f'{r}')

                if rs.index(r) == 4: name_cb = rs[0]

                object.setStyleSheet('padding: 3px; background: #effaef; color: #000; border-bottom: 1px solid #050;')
                object.setFixedHeight(25)
                object.setAlignment(Qt.AlignmentFlag.AlignHCenter)
                hbox.addWidget(object)

            cb = QComboBox()
            cb.setCurrentIndex(0)
            cb.setObjectName(name_cb)
            cb.setCursor(Qt.CursorShape.PointingHandCursor)
            cb.addItem('Pendiente')
            cb.addItem('Seguimiento')
            cb.addItem('Completado')
            for fn in self.fname_users:
                cb.addItem(fn)

            hbox.addWidget(cb)

            self.action_table.addLayout(hbox)
            self.action_table.setAlignment(Qt.AlignmentFlag.AlignTop)
            hbox.setAlignment(Qt.AlignmentFlag.AlignTop)

        con.close()

    def write_changes(self):
        self.cbox_collector = []

        for i in range(self.action_table.count()):
            sublayout = self.action_table.itemAt(i)
            if i > 0:
                for widget in range(sublayout.count()):
                    widget = sublayout.itemAt(widget)
                    if widget.widget().objectName(): self.cbox_collector.append(widget.widget())

        con = sqlite3.connect('hub.db')
        cur = con.cursor()

        for item in self.cbox_collector:
            if item.currentText() != 'Pendiente':
                write = f'UPDATE core SET system_assigned_to = "{item.currentText()}" WHERE helpdesk = {item.objectName()}'
                cur.execute(write)

                time_mark = datetime.now().strftime('%d/%m/%Y %H:%M:%SH')
                description = f'Cambio de asignación / [Pendiente] → [{item.currentText()}]'
                write = f'INSERT INTO tracelog VALUES ("{item.objectName()}", "{time_mark}", "{self.connected_user[0]}", "{description}")'
                cur.execute(write)

        if self.action_table.count() > 0:
            while self.action_table.count():
                child = self.action_table.takeAt(0)
                while child.count() > 0:
                    subchild = child.takeAt(0)
                    subchild.widget().deleteLater()
                child.deleteLater()

        con.commit()
        con.close()