# (10:00:12)

# PyQt5 checkboxes

import sys
from PyQt5.QtWidgets import QApplication , QMainWindow , QCheckBox
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)

        #checkbox
        self.checkbox = QCheckBox("Do you like food", self)
        self.initUI()

    def initUI(self):
        self.checkbox.setStyleSheet("font-size: 30px; font-family: Arial; color : #000000")
        self.checkbox.setGeometry(1,2,510,100)

        # To make already checked
        # self.checkbox.setChecked(True)

        #To check change in state
        self.checkbox.stateChanged.connect(self.checkbox_changed)

    def checkbox_changed(self , state):
        if state == Qt.Checked :
            print("You like food")
        else:
            print("You do not like food")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
