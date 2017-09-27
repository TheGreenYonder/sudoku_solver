#console based solver
import random
import secrets
#function to print grid
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
    for y in range(9):
        for x in range(9):
            sudoku[y][x] = "X"
            prnt_grd(sudoku)
            inpt = input("Enter number or nothing for X - exit for exit: ")

            if inpt == "":
                inpt = " "

            sudoku[y][x] = inpt


def check_h(sudoku, cp_sudoku):
    t1 = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    x = 0
    y = 0
    while y < 9:
        x = 0
        while x < 9:
            if sudoku[y][x] == " ":
                t1[x] = str(random.randrange(1, 10))
            else:
                t1[x] = sudoku[y][x]

            x = x + 1

        if len(set(t1)) != len(t1):
            y = y - 1

            for a in range(9):
                for b in range(9):
                    sudoku[a][b] = cp_sudoku[a][b]
        else:
            for z in range(9):
                sudoku[y][z] = t1[z]
                cp_sudoku[y][z] = t1[z]

        y = y + 1


def better(sudoku, cp_sudoku):
    t1 = []
    t2 = []
    for y in range(9):
        t1.append(sudoku[y])

    for y in range(9):
        tmp = ["", "", "", "", "", "", "", "", ""]
        for x in range(9):
            tmp[x] = sudoku[x][y]

        t1.append(tmp)

    for x in range(len(t1)):
        t2.append(t1[x])

    x = 0
    y = 0

    while y < 18:
        x = 0
        while x < 9:
            if t1[y][x] == " ":
                t1[y][x] = str(random.randrange(1, 10))

            x = x + 1

        if len(set(t1[x])) != len(t1[x]):
            y = -1

            for a in range(18):
                for b in range(9):
                    t1[a][b] = t2[a][b]

        y = y + 1
    prnt_grd(t1)

#two dimensional list
#sudoku[y][x] coordinates
sudoku1 = [[" " for x in range(9)] for y in range(9)]
sudoku_cp = [[" " for x in range(9)] for y in range(9)]
get_inpt(sudoku1)


for y in range(9):
    for x in range(9):
        sudoku_cp[y][x] = sudoku1[y][x]




#check_h(sudoku1, sudoku_cp)
better(sudoku1, sudoku_cp)
