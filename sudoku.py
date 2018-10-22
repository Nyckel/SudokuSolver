from queue import Queue


class Sudoku:

    def __init__(self, initial_grid):
        self.initial_grid = initial_grid #une grille de box
        self.DIMENTION = 9

    def solve(self):
        print("Starting sudoku resolution")

    def backtracking_search(self, csp):
        """ Backtracking is equivalent to DFS with a variable per node """
        return self.recursive_backtracking((), csp)

    def recursive_backtracking(self, assignment, csp):
        if len(assignment) == len(self.initial_grid):  # Assignment is complete
            return assignment
        node = self.select_unasigned_variable(csp)
        for val in self.order_domain_values(node, assignment, csp):
            if self.is_value_consistent_with_asignment(val, assignment):
                node.set_value(val)
                csp.remove(node)
                assignment.append(node)
                result = self.recursive_backtracking(assignment, csp)
                if result:
                    return result
                node.set_value(None)
                csp.append(node)  # TODO: See if append_left improves performance here
                assignment.remove(node)
        return False

    def select_unasigned_variable(self, csp):
        min_nodes = self.mrv(csp)
        min_nodes = self.degree_heuristic(min_nodes)
        if len(min_nodes) > 0:
            return min_nodes[0]
        else:
            raise Exception("No node selected after MRV ans Degree heuristic")

    @staticmethod
    def mrv(node_list):
        """ Use Minimum Remaining Values """
        min_val = 10
        min_nodes = list()
        for node in node_list:
            if len(node.get_possible_values()) < min_val:
                min_val = len(node.get_possible_values())
                min_nodes = [node]
            elif len(node.get_possible_values()) == min_val:
                min_nodes.append(node)
        return min_nodes

    @staticmethod
    def degree_heuristic(self, node_list):
        return node_list  # TODO

    @staticmethod
    def order_domain_values(node, assignment, csp):
        return node.get_possible_values()[0]  # TODO

    @staticmethod
    def is_value_consistent_with_asignment(node, assignment, csp):
        # TODO
        return False

    def ac3(self, csp):
        """ Arc Consistency 3 Algorithm,
            Possibly reduces CSP domains """
        q = Queue()

        for nodea in csp:  # Initially add all arcs in the queue
            for nodeb in nodea.constraints:
                if (nodea, nodeb) not in q and (nodeb, nodea) not in q:
                    q.put_nowait((nodea, nodeb))

        while not q.empty():
            nodea, nodeb = q.get_nowait()
            if self.remove_inconsistent_values(nodea, nodeb):
                if nodea.get_possible_values().size() == 0:
                    return False
                for nodec in nodea.get_constraint_nodes().remove(nodeb):
                    q.put_nowait((nodec, nodea))
        return True

    @staticmethod
    def remove_inconsistent_values(nodea, nodeb):
        """ Returns true if some inconsistent values were found and removed """
        removed = False
        for val in nodea.get_possible_values():
            if not nodeb.can_have_constraint_with_val(val):
                nodea.remove_possible_value(val)
                removed = True
        return removed


    def assignment_complet(self, grid):
        for i in range (0,self.DIMENTION^2):
            if (1 < grid[i].possible_values):
                return False
        return True
