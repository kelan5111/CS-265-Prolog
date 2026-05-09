#################################
####    Greedy Search application on Search Problem
###     @kelan5111
#################################

from queue import PriorityQueue

class GreedySearch():
    def __init__(self, problem=None, goal=None):

        if problem is None: return

        try:
            if goal != None: self._goal = goal

            self.set_problem(problem)

            self._curr_action = None
            self._curr_depth = 0
            self._frontier = PriorityQueue()

        except TypeError as e:
            print("Should be type Dic however got " + e)


    def execute_search(self):
        while(True):
            if self._problem is None: 
                print("No problem to solve.")
                break
            
            # 1. Goal test: return true or false
            found = self._goal_test(self._curr_node["state"])
            if found:
                print("Success")
                break
            elif self._frontier.empty() and not found:
                print("Failure.")
                break

            # 2. Expand func: successor func & forming nodes
            self._expand()

            # 3. Search: heuristic which is lowest
            next_node = self._search()

            if next_node != None:
                self._curr_node = next_node
                self._curr_action = next_node["action"]

    def _search(self):
        # Remove the highest f(n) from priority queue
        next_node = self._frontier.get()

        # Checking if node is child (depth)
        if next_node["parent"] == self._curr_node["state"]:
            self._curr_depth += 1
        else:
            self._curr_depth -= 1
        
        return next_node
    
    def _evaluation(self, path_cost):
        if not hasattr(self, "_goal"): 
            return 0

        return self._goal["path_cost"] - path_cost

    def _expand(self):
       # 1. Expanding current node
       children = self._get_successors(self._curr_node["state"])

       # 2. Creating nodes
       for action, state in children:
            new_node = {
                "state": state,
                "parent": self._curr_node,
                "action": action,
                "path_cost": self._curr_node["path_cost"] + self._get_path_cost(state),
                "h(n)": self._evaluation(self._get_path_cost(state))
            }

            self._frontier.put((new_node["h(n)"], new_node)) # New node added to frontier
        

    def set_problem(self, problem):
        self._problem = problem
        self._goal_test = problem["goal_test"]  # Returns: True/False
        self._get_successors = problem["successor_func"]    # Returns Dict: action-state pairs
        self._get_path_cost = problem["path_cost"]  # Returns: path cost of a specified state

        # Setting Initial State as Current State
        self._curr_node = {
            "state": problem["initial_state"],
            "parent": None,
            "action": None,
            "path_cost": 0,
            "h(n)": 0
        }

def _successor_func(self):
        # Expanding current node children and adding to frontier
        return self._successors[self._curr_node]




############################
## Time Complexity: O(b^m)      b = branching factor, m = max depth
## Space Complexity: O(b^m)     stores all nodes in frontier- can memory drain
## Completeness: False          may reach dead ends- lead nowhere
## Optimality: False            may reach dead ends- lead nowhere
########################