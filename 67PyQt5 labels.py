# (09:31:27)

# PyQt5 labels

import sys
from PyQt5.QtWidgets import QApplication , QMainWindow , QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.setWindowTitle(title_name)
        self.setWindowTitle("Chat GPT 4.0")
        # self.setGeometry(X , y ,HEIGHT , WIDTH)
        self.setGeometry(700 , 300 ,500 , 500)
        self.setWindowIcon(QIcon("test.png"))
        label = QLabel("Hello", self)
        label.setFont(QFont("Arial",25))
        label.setGeometry(0,0,500,100)
        label.setStyleSheet("color:black;"
                            "background-color:yellow;"
                            "font-weight:bold;"
                            "font-style:italic;"
                            "text-decoration:underline;")
        # label.setAlignment(Qt.AlignTop)
        # label.setAlignment(Qt.AlignBottom)
        # label.setAlignment(Qt.AlignVCenter)
        # label.setAlignment(Qt.AlignRight)
        # label.setAlignment(Qt.AlignHCenter)
        # label.setAlignment(Qt.AlignLeft)

        # label.setAlignment(Qt.AlignHCenter | Qt.AlignTop )
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom )
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter )
        label.setAlignment(Qt.AlignCenter )



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()