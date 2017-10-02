from copy import deepcopy


class Solver:
    def __init__(self):
        self.sudoku_horizontal = []
        self.sudoku_vertical = []
        self.possible_numbers = []

    # generates 9 lists each holding 9 times " "
    def generate_horizontal_sudoku(self):
        for y in range(9):
            self.sudoku_horizontal.append([" " for x in range(9)])

        return self.sudoku_horizontal

    # prints the grid in sudoku formatting to the console
    def print_grid(self, sudoku):
        for list_index in range(9):
            grid = ""

            for item_index in range(9):
                if item_index % 3 == 0:
                    grid = grid + " |"

                grid = grid + " " + sudoku[list_index][item_index]

            if list_index % 3 == 0:
                print(" -------------------------")

            print(grid + " |")

        print(" -------------------------")

    # lets the user fill the empty grid
    def get_user_input(self):
        list_index = 0
        while list_index < 9:
            item_index = 0
            while item_index < 9:
                self.sudoku_horizontal[list_index][item_index] = "X"
                self.print_grid(self.sudoku_horizontal)
                inpt = input("Enter number, nothing/space, x for redo: ")

                if inpt == "":
                    inpt = " "

                if inpt == "x":
                    if item_index == 0 and list_index == 0:
                        pass
                    else:
                        self.sudoku_horizontal[list_index][item_index] = " "

                        if item_index == 0:
                            list_index = list_index - 1
                            item_index = 9

                        item_index = item_index - 1
                else:
                    self.sudoku_horizontal[list_index][item_index] = str(inpt)
                    item_index = item_index + 1

            list_index = list_index + 1

    # from sudoku(left to right) get a second list (top to bottom)
    def generate_vertical_sudoku(self):
        for item_index in range(9):
            tmp_list = []
            for list_index in range(9):
                tmp_list.append((self.sudoku_horizontal[list_index][item_index]))

            self.sudoku_vertical.append(tmp_list)

        return self.sudoku_vertical

    def find_possible_numbers(self):
        # generate list of all possible numbers (1-9) for ever single position

        tmp_list = []
        for i in range(9):
            tmp_list.append((str(i + 1)))

        # 3d list, is it the best idea? who knows
        for y in range(9):
            self.possible_numbers.append([deepcopy(tmp_list) for x in range(9)])

        for row_index in range(9):
            for column_index in range(9):
                self.possible_numbers[row_index][column_index] = list(
                    set(self.possible_numbers[row_index][column_index]) - set(self.sudoku_horizontal[row_index]))
                self.possible_numbers[row_index][column_index] = list(
                    set(self.possible_numbers[row_index][column_index]) - set(self.sudoku_vertical[row_index]))

        return self.possible_numbers

    def rnd_solve(self):

        sudoku = deepcopy(self.sudoku_horizontal)

        return sudoku
