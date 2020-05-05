from typing import List

grid = [[3, 0, 0, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]


class SudokuSolver:
    def __init__(self):
        print('Starting sudoku solver...')

    def solve(self, grid: List):
        solved = self._solve(grid)
        if solved:
            return grid
        print('Cannot be solved!')
        return False

    def _solve(self, grid: List) -> bool:
        empty_location = self._find_empty(grid)
        if empty_location[0] == 'None found':
            return True
        for i in range(9):
            i += 1
            in_column = self._check_in_column(sudoku_grid=grid, number=i, column_index=empty_location[1])
            in_row = self._check_in_row(sudoku_grid=grid, number=i, row_index=empty_location[0])
            in_three_by_three = self._check_in_three_by_three(sudoku_grid=grid, number=i, location=empty_location)
            if not in_column and not in_row and not in_three_by_three:
                grid[empty_location[0]][empty_location[1]] = i
                if self._solve(grid):
                    return True
                grid[empty_location[0]][empty_location[1]] = 0
        return False

    def _find_empty(self, grid: List) -> List:
        for i in range(9):
            for j in range(9):
                if grid[i][j] == 0:
                    return [i, j]
        return ['None found']

    def _check_in_column(self, sudoku_grid: List, number: int, column_index: int) -> bool:
        for row in sudoku_grid:
            if number == row[column_index]:
                return True
        return False

    def _check_in_row(self, sudoku_grid: List, number: int, row_index: int) -> bool:
        if number in sudoku_grid[row_index]:
            return True
        return False

    def _check_in_three_by_three(self, sudoku_grid: List, number: int, location: List) -> bool:
        row = location[0] - location[0] % 3
        column = location[1] - location[1] % 3
        for i in range(3):
            for j in range(3):
                if number == sudoku_grid[row + i][column + j]:
                    return True
        return False


if __name__ == '__main__':
    sudoku_solver = SudokuSolver()
    solved_grid = sudoku_solver.solve(grid)
    for row in solved_grid:
        print(row)
        print('\n')
