import sys
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton

class PomodoroTimer(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle('Pomodoro Timer')
        self.setGeometry(300, 300, 300, 300)

        # Set font
        font = QFont()
        font.setPointSize(20)

        # Create labels
        self.timer_label = QLabel('25:00', self)
        self.timer_label.setGeometry(50, 50, 200, 100)
        self.timer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.timer_label.setFont(font)

        self.status_label = QLabel('Work Time', self)
        self.status_label.setGeometry(50, 150, 200, 50)
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Create buttons
        self.start_button = QPushButton('Start', self)
        self.start_button.setGeometry(50, 200, 80, 40)
        self.start_button.clicked.connect(self.start_timer)

        self.stop_button = QPushButton('Stop', self)
        self.stop_button.setGeometry(170, 200, 80, 40)
        self.stop_button.clicked.connect(self.stop_timer)
        self.stop_button.setEnabled(False)

        # Create timer
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_timer)

        # Initialize variables
        self.minutes = 25
        self.seconds = 0
        self.work_time = True
        self.timer_running = False

    def start_timer(self):
        self.timer_running = True
        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)
        self.timer.start()

    def stop_timer(self):
        self.timer_running = False
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)
        self.timer.stop()

    def update_timer(self):
        if self.minutes == 0 and self.seconds == 0:
            if self.work_time:
                self.status_label.setText('Break Time')
                self.minutes = 5
            else:
                self.status_label.setText('Work Time')
                self.minutes = 25
            self.work_time = not self.work_time
            self.seconds = 0
        elif self.seconds == 0:
            self.minutes -= 1
            self.seconds = 59
        else:
            self.seconds -= 1

        time_string = '{:02d}:{:02d}'.format(self.minutes, self.seconds)
        self.timer_label.setText(time_string)

    def closeEvent(self, event):
        self.timer.stop()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    timer = PomodoroTimer()
    timer.show()
    sys.exit(app.exec())
