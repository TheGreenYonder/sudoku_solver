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

grid = [[" " for x in range(9)] for y in range(9)]