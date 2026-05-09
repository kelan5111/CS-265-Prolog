#################################
####    A* Search application on Search Problem
###     @kelan5111
#################################


class ASearch():
    def __init__(self, problem=None, goal=None):

        if problem is None: return

        try:
            self.set_problem(problem)

            self._curr_action = None
            self._curr_depth = 0
            self._frontier = []

            if goal != None: self._goal = goal

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
            elif len(self._frontier) == 0 and not found:
                print("Failure.")
                break

            # 2. Expand func: successor func & forming nodes
            self._expand()

            # 3. Search: searches lowest g(n)
            next_node = self._search()

            if next_node != None:
                self._curr_node = next_node
                self._curr_action = next_node["action"]

    def _search(self):
        next_node = None

        for node in self._frontier:
            if next_node == None:
                next_node = node
                continue
            
            # Next node is the one with lowest cost
            if node["path_cost"] <= next_node["path_cost"]:
                next_node = node

        # Remove the next node from frontier
        self._frontier.remove(next_node)

        # Checking if node is child (depth)
        if next_node["parent"] == self._curr_node["state"]:
            self._curr_depth += 1
        else:
            self._curr_depth -= 1
        
        return next_node

    def _expand(self):
       # 1. Expanding current node
       children = self._get_successors(self._curr_node["state"])

       # 2. Creating nodes
       for action, state in children:
            new_node = {
                "state": state,
                "parent": self._curr_node,
                "action": action,
                "path_cost": self._get_path_cost(state)
            }
            self._frontier.append(new_node) # New node added to frontier
        

    def set_problem(self, problem):
        self._problem = problem

        # Setting Initial State as Current State
        self._curr_node = {
            "state": problem["initial_state"],
            "parent": None,
            "action": None,
            "path_cost": 0
        }
        
        self._goal_test = problem["goal_test"]  # Returns: True/False
        self._get_successors = problem["successor_func"]    # Returns Dict: action-state pairs
        self._get_path_cost = problem["path_cost"]  # Returns: path cost of a specified state



def _successor_func(self):
        # Expanding current node children and adding to frontier
        return self._successors[self._curr_node]


##############################
## Time Complexity: O(b^m)          b = branch factor, d = shallowest depth
## Space Complexity: O(b^m)         stores all nodes in frontier- can memory drain
## Completeness: True               always find a solution as long as step costs > 0 (relies on costs to calculate g(n))
## Optimality: True                 first solution = cheapest
#########################