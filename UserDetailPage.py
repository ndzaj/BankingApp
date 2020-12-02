import userDetailsDict as udd

from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from functools import partial


class UserDetailPage(QWidget):
    def __init__(self, username):
        super().__init__()
        self.generalLayout = QVBoxLayout()
        self.heading = QLabel()
        self.heading.setText('Welcome ' + udd.dict_userDetails[username]['Name'] + '!\n')
        self.generalLayout.addWidget(self.heading)
        self.accountDetails = QLabel()
        self.accountDetails.setText("Username: " + username + "\nPassword: " + udd.dict_userDetails[username]['Password'] + 
            "\n\n Your CHECKING account balance is: $" + str(udd.dict_userDetails[username]['Checking']) +
            "\n\n Your SAVINGS account balance is: $" + str(udd.dict_userDetails[username]['Savings']))
        self.generalLayout.addWidget(self.accountDetails)
        self.buttons = QGridLayout()
        self.buttons.addWidget(QPushButton('Deposit to CHECKING'), 0,0)
        self.buttons.addWidget(QPushButton('Withdraw from CHECKING'), 0,1)
        self.buttons.addWidget(QPushButton('Deposit to SAVINGS'), 1,0)
        self.buttons.addWidget(QPushButton('Withdraw from SAVINGS'), 1,1)
        self.generalLayout.addLayout(self.buttons)
        self.setLayout(self.generalLayout)
