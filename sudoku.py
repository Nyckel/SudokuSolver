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
        if len(min_nodes) == 1:
            return min_nodes[0]
        elif len(min_nodes) > 1:
            return self.degree_heuristic(min_nodes)
        else:
            raise Exception("No node selected after MRV ans Degree heuristic")

    @staticmethod
    def mrv(node_list):
        """ Minimum Remaining Values """
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
    def degree_heuristic(node_list):
        if len(node_list) == 1:
            return node_list
        min_val = 21  # Number of constraints for any nodes + 1
        min_node = None
        for node in node_list:
            nb_constraints = sum([1 if n.is_assigned() else 0 for n in node.get_constraint_nodes()])
            if nb_constraints < min_val:
                min_val = nb_constraints
                min_node = node
        return min_node

    @staticmethod
    def order_domain_values(node, assignment, csp):
        """ Least constraining value
            Here the least constraining value is the one that is least present in the constraint nodes possible values
        """
        # TODO: Check if it's possible to do this step only once and have the values ordered on the Box object
        vals = dict()
        for val in node.get_possible_values():
            if val in vals:
                vals[val] += 1
            else:
                vals[val] = 1
        sorted_list = sorted(vals.items(), key=lambda kv: kv[1])
        return [key for key, val in sorted_list]

    @staticmethod

    def is_value_consistent_with_asignment(node, assignment, csp):
        node_poss=csp.get_possible_values()
        for i in range (0,len(node_poss.size())):
            if (node_poss[i] == node):
                return True
        return False

    def ac3(self, csp):
        """ Arc Consistency 3 Algorithm,
            Possibly reduces CSP domains """
        q = Queue()

        for nodea in csp:  # Initially add all arcs in the queue
            for nodeb in nodea.get_constraint_nodes():
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
