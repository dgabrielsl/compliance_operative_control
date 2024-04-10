import os, sys, sqlite3

from datetime import datetime
from plyer import notification

from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt

from queries import *
from excel_loads import *

os.system('cls')

class Main(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        self.ddbb()
        self.init()
        self.site()
        self.show()

    def ddbb(self):
        con = sqlite3.connect('hub.db')
        cur = con.cursor()
    
        # Users >>> CREATED / LAST_MODIFIED / CREATED_BY / USERNAME / FULLNAME / PASSWORD / DISABLED_USER / REQUESTS_PROCESSING / CREATE_NEW_LOGS / EDIT_ALL_FIELDS / DATA_LOAD / MAKE_ASSIGNMENTS / MAKE_REPORTS / ADMIN_USERS / EDIT_DICT
        try:
            cur.execute('CREATE TABLE users(CREATED VARCHAR(12), LAST_MODIFIED VARCHAR(12), CREATED_BY VARCHAR(50), USERNAME VARCHAR(30) UNIQUE, FULLNAME VARCHAR(50), PASSWORD VARCHAR(20), DISABLED_USER BOOLEAN, REQUESTS_PROCESSING BOOLEAN, CREATE_NEW_LOGS BOOLEAN, EDIT_ALL_FIELDS BOOLEAN, DATA_LOAD BOOLEAN, MAKE_ASSIGNMENTS BOOLEAN, MAKE_REPORTS BOOLEAN, ADMIN_USERS BOOLEAN, EDIT_DICT BOOLEAN)')
            time_mark = datetime.now().strftime('%d/%m/%Y %H:%M:%SH')
            rec = f'INSERT INTO users VALUES ("{time_mark}", "{time_mark}", "Developer", "system.gabriel.solano", "Gabriel Solano", "root", 0, 1, 1, 1, 1, 1, 1, 1, 1)'
            cur.execute(rec)
            con.commit()
        except Exception as e: pass

        # Sysde >>> ID / EMAIL / PHONE
        try:
            cur.execute('CREATE TABLE sysde(TIMESTAMP VARCHAR(15), TAGNAME VARCHAR(99), ID VARCHAR(25) UNIQUE, EMAIL VARCHAR(99), PHONE VARCHAR(25))')
            con.commit()
        except Exception as e: pass

        # Indicators >>> DATE_MARK / ASSIGNED / HD_REQUEST / USERNAME / START_TIME / END_TIME / CONSUMED_TIME
        try:
            cur.execute('CREATE TABLE indicators(DATE_MARK VARCHAR(12), ASSIGNED VARCHAR(12), HD_REQUEST VARCHAR(15), USERNAME VARCHAR(50), START_TIME VARCHAR(15), END_TIME VARCHAR(15), CONSUMED_TIME VARCHAR(3))')
            con.commit()
        except Exception as e: pass

        # Core >>> CREATED / TAG_NAME / SYSTEM_ASSIGNED_TO / HELPDESK / ID / DOCUMENT / CODE / CLASS_CASE / STATUS / PRODUCT / INCOME_SOURCE / WARNING_AMOUNT / CUSTOMER_PROFILE / NOTIFICATION_TYPE / CONTACT_TYPE / CUSTOMER_ANSWER / AUTHOR / ASSIGNED_TO / RESULT / UPDATED / DEADLINE / FNAME
        try:
            cur.execute('CREATE TABLE core(CREATED VARCHAR(12), TAG_NAME VARCHAR(100), SYSTEM_ASSIGNED_TO VARCHAR(30), HELPDESK VARCHAR(15) UNIQUE, ID VARCHAR(30), DOCUMENT VARCHAR(20), CODE VARCHAR(20), CLASS_CASE VARCHAR(150), STATUS VARCHAR(30), PRODUCT VARCHAR(20), INCOME_SOURCE VARCHAR(100), WARNING_AMOUNT VARCHAR(50), CUSTOMER_PROFILE VARCHAR(200), NOTIFICATION_TYPE VARCHAR(100), CONTACT_TYPE VARCHAR(150), CUSTOMER_ANSWER VARCHAR(150), AUTHOR VARCHAR(30), ASSIGNED_TO VARCHAR(30), RESULT VARCHAR(300), UPDATED VARCHAR(15), DEADLINE VARCHAR(15), FNAME VARCHAR(250))')
            con.commit()
        except Exception as e: pass

        # Trace-log >>> HELPDESK / TIME_MARK / OPERATIVE / DESCRIPTION
        try:
            cur.execute('CREATE TABLE tracelog(HELPDESK VARCHAR(12), TIME_MARK VARCHAR(12), OPERATIVE VARCHAR(99), DESCRIPTION VARCHAR(3000))')
            con.commit()
        except Exception as e: pass

        # Dictionary >>> Word
        try:
            cur.execute('CREATE TABLE dictionary(WORD VARCHAR(50) UNIQUE)')
            valueslist = ('.', ',', '+', '-', '*', '#', '_', ':', ';', '?', '!', '/', '(', ')', '[', ']', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'ingresos', 'datos', 'activar', 'alertas', 'articulo', 'artículo', 'cuentas', 'desinscrito', 'documento', 'duplicadas', 'fondos', 'fondo', 'peps', 'varios', 'smart', 'smar', 'smat', 'samrt', 'revexpedientes', 'revisiónexpediente', 'revisión', 'revision', 'expedientes', 'expediente', 'consultas', 'consulta', 'liberación', 'liberacion', 'transacción', 'transaccion', 'actualizacion', 'actualización', 'actualizar', 'alerta', 'alrta', 'aerta', 'arti', 'art', 'solicitar', 'solicitud', 'bis ', ' bis', 'captación', 'captacion', 'cancelación', 'cancelacion', 'cliente', 'colaboradora', 'colaborador', 'conducir', 'cripto', 'critico', 'crítico', 'cuenta', 'dimex', 'doc', 'duplicada', 'error', 'fatca', 'id ', ' id', 'autorización', 'autorizacion', 'inactivación', 'inactivacion', 'ingresar', 'inscrito', 'inscrita', 'licencia', 'limitada', 'línea', 'linea', 'mm ', ' mm', 'nicaragua', 'nivel', 'número', 'numero', 'origen', 'pep', 'respaldo de', 'respaldo', 'riesgo', 'serv', 'vencida', 'vencido', 'vigente', 'zero', ' por', 'aleta', 'dato', 'cancelaciión', 'actualiación', 'actualiacion', 'actualiazación', 'actualiazacion', 'vario', 'puc ', ' puc', 'cancelació', 'cancelacio', 'originación', 'originacion', 'kit ', ' kit', 'app ', ' app', 'a ln', ' ln ', 'ln ', 'lista', 'negra', 'clliente', 'bloqueo', 'parcial', 'ajuste', 'perfil', 'mensual', 'critpo', 'rev ', ' rev', ' de ', ' gg ', ' no ', ' y ', ' i ', ' s ', 'sm ', ' im ', ' b ', ' r ', 'crédito', 'credito', 'nivel de riesgo', 'guardia', 'actulización', 'actulizacion', 'kit', 'app', 'por ', 'bcr', 'doc ')
            for vl in valueslist:
                try:
                    rec = f'INSERT INTO dictionary VALUES ("{vl}")'
                    cur.execute(rec)
                except Exception as e: pass
        except Exception as e: pass

        con.commit()
        con.close()

    def init(self):
        self.setWindowIcon(QIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_ComputerIcon)))
        self.setWindowTitle('DeskPyL - ERP Compliance Operative Control')
        self.setMinimumWidth(1400)
        self.setMinimumHeight(550)
        # self.showMaximized()
        # self.setWindowFlags(Qt.WindowType.WindowMaximizeButtonHint | Qt.WindowType.WindowMinimizeButtonHint)

        menubar = self.menuBar()
        menubar.setObjectName('menu-bar')

    # (1) File.
        opt_menu_1 = menubar.addMenu('&Archivo')
        opt_menu_1.setObjectName('opt_menu_1')
        opt_menu_1.setCursor(Qt.CursorShape.PointingHandCursor)

        self.action_1_1 = QAction(QIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_DesktopIcon)), '&Inicio', self)
        self.action_1_1.setShortcut('F2')
        self.action_1_1.setStatusTip('Ir a la página de inicio.')
        self.action_1_1.triggered.connect(self.navigation)
        self.action_1_1.setDisabled(True)
        opt_menu_1.addAction(self.action_1_1)

        self.action_1_2 = QAction(QIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_DesktopIcon)), '&Cerrar sesión', self)
        self.action_1_2.setShortcut('F11')
        self.action_1_2.setStatusTip('Cierra la sesión actual, debe ingresar las credenciales para volver a iniciar sesión.')
        self.action_1_2.triggered.connect(self.logout)
        self.action_1_2.setDisabled(True)
        opt_menu_1.addAction(self.action_1_2)

        self.action_1_3 = QAction(QIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_DesktopIcon)), '&Salir', self)
        self.action_1_3.setShortcut('F12')
        self.action_1_3.setStatusTip('Cierra la aplicación.')
        self.action_1_3.triggered.connect(lambda:print(self.sender().text()))
        opt_menu_1.addAction(self.action_1_3)

    # (2) Requests.
        opt_menu_2 = menubar.addMenu('&Gestiones')
        opt_menu_2.setObjectName('opt_menu_2')
        opt_menu_2.setCursor(Qt.CursorShape.PointingHandCursor)

        self.action_2_1 = QAction(QIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_DesktopIcon)), '&Mis asignaciones', self)
        self.action_2_1.setShortcut('F5')
        self.action_2_1.setStatusTip('Ver mi bandeja de gestiones asignadas activas (pendientes de procesar).')
        self.action_2_1.triggered.connect(self.navigation)
        self.action_2_1.setDisabled(True)
        opt_menu_2.addAction(self.action_2_1)

        self.action_2_2 = QAction(QIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_DesktopIcon)), '&Registrar solicitud', self)
        self.action_2_2.setShortcut('F6')
        self.action_2_2.setStatusTip('Ingresar manualmente una nueva gestión.')
        self.action_2_2.triggered.connect(self.navigation)
        self.action_2_2.setDisabled(True)
        opt_menu_2.addAction(self.action_2_2)

    # (3) Settings.
        opt_menu_3 = menubar.addMenu('&Configuración')
        opt_menu_3.setObjectName('opt_menu_3')
        opt_menu_3.setCursor(Qt.CursorShape.PointingHandCursor)

        self.action_3_1 = QAction(QIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_DesktopIcon)), '&Administrar usuarios', self)
        self.action_3_1.setShortcut('Ctrl+U')
        self.action_3_1.setStatusTip('Crear, modificar, eliminar y configurar permisos de usuarios.')
        self.action_3_1.triggered.connect(self.navigation)
        self.action_3_1.setDisabled(True)
        opt_menu_3.addAction(self.action_3_1)

        self.action_3_2 = QAction(QIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_DesktopIcon)), '&Configurar diccionario', self)
        self.action_3_2.setShortcut('Ctrl+D')
        self.action_3_2.setStatusTip('Configurar las reglas del diccionario.')
        self.action_3_2.triggered.connect(self.navigation)
        self.action_3_2.setDisabled(True)
        opt_menu_3.addAction(self.action_3_2)

    # (4) Data analysis.
        opt_menu_4 = menubar.addMenu('&Datos')
        opt_menu_4.setObjectName('opt_menu_4')
        opt_menu_4.setCursor(Qt.CursorShape.PointingHandCursor)

        self.action_4_1 = QAction(QIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_DesktopIcon)), '&Cargar datos', self)
        self.action_4_1.setShortcut('Shift+F5')
        self.action_4_1.setStatusTip('Cargar reportes nuevos de Excel.')
        self.action_4_1.triggered.connect(self.navigation)
        self.action_4_1.setDisabled(True)
        opt_menu_4.addAction(self.action_4_1)

        self.action_4_2 = QAction(QIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_DesktopIcon)), '&Generar reportes', self)
        self.action_4_2.setShortcut('Shift+F6')
        self.action_4_2.setStatusTip('Descargar reportes de gestiones.')
        self.action_4_2.triggered.connect(self.navigation)
        self.action_4_2.setDisabled(True)
        opt_menu_4.addAction(self.action_4_2)

        self.action_4_3 = QAction(QIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_DesktopIcon)), '&Métricas', self)
        self.action_4_3.setShortcut('Shift+F7')
        self.action_4_3.setStatusTip('Números e indicadores operativos.')
        self.action_4_3.triggered.connect(self.navigation)
        self.action_4_3.setDisabled(True)
        opt_menu_4.addAction(self.action_4_3)

    # (5) Others.
        opt_menu_5 = menubar.addMenu('&Otros')
        opt_menu_5.setObjectName('opt_menu_5')
        opt_menu_5.setCursor(Qt.CursorShape.PointingHandCursor)
        opt_menu_5.setDisabled(True)

    # (6) Support.
        opt_menu_6 = menubar.addMenu('&Ayuda')
        opt_menu_6.setObjectName('opt_menu_6')
        opt_menu_6.setCursor(Qt.CursorShape.PointingHandCursor)

        self.action_6_1 = QAction(QIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_DesktopIcon)), '&Ayuda', self)
        self.action_6_1.setShortcut('F1')
        self.action_6_1.setStatusTip('Ver el manual de uso.')
        self.action_6_1.triggered.connect(self.navigation)
        opt_menu_6.addAction(self.action_6_1)

        self.action_6_2 = QAction(QIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_DesktopIcon)), '&Documentación', self)
        self.action_6_2.setShortcut('Ctrl+B')
        self.action_6_2.setStatusTip('Ver documentación del proyecto - https://github.com/dgabrielsl/compliance_operative_control')
        self.action_6_2.triggered.connect(self.navigation)
        opt_menu_6.addAction(self.action_6_2)

        self.action_6_3 = QAction(QIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_DesktopIcon)), '&Acerca De', self)
        self.action_6_3.setShortcut('Ctrl+A')
        self.action_6_3.setStatusTip('Acerca de DeskPyL')
        self.action_6_3.triggered.connect(self.navigation)
        opt_menu_6.addAction(self.action_6_3)

        self.statusbar = self.statusBar()
        self.statusbar.setObjectName('status-bar')

    def site(self):
        central_widget = QWidget()
        _central_widget = QVBoxLayout()
        _central_widget.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        central_widget.setLayout(_central_widget)
        self.setCentralWidget(central_widget)

        _header = QVBoxLayout()
        _header.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        header = QWidget()
        header.setLayout(_header)
        header.setObjectName('header')
        _central_widget.addWidget(header)

        self.deskpyl_link = QPushButton('DeskPyL ↗')
        self.deskpyl_link.setObjectName('deskpyl-link')
        self.deskpyl_link.setCursor(Qt.CursorShape.PointingHandCursor)
        self.deskpyl_link.setStatusTip('Ir al sitio web.')
        self.deskpyl_link.clicked.connect(lambda:print(self.sender().text()))

        product_name = QLabel('ERP Control Operativa Cumplimiento')
        product_name.setObjectName('product-name')
        product_name.setStatusTip('Enterprise Resource Planning')

        self.about_user = QLabel('↓↑ desconectado')
        self.about_user.setObjectName('about-user')
        self.about_user.setStatusTip('Estado de la sesión.')

        top_bar = QHBoxLayout()
        top_bar.addWidget(self.deskpyl_link)
        top_bar.addWidget(product_name)
        top_bar.addWidget(self.about_user)
        _header.addLayout(top_bar)

        _site_info = QHBoxLayout()
        site_info = QWidget()
        site_info.setLayout(_site_info)
        site_info.setObjectName('site-info')
        _central_widget.addWidget(site_info)

        self.user_location = QLabel('INGRESAR CREDENCIALES')
        self.user_location.setObjectName('user-location')
        self.user_location.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        _site_info.addWidget(self.user_location)

        self._body = QStackedLayout()
        self._body.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        body = QWidget()
        body.setLayout(self._body)
        _central_widget.addWidget(body)

        # UI: Login page.
        self.ui_login = QWidget()

        self._ui_login = QVBoxLayout()
        self._ui_login.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        self.ui_login.setLayout(self._ui_login)

        self._body.addWidget(self.ui_login)

        multimoney = QLabel('Financiera Multimoney')
        multimoney.setObjectName('multimoney')
        multimoney.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self._ui_login.addWidget(multimoney)

        self.credential_username = QLineEdit('')
        self.credential_username.setObjectName('credential-username')
        self.credential_username.setPlaceholderText('username')
        self.credential_username.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.credential_username.setFixedWidth(400)
        self._ui_login.addWidget(self.credential_username)

        self.credential_password = QLineEdit('')
        self.credential_password.setObjectName('credential-password')
        self.credential_password.setPlaceholderText('password')
        self.credential_password.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.credential_password.setFixedWidth(400)
        self.credential_password.setEchoMode(QLineEdit.EchoMode.Password)
        self._ui_login.addWidget(self.credential_password)

        self.onoff_echo_1 = QCheckBox('Mostrar contraseña')
        self.onoff_echo_1.setObjectName('onoff-echo')
        self.onoff_echo_1.setCursor(Qt.CursorShape.PointingHandCursor)
        self.onoff_echo_1.clicked.connect(self.echomode)
        self._ui_login.addWidget(self.onoff_echo_1)

        self.check_credentials = QPushButton('Ingresar')
        self.check_credentials.setFixedWidth(400)
        self.check_credentials.setCursor(Qt.CursorShape.PointingHandCursor)
        self.check_credentials.clicked.connect(self.get_logged)
        self._ui_login.addWidget(self.check_credentials)

        # UI: Logged page.
        self.ui_logged = QWidget()

        self._ui_logged = QVBoxLayout()
        self._ui_logged.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        self.ui_logged.setLayout(self._ui_logged)

        self._body.addWidget(self.ui_logged)

        self.welcome_banner = QLabel('Sesión iniciada correctamente')
        self.welcome_banner.setObjectName('welcome-banner')
        self.welcome_banner.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self._ui_logged.addWidget(self.welcome_banner)

        self.shorcut_1 = QPushButton('Mis asignaciones')
        self.shorcut_1.clicked.connect(self.action_2_1.trigger)
        self.shorcut_1.setCursor(Qt.CursorShape.PointingHandCursor)

        self.shorcut_2 = QPushButton('Registrar solicitud')
        self.shorcut_2.clicked.connect(self.action_2_2.trigger)
        self.shorcut_2.setCursor(Qt.CursorShape.PointingHandCursor)

        self.shorcut_3 = QPushButton('Asignar solicitudes')
        self.shorcut_3.clicked.connect(self.action_4_1.trigger)
        self.shorcut_3.setCursor(Qt.CursorShape.PointingHandCursor)

        hbox = QHBoxLayout()
        hbox.addWidget(self.shorcut_1)
        hbox.addWidget(self.shorcut_2)
        hbox.addWidget(self.shorcut_3)
        self._ui_logged.addLayout(hbox)

        self.shorcut_4 = QPushButton('Cargar datos')
        self.shorcut_4.clicked.connect(self.action_4_1.trigger)
        self.shorcut_4.setCursor(Qt.CursorShape.PointingHandCursor)

        self.shorcut_5 = QPushButton('Generar reportes')
        self.shorcut_5.clicked.connect(self.action_4_2.trigger)
        self.shorcut_5.setCursor(Qt.CursorShape.PointingHandCursor)

        self.shorcut_6 = QPushButton('Métricas')
        self.shorcut_6.clicked.connect(self.action_4_3.trigger)
        self.shorcut_6.setCursor(Qt.CursorShape.PointingHandCursor)

        hbox = QHBoxLayout()
        hbox.addWidget(self.shorcut_4)
        hbox.addWidget(self.shorcut_5)
        hbox.addWidget(self.shorcut_6)
        self._ui_logged.addLayout(hbox)

        self.shorcut_7 = QPushButton('Administrar usuarios')
        self.shorcut_7.clicked.connect(self.action_3_1.trigger)
        self.shorcut_7.setCursor(Qt.CursorShape.PointingHandCursor)

        self.shorcut_8 = QPushButton('Configurar diccionario')
        self.shorcut_8.clicked.connect(self.action_3_2.trigger)
        self.shorcut_8.setCursor(Qt.CursorShape.PointingHandCursor)

        self.shorcut_9 = QPushButton('Ayuda')
        self.shorcut_9.clicked.connect(self.action_6_1.trigger)
        self.shorcut_9.setCursor(Qt.CursorShape.PointingHandCursor)

        hbox = QHBoxLayout()
        hbox.addWidget(self.shorcut_7)
        hbox.addWidget(self.shorcut_8)
        hbox.addWidget(self.shorcut_9)
        self._ui_logged.addLayout(hbox)

        # UI: Assignments.
        self.ui_assignments = QWidget()

        self._ui_assignments = QVBoxLayout()
        self._ui_assignments.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        self.ui_assignments.setLayout(self._ui_assignments)

        self._body.addWidget(self.ui_assignments)

        # UI: Request log.
        self.ui_logrequest = QWidget()

        self._ui_logrequest = QVBoxLayout()
        self._ui_logrequest.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        self.ui_logrequest.setLayout(self._ui_logrequest)

        self._body.addWidget(self.ui_logrequest)

        scroll = QScrollArea()
        scroll_widget = QWidget()
        _scroll_widget = QVBoxLayout()

        hbox = QHBoxLayout()
        l = QLabel('Buscar')
        l.setStyleSheet('font-size: 15px;')

        self.logrequest_filter_field = QLineEdit()
        self.logrequest_filter_field.setObjectName('logrequest-filter-field')
        self.logrequest_filter_field.setPlaceholderText('Número de solicitud HD')
        self.logrequest_filter_field.setFixedWidth(300)

        self.logrequest_filter_btn = QPushButton('Aplicar')
        self.logrequest_filter_btn.setCursor(Qt.CursorShape.PointingHandCursor)

        hbox.addWidget(l)
        hbox.addWidget(self.logrequest_filter_field)
        hbox.addWidget(self.logrequest_filter_btn)
        hbox.setContentsMargins(0,0,0,15)

        _scroll_widget.addLayout(hbox)

        slots_hbox = QHBoxLayout()                          # Box #1 - (Solicitud, ID, Pagaré, Código)
        
        vbox_group_1 = QVBoxLayout()
        vbox_group_2 = QVBoxLayout()
        vbox_group_3 = QVBoxLayout()
        vbox_group_4 = QVBoxLayout()

        slots_hbox.addLayout(vbox_group_1)
        slots_hbox.addLayout(vbox_group_2)
        slots_hbox.addLayout(vbox_group_3)
        slots_hbox.addLayout(vbox_group_4)

        # slot_1
        shbx = QHBoxLayout()
        l = QLabel('Solicitud')
        l.setFixedWidth(80)
        l.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        shbx.addWidget(l)

        self.slot_1 = QLineEdit()
        self.slot_1.setFixedWidth(150)
        shbx.addWidget(self.slot_1)
        vbox_group_1.addLayout(shbx)

        # slot_2
        shbx = QHBoxLayout()
        l = QLabel('ID')
        l.setFixedWidth(80)
        l.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        shbx.addWidget(l)

        self.slot_2 = QLineEdit()
        self.slot_2.setFixedWidth(150)
        shbx.addWidget(self.slot_2)
        vbox_group_1.addLayout(shbx)

        # slot_3
        shbx = QHBoxLayout()
        l = QLabel('Pagaré')
        l.setFixedWidth(80)
        l.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        shbx.addWidget(l)

        self.slot_3 = QLineEdit()
        self.slot_3.setFixedWidth(150)
        shbx.addWidget(self.slot_3)
        vbox_group_1.addLayout(shbx)

        # slot_4
        shbx = QHBoxLayout()
        l = QLabel('Código')
        l.setFixedWidth(80)
        l.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        shbx.addWidget(l)

        self.slot_4 = QLineEdit()
        self.slot_4.setFixedWidth(150)
        shbx.addWidget(self.slot_4)
        vbox_group_1.addLayout(shbx)

        # slot_5
        shbx = QHBoxLayout()
        l = QLabel('Etapa')
        l.setFixedWidth(80)
        l.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        shbx.addWidget(l)

        self.slot_5 = QLineEdit()
        self.slot_5.setFixedWidth(150)
        shbx.addWidget(self.slot_5)

        vbox_group_1.addLayout(shbx)
        _scroll_widget.addLayout(slots_hbox)

        slots_hbox = QHBoxLayout()                          # Box #2 - (Asignado a, Estado, Correo, Teléfono, Autor)

        # slot_6
        shbx = QHBoxLayout()
        l = QLabel('Asignado a')
        l.setFixedWidth(80)
        l.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        shbx.addWidget(l)

        self.slot_6 = QLineEdit()
        self.slot_6.setFixedWidth(150)
        shbx.addWidget(self.slot_6)
        vbox_group_2.addLayout(shbx)

        # slot_7
        shbx = QHBoxLayout()
        l = QLabel('Estado')
        l.setFixedWidth(80)
        l.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        shbx.addWidget(l)

        self.slot_7 = QLineEdit()
        self.slot_7.setFixedWidth(150)
        shbx.addWidget(self.slot_7)
        vbox_group_2.addLayout(shbx)

        # slot_8
        shbx = QHBoxLayout()
        l = QLabel('Correo')
        l.setFixedWidth(80)
        l.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        shbx.addWidget(l)

        self.slot_8 = QLineEdit()
        self.slot_8.setFixedWidth(150)
        shbx.addWidget(self.slot_8)
        vbox_group_2.addLayout(shbx)

        # slot_9
        shbx = QHBoxLayout()
        l = QLabel('Teléfono')
        l.setFixedWidth(80)
        l.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        shbx.addWidget(l)

        self.slot_9 = QLineEdit()
        self.slot_9.setFixedWidth(150)
        shbx.addWidget(self.slot_9)
        vbox_group_2.addLayout(shbx)

        # slot_10
        shbx = QHBoxLayout()
        l = QLabel('Autor')
        l.setFixedWidth(80)
        l.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        shbx.addWidget(l)

        self.slot_10 = QLineEdit()
        self.slot_10.setFixedWidth(150)
        shbx.addWidget(self.slot_10)
        vbox_group_2.addLayout(shbx)







        scroll_widget.setLayout(_scroll_widget)
        scroll.setWidget(scroll_widget)
        self._ui_logrequest.addWidget(scroll)

        # UI: Users administration.
        self.ui_usersadmin = QWidget()

        self._ui_usersadmin = QVBoxLayout()
        self._ui_usersadmin.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        self.ui_usersadmin.setLayout(self._ui_usersadmin)

        self.existent_users = QComboBox()
        self.existent_users.setPlaceholderText('Seleccione un usuario')
        self.existent_users.setMinimumWidth(250)
        self.existent_users.setCursor(Qt.CursorShape.PointingHandCursor)

        self.existent_users_searchbt = QPushButton('Buscar')
        self.existent_users_searchbt.setCursor(Qt.CursorShape.PointingHandCursor)
        self.existent_users_searchbt.clicked.connect(self.select_user_account)

        vbox = QVBoxLayout()
        vbox.setContentsMargins(50,0,50,0)

        hbox = QHBoxLayout()
        hbox.addWidget(self.existent_users)
        hbox.addWidget(self.existent_users_searchbt)
        hbox.setContentsMargins(0,0,0,25)
        hbox.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self._ui_usersadmin.addLayout(hbox)

        l = QLabel('Usuario')
        l.setFixedWidth(120)
        self.input_username = QLineEdit()
        self.input_username.setFixedWidth(260)
        self.input_username.setPlaceholderText('formato: g.solano')
        hbox = QHBoxLayout()
        hbox.addWidget(l)
        hbox.addWidget(self.input_username)
        vbox.addLayout(hbox)

        l = QLabel('Nombre completo')
        l.setFixedWidth(120)
        self.input_fullname = QLineEdit()
        self.input_fullname.setFixedWidth(260)
        self.input_fullname.setPlaceholderText('formato: Nombre Apellido(s)')
        hbox = QHBoxLayout()
        hbox.addWidget(l)
        hbox.addWidget(self.input_fullname)
        vbox.addLayout(hbox)

        l = QLabel('Contraseña')
        l.setFixedWidth(120)
        self.input_password = QLineEdit()
        self.input_password.setFixedWidth(260)
        self.input_password.setPlaceholderText('******')
        self.input_password.setEchoMode(QLineEdit.EchoMode.Password)
        hbox = QHBoxLayout()
        hbox.addWidget(l)
        hbox.addWidget(self.input_password)
        vbox.addLayout(hbox)

        l = QLabel('Confirmar contraseña')
        l.setFixedWidth(120)
        self.input_password_confirm = QLineEdit()
        self.input_password_confirm.setFixedWidth(260)
        self.input_password_confirm.setPlaceholderText('******')
        self.input_password_confirm.setEchoMode(QLineEdit.EchoMode.Password)
        hbox = QHBoxLayout()
        hbox.addWidget(l)
        hbox.addWidget(self.input_password_confirm)
        vbox.addLayout(hbox)

        l = QLabel('Creado por')
        l.setFixedWidth(120)
        self.metadata_1 = QLabel('-')
        hbox = QHBoxLayout()
        hbox.addWidget(l)
        hbox.addWidget(self.metadata_1)
        vbox.addLayout(hbox)
        hbox.setContentsMargins(0,20,0,0)

        l = QLabel('Fecha de creación')
        l.setFixedWidth(120)
        self.metadata_2 = QLabel('-')
        hbox = QHBoxLayout()
        hbox.addWidget(l)
        hbox.addWidget(self.metadata_2)
        vbox.addLayout(hbox)

        l = QLabel('Última modificación')
        l.setFixedWidth(120)
        self.metadata_3 = QLabel('-')
        hbox = QHBoxLayout()
        hbox.addWidget(l)
        hbox.addWidget(self.metadata_3)
        vbox.addLayout(hbox)
        hbox.setContentsMargins(0,0,0,20)

        self.onoff_echo_2 = QCheckBox('Mostrar contraseña')
        self.onoff_echo_2.setObjectName('onoff-echo-2')
        self.onoff_echo_2.setCursor(Qt.CursorShape.PointingHandCursor)
        self.onoff_echo_2.clicked.connect(self.echomode_2)

        hbox = QHBoxLayout()
        hbox.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        hbox.addWidget(self.onoff_echo_2)
        vbox.addLayout(hbox)
        vbox.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        main_hbox = QHBoxLayout()
        main_hbox.addLayout(vbox)

        # Permissions.
        self.permission_1 = QCheckBox('Inhabilitar usuario')
        self.permission_2 = QCheckBox('Procesar solicitudes uno a uno')
        self.permission_3 = QCheckBox('Crear registros nuevos manualmente')
        self.permission_4 = QCheckBox('Editar todos los campos')
        self.permission_5 = QCheckBox('Cargar reportes')
        self.permission_6 = QCheckBox('Asignar solicitudes')
        self.permission_7 = QCheckBox('Generar/descargar reportes')
        self.permission_8 = QCheckBox('Administrar otros usuarios')
        self.permission_9 = QCheckBox('Editar el diccionario')

        self.permission_1.setCursor(Qt.CursorShape.PointingHandCursor)
        self.permission_2.setCursor(Qt.CursorShape.PointingHandCursor)
        self.permission_3.setCursor(Qt.CursorShape.PointingHandCursor)
        self.permission_4.setCursor(Qt.CursorShape.PointingHandCursor)
        self.permission_5.setCursor(Qt.CursorShape.PointingHandCursor)
        self.permission_6.setCursor(Qt.CursorShape.PointingHandCursor)
        self.permission_7.setCursor(Qt.CursorShape.PointingHandCursor)
        self.permission_8.setCursor(Qt.CursorShape.PointingHandCursor)
        self.permission_9.setCursor(Qt.CursorShape.PointingHandCursor)

        vbox = QVBoxLayout()
        vbox.setContentsMargins(50,0,50,0)

        vbox.addWidget(self.permission_1)
        vbox.addWidget(self.permission_2)
        vbox.addWidget(self.permission_3)
        vbox.addWidget(self.permission_4)
        vbox.addWidget(self.permission_5)
        vbox.addWidget(self.permission_6)
        vbox.addWidget(self.permission_7)
        vbox.addWidget(self.permission_8)
        vbox.addWidget(self.permission_9)

        main_hbox.addLayout(vbox)

        scroll = QScrollArea()
        scroll_widget = QWidget()
        _scroll_widget = QHBoxLayout()

        _scroll_widget.addLayout(main_hbox)

        scroll_widget.setLayout(_scroll_widget)
        scroll.setWidget(scroll_widget)
        self._ui_usersadmin.addWidget(scroll)

        self.save_user_changes = QPushButton('Guardar/Actualizar')
        self.save_user_changes.setCursor(Qt.CursorShape.PointingHandCursor)
        self.save_user_changes.clicked.connect(self.crud_user_accounts)

        self.delete_user = QPushButton('Eliminar')
        self.delete_user.setCursor(Qt.CursorShape.PointingHandCursor)
        self.delete_user.clicked.connect(self.crud_user_accounts)

        hbox = QHBoxLayout()
        hbox.addWidget(self.save_user_changes)
        hbox.addWidget(self.delete_user)
        hbox.setContentsMargins(30,30,30,30)
        hbox.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self._ui_usersadmin.addLayout(hbox)

        self._body.addWidget(self.ui_usersadmin)

        # UI: Dictionary settings.
        self.ui_dictionary = QWidget()

        self._ui_dictionary = QVBoxLayout()
        self._ui_dictionary.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        self.ui_dictionary.setLayout(self._ui_dictionary)

        self._body.addWidget(self.ui_dictionary)

        self.dict_ptext = QPlainTextEdit()
        self.dict_ptext.setObjectName('dict-ptext')
        self.dict_ptext.setPlaceholderText('Los elementos aquí guardados permiten al sistema limpiar la información del nombre del cliente al cargar reportes de HDs.')
        self._ui_dictionary.addWidget(self.dict_ptext)

        self.save_dict_params = QPushButton('Guardar cambios')
        self.save_dict_params.setCursor(Qt.CursorShape.PointingHandCursor)
        self.save_dict_params.clicked.connect(self.run_dict_changes)
        self._ui_dictionary.addWidget(self.save_dict_params)

        # UI: Load new Excel's reports.
        self.ui_dataload = QWidget()

        self._ui_dataload = QVBoxLayout()
        self._ui_dataload.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        self.ui_dataload.setLayout(self._ui_dataload)

        self.load_sysde_btn_search = QPushButton('+ SYSDE')
        self.load_sysde_btn_search.clicked.connect(self.load_books_search)
        self.load_sysde_btn_search.setFixedWidth(250)
        self.load_sysde_btn_search.setCursor(Qt.CursorShape.PointingHandCursor)

        self.load_sysde_tagname = QLineEdit()
        self.load_sysde_tagname.setPlaceholderText('Nombre de la etiqueta')

        self.load_sysde_btn_save = QPushButton('Guardar')
        self.load_sysde_btn_save.setObjectName('load_sysde_btn_save')
        self.load_sysde_btn_save.clicked.connect(self.load_books_saving)
        self.load_sysde_btn_save.setCursor(Qt.CursorShape.PointingHandCursor)

        hbox = QHBoxLayout()
        hbox.addWidget(self.load_sysde_btn_search)
        hbox.addWidget(self.load_sysde_tagname)
        hbox.addWidget(self.load_sysde_btn_save)

        self._ui_dataload.addLayout(hbox)

        self.load_hds_btn_search = QPushButton('+ Reporte de HDs')
        self.load_hds_btn_search.clicked.connect(self.load_books_search)
        self.load_hds_btn_search.setFixedWidth(250)
        self.load_hds_btn_search.setCursor(Qt.CursorShape.PointingHandCursor)

        self.load_hds_tagname = QLineEdit()
        self.load_hds_tagname.setPlaceholderText('Nombre de la etiqueta')

        self.load_hds_btn_save = QPushButton('Guardar')
        self.load_hds_btn_save.setObjectName('load_hds_btn_save')
        self.load_hds_btn_save.clicked.connect(self.load_books_saving)
        self.load_hds_btn_save.setCursor(Qt.CursorShape.PointingHandCursor)

        hbox = QHBoxLayout()
        hbox.addWidget(self.load_hds_btn_search)
        hbox.addWidget(self.load_hds_tagname)
        hbox.addWidget(self.load_hds_btn_save)

        self._ui_dataload.addLayout(hbox)

        hbox = QHBoxLayout()
        hbox.setContentsMargins(0,20,0,20)
        hbox.addWidget(QLabel('Filtrar:'))

        self.type_filter_param = QLineEdit()
        self.type_filter_param.setObjectName('type-filter-param')
        self.type_filter_param.setFixedWidth(200)

        self.apply_filters = QPushButton('Buscar')
        self.apply_filters.clicked.connect(lambda:print(self.sender().text()))
        self.apply_filters.setCursor(Qt.CursorShape.PointingHandCursor)

        self.clean_filters = QPushButton('Limpiar')
        self.clean_filters.clicked.connect(lambda:print(self.sender().text()))
        self.clean_filters.setCursor(Qt.CursorShape.PointingHandCursor)

        hbox.addWidget(self.type_filter_param)
        hbox.addWidget(self.apply_filters)
        hbox.addWidget(self.clean_filters)

        self._ui_dataload.addLayout(hbox)

        hbox.addStretch()

        scroll = QScrollArea()
        swidget = QWidget()
        self.action_table = QVBoxLayout()

        Queries.clean_table_list(self)
        Queries.action_table_list(self)

        swidget.setLayout(self.action_table)
        scroll.setWidget(swidget)

        self._ui_dataload.addWidget(scroll)

        self.commit_assignments = QPushButton('↑↓ Guardar')
        self.commit_assignments.setMaximumWidth(300)
        self.commit_assignments.setCursor(Qt.CursorShape.PointingHandCursor)
        self.commit_assignments.clicked.connect(self.manage_action_table_saving_ev)

        vbox = QVBoxLayout()
        vbox.addWidget(self.commit_assignments)
        vbox.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self._ui_dataload.addLayout(vbox)

        self._body.addWidget(self.ui_dataload)

        # UI: Download reports.
        self.ui_reports = QWidget()

        self._ui_reports = QVBoxLayout()
        self._ui_reports.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        self.ui_reports.setLayout(self._ui_reports)

        self._body.addWidget(self.ui_reports)

        # UI: Download indicators.
        self.ui_indicators = QWidget()

        self._ui_indicators = QVBoxLayout()
        self._ui_indicators.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        self.ui_indicators.setLayout(self._ui_indicators)

        self._body.addWidget(self.ui_indicators)

        self._body.setCurrentIndex(0)

        # Autologin.
        self.credential_username.setText('system.gabriel.solano')
        self.credential_password.setText('root')
        self.check_credentials.click()
        # self.action_4_1.trigger() # Data load
        # self.action_3_2.trigger() # Dictionary settings
        self.action_2_2.trigger() # Request processcing

    def echomode(self):
        if self.onoff_echo_1.isChecked(): self.credential_password.setEchoMode(QLineEdit.EchoMode.Normal)
        else: self.credential_password.setEchoMode(QLineEdit.EchoMode.Password)

    def echomode_2(self):
        if self.onoff_echo_2.isChecked():
            self.input_password.setEchoMode(QLineEdit.EchoMode.Normal)
            self.input_password_confirm.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.input_password.setEchoMode(QLineEdit.EchoMode.Password)
            self.input_password_confirm.setEchoMode(QLineEdit.EchoMode.Password)

    def get_logged(self):
        cred_username = self.credential_username.text()
        cred_password = self.credential_password.text()

        if cred_username.strip() != '' and cred_password.strip() != '':
            con = sqlite3.connect('hub.db')
            cur = con.cursor()
            cur.execute('SELECT disabled_user, username, password FROM users WHERE username = ?', (cred_username,))
            res = cur.fetchone()

            if res == None: QMessageBox.warning(self, 'DeskPyL', '\nEl nombre de usuario no existe.\t\t\n', QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok)
            else:
                if res[2] == cred_password:
                    if res[0] == 0:
                        cur.execute('SELECT username, requests_processing, create_new_logs, edit_all_fields, data_load, make_assignments, make_reports, admin_users, edit_dict, fullname FROM users WHERE username = ?', (cred_username,))
                        self.connected_user = cur.fetchone()

                        # print(self.connected_user)

                        self._body.setCurrentIndex(1)
                        self.user_location.setText('INICIO')
                        self.about_user.setText(f'↑↓ {self.connected_user[0]}')
                        self.about_user.setStyleSheet('color: #0f0;')
                        self.credential_username.setText('')
                        self.credential_password.setText('')
                        self.action_1_1.setDisabled(False)
                        self.action_1_2.setDisabled(False)

                        # 3 edit_all_fields

                        # 5 make_assignments
                        if self.connected_user[5] == 1: self.shorcut_3.setDisabled(False)
                        else: self.shorcut_3.setDisabled(True)

                        # 1 requests_processing
                        if self.connected_user[1] == 1:
                            self.action_2_1.setDisabled(False)
                            self.shorcut_1.setDisabled(False)
                        else:
                            self.action_2_1.setDisabled(True)
                            self.shorcut_1.setDisabled(True)

                        # 2 create_new_logs
                        if self.connected_user[2] == 1:
                            self.action_2_2.setDisabled(False)
                            self.shorcut_2.setDisabled(False)
                        else:
                            self.action_2_2.setDisabled(True)
                            self.shorcut_2.setDisabled(True)

                        # 7 admin_users
                        if self.connected_user[7] == 1:
                            self.action_3_1.setDisabled(False)
                            self.shorcut_7.setDisabled(False)
                        else:
                            self.action_3_1.setDisabled(True)
                            self.shorcut_7.setDisabled(True)

                        # 8 edit_dict
                        if self.connected_user[8] == 1:
                            self.action_3_2.setDisabled(False)
                            self.shorcut_8.setDisabled(False)
                        else:
                            self.action_3_2.setDisabled(True)
                            self.shorcut_8.setDisabled(True)

                        # 4 data_load
                        if self.connected_user[4] == 1:
                            self.action_4_1.setDisabled(False)
                            self.shorcut_4.setDisabled(False)
                        else:
                            self.action_4_1.setDisabled(True)
                            self.shorcut_4.setDisabled(True)

                        # 6 make_reports
                        if self.connected_user[6] == 1:
                            self.action_4_2.setDisabled(False)
                            self.action_4_3.setDisabled(False)
                            self.shorcut_5.setDisabled(False)
                            self.shorcut_6.setDisabled(False)
                        else:
                            self.action_4_2.setDisabled(True)
                            self.action_4_3.setDisabled(True)
                            self.shorcut_5.setDisabled(True)
                            self.shorcut_6.setDisabled(True)

                        self.welcome_banner.setText(f'Bienvenido(a) {self.connected_user[9]}')
                    else: QMessageBox.warning(self, 'DeskPyL', '\nEste usuario se encuentra deshabilidado, por favor contacte un administrador.\t\t\n', QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok)
                else: QMessageBox.warning(self, 'DeskPyL', '\nLa contraseña es incorrecta.\t\t\n', QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok)

            con.close()
        else: QMessageBox.warning(self, 'DeskPyL', '\nHay campos sin completar\t\t\n', QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok)

    def logout(self):
        self._body.setCurrentIndex(0)
        self.user_location.setText('INGRESAR CREDENCIALES')
        self.about_user.setText(f'↓↑ desconectado')
        self.about_user.setStyleSheet('color: #f33;')

    def navigation(self):
        _sender = self.sender().text()

        if _sender == ('&Inicio'):
            self.user_location.setText('INICIO')
            self._body.setCurrentIndex(1)

        if _sender == ('&Mis asignaciones'):
            self.user_location.setText('MIS ASIGNACIONES')
            self._body.setCurrentIndex(2)

        elif _sender == ('&Registrar solicitud'):
            self.user_location.setText('PROCESAR SOLICITUD')
            self._body.setCurrentIndex(3)

        elif _sender == ('&Administrar usuarios'):
            self.user_location.setText('ADMINISTRAR USUARIOS')
            self._body.setCurrentIndex(4)
            Queries.get_users(self)

        elif _sender == ('&Configurar diccionario'):
            self.user_location.setText('CONFIGURAR DICCIONARIO')
            self._body.setCurrentIndex(5)

            self.dict_ptext.setPlainText('')

            con = sqlite3.connect('hub.db')
            cur = con.cursor()

            cur.execute('SELECT * FROM dictionary')
            res = cur.fetchall()

            req = []

            for r in res:
                for rr in r:
                    req.append(rr)

            for r in req:
                self.dict_ptext.insertPlainText(f'{r}\n')

            self.dict_ptext.verticalScrollBar().setValue(self.dict_ptext.verticalScrollBar().maximum())

            con.close()

        elif _sender == ('&Cargar datos'):
            self.user_location.setText('CARGAR DATOS & ASIGNAR SOLICITUDES')
            self._body.setCurrentIndex(6)

        elif _sender == ('&Generar reportes'):
            self.user_location.setText('GENERAR REPORTES')
            self._body.setCurrentIndex(7)

        elif _sender == ('&Métricas'):
            self.user_location.setText('MÉTRICAS')
            self._body.setCurrentIndex(8)

        elif _sender == ('&Ayuda'): print(_sender)

        elif _sender == ('&Documentación'): print(_sender)

        elif _sender == ('&Acerca De'): print(_sender)

    def select_user_account(self):
        query = self.existent_users.currentText()

        if not query == '':
            con = sqlite3.connect('hub.db')
            cur = con.cursor()
            cur.execute('SELECT * FROM users WHERE username = ?', (query,))
            res = cur.fetchone()

            self.queued_user = list(res)
            print(self.queued_user)

            self.metadata_1.setText(self.queued_user[2])
            self.metadata_2.setText(self.queued_user[0])
            self.metadata_3.setText(self.queued_user[1])

            self.input_username.setText(self.queued_user[3])
            self.input_fullname.setText(self.queued_user[4])
            self.input_password.setText(self.queued_user[5])
            self.input_password_confirm.setText(self.queued_user[5])

            # DISABLED_USER
            if self.queued_user[6] == 1: self.permission_1.setChecked(True)
            else: self.permission_1.setChecked(False)

            # REQUESTS_PROCESSING
            if self.queued_user[7] == 1: self.permission_2.setChecked(True)
            else: self.permission_2.setChecked(False)

            # CREATE_NEW_LOGS
            if self.queued_user[8] == 1: self.permission_3.setChecked(True)
            else: self.permission_3.setChecked(False)

            # Jump EDIT_ALL_FIELDS
            if self.queued_user[9] == 1: self.permission_4.setChecked(True)
            else: self.permission_4.setChecked(False)

            # DATA_LOAD
            if self.queued_user[10] == 1: self.permission_5.setChecked(True)
            else: self.permission_5.setChecked(False)

            # MAKE_ASSIGNMENTS
            if self.queued_user[11] == 1: self.permission_6.setChecked(True)
            else: self.permission_6.setChecked(False)

            # MAKE_REPORTS
            if self.queued_user[12] == 1: self.permission_7.setChecked(True)
            else: self.permission_7.setChecked(False)

            # ADMIN_USERS
            if self.queued_user[13] == 1: self.permission_8.setChecked(True)
            else: self.permission_8.setChecked(False)

            # EDIT_DICT
            if self.queued_user[14] == 1: self.permission_9.setChecked(True)
            else: self.permission_9.setChecked(False)

            self.system_user_validation()

            con.close()
        else:
            self.statusbar.showMessage('No se ha seleccionado un usuario para consultar',3000)
            self.existent_users.showPopup()

    def system_user_validation(self):
        if self.existent_users.currentText() == 'system.gabriel.solano':
            self.permission_1.setDisabled(True)
            self.permission_2.setDisabled(True)
            self.permission_3.setDisabled(True)
            self.permission_4.setDisabled(True)
            self.permission_5.setDisabled(True)
            self.permission_6.setDisabled(True)
            self.permission_7.setDisabled(True)
            self.permission_8.setDisabled(True)
            self.permission_9.setDisabled(True)

            self.input_username.setDisabled(True)
            self.input_fullname.setDisabled(True)
            self.input_password.setDisabled(True)
            self.input_password_confirm.setDisabled(True)

            self.onoff_echo_2.setDisabled(True)

            self.save_user_changes.setDisabled(True)
            self.delete_user.setDisabled(True)

            self.statusbar.showMessage('Usuario de sistema, no puede ser modificado o eliminado.')

        else:
            self.permission_1.setDisabled(False)
            self.permission_2.setDisabled(False)
            self.permission_3.setDisabled(False)
            self.permission_4.setDisabled(False)
            self.permission_5.setDisabled(False)
            self.permission_6.setDisabled(False)
            self.permission_7.setDisabled(False)
            self.permission_8.setDisabled(False)
            self.permission_9.setDisabled(False)

            self.input_username.setDisabled(False)
            self.input_fullname.setDisabled(False)
            self.input_password.setDisabled(False)
            self.input_password_confirm.setDisabled(False)

            self.onoff_echo_2.setDisabled(False)

            self.save_user_changes.setDisabled(False)
            self.delete_user.setDisabled(False)

            self.statusbar.showMessage('')

    def crud_user_accounts(self):
        Queries.check_username(self)
        Queries.get_users(self)

    def manage_action_table_saving_ev(self):
        Queries.write_changes(self)
        Queries.clean_table_list(self)
        Queries.action_table_list(self)
        self.statusbar.showMessage('Cambios aplicados correctamente',3000)

    def load_books_search(self):
        if self.sender().text() == '+ SYSDE':
            try: 
                Excel.load_sysde(self)
            except Exception as e:
                print(e)
                QMessageBox.information(self, 'DeskPyL', f'\nPor favor verifique el reporte de Excel, debe cargar un reporte de datos de SYSDE\t\t\t\n', QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok)
        else:
            try:
                Excel.load_hds(self)
            except Exception as e:
                print(e)
                QMessageBox.information(self, 'DeskPyL', f'\nPor favor verifique el reporte de Excel, debe cargar un reporte de datos de HDs\t\t\t\n', QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok)

    def load_books_saving(self):
        if self.sender().objectName() == 'load_sysde_btn_save':
            try: Excel.save_sysde(self)
            except Exception as e: QMessageBox.information(self, 'DeskPyL', f'\nPor favor verifique el reporte de Excel, debe cargar un reporte de datos de SYSDE\t\t\t\n', QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok)
        else:
            try:
                Excel.save_hdsreport(self)
                self.statusbar.showMessage('🐛 Aviso de bug: se requiere reiniciar la aplicación.')
            except Exception as e: QMessageBox.information(self, 'DeskPyL', f'\nPor favor verifique el reporte de Excel, debe cargar un reporte de datos de HDs\t\t\t\n', QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok)

    def run_dict_changes(self):
        con = sqlite3.connect('hub.db')
        cur = con.cursor()

        cur.execute('DELETE FROM dictionary')

        valueslist = self.dict_ptext.toPlainText().split('\n')

        for vl in valueslist:
            if vl.strip() != '':
                try: cur.execute('INSERT INTO dictionary VALUES(?)', (vl,))
                except Exception as e: pass

        self.dict_ptext.verticalScrollBar().setValue(self.dict_ptext.verticalScrollBar().maximum())

        con.commit()
        con.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet("""
            QWidget{
                background: #111;
                color: #fff;
            }
            QPushButton{
                padding: 5px 50px;
                background: #003600;
                color: #0f0;
                font-size: 15px;
                border: 1px solid #0f0;
                border-radius: 5px;
            }
            QPushButton:hover,
            QPushButton:focus{
                background: #050;
                color: #fff;
                border: 1px solid #fff;
            }
            QPushButton:disabled{
                background: #222;
                color: #888;
                border: 1px solid #888;
            }
            QComboBox{
                margin: 0 10px;
                padding: 5px 10px;
                background: #041;
                color: #0f0;
                border: 1px solid #0f0;
                border-radius: 5px;
            }
            QLineEdit{
                padding: 5px;
                background: #333;
                font-size: 14px;
                border: 1px solid #0f0;
                border-radius: 5px;
                selection-color: #000;
                selection-background-color: #0f0;
            }
            QLineEdit:hover, QLineEdit:focus{
                background: #222;
                color: #0f0;
            }
            QLineEdit:disabled{
                background: #222;
                color: #888;
                border: 1px solid #888;
            }
            QCheckBox:hover{
                color: #afa;
            }
            QCheckBox:checked{
                color: #0f0;
            }
            QCheckBox:disabled{
                color: #888;
            }
            QScrollArea{
                border: none;
            }
            #menu-bar,
            #status-bar{
                padding: 3px;
                background: #021;
                color: #0fa;
                font-size: 13px;
                font-family: Segoe-UI;
            }
            #menu-bar::disabled{
                color: #0a5;
            }
            #menu-bar::item:selected{
                color: #0f0;
                border-bottom: 1px solid #0f0;
            }
            #opt_menu_1, #opt_menu_2, #opt_menu_3, #opt_menu_4, #opt_menu_5, #opt_menu_6{
                color: #0fa;
            }
            #opt_menu_1:item:selected, #opt_menu_2:item:selected, #opt_menu_3:item:selected, #opt_menu_4:item:selected, #opt_menu_5:item:selected, #opt_menu_6:item:selected{
                background: #fff;
                color: #000;
            }
            #opt_menu_1:item:disabled, #opt_menu_2:item:disabled, #opt_menu_3:item:disabled, #opt_menu_4:item:disabled, #opt_menu_5:item:disabled, #opt_menu_6:item:disabled{
                color: #0a5;
            }
            #opt_menu_1:item:disabled:selected, #opt_menu_2:item:disabled:selected, #opt_menu_3:item:disabled:selected, #opt_menu_4:item:disabled:selected, #opt_menu_5:item:disabled:selected, #opt_menu_6:item:disabled:selected{
                background: #111;
            }
            #header{
                background: #222;
                border-radius: 5px;
            }
            #deskpyl-link{
                background: #222;
                color: #ffd600;
                border: none;
            }
            #deskpyl-link:hover{
                color: #ffa600;
            }
            #product-name{
                background: #222;
                font-size: 15px;
            }
            #about-user{
                background: #222;
                color: #f33;
            }
            #site-info{
                background: #333;
                border-radius: 5px;
            }
            #user-location{
                padding: 12px;
                background: #333;
                font-size: 16px;
            }
            #multimoney{
                margin-top: 25px;
                padding: 5px;
                color: #333;
                font-weight: 500;
                letter-spacing: 3px;
                font-size: 25px;
            }
            #credential-username, #credential-password{
                margin: 5px;
                padding: 5px;
                background: #fff;
                color: #000;
                font-size: 14px;
                border-radius: 15px;
            }
            #onoff-echo{
                padding: 15px;
            }
            #welcome-banner{
                margin: 15px;
                color: #777;
                font-size: 14px;
                font-style: italic;
            }
            #onoff-echo-2{
                padding: 15px 10px;
            }
            #type-filter-param{
                padding: 3px 8px;
                background: #d9d9d9;
                color: #000;
                border: none;
                border-radius: 9px;
            }
            #scroll-action-table{
                background: #000;
                border: 1px solid #60a15f;
                border-radius: 2px;
            }
            #logrequest-filter-field{
                margin: 0 5px;
                padding: 5px 8px;
                background: #535353;
                color: #fff;
            }
            #dict-ptext{
                padding: 5px;
                background: #010;
                color: #0a0;
                font-size: 15px;
                border: 1px solid #0f0;
                border-radius: 5px;
                selection-color: #050;
                selection-background-color: #fff;
            }
        """)
    win = Main()
    sys.exit(app.exec())