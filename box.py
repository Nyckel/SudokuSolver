
class Box:

    def __init__(self, position, start_value: int):
        self.constraints = set()
        self.position = position
        if start_value != 0:
            self.value = start_value
            self.original = True
            self.possible_values = [start_value]
        else:
            self.value = None
            self.original = False
            self.possible_values = list(range(1, 10))

    def is_original(self):
        return self.original

    def add_constraint(self, node):
        if node.get_position() != self.get_position():
            self.constraints.add(node)

    def get_constraint_nodes(self):
        return self.constraints

    def get_position(self):
        return self.position

    def get_possible_values(self):
        return self.possible_values

    def remove_possible_value(self, value):
        self.possible_values.remove(value)

    def get_value(self):
        return self.value

    def set_value(self, val):
        self.value = val

    def is_assigned(self):
        return self.value is not None

    def get_isOriginal(self):
        return self.is_original

    def can_have_constraint_with_val(self, value):
        for val in self.possible_values:
            if val != value:
                return True
        return False
        # return not (len(self.possible_values) == 0 and self.possible_values[0] == val)

    def printconstraints(self):
        print("Cell", self.get_position(), len(self.constraints), " constraints")
        for c in self.constraints:
            print(c.get_position())
