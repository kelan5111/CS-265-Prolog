#######################################
#####   @kelan5111
###     Program represents the process of searching an agent's
##      state-space graph
####    NOTE: not executable
#######################################


frontier = []

newcastle = 10  # path cost is 10 (no meaning)
birmingham = 30
bristol = 60
brighton = 70

problem = {"initial_state": newcastle,
           "successors": {
                            newcastle : birmingham,
                            birmingham: bristol,
                            bristol: brighton
                        },
           "goal_state": brighton
          }

def expand(current_node, problem):
    child = problem["successors"].get(current_node)  # get child from successors
    if child:
        frontier.append(child)


def searching_algorithm(problem):
    found = False
    current_node = problem["initial_state"]

    frontier.append(current_node)

    while not found:
        current_node = frontier.pop(0)

        found = expand(current_node)

        if not found and (len(frontier) == 0):
            print("Failure.")

        elif found:
            print("Success")
    


def main():
    searching_algorithm(problem)


if __name__ == "__main__":
    main()