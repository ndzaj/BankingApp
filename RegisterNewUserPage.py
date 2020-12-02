import bankgui
import userDetailsDict as udd

from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from functools import partial

class RegisterNewUserPage(QWidget):
    def __init__(self):
        super().__init__()
        self.generalLayout = QVBoxLayout()
        self._newUserForm()
        self.setLayout(self.generalLayout)

    def _newUserForm(self):
        """Create the new user form"""
        self.heading = QLabel()
        self.heading.setText('Complete the form below to register a new account')
        self.generalLayout.addWidget(self.heading)

        self.form = QFormLayout()
        self.name = QLineEdit()
        self.username = QLineEdit()
        self.password = QLineEdit()
        self.form.addRow("Name:", self.name)
        self.form.addRow("Username:", self.username)
        self.form.addRow("Password:", self.password)
        self.generalLayout.addLayout(self.form)
        self.btns = QHBoxLayout()
        self.back_btn = QPushButton('Back')
        self.clear_btn = QPushButton('Clear')
        self.register_btn = QPushButton('Register')
        self.btns.addWidget(self.back_btn)
        self.btns.addWidget(self.clear_btn)
        self.btns.addWidget(self.register_btn)
        self.generalLayout.addLayout(self.btns)
        
    def _clearForm(self):
        self.name.setText('')
        self.username.setText('')
        self.password.setText('')
