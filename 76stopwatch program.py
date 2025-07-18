# (10:48:38)

# stopwatch program

import sys
from PyQt5.QtWidgets import QApplication , QWidget , QLabel , QVBoxLayout ,QPushButton  , QHBoxLayout
from PyQt5.QtCore import QTimer , QTime , Qt


class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0,0,0,0)
        self.time_label = QLabel("00:00:00:00",self)
        self.start_button = QPushButton("Start",self)
        self.stop_button = QPushButton("Stop",self)
        self.reset_button = QPushButton("Reset",self)
        self.timer = QTimer(self)

        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("StopWatch")

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)

        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)

        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)

        vbox.addLayout(hbox)

        self.setStyleSheet("""
                           
            QPushButton,QLabel{
                           padding:20px;
                           font-weight:bold;
                           font-family: calibri;s
                           }
            QPushButton{
                           font-size:50px;}
            QLabel{
                           font-size:120px;
                           background-color:#00dfeb;
                           border-radius:20px;
                           }
""")

        self.start_button.clicked.connect(self.Start)
        self.stop_button.clicked.connect(self.Stop)
        self.reset_button.clicked.connect(self.Reset)
        self.timer.timeout.connect(self.update_display)

    def Start(self):
        self.timer.start(10)

    def Stop(self):
        self.timer.stop()
        

    def Reset(self):
        self.timer.stop()
        self.time = QTime(0,0,0,0)
        self.time_label.setText(self.format_time(self.time))

    def format_time(self,time):
        hours = time.hour()  
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec() // 10
        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"

    def update_display(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))

def main():
    app = QApplication(sys.argv)
    clockstopwatch = Stopwatch()
    clockstopwatch.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()