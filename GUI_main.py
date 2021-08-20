import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor



app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Chess")
window.setFixedWidth(800)
window.setFixedHeight(800) 

class ClickLabel(QtWidgets.QLabel):
    clicked = QtCore.pyqtSignal()

    def mousePressEvent(self, event):
        self.clicked.emit()
        QtWidgets.QLabel.mousePressEvent(self, event)

window.move(500, 200)

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

def clicked(name, letter, column,x,y):
    def whoami():
        print("Pozycja: " + str(letter)+ str(column))
        print("Jest to x: " + str(x) + " ; y: " + str(y))
    name.clicked.connect(whoami)
def createPlansza():
    black = "background-color:#6A4B35; color:#CDBDB1;"
    white = "background-color:#CDBDB1; color:#6A4B35;"
    row=["A","B","C","D","E","F","G","H"]
    for x in range(8):
        for i in range (8):
            letter=row[x]
            column=i+1
            name = letter+ str(column)
            name = QLabel(name)
            name = ClickLabel()
            name.setAlignment(QtCore.Qt.AlignCenter)
            
            clicked(name,letter,column,x,i)
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
                name_of_figure = QPixmap("/home/chrupek/Documents/Github/pyqt5-chess/images/rook_white.png")
                name.setPixmap(name_of_figure.scaled(90,90))
            if start[x][i] == "Knw":
                name_of_figure = QPixmap("/home/chrupek/Documents/Github/pyqt5-chess/images/knight_white.png")
                name.setPixmap(name_of_figure.scaled(90,90))
            if start[x][i] == "Bw":
                name_of_figure = QPixmap("/home/chrupek/Documents/Github/pyqt5-chess/images/bishop_white.png")
                name.setPixmap(name_of_figure.scaled(90,90))
            if start[x][i] == "Qw":
                name_of_figure = QPixmap("/home/chrupek/Documents/Github/pyqt5-chess/images/queen_white.png")
                name.setPixmap(name_of_figure.scaled(90,90))
            if start[x][i] == "Kw":
                name_of_figure = QPixmap("/home/chrupek/Documents/Github/pyqt5-chess/images/king_white.png")
                name.setPixmap(name_of_figure.scaled(90,90))
            if start[x][i] == "Pw":
                name_of_figure = QPixmap("/home/chrupek/Documents/Github/pyqt5-chess/images/piece_white.png")
                name.setPixmap(name_of_figure.scaled(90,90))
            if start[x][i] == "Pb":
                name_of_figure = QPixmap("/home/chrupek/Documents/Github/pyqt5-chess/images/piece_black.png")
                name.setPixmap(name_of_figure.scaled(90,90))
            if start[x][i] == "Kb":
                name_of_figure = QPixmap("/home/chrupek/Documents/Github/pyqt5-chess/images/king_black.png")
                name.setPixmap(name_of_figure.scaled(90,90))
            if start[x][i] == "Qb":
                name_of_figure = QPixmap("/home/chrupek/Documents/Github/pyqt5-chess/images/queen_black.png")
                name.setPixmap(name_of_figure.scaled(90,90))
            if start[x][i] == "Bb":
                name_of_figure = QPixmap("/home/chrupek/Documents/Github/pyqt5-chess/images/bishop_black.png")
                name.setPixmap(name_of_figure.scaled(90,90))
            if start[x][i] == "Knb":
                name_of_figure = QPixmap("/home/chrupek/Documents/Github/pyqt5-chess/images/knight_black.png")
                name.setPixmap(name_of_figure.scaled(90,90))
            if start[x][i] == "Rb":
                name_of_figure = QPixmap("/home/chrupek/Documents/Github/pyqt5-chess/images/rook_black.png")
                name.setPixmap(name_of_figure.scaled(90,90))

def make_a_move():
    print("Wykonuję ruch")
    
createPlansza()
window.show()
window.setLayout(grid)
sys.exit(app.exec())