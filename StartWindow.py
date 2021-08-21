import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor


#zmienne okna w PyQt5
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Chess - MainWindow")
window.setFixedWidth(800)
window.setFixedHeight(800) 

class ClickLabel(QtWidgets.QLabel):
    clicked = QtCore.pyqtSignal()

    def mousePressEvent(self, event):
        self.clicked.emit()
        QtWidgets.QLabel.mousePressEvent(self, event)

window.move(500, 50)

window.setStyleSheet(
    "background-color: #202020;"
)
grid = QGridLayout()

logo = QLabel()
logo_img =  QPixmap("/home/chrupek/Documents/Github/pyqt5-chess/images/logo.png")
logo.setPixmap(logo_img.scaled(300,300))
logo.setAlignment(Qt.AlignCenter)

label_welcome = QLabel("Szachy to piękna gra dla inteligentnych ludzi, nie spierdol tego \n Wybierz opcję gry i pokaż na co Cię stać")
label_welcome.setStyleSheet(
    "color: white; font-size: 20px; font-family: URW Palladio L;"
)
label_welcome.setAlignment(Qt.AlignCenter)

button1 = QPushButton("5 minutowe")
button2 = QPushButton("10 minutowe")
button3 = QPushButton("30 minutowe")

grid.addWidget(logo,1,1,1,3)
grid.addWidget(label_welcome,2,1,2,3)
grid.addWidget(button1,3,1)
grid.addWidget(button2,3,2)
grid.addWidget(button3,3,3)
window.show()
window.setLayout(grid)
sys.exit(app.exec())