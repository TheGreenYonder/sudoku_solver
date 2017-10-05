from solver import Solver

my_solver = Solver()
horizontal_sudoku = my_solver.generate_horizontal_sudoku()
my_solver.get_user_input()
my_solver.print_grid(horizontal_sudoku)
vertical_sudoku = my_solver.generate_vertical_sudoku()
# my_solver.print_grid(vertical_sudoku)
possible_numbers = my_solver.find_possible_numbers()
solved = my_solver.rnd_solve()
my_solver.print_grid(solved)