import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtGui import QIcon, QPixmap
from src.modules import version

ver = version.get_version()

class TestApp(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the window
        self.setWindowTitle(f'TestApp {ver}')
        self.setFixedSize(400,250)
        self.setWindowIcon(QIcon(QPixmap('src/res/icons/testAppLogo.png')))
        
        # Create layout and widgets
        layout = QVBoxLayout()

        # Application name
        self.name_label = QLabel('Application Name: TestApp')
        layout.addWidget(self.name_label)

        # Application version
        self.version_label = QLabel(f'Version: {ver}')
        layout.addWidget(self.version_label)

        # Application features
        self.features_label = QLabel('Features:\n- a\n- b')
        # \n- c\n- d
        layout.addWidget(self.features_label)

        # Close button
        self.close_button = QPushButton('Close')
        self.close_button.clicked.connect(self.close)
        layout.addWidget(self.close_button)

        # Set the layout for the window
        self.setLayout(layout)

