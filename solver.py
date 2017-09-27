#console based solver

#two dimensional list

def prnt():

    for y in range(9):
        s = ""

        for x in range(9):
            if x%3 == 0:
                s = s + " |"

            s = s + " " + str(sudoku[y][x])

        if y%3 == 0:
            print(" -------------------------")

        print(s + " |")

    print(" -------------------------")



sudoku = [[0 for x in range(9)] for y in range(9)]
#sudoku[y][x] coordinates


prnt()
