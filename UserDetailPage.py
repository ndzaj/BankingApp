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
        self.heading.setText('Welcome ' + udd.dict_userDetails[username]['Name'] + '!')
        self.generalLayout.addWidget(self.heading)
        self.setLayout(self.generalLayout)
