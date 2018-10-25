from box import Box


class Parser:

    @staticmethod
    def parse(path):
        print("Parsing...")
        file = open(path, 'r')
        grid = []
        index = 0
        for line in file.read().rstrip():
            for nb in line.strip():
                grid.append(Box((index % 9, index // 9), int(nb)))
                index += 1
        if len(grid) != 81:
            print("Error, sudoku has", len(grid), "cells, should be 81 !")
            raise Exception("Wrong sudoku file format, incorrect number of cells")
        Parser.create_constraints(grid)
        return grid

    @staticmethod
    def create_constraints(grid):
        for index, cell in enumerate(grid):
            if cell.is_assigned():
                continue  # We don't generate constraints on boxes that already have a value set
            x, y = cell.get_position()

            # Zone constraints
            x_range = Parser.get_range(x)
            y_range = Parser.get_range(y)

            for row in [(y + y_index) * 9 for y_index in y_range]:
                for col in x_range:
                    other_cell = grid[int(row + col + x)]
                    cell.add_constraint(other_cell)

            # Lines constraints
            for i in range(9):
                cell.add_constraint(grid[i * 9 + x])  # Other cell on same column
                cell.add_constraint(grid[y * 9 + i])  # Other cell on same line

            # cell.printconstraints()  # For debug

    @staticmethod
    def get_range(pos: int):
        """
        Defines the range of lines or columns to get around the cell
        depending on placement (if it's on the edge...)
        """
        r = []
        if pos % 3 == 0:
            r = [0, 1, 2]
        elif pos % 3 == 2:
            r = [-2, -1, 0]
        else:
            r = [-1, 0., 1]
        return r
