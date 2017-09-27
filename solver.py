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


def check(sudoku, cp_sudoku):
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


#two dimensional list
#sudoku[y][x] coordinates
sudoku1 = [[" " for x in range(9)] for y in range(9)]
sudoku_cp = [[" " for x in range(9)] for y in range(9)]
get_inpt(sudoku1)


for y in range(9):
    for x in range(9):
        sudoku_cp[y][x] = sudoku1[y][x]

check(sudoku1, sudoku_cp)
prnt_grd(sudoku1)
