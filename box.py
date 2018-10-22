
class Box:

    def __init__(self, initial_grid,pos):
        self.is_original = False
        self.possible_values = {1,2,3,4,5,6,7,8,9}
        self.position = pos


    def get_position(self):
        return self.position

    def get_possible_values(self):
        return self.possible_values