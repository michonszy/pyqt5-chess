import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout, QTextEdit
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("ZAP Image Tools")
window.setFixedWidth(1000)
window.setFixedHeight(1000)
window.move(500, 200)
window.setWindowOpacity(0.9)
window.setStyleSheet(
    "background-color: #202020;"
)
grid = QGridLayout()

def createPlansza():
    black = "background-color:#6A4B35; color:#CDBDB1;"
    white = "background-color:#CDBDB1; color:#6A4B35;"
    row=["A","B","C","D","E","F","G","H"]
    for x in range(8):
        for i in range (8):
            print(i)
            letter=row[i]
            column=i+1
            name = letter+ str(column)
            name = QLabel(name)
            name.setAlignment(QtCore.Qt.AlignCenter)

            if x%2 == 0:
                if i%2==0:
                    name.setStyleSheet(black)
                else:
                    name.setStyleSheet(white)
            else:
                if i%2==1:
                    name.setStyleSheet(black)
                else:
                    name.setStyleSheet(white)
            grid.addWidget(name, x, i)
            if x == 1:
                name_of_figure = "figura"+letter+str(column)
                name_of_figure = QPixmap("/home/szymon/PycharmProjects/test/chess/piece_black.png")
                name.setPixmap(name_of_figure.scaled(90,90))




createPlansza()


window.show()
window.setLayout(grid)
sys.exit(app.exec())
