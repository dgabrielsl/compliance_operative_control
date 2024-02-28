import os, re
from PyQt6.QtWidgets import QMessageBox

class Text():
    def __init__(self):
        super().__init__()

    def check_inputs(self):
        os.system('cls')

        self.output_errors_message = []

        _input_username = self.input_username.text()
        _input_fullname = self.input_fullname.text()
        _input_password = self.input_password.text()
        _input_password_confirm = self.input_password_confirm.text()

        if not re.search(r'^(\D{1}[.]{1}){1}(\D{4,15})',_input_username): self.output_errors_message.append('\nEl campo USUARIO tiene un formato incorrecto, ejemplo del formato correcto: "p.castro"\t')

        if re.search(r'\s',_input_username): self.output_errors_message.append('\nEl campo USUARIO tiene espacios en blanco.\t')

        if len(_input_username) < 6 or len(_input_username) > 12: self.output_errors_message.append(f'\nEl nombre de usuario debe contener mínimo 6 letras y máximo 12 (tiene {len(_input_username)}).\t')

        if len(_input_fullname) < 6 or len(_input_fullname) > 50: self.output_errors_message.append(f'\nEl campo NOMBRE COMPLETO debe contener mínimo 6 letras y máximo 50 (tiene {len(_input_fullname)}).\t')

        if _input_password != _input_password_confirm: self.output_errors_message.append('\nLas contraseñas no coinciden.\t')

        if len(_input_password) < 6 or len(_input_password) > 12: self.output_errors_message.append(f'\nLa contraseña debe contener mínimo 8 letras y máximo 12 (tiene {len(_input_password)}).\t')

        if len(self.output_errors_message) == 0:
            QMessageBox.warning(
                self, 'DeskPyL',
                f'\nEl usuario «{_input_username.lower()}» se ha creado/actualizado correctamente.\t\n',
                QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok)
            self.statusbar.showMessage(f'El usuario «{_input_username.lower()}» se ha creado/actualizado correctamente.')

        else:
            response = ''

            for i in self.output_errors_message:
                response += i

            QMessageBox.warning(
                self, 'DeskPyL',
                f'Por favor corrija los siguientes campos:\n{response}',
                QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok)