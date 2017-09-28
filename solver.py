class Solver():
    def __init__(self):
        self.sudoku = []

    # generates 9 lists each holding 9 times " "
    def generate_empty_sudoku(self):
        for y in range(9):
            self.sudoku.append([" " for x in range(9)])

    # prints the grid in sudoku formatting to the console
    def print_grid(self):
        for y in range(9):
            grid = ""

            for x in range(9):
                if x % 3 == 0:
                    grid = grid + " |"

                grid = grid + " " + str(self.sudoku[y][x])

            if y % 3 == 0:
                print(" -------------------------")

            print(grid + " |")

        print(" -------------------------")

    def get_user_input(self):
        item_number = 0
        list_number = 0
        while list_number < 9:
            item_number = 0
            while item_number < 9:
                self.sudoku[list_number][item_number] = "X"
                self.print_grid()
                inpt = input("Enter number, nothing/space, x for redo: ")

                if inpt == "":
                    inpt = " "

                if inpt == "x":
                    if item_number == 0 and list_number == 0:
                        pass
                    else:
                        self.sudoku[list_number][item_number] = " "

                        if item_number == 0:
                            list_number = list_number - 1
                            item_number = 9

                        item_number = item_number - 1
                else:
                    self.sudoku[list_number][item_number] = inpt
                    item_number = item_number + 1

            list_number = list_number + 1
