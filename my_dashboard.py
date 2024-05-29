import sqlite3

from PyQt6.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout, QScrollArea
from PyQt6.QtCore import Qt

class Dashboard():
    def __init__(self):
        super().__init__()
    
    def clear_layouts(self):
        # if self.reqs_dboard_1_l.count() is not None:
        #     while self.reqs_dboard_1_l.count():
        #         child = self.reqs_dboard_1_l.takeAt(0)
        #         child.widget().deleteLater()
        pass

    def get_requests(self):
        con = sqlite3.connect('hub.db')
        cur = con.cursor()
        query = self.connected_user[-1]
        query = 'Paola Castro'

        cur.execute('SELECT * FROM core WHERE system_assigned_to = ?',(query,))
        res = cur.fetchall()

        self.res_panel_1 = []
        # self.res_panel_2 = []

        for r in res:
            if r[8] == 'Nueva': self.res_panel_1.append(r[3])
            elif r[8] == 'En curso': self.res_panel_2.append(r[3])

        print(self.res_panel_1)

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

        for rp1 in range(len(self.res_panel_1)):
            # vbox1.addWidget(QLabel(self.res_panel_1[rp1]))
            vbox2.addWidget(QLabel(self.res_panel_1[rp1]))
            vbox2.addWidget(QLabel(self.res_panel_1[rp1]))
            vbox2.addWidget(QLabel(self.res_panel_1[rp1]))
            # vbox3.addWidget(QLabel(self.res_panel_1[rp1]))

        self.my_dahsboard.addLayout(vbox1)
        self.my_dahsboard.addLayout(vbox2)
        self.my_dahsboard.addLayout(vbox3)

        _scroll_widget.addLayout(self.my_dahsboard)
        scroll_widget.setLayout(_scroll_widget)
        scroll.setWidget(scroll_widget)
        scroll.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self._ui_assignments.addWidget(scroll)

        con.close()