from sudoku import Sudoku
from box import Box
import argparse

class Parser:

    def __init__(self):
        self.path = 'C:/Users/camil/Documents/Polytech/UQAC/trimestre 1/IA/TP2'
        self.columns = [1,10,19,28,37,46,55,64,73]
        self.lines = [1,2,3,4,5,6,7,8,9]
        self.case = [0,1,2,9,10,11,18,19,20]
    @staticmethod
    def parse(file):
        print("Parsing...")
        text = file.read().rstrip()

    def parse(self):
        sudoku = Sudoku()
        j = 1
        with open(self.path) as f:
            for line in f:
                for i in line:
                    if i != 0:
                        Box.newbox = Box(j,1)
                        Box.newbox.possible_values = i
                        sudoku.initial_grid.add(Box.newbox)
                        j = j+1
                    if i == 0:
                        Box.newbox = Box(j, 0)
                        Box.newbox.possible_values = [1,2,3,4,5,6,7,8,9]
                        sudoku.initial_grid.add(Box.newbox)
                        j = j + 1
        return 0;

    def isInitil(self,sudoku):
        for i in sudoku :
            if i.possible_values.size() != 1:
                i.is_original = False
            else :
                i.is_original = True

    def initConstraintLines(self, sudoku, box):
        if box.possible_values.size() != 1 :
            return 0;
        else :
            j = box.position%9
            if j == 0 :
                j=9
            j = ((box.position - j) / 9) + 1
            ligne = self.lines*j
            for i in ligne :
                if sudoku(i).possible_values.size() == 1 :
                    box.possible_values.remove(i.possible_values - 1)

        return 0;

    def initConstraintColumns(self, sudoku, box):
        if box.possible_values.size() != 1:
            return 0;
        else:
            j = box.position%9
            if j == 0 :
                j = 9
            j = (box.position - j)
            colonne = self.columns+9*j
            for i in colonne:
                if sudoku(i).possible_values.size() == 1:
                    box.possible_values.remove(i.possible_values - 1)
        return 0;

    def initConstraintSquare(self, sudoku, box):
        if box.possible_values.size() != 1:
            return 0;
        else:
            carre = self.case + box.position
            for i in carre:
                if sudoku(i).possible_values.size() == 1:
                    box.possible_values.remove(i.possible_values - 1)
        return 0;
