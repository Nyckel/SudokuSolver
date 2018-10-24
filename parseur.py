from sudoku import Sudoku
from box import Box
import argparse
import os
class Parser:

    def __init__(self):
        self.path = 'C:/Users/camil/Documents/Polytech/UQAC/trimestre 1/IA/TP2/sudoku.txt'
        self.columns = [0,9,18,27,36,45,54,63,72]
        self.lines = [0,1,2,3,4,5,6,7,8]
        self.case = [0,1,2,9,10,11,18,19,20]
    @staticmethod
    #def parse(file):
     #   print("Parsing...")
     #   text = file.read().rstrip()

    def parse(self):
        sudoku = Sudoku()
        j = 1
        file = open(self.path,"r")
        m = file.readline()
        for k in range(1,90):
            i = file.read(1)
            print(i)
            if k%10 != 0 :
                i = float(i)
                i = int(i)
                if i != 0:
                    newbox = Box(j,1)
                    newbox.possible_values = [i]
                    sudoku.initial_grid.append(newbox)
                    j = j + 1
                if i == 0:
                    newbox = Box(j, 0)
                    newbox.possible_values = [1,2,3,4,5,6,7,8,9]
                    sudoku.initial_grid.append(newbox)
                    j = j + 1
        file.close()
        return sudoku;

    def isInitil(self,sudoku):
        for i in sudoku :
            if i.possible_values.size() != 1:
                i.is_original = False
            else :
                i.is_original = True

    def initConstraintLines(self, sudoku, box):
        if len(box.possible_values) == 1 :
            return 0;
        else :
            j = box.position%9
            j = int(((box.position - j) / 9))
            ligne = []
            for b in self.lines :
                ligne.append(b+9*j)
            for i in ligne :
                if box.position !=  i :
                    if len(sudoku.initial_grid[i].possible_values) == 1 :
                        if sudoku.initial_grid[i].possible_values[0] in box.possible_values :
                           box.possible_values.remove(sudoku.initial_grid[i].possible_values[0])

        return 0;

    def initConstraintColumns(self, sudoku, box):
        if len(box.possible_values) == 1:
            return 0;
        else:
            j = ((box.position -1 - (box.position -1)%9)/9)
            print('mjfeo')
            j = int(box.position -j*9 -1)
            print(j)
            colonne = []
            for c in self.columns :
                col = c +j
                colonne.append(col)
            for i in colonne:
                if box.position -1 != i:
                    if len(sudoku.initial_grid[i].possible_values) == 1:
                        if sudoku.initial_grid[i].possible_values[0] in box.possible_values :
                            box.possible_values.remove(sudoku.initial_grid[i].possible_values[0])
        return 0;

    def initConstraintSquare(self, sudoku, box):
        if len(box.possible_values) != 1:
            return 0;
        else:
            carre = []
            l = ((box.position - 1 - (box.position - 1) % 9) / 9) #num ligne
            c = (box.position - 1) % 9 #numero colonne
            j = int((l%3)+(c%3)*3)
            for b in self.case :
                carre.append(b + 3*j)
            for i in carre:
                if box.position != i:
                    if len(sudoku.initial_grid[i].possible_values) == 1:
                        if sudoku.initial_grid[i].possible_values[0] in box.possible_values :
                            box.possible_values.remove(sudoku.initial_grid[i].possible_values[0])
        return 0;

    def Constraints(self, sudoku):
        for box in sudoku.initial_grid:
            self.initConstraintLines(sudoku,box)
            self.initConstraintColumns(sudoku,box)
            self.initConstraintSquare(sudoku,box)
        return sudoku;