import userDetailsDict as udd

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from functools import partial


class UserDetailPage(QMainWindow):
    def __init__(self, username):
        super().__init__()
        self.setWindowTitle("You've Successfully Logged In!")
        # self.setFixedSize(280,150)
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)

        self.heading = QLabel()
        self.heading.setText('Welcome ' + udd.dict_userDetails[username]['Name'] + '!')
        self.generalLayout.addWidget(self.heading)

        # self.display = Q