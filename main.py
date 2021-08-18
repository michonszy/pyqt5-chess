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
        print("Ludzie tu nikogo nie ma")
    else:
        print("A dokąd?")
        to_x = input("Podaj wiersz: ")
        to_y = input("Podaj kolumnę: ")
        to_y = int(to_y)
        to_x = int(to_x)
        start[to_x][to_y] = start[from_x][from_y]
        start[from_x][from_y] = " "

print("Oto obecna plansza: ")
def print_plansza():
    for x in range(8):
        print(start[x][0] + " | " + start[x][1] + " | " + start[x][2] + " | " + start[x][3] + " | " + start[x][4] + " | " + start[x][5] + " | " + start[x][6] + " | " + start[x][7] + " | ")

while True:
    make_a_move()
    print_plansza()