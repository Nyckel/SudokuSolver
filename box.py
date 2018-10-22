
class Box:


    def __init__(self, position, start_value: int):
        self.constraints = []
        self.position = position
        if start_value != 0:
            self.original = True
            self.possible_values = [start_value]
        else:
            self.original = False
            self.possible_values = list(range(1, 10))

    def is_original(self):
        return self.original

    def get_constraint_nodes(self):
        return self.constraints

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

    def get_constraint_nodes(self):
        return self.box_in_conflict

