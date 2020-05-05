from sudoku_solver import SudokuSolver
from random import randint, sample
from copy import deepcopy


def generate_sudoku():
    sudoku_solver = SudokuSolver()
    array = [[0 for i in range(9)] for j in range(9)]
    rand_entry = randint(1, 9)
    rand_row, rand_col = (randint(0, 8), randint(0, 8))
    array[rand_row][rand_col] = rand_entry
    sudoku_solver.solve(array)

    values_to_remove = sample([(j, k) for j in range(0, 9) for k in range(0, 9)], 48)
    for el in values_to_remove:
        array[el[0]][el[1]] = 0
        solvable_array = deepcopy(array)
        if not sudoku_solver.solve(solvable_array):
            break
    return array


if __name__ == '__main__':
    sudoku = generate_sudoku()
    for row in sudoku:
        print(row)
        print('\n')
