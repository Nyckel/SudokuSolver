class Parser:
    def __init__(self):
      self.path

    @staticmethod
    def parse(file):
        print("Parsing...")
        text = file.read().rstrip()

    def parse(self):
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
            ligne = sudoku
            for i in ligne :
                if i.possible_values.size() == 1 :
                    box.possible_values.remove(i.possible_values - 1)

        return 0;

    def initConstraintColumns(self, sudoku, box):
        if box.possible_values.size() != 1:
            return 0;
        else:
            colonne = sudoku
            for i in colonne:
                if i.possible_values.size() == 1:
                    box.possible_values.remove(i.possible_values - 1)
        return 0;

    def initConstraintSquare(self, sudoku, box):
        if box.possible_values.size() != 1:
            return 0;
        else:
            carre = sudoku
            for i in carre:
                if i.possible_values.size() == 1:
                    box.possible_values.remove(i.possible_values - 1)
        return 0;