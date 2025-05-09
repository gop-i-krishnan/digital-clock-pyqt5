import sys
from PyQt5.QtCore import QTime, QTimer, Qt, QPropertyAnimation, QDate
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtGui import QFont, QFontDatabase, QIcon
from PyQt5.QtMultimedia import QSound

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        # Timer to update the time every second
        self.timer = QTimer(self)
        # Main label to display the current time
        self.time_label = QLabel(self)
        # Set window icon (make sure the file exists)
        self.setWindowIcon(QIcon("clock.png"))
         # Sound that plays each second (make sure the file exists)
        self.sound = QSound("ticking-clock_1-27477.wav")
        # Date label to display the date
        self.date_label = QLabel(self)  
         # Button to toggle date visibility
        self.toggle_date_button = QPushButton("Show Date", self) 
        # Set the initial visibility of the date label
        self.date_label.setVisible(False)
        self.date_visible = False  

        self.initUI()

    def initUI(self):
        self.setWindowTitle("DIGITAL CLOCK")
        self.setGeometry(600, 400, 500, 100)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("""
            font-size: 150px;
            color: hsl(115, 95%, 58%);
            text-shadow: 0px 0px 10px hsl(115, 95%, 58%), 
                         0px 0px 20px hsl(115, 95%, 58%), 
                         0px 0px 30px hsl(115, 95%, 58%);
            background-color: transparent;
        """)
        self.setStyleSheet("""
            background-color: black;
            background-image: linear-gradient(to right, #0f2027, #203a43, #2c5364);
        """)

        font_id = QFontDatabase.addApplicationFont("DS-DIGII.TTF")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_family, 150)
        self.time_label.setFont(my_font)

        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.date_label = QLabel(self)
        vbox.addWidget(self.date_label)

        self.date_label.setAlignment(Qt.AlignCenter)
        self.date_label.setStyleSheet("font-size: 50px; color: red;")
        vbox.addWidget(self.date_label)  # Add the date label to the layout
        self.date_label.hide()  # Hide the date initially

        # Set up the toggle button to show/hide the date
        self.toggle_date_button.setStyleSheet("""
            font-size: 20px;
            margin-top: 10px;
            background-color: white;
            color: black;
            border: 2px solid white;
            border-radius: 5px;
            padding: 10px;
        """)
        vbox.addWidget(self.toggle_date_button)  # Add button to the layout
        self.toggle_date_button.clicked.connect(self.toggle_date_visibility)  # Connect button click to method

        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        # Split the time and the AM/PM portion
        time_parts = current_time.split(" ")
        time_only = time_parts[0]  # The "hh:mm:ss" part
        am_pm = time_parts[1]  # The "AM" or "PM" part

        # Format the text with reduced size for AM/PM
        formatted_time = f"{time_only} <span style='font-size:50px;'>{am_pm}</span>"

        # Set the formatted text using rich text
        self.time_label.setText(f"<html><body>{formatted_time}</body></html>")

        current_date = QDate.currentDate().toString("dddd, MMMM d, yyyy")  # Format: Day, Month Date, Year
        self.date_label.setText(current_date)  # Set the date label text

        self.animate_label()
        self.sound.play()

    def animate_label(self):
        animation = QPropertyAnimation(self.time_label, b"geometry")
        animation.setDuration(500)
        animation.setStartValue(self.time_label.geometry())
        animation.setEndValue(self.time_label.geometry().adjusted(0, 0, 10, 10))
        animation.start()

    def toggle_date_visibility(self):
        if self.date_visible:
            self.date_label.hide()
            self.toggle_date_button.setText("Show Date")  # Corrected line
            self.date_visible = False
        else:
            self.date_label.show()
            self.toggle_date_button.setText("Hide Date")  # Corrected line
            self.date_visible = True


def main():
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
