# GUI for Banking App

import sys
import userDetailsDict as udd
import UserDetailPage
import RegisterNewUserPage
import Login
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QStackedWidget

from functools import partial

class BankAppGUI(QWidget):
    """BankApp's View"""
    def __init__(self):
        super().__init__()
        # Set properties of main window
        self.setWindowTitle('Banking App')
        self.setFixedSize(400, 200)
        self.stack = QStackedWidget(self)
        self.loginView = Login.LoginView()
        self.registerUserView = RegisterNewUserPage.RegisterNewUserPage()
        self.stack.addWidget(self.loginView)
        self.stack.addWidget(self.registerUserView)
        self.stack.setCurrentWidget(self.loginView)
        self._connectLoginSignal()
        self._connectRegisterNewUserSignal()
        self.show()
    
    def _connectLoginSignal(self):
        # For OK
        self.loginView.login_btn.clicked.connect(partial(self.checkUserDetails))
        # For Cancel
        self.loginView.clear_btn.clicked.connect(partial(self.loginView.clearFormDisplay))
        # For Register
        self.loginView.register_btn.clicked.connect(partial(self.registerUser))

    def checkUserDetails(self):
        username = self.loginView.username.text()
        if username in udd.dict_userDetails:
            self.loginAccepted(username)

    def loginAccepted(self, username):
        # todo: we are creating a new UserDetailsPage object every time we do this function, fix this...
        self.userDetailsView = UserDetailPage.UserDetailPage(username)
        self.stack.addWidget(self.userDetailsView)
        self.stack.setCurrentWidget(self.userDetailsView)

    def registerUser(self):

        self.stack.setCurrentWidget(self.registerUserView)

    # RegisterNewUserPage CTRL
    def _connectRegisterNewUserSignal(self):
        # For Clear
        self.registerUserView.clear_btn.clicked.connect(partial(self.registerUserView._clearForm))
        # For Back
        self.registerUserView.back_btn.clicked.connect(self.setLoginView)    
        # For Register
        self.registerUserView.register_btn.clicked.connect(self._addNewUserToDictionary)

    def setLoginView(self):
        self.stack.setCurrentWidget(self.loginView)
        # todo: I may have created a new instance of the LoginView page... 
    
    def _addNewUserToDictionary(self):
        details = RegisterNewUserPage.RegisterNewUserPage._newUserForm
        udd.dict_userDetails[details.username.text()] = {"Name": details.name.text(), "Password": details.password.text(), "Checking": 0, "Savings": 0}

def main():
    """Main Function"""
    # Create instance of QApplication
    bankapp = QApplication(sys.argv)
    # Show the bank app's GUI
    view = BankAppGUI()
    # Execute the bank app's main loop
    sys.exit(bankapp.exec_())

if __name__ == '__main__':
    main()
