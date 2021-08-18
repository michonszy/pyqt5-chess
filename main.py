import sys

#definicja planszy
start = [["Rw","Knw","Bw","Qw","Kw","Bw","Knw","Rw"],
         ["Pw","Pw","Pw","Pw","Pw","Pw","Pw","Pw"],
         [" "," "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "," "],
         ["Pb","Pb","Pb","Pb","Pb","Pb","Pb","Pb"],
         ["Rb","Knb","Bb","Qb","Kb","Bb","Knb","Rb"]]

def make_a_move():
    print("Podaj figurę skąd chcesz przemieścić")
    from_x = input("Jej wiersz: ")
    from_y = input("Jej kolumna: ")
    from_x = int(from_x)
    from_y = int(from_y)
    if start[from_x][from_y] == " ":
        print("Ludzie tu nikogo nie ma, co ty niby chcesz przemieścić?")
    else:
        print("A dokąd?")
        to_x = input("Podaj wiersz: ")
        to_y = input("Podaj kolumnę: ")
        to_y = int(to_y)
        to_x = int(to_x)

        #sprawdzenie czy nie jest to pusty ruch, położenie w to samo miejsce
        if from_x == to_x and from_y == to_y:
            print("No co Ty w to samo miejsce będziesz kładł?")
        else:
        #zakres ruchu piona
            if start[from_x][from_y] == "Pb" or start[from_x][from_y] == "Pw":
                if from_y == to_y and to_x == (from_x+1):
                    print("Ruch dozwolony, poruszam pionem")
                    start[to_x][to_y] = start[from_x][from_y]
                    start[from_x][from_y] = " "
                else:
                    print("Ruch niedozwolony dla piona")
            else:
                print("To nie Pion")
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




print("Oto obecna plansza: ")
def print_plansza():
    for x in range(8):
        print(start[x][0] + " | " + start[x][1] + " | " + start[x][2] + " | " + start[x][3] + " | " + start[x][4] + " | " + start[x][5] + " | " + start[x][6] + " | " + start[x][7] + " | ")

while True:
    print_plansza()
    make_a_move()
    