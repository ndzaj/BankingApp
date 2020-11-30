import bankgui
import userDetailsDict as udd

from PyQt5.QtWidgets import QMainWindow
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
        self.register_btn = QPushButton('Register')
        self.back_btn = QPushButton('Back')
        self.clear_btn = QPushButton('Clear')
        self.btns.addWidget(self.register_btn)
        self.btns.addWidget(self.clear_btn)
        self.btns.addWidget(self.back_btn)
        self.generalLayout.addLayout(self.btns)
        
    def _clearForm(self):
        self.name.setText('')
        self.username.setText('')
        self.password.setText('')
    
class RegNewUserCtrl:
    def __init__(self, newUserView):
        self._view = newUserView
        self._connectButtons()

    def setPrevView(self, view):
        self.previousView = view

    def _connectButtons(self):
        # For Clear
        self._view.clear_btn.clicked.connect(partial(self._view._clearForm))
        # For Back
        self._view.back_btn.clicked.connect(self._goBack)    
        # For Register
        self._view.register_btn.clicked.connect(self._addNewUserDetails)

    def _goBack(self):
        pass
        # self._view.close()
        # self._view = self.previousView      
        # self._view.show()
        self.previousView.setCentralWidget(self.previousView)

    def _addNewUserDetails(self):
        self._view.username.text() 
