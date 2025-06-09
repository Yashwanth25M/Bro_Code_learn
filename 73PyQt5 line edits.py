# (10:15:55)

# PyQt5 line edits
# input box

import sys
from PyQt5.QtWidgets import QApplication , QMainWindow , QLabel , QLineEdit , QPushButton
from PyQt5.QtGui import QFont

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 1000, 1000)
        
        self.line_edit = QLineEdit(self)
        self.button = QPushButton("🡅Send",self)

        self.initUI()

    def initUI(self):
        self.line_edit.setGeometry(10,10,200,40)
        self.line_edit.setStyleSheet("font-size : 18px;"
                                     "font-family : Arial")
        self.button.setGeometry(210,10,80,40)
        self.button.setStyleSheet("font-size : 18px;"
                                     "font-family : Arial")
        self.line_edit.setPlaceholderText("Enter a Message")
        self.button.clicked.connect(self.send)

    def send(self):
        text = self.line_edit.text()
        print(f"User entered : {text}")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
