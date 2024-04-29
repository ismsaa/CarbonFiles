import sys
import os
import psutil
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QLineEdit, QPushButton, QTextEdit, QVBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon

app_version = 'v0.0.1'

class myApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Carbon Files '+ app_version)
        self.setWindowIcon(QIcon('maps.ico'))
        self.resize(900, 600) # Width, Height
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # Widgets
        self.inputField = QLineEdit()
        button = QPushButton('&Say Hello!')
        button.clicked.connect(self.sayHello)
        self.output = QTextEdit()
        
        layout.addWidget(self.inputField)
        layout.addWidget(button)
        layout.addWidget(self.output)

    def sayHello(self):
        inputText = self.inputField.text()
        self.output.setText('Hello {0}'.format(inputText))

app = QApplication([])

app.setStyleSheet('''
    QWidget {
        font-size: 25px;
    }
    
    QPushButton {
        font-size: 20px;
    }
''')

window = myApp()
window.show()


# Run your application's event loop
sys.exit(app.exec())
