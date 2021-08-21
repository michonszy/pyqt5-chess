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
window.setWindowTitle("Chess")
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


#zdefiniowanie poczatkowej planszy
start = [["Rw","Knw","Bw","Qw","Kw","Bw","Knw","Rw"],
         ["Pw","Pw","Pw","Pw","Pw","Pw","Pw","Pw"],
         ["","","","","","","",""],
         ["","","","","","","",""],
         ["","","","","","","",""],
         ["","","","","","","",""],
         ["Pb","Pb","Pb","Pb","Pb","Pb","Pb","Pb"],
         ["Rb","Knb","Bb","Qb","Kb","Bb","Knb","Rb"]]

#zmienna globalna do określenia ostatniej pozycji
ostatnia_pozycja=""
ostatnia_pozycja_x = ""
ostatnia_pozycja_y = ""

#funkcja wykonująca się przy naciśnięciu pola
def clicked(name, letter, column,x,y):
    def whoami():
        print("----------------------------------------------------------")
        global ostatnia_pozycja
        global ostatnia_pozycja_x
        global ostatnia_pozycja_y
        print("Ostatnia pozycja: " + ostatnia_pozycja)
        print("Pozycja: " + str(letter)+ str(column))
        print("Jest to x: " + str(x) + " ; y: " + str(y))
        if start[x][y] == "":
            print("Nacisnięto puste pole")
            ostatnia_pozycja="Puste"
            if ostatnia_pozycja == "":
                print("Ostatnia pozycja jest pusta więc nic nie przenoszę")
            else:
                print("Ostatnia pozycja nie jest pusta dlatego czas zrobić ruch")
                print("From_x: " + str(ostatnia_pozycja_x))
                print("From y: "+ str(ostatnia_pozycja_y))
                print("To x: " + str(x))
                print("To y: " + str(y))
                make_a_move(ostatnia_pozycja_x,ostatnia_pozycja_y,x,y)
        else:
            print("Na tej pozycji znajduje się: " + start[x][y])
            ostatnia_pozycja = start[x][y]
            ostatnia_pozycja_x = x
            ostatnia_pozycja_y = y
        

    name.clicked.connect(whoami)



#generowanie planszy
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
            name.setText(letter+ str(column))
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
                name_of_figure = QPixmap("/Users/smichon/Downloads/Git/pyqt5-chess/images/rook_white.png")
                name.setPixmap(name_of_figure.scaled(90,90))
            if start[x][i] == "Knw":
                name_of_figure = QPixmap("/Users/smichon/Downloads/Git/pyqt5-chess/images/knight_white.png")
                name.setPixmap(name_of_figure.scaled(90,90))
            if start[x][i] == "Bw":
                name_of_figure = QPixmap("/Users/smichon/Downloads/Git/pyqt5-chess/images/bishop_white.png")
                name.setPixmap(name_of_figure.scaled(90,90))
            if start[x][i] == "Qw":
                name_of_figure = QPixmap("/Users/smichon/Downloads/Git/pyqt5-chess/images/queen_white.png")
                name.setPixmap(name_of_figure.scaled(90,90))
            if start[x][i] == "Kw":
                name_of_figure = QPixmap("/Users/smichon/Downloads/Git/pyqt5-chess/images/king_white.png")
                name.setPixmap(name_of_figure.scaled(90,90))
            if start[x][i] == "Pw":
                name_of_figure = QPixmap("/Users/smichon/Downloads/Git/pyqt5-chess/images/piece_white.png")
                name.setPixmap(name_of_figure.scaled(90,90))
            if start[x][i] == "Pb":
                name_of_figure = QPixmap("/Users/smichon/Downloads/Git/pyqt5-chess/images/piece_black.png")
                name.setPixmap(name_of_figure.scaled(90,90))
            if start[x][i] == "Kb":
                name_of_figure = QPixmap("/Users/smichon/Downloads/Git/pyqt5-chess/images/king_black.png")
                name.setPixmap(name_of_figure.scaled(90,90))
            if start[x][i] == "Qb":
                name_of_figure = QPixmap("/Users/smichon/Downloads/Git/pyqt5-chess/images/queen_black.png")
                name.setPixmap(name_of_figure.scaled(90,90))
            if start[x][i] == "Bb":
                name_of_figure = QPixmap("/Users/smichon/Downloads/Git/pyqt5-chess/images/bishop_black.png")
                name.setPixmap(name_of_figure.scaled(90,90))
            if start[x][i] == "Knb":
                name_of_figure = QPixmap("/Users/smichon/Downloads/Git/pyqt5-chess/images/knight_black.png")
                name.setPixmap(name_of_figure.scaled(90,90))
            if start[x][i] == "Rb":
                name_of_figure = QPixmap("/Users/smichon/Downloads/Git/pyqt5-chess/images/rook_black.png")
                name.setPixmap(name_of_figure.scaled(90,90))


