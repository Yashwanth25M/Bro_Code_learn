# (10:21:55)

# PyQt5 CSS styles

import sys
from PyQt5.QtWidgets import QApplication , QMainWindow , QPushButton , QWidget , QHBoxLayout
from PyQt5.QtGui import QFont

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button1 = QPushButton("Red")
        self.button2 = QPushButton("Green")
        self.button3 = QPushButton("Blue")

        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        hbox = QHBoxLayout()

        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)

        central_widget.setLayout(hbox)

        self.button1.setObjectName("Red")
        self.button2.setObjectName("Green")
        self.button3.setObjectName("Blue")

        self.setStyleSheet("""
                           QMainWindow {
        background-color: black;}

            QPushButton{
                font-size : 40px;
                font-family : Arial;
                padding :15px 75px; 
                margin :25px;
                border: 3px solid;
                border-radius : 15px;           
                           }
                QPushButton#Red{
                           background-color:red}                           
                QPushButton#Green{
                           background-color:green}                           
                QPushButton#Blue{
                           background-color:blue}   

                QPushButton#Red:hover{
                           background-color:yellow}                           
                QPushButton#Green:hover{
                           background-color:orange}                           
                QPushButton#Blue:hover{
                           background-color:purple}                         
""")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()