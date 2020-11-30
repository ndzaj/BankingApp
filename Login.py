import bankcontent as bc

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QDialogButtonBox
from PyQt5.QtWidgets import QHBoxLayout

from functools import partial


class LoginView(QWidget):
    def __init__(self):
        super().__init__()
        self.generalLayout = QVBoxLayout()
        self._createLoginDisplay()
        self.setLayout(self.generalLayout)

    def _createLoginDisplay(self):
        """Create the display"""
        self.display = QFormLayout()
        self.username = QLineEdit()
        self.password = QLineEdit()
        self.display.addRow("Username:", self.username)
        self.display.addRow("Password:", self.password)
        self.generalLayout.addLayout(self.display)
        self.btns = QHBoxLayout()
        self.login_btn = QPushButton('Login')
        self.clear_btn = QPushButton('Cancel')
        self.btns.addWidget(self.login_btn)
        self.btns.addWidget(self.clear_btn)
        self.generalLayout.addLayout(self.btns)

    def clearFormDisplay(self):
        """Clear the display"""
        self.username.setText('')
        self.password.setText('')