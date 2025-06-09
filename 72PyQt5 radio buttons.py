# (10:06:42)

# PyQt5 radio buttons

import sys
from PyQt5.QtWidgets import QApplication , QMainWindow , QLabel , QRadioButton , QButtonGroup
from PyQt5.QtGui import QFont

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 1000, 1000)

        label = QLabel("💳 Choose Your Card", self)
        label.setFont(QFont("Arial",18))
        label.setGeometry(0,0,500,100)
        
        self.radio1 = QRadioButton("VISA" , self)
        self.radio2 = QRadioButton("MasterCard" , self)
        self.radio3 = QRadioButton("Rupay" , self)

        label = QLabel("📍Location", self)
        label.setFont(QFont("Arial",18))
        label.setGeometry(0,250,500,100)
        self.radio4 = QRadioButton("🏬 In-store" , self)
        self.radio5 = QRadioButton("💻 online" , self)
        self.button_group1 = QButtonGroup(self)        
        self.button_group2 = QButtonGroup(self) 
        self.selected_card = None
        self.selected_location = None
       
        self.initUI()

    def initUI(self):
        self.radio1.setGeometry(50,100,300,50)
        self.radio2.setGeometry(50,150,300,50)
        self.radio3.setGeometry(50,200,300,50)
        self.radio4.setGeometry(50,350,300,50)
        self.radio5.setGeometry(50,400,300,50)

        self.setStyleSheet("QRadioButton{" 
        "font-size : 30px ; " 
        "font-family:Arial;"
        "padding :10px;""}")

        self.button_group1.addButton( self.radio1 )
        self.button_group1.addButton( self.radio2 )
        self.button_group1.addButton( self.radio3 )
        self.button_group2.addButton( self.radio4 )
        self.button_group2.addButton( self.radio5 )

        self.radio1.toggled.connect(self.radio_button_changed)
        self.radio2.toggled.connect(self.radio_button_changed)
        self.radio3.toggled.connect(self.radio_button_changed)
        self.radio4.toggled.connect(self.radio_button_changed)
        self.radio5.toggled.connect(self.radio_button_changed)
    
    def radio_button_changed(self):                 
        radio_button = self.sender()                
        if radio_button.isChecked():                
            text = radio_button.text()              
            if radio_button in self.button_group1.buttons():     
                self.selected_card = text           
            elif radio_button in self.button_group2.buttons():   
                self.selected_location = text       

            if self.selected_card and self.selected_location:    
                print(f"{self.selected_card} is selected at {self.selected_location}") 
                
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
