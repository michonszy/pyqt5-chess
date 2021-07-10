import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("ZAP Image Tools")
window.setFixedWidth(1000)

window.move(500, 200)
window.setWindowOpacity(0.9)
window.setStyleSheet(
    "background-color: #202020;"
)
grid = QGridLayout()

start = [["Rw","Knw","Bw","Qw","Kw","Bw","Knw","Rw"],
         ["Pw","Pw","Pw","Pw","Pw","Pw","Pw","Pw"],
         ["","","","","","","",""],
         ["","","","","","","",""],
         ["","","","","","","",""],
         ["","","","","","","",""],
         ["Pb","Pb","Pb","Pb","Pb","Pb","Pb","Pb"],
         ["Rb","Knb","Bb","Qb","Kb","Bb","Knb","Rb"]]

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
            if start[x][i] == "Rw":
                name_of_figure = QPixmap("/home/szymon/PycharmProjects/test/chess/rook_white.png")
                name.setPixmap(name_of_figure.scaled(90,90))
            if start[x][i] == "Knw":
                name_of_figure = QPixmap("/home/szymon/PycharmProjects/test/chess/knight_white.png")
                name.setPixmap(name_of_figure.scaled(90,90))
            if start[x][i] == "Bw":
                name_of_figure = QPixmap("/home/szymon/PycharmProjects/test/chess/bishop_white.png")
                name.setPixmap(name_of_figure.scaled(90,90))
            if start[x][i] == "Qw":
                name_of_figure = QPixmap("/home/szymon/PycharmProjects/test/chess/queen_white.png")
                name.setPixmap(name_of_figure.scaled(90,90))
            if start[x][i] == "Kw":
                name_of_figure = QPixmap("/home/szymon/PycharmProjects/test/chess/king_white.png")
                name.setPixmap(name_of_figure.scaled(90,90))
            if start[x][i] == "Pw":
                name_of_figure = QPixmap("/home/szymon/PycharmProjects/test/chess/piece_white.png")
                name.setPixmap(name_of_figure.scaled(90,90))
            if start[x][i] == "Pb":
                name_of_figure = QPixmap("/home/szymon/PycharmProjects/test/chess/piece_black.png")
                name.setPixmap(name_of_figure.scaled(90,90))
            if start[x][i] == "Kb":
                name_of_figure = QPixmap("/home/szymon/PycharmProjects/test/chess/king_black.png")
                name.setPixmap(name_of_figure.scaled(90,90))
            if start[x][i] == "Qb":
                name_of_figure = QPixmap("/home/szymon/PycharmProjects/test/chess/queen_black.png")
                name.setPixmap(name_of_figure.scaled(90,90))
            if start[x][i] == "Bb":
                name_of_figure = QPixmap("/home/szymon/PycharmProjects/test/chess/bishop_black.png")
                name.setPixmap(name_of_figure.scaled(90,90))
            if start[x][i] == "Knb":
                name_of_figure = QPixmap("/home/szymon/PycharmProjects/test/chess/knight_black.png")
                name.setPixmap(name_of_figure.scaled(90,90))
            if start[x][i] == "Rb":
                name_of_figure = QPixmap("/home/szymon/PycharmProjects/test/chess/rook_black.png")
                name.setPixmap(name_of_figure.scaled(90,90))

createPlansza()
window.show()
window.setLayout(grid)
sys.exit(app.exec())
