from tkinter import *
from tkinter import ttk
from typing import List
import copy

from sudoku_solver import SudokuSolver
from sudokus import generate_sudoku


class SudokuGUI:
    def __init__(self, grid: List):
        self.original_grid = copy.deepcopy(grid)
        self.grid = grid
        self.window = Tk()
        self.window.title('Play a game of sudoku!')
        self.row, self.col = -1, -1
        self.margin = 10
        self.width = 500
        self.height = 500
        self.side = (self.width - 2 * self.margin) / 9
        sudoku_frame = Frame(self.window, bd=5)
        sudoku_frame.pack(fill=BOTH, side=TOP)
        self.canvas = Canvas(sudoku_frame, width=self.width, height=self.height)
        self.canvas.pack(side=TOP, fill=BOTH)
        button_frame = Frame(self.window).pack(side=BOTTOM)
        self.solve_button = ttk.Button(button_frame, text='Solve')
        self.solve_button.pack(side=RIGHT)
        self.new_game_button = ttk.Button(button_frame, text='New Game')
        self.new_game_button.pack(side=LEFT)
        self._draw_sudoku_grid()
        self._enter_numbers()

        self.canvas.bind('<Button-1>', self._square_clicked)
        self.canvas.bind('<Key>', self._key_pressed)
        self.solve_button.bind('<Button-1>', self._solve_button_clicked)
        self.new_game_button.bind('<Button-1>', self._new_button_clicked)

        self.window.mainloop()

    def _new_button_clicked(self, event):
        print('New game starting...')
        self.grid = generate_sudoku('intermediate')
        self._enter_numbers()

    def _solve_button_clicked(self, event):
        print('Solving sudoku')
        self._enter_user_numbers()
        self.grid = self.original_grid
        SudokuSolver().solve(self.grid)
        self._enter_numbers()

    def _square_clicked(self, event):
        margin, side, height, width = self.margin, self.side, self.height, self.width

        x, y = event.x, event.y
        if margin < x < width - margin and margin < y < height - margin:
            self.canvas.focus_set()

            row, col = int((y - margin) / side), int((x - margin) / side)

            if (self.row, self.col) == (row, col):
                self.row, self.col = -1, -1
            elif self.grid[row][col] == 0:
                self.row, self.col = row, col

        self.canvas.delete('focus')
        if self.row >= 0 and self.col >= 0:
            x0 = margin + side * self.col
            y0 = margin + side * self.row
            x1 = margin + side * (self.col + 1)
            y1 = margin + side * (self.row + 1)
            self.canvas.create_rectangle(x0, y0, x1, y1, outline='turquoise', tags='focus')

    def _key_pressed(self, event):
        if self.row >= 0 and self.col >= 0 and event.char in '123456789':
            self.grid[self.row][self.col] = int(event.char)
            self._enter_numbers()

    def _draw_sudoku_grid(self):
        margin, side, height, width = self.margin, self.side, self.height, self.width
        for i in range(10):
            color = "sea green" if i % 3 == 0 else "gray"

            x0 = margin + i * side
            y0 = margin
            x1 = margin + i * side
            y1 = height - margin
            self.canvas.create_line(x0, y0, x1, y1, fill=color)

            x0 = margin
            y0 = margin + i * side
            x1 = width - margin
            y1 = margin + i * side
            self.canvas.create_line(x0, y0, x1, y1, fill=color)

    def enter_numbers(self):
        self._enter_numbers()
        self.window.update()

    def _enter_user_numbers(self):
        margin, side, grid = self.margin, self.side, self.grid
        self.canvas.delete('user_numbers')
        for i in range(9):
            for j in range(9):
                entry = grid[i][j]
                if entry != 0:
                    x = margin + j * side + 3 * side / 4
                    y = margin + i * side + 3 * side / 4
                    self.canvas.create_text(x, y, tags='user_numbers', text=entry, fill='red')

    def _enter_numbers(self):
        margin, side, grid = self.margin, self.side, self.grid
        self.canvas.delete('numbers')
        for i in range(9):
            for j in range(9):
                entry = grid[i][j]
                if entry != 0:
                    x = margin + j * side + side / 2
                    y = margin + i * side + side / 2
                    self.canvas.create_text(x, y, tags='numbers', text=entry, fill='black')

    def add_rect(self, row, col):
        margin, side, height, width = self.margin, self.side, self.height, self.width
        self.canvas.delete('focus')
        self.canvas.focus_set()
        x0 = margin + side * col
        y0 = margin + side * row
        x1 = margin + side * (col + 1)
        y1 = margin + side * (row + 1)
        self.canvas.create_rectangle(x0, y0, x1, y1, outline='red', tags='focus')


if __name__ == '__main__':
    sudoku_grid = generate_sudoku()
    print('Starting GUI')
    SudokuGUI(sudoku_grid)
