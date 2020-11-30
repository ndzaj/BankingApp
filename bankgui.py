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
from PyQt5.QtWidgets import QStackedWidget

from functools import partial

class BankAppGUI(QWidget):
    """BankApp's View"""
    def __init__(self):
        super().__init__()
        # Set properties of main window
        self.setWindowTitle('Banking App')
        self.setFixedSize(280,150)
        self.stack = QStackedWidget(self)
        self.loginView = Login.LoginView()
        self.stack.addWidget(self.loginView)
        self.stack.setCurrentWidget(self.loginView)
        self._connectLoginSignal()
        self.show()
    
    def _connectLoginSignal(self):
        # For OK
        self.loginView.login_btn.clicked.connect(partial(self.checkUserDetails))
        # For Cancel
        self.loginView.clear_btn.clicked.connect(partial(self.loginView.clearFormDisplay))

    def checkUserDetails(self):
        username = self.loginView.username.text()
        if username in bc.dict_userDetails:
            self.loginAccepted(username)

    def loginAccepted(self, username):
        self.userDetailsView = UserDetailPage.UserDetailPage(username)
        self.stack.addWidget(self.userDetailsView)
        self.stack.setCurrentWidget(self.userDetailsView)

    def registerUser(self):
        # self._view.close()
        # self._view = self._newUserView
        # self._view.show()
        self._view.setCentralWidget(self._newUserView)

#Client Code
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
