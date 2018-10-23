"""
    TP2 - Intelligence artificielle
    Ce travail a pour but l'implémentation d'un résolveur de sudoku sous forme de CSP.
    On utilisera AC-3, MRV, degree heuristic et least constraining value.

"""
import argparse

from display import Display
from parseur import Parser
from sudoku import Sudoku


class Main:
    def __init__(self):
        self.path = 'C:/Users/camil/Documents/Polytech/UQAC/trimestre 1/IA/TP2'
        #parser = argparse.ArgumentParser()
        #parser.add_argument("-f", "--file", help="Path to the file containing the sudoku", required=True)
        #args = parser.parse_args()
        Sudoku.sudoku = Sudoku()
        sudoku = Parser.parse(self)
        sudoku = Parser.Constraints(self, sudoku)

        window = Display(sudoku)


if __name__ == '__main__':
    Main()
