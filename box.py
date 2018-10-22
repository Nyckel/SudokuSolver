
class Box:

    def __init__(self, initial_grid,pos,original):
        self.is_original = original
        self.possible_values = {1,2,3,4,5,6,7,8,9}
        self.position = pos


    def get_position(self):
        return self.position

    def get_possible_values(self):
        return self.possible_values

    def get_value(self):
        return self.possible_values[0]

    def set_value(self,val):
        self.possible_values = {val}
        
    def get_isOriginal(self):
        return self.is_original