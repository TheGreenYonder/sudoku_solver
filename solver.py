# console based solver
import random
from copy import deepcopy


# function to print grid
def prnt_grd(sudoku):
    for y in range(9):
        s = ""

        for x in range(9):
            if x % 3 == 0:
                s = s + " |"

            s = s + " " + str(sudoku[y][x])

        if y % 3 == 0:
            print(" -------------------------")

        print(s + " |")

    print(" -------------------------")


def get_inpt(sudoku):
    x = 0
    y = 0
    while y < 9:
        x = 0
        while x < 9:
            print(str(x) + " " + str(y))
            sudoku[y][x] = "X"
            prnt_grd(sudoku)
            inpt = input("Enter number or nothing/space: ")

            if inpt == "":
                inpt = " "

            sudoku[y][x] = inpt
            x = x + 1
            if inpt == "x":
                x = x - 2
        y = y + 1


def better(sudoku):
    t1 = []
    t1 = deepcopy(sudoku)

    for y in range(9):
        tmp = ["", "", "", "", "", "", "", "", ""]
        for x in range(9):
            tmp[x] = sudoku[x][y]

        t1.append(tmp)

    for y in range(18):
        for x in range(9):
            if t1[y][x] == " ":
                t1[y][x] = str(random.randrange(1, 10))

                #only error when it is finished
                try:
                    t1[y+9][x] = t1[y][x]
                except IndexError:
                    prnt_grd(t1)
                    return False

        if len(set(t1[y])) != 9:
            return True

#    for y in range(18):
 #       for x in range(9):
  #          if len(set(t1[x])) != 9:
   #             return True

    prnt_grd(t1)
    return False

# two dimensional list
# sudoku[y][x] coordinates
sudoku1 = [[" " for x in range(9)] for y in range(9)]
#get_inpt(sudoku1)

#fill grid (invalid sudoku, just for testing)
for y in range(9):
    for x in range(9):
        sudoku1[y][x] = str((x+y+1) % 9)
        if sudoku1[y][x] == "0":
            sudoku1[y][x] = "9"


sudoku1[0][0] = " "
sudoku1[5][0] = " "
sudoku1[8][1] = " "
sudoku1[2][4] = " "
sudoku1[2][1] = " "
sudoku1[3][5] = " "

tries = 1
prnt_grd(sudoku1)
cp_sudoku = deepcopy(sudoku1)
while better(sudoku1):
    tries = tries + 1
    sudoku1 = deepcopy(cp_sudoku)

print(str(tries))