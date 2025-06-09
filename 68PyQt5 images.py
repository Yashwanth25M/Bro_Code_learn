# (09:40:23)

# PyQt5 images

import sys
from PyQt5.QtWidgets import QApplication , QMainWindow , QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.setWindowTitle(title_name)
        self.setWindowTitle("Chat GPT 4.0")
        # self.setGeometry(X , y ,HEIGHT , WIDTH)
        self.setGeometry(700 , 300 ,500 , 500)
        self.setWindowIcon(QIcon("test.png"))

        label = QLabel(self)
        label.setGeometry(0 , 0 , 500 , 500)

        pixmap = QPixmap("test.png")
        label.setPixmap(pixmap)

        label.setScaledContents(True)

        label.setGeometry((self.width()-label.width()//2)
                          ,(self.height()-label.height()//2),
                          label.width(),
                          label.height())

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()