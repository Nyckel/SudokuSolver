from os import getcwd
from tkinter import *
from tkinter import filedialog

from parseur import Parser
from sudoku import Sudoku


class Display:
    CELL_SIZE = 40

    def __init__(self, solver: Sudoku):
        self.window = Tk()
        self.window.title("SudokuSolver")
        self.canvas = Canvas(self.window, width=9*self.CELL_SIZE, height=9*self.CELL_SIZE, bd=0, background="blue")
        btn_open_sudoku = Button(self.window, text="Select sudoku", command=self.select_sudoku)
        btn_open_sudoku.pack()
        self.canvas.pack()
        self.solver = solver
        self.show_and_solve_sudoku()
        self.window.mainloop()

    def show_and_solve_sudoku(self):
        self.update_sudoku(self.solver.get_initial_grid())
        res = self.solver.solve()
        if res:
            self.update_sudoku(res)
        else:
            self.could_not_solve()

    def update_sudoku(self, grid):
        self.canvas.delete("all")
        for index, cell in enumerate(grid):
            self.draw_cell(cell)

    def draw_cell(self, cell):
        x, y = cell.get_position()
        self.canvas.create_rectangle(x * self.CELL_SIZE,
                                     y * self.CELL_SIZE,
                                     (x + 1) * self.CELL_SIZE,
                                     (y + 1) * self.CELL_SIZE,
                                     fill='white')

        for i in range(1, 3):  # Bold lines to separate zones
            self.canvas.create_line(i*3*self.CELL_SIZE, 0, i*3*self.CELL_SIZE, 9*self.CELL_SIZE, width="2")
            self.canvas.create_line(0, i * 3 * self.CELL_SIZE, 9 * self.CELL_SIZE, i * 3 * self.CELL_SIZE, width="2")

        if not len(cell.get_possible_values()) == 1:
            return  # We only write a number when we are sure of the cell's value

        if cell.is_original():
            self.canvas.create_text(x*self.CELL_SIZE + self.CELL_SIZE / 2,
                                    y*self.CELL_SIZE + self.CELL_SIZE / 2,
                                    text=cell.get_possible_values()[0], fill="red")
        else:
            self.canvas.create_text(x*self.CELL_SIZE + self.CELL_SIZE / 2,
                                    y * self.CELL_SIZE + self.CELL_SIZE / 2,
                                    text=cell.get_possible_values()[0], fill="black")

    def select_sudoku(self):
        cwd = getcwd()
        filename = filedialog.askopenfilename(initialdir=cwd+'/exemples', title="Select sudoku file",
                                              filetypes=[("Text files", "*.txt")])
        self.solver = Sudoku(Parser.parse(filename))
        self.show_and_solve_sudoku()

    def could_not_solve(self):
        print("Display: Could not solve sudoku")