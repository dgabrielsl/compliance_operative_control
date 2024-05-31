import os
import sqlite3

from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QScrollArea
from PyQt6.QtCore import Qt, QDate
from datetime import datetime
from dates import *

class Dashboard():
    def __init__(self):
        self.get_reqclicked_request()
        self.clear_layouts()
        self.get_requests()
        super().__init__()

    def clicked_request(self):
        print(True)
    
    def clear_layouts(self):
        if self._ui_assignments.count() is not None:
            while self._ui_assignments.count():
                child = self._ui_assignments.takeAt(0)
                if child.widget() is not None:
                    child.widget().deleteLater()
                elif child.layout() is not None:
                    while child.count():
                        subchild = child.takeAt(0)
                        subchild.widget().deleteLater()
                    child.layout().deleteLater()

    def get_requests(self):
        con = sqlite3.connect('hub.db')
        cur = con.cursor()
        query = self.connected_user[-1]
        cur.execute('SELECT * FROM core WHERE system_assigned_to = ?',(query,))
        res = cur.fetchall()

        self.res_panel_1 = []
        self.res_panel_2 = []
        self.res_panel_2_temp = []

        for r in res:
            if r[8] == 'Nueva': self.res_panel_1.append(r[3])
            elif r[8] == 'En curso':
                self.res_panel_2_temp.append(r[3])
                self.res_panel_2.append(r[3])

        for rp2t in self.res_panel_2_temp:
            cur.execute('SELECT updated, deadline FROM core WHERE helpdesk = ?',(rp2t,))
            res = cur.fetchone()

            datetocheck = res[0]
            datetocheck = datetocheck.split(' ')
            datetocheck = datetocheck[0]
            datetocheck = datetocheck.split('/')
            datetocheck = f'{datetocheck[2]}{datetocheck[1]}{datetocheck[0]}'

            datestamp = datetime.now().strftime('%Y%m%d')

            print()

            if int(datetocheck) <= int(datestamp): print(datetocheck,datestamp,'DATETOCHECK es de ayer o anterior')
            elif int(datetocheck) == int(datestamp): print('datetocheck,datestamp,DATETOCHECK es de hoy (mostrar en bandeja de seguimientos)')
            else: print(datetocheck,datestamp,'DATETOCHECK es mayor a hoy, NO mostrar aún en seguimientos')




        con.close()

        scroll = QScrollArea()
        scroll_widget = QWidget()
        _scroll_widget = QVBoxLayout()
        self.my_dahsboard = QHBoxLayout()

        vbox1 = QVBoxLayout()
        vbox2 = QVBoxLayout()
        vbox3 = QVBoxLayout()

        vbox1.setAlignment(Qt.AlignmentFlag.AlignTop)
        vbox2.setAlignment(Qt.AlignmentFlag.AlignTop)
        vbox3.setAlignment(Qt.AlignmentFlag.AlignTop)

        def panel_title(txt,lyt):
            tt = QLabel(txt)
            tt.setMinimumWidth(250)
            tt.setAlignment(Qt.AlignmentFlag.AlignHCenter)
            tt.setStyleSheet('margin: .5em 0; padding: .5em; background: #ddd; color: #222; border-radius: 5px;')
            lyt.addWidget(tt)

        panel_title('NUEVAS',vbox1)
        panel_title('EN SEGUIMIENTO',vbox2)
        panel_title('VENCIDAS',vbox3)

        self.collected_request_btns = []

        for rp1 in range(len(self.res_panel_1)):
            object = QPushButton(self.res_panel_1[rp1], cursor=Qt.CursorShape.PointingHandCursor)
            object.setObjectName(self.res_panel_1[rp1])
            object.setStyleSheet('margin: 0; padding: 2px 0; background: #222; color: #0f0; text-align: left; border: none; border-radius: 0;')
            self.collected_request_btns.append(object)
            vbox1.addWidget(object)

        for rp2 in range(len(self.res_panel_2)):
            object = QPushButton(self.res_panel_2[rp2], cursor=Qt.CursorShape.PointingHandCursor)
            object.setObjectName(self.res_panel_2[rp2])
            object.setStyleSheet('margin: 0; padding: 2px 0; background: #222; color: #0f0; text-align: left; border: none; border-radius: 0;')
            self.collected_request_btns.append(object)
            vbox2.addWidget(object)

            # vbox3.addWidget(QLabel(self.res_panel_1[rp1]))

        self.my_dahsboard.addLayout(vbox1)
        self.my_dahsboard.addLayout(vbox2)
        self.my_dahsboard.addLayout(vbox3)

        _scroll_widget.addLayout(self.my_dahsboard)
        scroll_widget.setLayout(_scroll_widget)
        scroll.setWidget(scroll_widget)
        scroll.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self._ui_assignments.addWidget(scroll)

    def get_number_req(self):
        import os
        os.system('cls')
        self.action_2_2.trigger()

        con = sqlite3.connect('hub.db')
        cur = con.cursor()

        query = self.active_request
        cur.execute('SELECT * FROM core WHERE helpdesk = ?',(query,))
        res = cur.fetchone()
        self.active_request = list(res[3:])

        query = res[4]
        cur.execute('SELECT email, phone FROM sysde WHERE id = ?',(query,))
        res = cur.fetchone()

        if res is not None: self.sysde_email_phone = list(res)
        else: self.sysde_email_phone = []

        _to_clean = [self.slot_1, self.slot_2, self.slot_3, self.slot_4, self.slot_7, self.slot_8, self.slot_9, self.slot_11, self.slot_12, self.slot_13, self.slot_14, self.slot_15, self.slot_16, self.slot_17, self.slot_18, self.slot_19, self.slot_20]

        for tc in _to_clean:
            tc.setText('')

        self.user_location.setText(f'PROCESAR SOLICITUD ({self.active_request[18]})')

        self.slot_1.setText(self.active_request[0])
        self.slot_2.setText(self.active_request[1])
        self.slot_3.setText(self.active_request[2])
        self.slot_4.setText(self.active_request[3])

        try: self.slot_6.setCurrentText(self.active_request[5])
        except Exception as e: pass

        if len(self.sysde_email_phone) > 0:
            self.slot_7.setText(self.sysde_email_phone[0])
            self.slot_8.setText(self.sysde_email_phone[1])

        self.slot_9.setText(self.active_request[13])

        if self.active_request[17] != '':
            date = self.active_request[17].split('/')
            self.slot_10.setDate(QDate(int(date[2]),int(date[1]),int(date[0])))
        else: self.slot_10.setDate(QDate(2000,1,1))

        # for ar in self.active_request:
        #     print(f'{self.active_request.index(ar)}\t::\t{ar}')

        self.slot_11.setText(self.active_request[11])
        self.slot_12.setText(self.active_request[10])
        self.slot_13.setText(self.active_request[6])
        self.slot_15.setText(self.active_request[9])
        self.slot_16.setText(self.active_request[7])
        self.slot_17.setText(self.active_request[8])
        self.slot_18.setText(self.active_request[16])
        self.slot_19.setText(self.active_request[15])
        self.slot_20.setText(self.active_request[19])

        con.close()
    
    def indicators(self):
        self.indicator_row = []

        self.indicator_row.append(datetime.now().strftime('%d/%m/%Y'))
        self.indicator_row.append(self.connected_user[-1])
        self.indicator_row.append(self.active_request[0])
        self.indicator_row.append(self.connected_user[0])
        self.indicator_row.append(datetime.now().strftime('%H:%M:%S'))

    def run_update(self):
        self.tracelog_row = []

        self.tracelog_row.append(self.active_request[0])

        time_mark = datetime.now().strftime('%d/%m/%Y %H:%M:%SH')
        self.tracelog_row.append(time_mark)

        self.tracelog_row.append(self.connected_user[-1])

        self.grouped_description = []

        if self.slot_2.text() != self.active_request[1]: self.grouped_description.append(f'(IDENTIFICACIÓN / {self.slot_2.text()})')
        if self.slot_3.text() != self.active_request[2]: self.grouped_description.append(f'(PAGARÉ / {self.slot_3.text()})')
        if self.slot_4.text() != self.active_request[3]: self.grouped_description.append(f'(CÓDIGO / {self.slot_4.text()})')

        con = sqlite3.connect('hub.db')
        cur = con.cursor()
        query = self.active_request[0]
        cur.execute('SELECT system_assigned_to FROM core WHERE helpdesk = ?',(query,))
        res = cur.fetchone()

        if self.slot_5.currentText() != res[0]: self.grouped_description.append(f'(ASIGNADO A / {res[0]})')
        if self.slot_6.currentText() != self.active_request[5]: self.grouped_description.append(f'(ESTADO / {self.slot_6.currentText()})')

        try:
            if self.slot_7.text() != self.sysde_email_phone[0]: self.grouped_description.append(f'(CORREO / {self.slot_7.text()})')
        except Exception as e: pass
        try:
            if self.slot_8.text() != self.sysde_email_phone[1]: self.grouped_description.append(f'(TELEFONO / {self.slot_8.text()})')
        except Exception as e: pass

        if self.slot_10.text() != '01/01/2000': self.grouped_description.append(f'(PRÓRROGA / {self.slot_10.text()})')
        if self.slot_11.text() != self.active_request[11]: self.grouped_description.append(f'(CONTACTO / {self.slot_11.text()})')
        if self.slot_12.text() != self.active_request[10]: self.grouped_description.append(f'(TIPO DE CONTACTO / {self.slot_12.text()})')
        if self.slot_13.text() != self.active_request[6]: self.grouped_description.append(f'(PRODUCTO / {self.slot_13.text()})')
        # if self.slot_14.text() != self.active_request[*]: self.grouped_description.append(f'(SALDO / {self.slot_14.text()})')
        if self.slot_15.text() != self.active_request[9]: self.grouped_description.append(f'(PERFIL / {self.slot_15.text()})')
        if self.slot_16.text() != self.active_request[7]: self.grouped_description.append(f'(ORIGEN FONDOS / {self.slot_16.text()})')
        if self.slot_17.text() != self.active_request[8]: self.grouped_description.append(f'(MONTO ALERTA / {self.slot_17.text()})')
        if self.slot_18.text() != self.active_request[16]: self.grouped_description.append(f'(ACTUALIZADO / {time_mark})')
        if self.slot_19.text() != self.active_request[15]: self.grouped_description.append(f'(RESULTADO GESTION / {self.slot_19.text()})')
        if self.slot_20.text() != self.active_request[19]: self.grouped_description.append(f'(PERIODO ALERTA / {self.slot_20.text()})')

        if self.remark_pannel.toPlainText().strip() != '': self.grouped_description.append(f'(COMENTARIOS / {self.remark_pannel.toPlainText()})')
        else: self.grouped_description.append(f'(COMENTARIOS / {time_mark} No se ingresan comentarios)')

        self.grouped_description = ' '.join(self.grouped_description)
        self.tracelog_row.append(self.grouped_description)

        cur.execute('INSERT INTO tracelog VALUES(?,?,?,?)',(self.tracelog_row))
        con.commit()
        con.close()

    def core(self):
        con = sqlite3.connect('hub.db')
        cur = con.cursor()

        query = self.active_request[1]
        rec = f'UPDATE sysde SET email = "{self.slot_7.text()}", phone = "{self.slot_8.text()}" WHERE id = ?'
        cur.execute(rec,(query,))
        con.commit()

        query = self.active_request[0]

        tm = datetime.now().strftime('%d/%m/%Y %H:%M:%SH')
        rec = f'UPDATE core SET id = "{self.slot_2.text()}", document = "{self.slot_3.text()}", code = "{self.slot_4.text()}", system_assigned_to = "{self.slot_5.currentText()}", status = "{self.slot_6.currentText()}", deadline = "{self.slot_10.text()}", contact_type = "{self.slot_11.text()}", notification_type = "{self.slot_12.text()}", product = "{self.slot_13.text()}", customer_profile = "{self.slot_15.text()}", income_source = "{self.slot_16.text()}", warning_amount = "{self.slot_17.text()}", updated = "{tm}", result = "{self.slot_19.text()}", warning_period = "{self.slot_20.text()}" WHERE helpdesk = ?'
        cur.execute(rec,(query,))
        con.commit()

        if len(self.indicator_row) == 5: self.indicator_row.append(datetime.now().strftime('%H:%M:%S'))
        elif len(self.indicator_row) == 6: self.indicator_row[5] = datetime.now().strftime('%H:%M:%S')

        if len(self.indicator_row) == 6: self.indicator_row.append('')

        # print(f'self.indicator_row // \t{self.indicator_row}')

        cur.execute('INSERT INTO indicators VALUES(?,?,?,?,?,?,?)',(self.indicator_row))

        con.commit()
        con.close()

        self.action_2_1.trigger()
