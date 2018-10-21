class Sudoku:



    def __init__(self, initial_grid):
        self.initial_grid = initial_grid #une grille de box
        self.DIMENTION = 9


    def solve(self):
        print("Starting sudoku resolution")


    def assignment_complet(self, grid):
        for i in range (0,self.DIMENTION^2):
            if (1 < grid[i].possible_values):
                return False
        return True

    def backtracking_search(self,assignment,csp):
        grid=self.initial_grid
        if self.assignment_complet(grid):
            return grid
        


    def mrv(self):
        nb_val = 10
        for i in range (0,self.DIMENTION^2):
            nb_val_box = len(self.initial_grid[i].possible_values)
            if (1 < nb_val_box < nb_val):
                nb_val = nb_val_box
                var=self.initial_grid[i]
            elif (nb_val_box == nb_val):
               self.degree_heuristic()
        return var



    def degree_heuristic(self):
        return 0