class Solver():
    def __init__(self):
        self.sudoku_horizontal = []
        self.sudoku_vertical = []

    # generates 9 lists each holding 9 times " "
    def generate_empty_sudoku(self):
        for y in range(9):
            self.sudoku_horizontal.append([" " for x in range(9)])

        return self.sudoku_horizontal

    # prints the grid in sudoku formatting to the console
    def print_grid(self, sudoku):
        for list_number in range(9):
            grid = ""

            for item_number in range(9):
                if item_number % 3 == 0:
                    grid = grid + " |"

                grid = grid + " " + sudoku[list_number][item_number]

            if list_number % 3 == 0:
                print(" -------------------------")

            print(grid + " |")

        print(" -------------------------")

    # lets the user fill the empty grid
    def get_user_input(self):
        list_number = 0
        while list_number < 9:
            item_number = 0
            while item_number < 9:
                self.sudoku_horizontal[list_number][item_number] = "X"
                self.print_grid(self.sudoku_horizontal)
                inpt = input("Enter number, nothing/space, x for redo: ")

                if inpt == "":
                    inpt = " "

                if inpt == "x":
                    if item_number == 0 and list_number == 0:
                        pass
                    else:
                        self.sudoku_horizontal[list_number][item_number] = " "

                        if item_number == 0:
                            list_number = list_number - 1
                            item_number = 9

                        item_number = item_number - 1
                else:
                    self.sudoku_horizontal[list_number][item_number] = str(inpt)
                    item_number = item_number + 1

            list_number = list_number + 1

    # from sudoku(left to right) get a second list (top to bottom)
    def generate_vertical_sudoku(self):
        for item_number in range(9):
            tmp_list = []
            for list_number in range(9):
                tmp_list.append((self.sudoku_horizontal[list_number][item_number]))

            self.sudoku_vertical.append(tmp_list)

        return self.sudoku_vertical
