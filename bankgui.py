# GUI for Banking App

import sys
import userDetailsDict as udd
import UserDetailPage
import RegisterNewUserPage
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget
from functools import partial

class BankAppGUI(QMainWindow):
    """BankApp's View"""
    def __init__(self):
        super().__init__()
        # Set properties of main window
        self.setWindowTitle('Banking App')
        self.setFixedSize(280,150)
        # Set central widget and general layout
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        # Create dispaly and buttons
        self._createLoginDisplay()

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
        self.clear_btn = QPushButton('Clear')
        self.register_btn = QPushButton('Register')
        self.btns.addWidget(self.login_btn)
        self.btns.addWidget(self.clear_btn)
        self.btns.addWidget(self.register_btn)
        self.generalLayout.addLayout(self.btns)
    
    def clearFormDisplay(self):
        """Clear the display"""
        self.username.setText('')
        self.password.setText('')

class BankAppCtrl:
    """Controller class for Bank app"""
    def __init__(self, view):
        self._view = view
        self._connectLoginSignal() 

    def _connectLoginSignal(self):
        # For OK
        self._view.login_btn.clicked.connect(partial(self.checkUserDetails))
        # For Cancel
        self._view.clear_btn.clicked.connect(partial(self._view.clearFormDisplay))
        # For Register
        self._view.register_btn.clicked.connect(self.registerUser)

    def checkUserDetails(self):
        username = self._view.username.text()
        if username in udd.dict_userDetails:
            self.loginAccepted(username)

    def loginAccepted(self, username):
        self._view.close()
        self._view = UserDetailPage.UserDetailPage(username)        
        self._view.show()

    def registerUser(self):
        self._view.close()
        self._view = RegisterNewUserPage.RegisterNewUserPage()
        self._view.show()

#Client Code
def main():
    """Main Function"""
    # Create instance of QApplication
    bankapp = QApplication(sys.argv)
    # Show the bank app's GUI
    view = BankAppGUI()
    view.show()
    # Create instances of the model and controller
    BankAppCtrl(view = view)
    RegisterNewUserPage.RegNewUserCtrl(view = view)
    # Execute the bank app's main loop
    sys.exit(bankapp.exec_())

if __name__ == '__main__':
    main()
