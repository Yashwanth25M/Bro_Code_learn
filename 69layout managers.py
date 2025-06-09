# (09:46:28)

# layout managers

import sys
from PyQt5.QtWidgets import (QApplication , QMainWindow , QLabel , QWidget, QVBoxLayout ,
                              QHBoxLayout, QGridLayout)
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chat GPT 4.0")
        self.setGeometry(700 , 300 ,500 , 500)
        self.setWindowIcon(QIcon("test.png"))
        
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        label1 = QLabel("#1",self)
        label2 = QLabel("#2",self)
        label3 = QLabel("#3",self)
        label4 = QLabel("#4",self)

        label1.setStyleSheet("background-color : red;")
        label2.setStyleSheet("background-color : blue;")
        label3.setStyleSheet("background-color : black;")
        label4.setStyleSheet("background-color : yellow;")

# for vertical
        # v_box = QVBoxLayout()
        # v_box.addWidget(label1)
        # v_box.addWidget(label2)
        # v_box.addWidget(label3)
        # v_box.addWidget(label4)

        # central_widget.setLayout(v_box)

#for horizontal
        # h_box = QHBoxLayout()
        # h_box.addWidget(label1)
        # h_box.addWidget(label2)
        # h_box.addWidget(label3)
        # h_box.addWidget(label4)

        # central_widget.setLayout(h_box)


# #for grid
        grid = QGridLayout()
        # grid.addWidget(label1, row , column )
        grid.addWidget(label1, 0 , 0 )
        grid.addWidget(label2 , 0 , 1)
        grid.addWidget(label3 ,1,0)
        grid.addWidget(label4, 1, 1)

        central_widget.setLayout(grid)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()