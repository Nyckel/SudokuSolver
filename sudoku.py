class Sudoku:

    def __init__(self, initial_grid):
        self.initial_grid = initial_grid #une grille de box

    def solve(self):
        print("Starting sudoku resolution")


    def backtracking_search(self,assignment,csp):
      return 0


    def mrv(self):
        nb_val = 10
        for i in range (0,81):
            nb_val_box = len(self.initial_grid[i].possible_values)
            if (nb_val_box < nb_val):
                nb_val = nb_val_box
                var=self.initial_grid[i]
            elif (nb_val_box < nb_val):
               self.degree_heuristic()



    def degree_heuristic(self):
        return 0