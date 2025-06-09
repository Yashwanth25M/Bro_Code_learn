# (09:53:07)

# PyQt5 buttons

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Chat GPT 4.0")
        self.setGeometry(700, 300, 500, 500)
        self.setWindowIcon(QIcon("test.png"))

        # Label
        self.label = QLabel("Hey ready to Dive in !!", self)
        self.label.setFont(QFont("Arial", 16))
        self.label.setGeometry(30, 300, 500, 100)
        self.label.setStyleSheet("color:black;")
        self.label.setAlignment(Qt.AlignCenter)

        # Button
        self.button = QPushButton("Chat", self)
        self.initUI()

    def initUI(self):
        self.button.setGeometry(15, 375, 200, 50)
        self.button.setFont(QFont("Verdana", 14))
        self.button.setStyleSheet("font-size:30px; color: black;")
        self.button.clicked.connect(self.on_click)

    def on_click(self):
        print("Chat initialized")
        self.button.setText("Chat started")
        self.button.setDisabled(True)
        self.label.setText("Bye")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