#funkcja odpowiadająca za zakres ruchu oraz zmianę w planszy, po wykonaniu zmiany w planszy generuje nowy widok
def make_a_move(from_x, from_y, to_x, to_y):
    from_x = int(from_x)
    from_y = int(from_y)
    if start[from_x][from_y] == "":
        print("Ludzie tu nikogo nie ma, co ty niby chcesz przemieścić?")
    else:
        print("A dokąd?")

        to_y = int(to_y)
        to_x = int(to_x)

        #sprawdzenie czy nie jest to pusty ruch, położenie w to samo miejsce
        if from_x == to_x and from_y == to_y:
            print("No co Ty w to samo miejsce będziesz kładł?")
        else:
        #zakres ruchu piona białego
            if start[from_x][from_y] == "Pw":
                if from_y == to_y and to_x == (from_x+1):
                    print("Ruch dozwolony, poruszam białym pionem")
                    start[to_x][to_y] = start[from_x][from_y]
                    start[from_x][from_y] = " "
                else:
                    print("Ruch niedozwolony dla piona białego")
            else:
                print("To nie biały Pion")

            if start[from_x][from_y] == "Pb":
                if from_y == to_y and to_x == (from_x-1):
                    print("Ruch dozwolony, poruszam czarnym pionem")
                    start[to_x][to_y] = start[from_x][from_y]
                    start[from_x][from_y] = " "
                else:
                    print("Ruch niedozwolony dla czarnego piona")
            else:
                print("To nie czarny Pion")
        #zakres ruchu wieży
            if start[from_x][from_y] == "Rb" or start[from_x][from_y] == "Rw":
                if from_y == to_y or from_x == to_x:
                    print("Ruch dozwolony, poruszam wieżą")
                    start[to_x][to_y] = start[from_x][from_y]
                    start[from_x][from_y] = " "
                else:
                    print("Ruch niedozwolony dla wieży")
            else:
                print("To nie Wieża")
        #zakres ruchu konia
            if start[from_x][from_y] == "Knb" or start[from_x][from_y] == "Knw":
                if (from_x == (to_x+2) and from_y == (to_y-1)) or (from_x == (to_x+1) and from_y == (to_y-2)) or (from_x == (to_x-1) and from_y == (to_y-2)) or (from_x == (to_x-2) and from_y == (to_y-1)) or (from_x == (to_x-2) and from_y == (to_y+1)) or (from_x == (to_x-1) and from_y == (to_y+2)) or (from_x == (to_x+1) and from_y == (to_y+2)) or (from_x == (to_x+2) and from_y == (to_y+2)):
                    print("Ruch dozwolony, poruszam koniem")
                    start[to_x][to_y] = start[from_x][from_y]
                    start[from_x][from_y] = " "
                else:
                    print("Ruch niedozwolony dla konia")
            else:
                print("To nie Koń")
        #zakres ruchu gońca
            if start[from_x][from_y] == "Bb" or start[from_x][from_y] == "Bw":
                if from_y == to_y or from_x == to_x:
                    print("Ruch dozwolony, poruszam gońcem")
                    start[to_x][to_y] = start[from_x][from_y]
                    start[from_x][from_y] = " "
                else:
                    print("Ruch niedozwolony dla gońca")
            else:
                print("To nie Goniec")

        #zakres ruchu damy
            if start[from_x][from_y] == "Qb" or start[from_x][from_y] == "Qw":
                if from_y == to_y or from_x == to_x:
                    print("Ruch dozwolony, poruszam damą")
                    start[to_x][to_y] = start[from_x][from_y]
                    start[from_x][from_y] = " "
                else:
                    print("Ruch niedozwolony dla damy")
            else:
                print("To nie Dama")
        #zakres ruchu króla
            if start[from_x][from_y] == "Kb" or start[from_x][from_y] == "Kw":
                if from_y == to_y or from_x == to_x:
                    print("Ruch dozwolony, poruszam królem")
                    start[to_x][to_y] = start[from_x][from_y]
                    start[from_x][from_y] = " "
                else:
                    print("Ruch niedozwolony dla króla")
            else:
                print("To nie Król")

    createPlansza()



createPlansza()
window.show()
window.setLayout(grid)
sys.exit(app.exec())