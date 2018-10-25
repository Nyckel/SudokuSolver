"""
    TP2 - Intelligence artificielle
    Ce travail a pour but l'implémentation d'un résolveur de sudoku sous forme de CSP.
    On utilisera AC-3, MRV, degree heuristic et least constraining value.

"""
import argparse
from os import *

from display import Display
from parseur import Parser
from sudoku import Sudoku


class Main:
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-f", "--file", help="Path to the file containing the sudoku")
        args = parser.parse_args()

        if args.file is not None:
            sudoku = Sudoku(Parser.parse(args.file))
        else:
            print("Using default sudoku file")
            sudoku = Sudoku(Parser.parse(Main.resource_path("exemples/easy_1.txt")))
        Display(sudoku)

    @staticmethod
    def resource_path(relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)


if __name__ == '__main__':
    Main()
