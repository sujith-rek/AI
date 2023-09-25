# Take the same example of the action graph for the 8-puzzle problem. Answer the following and
# submit in zipped format to the BB link.
# 1. Apply any admissible heuristic function, to find the heuristic values for each node of the
# action graph. You should mention the heuristic function you are applying.
# 2. Use this graph alongwith the heuristic values, to apply greedy search algorithm to find a
# solution.
# 3. Assume the edge weight between any pair of nodes as 1. Then apply A* algorithm to
# find a solution to the problem.

import random

class Puzzle:
    puzzle_string = ""
    goal_state = "123456780"


    def __init__(self, puzzle_string = "123456780"):
        self.puzzle_string = puzzle_string


    def get_empty_index(self):
        return self.puzzle_string.index('0')
    

    def update_puzzle_string(self, new_string):
        self.puzzle_string = new_string


    def move(self, direction):
        empty_index = self.get_empty_index()
        new_string = ""
        if direction == 0:
            if empty_index not in [0, 3, 6]:
                new_string = self.puzzle_string[:empty_index-1] + '0' + self.puzzle_string[empty_index-1] + self.puzzle_string[empty_index+1:]
        elif direction == 1:
            if empty_index not in [2, 5, 8]:
                new_string = self.puzzle_string[:empty_index] + self.puzzle_string[empty_index+1] + '0' + self.puzzle_string[empty_index+2:]
        elif direction == 2:
            if empty_index not in [0, 1, 2]:
                new_string = self.puzzle_string[:empty_index-3] + '0' + self.puzzle_string[empty_index-2:empty_index] + self.puzzle_string[empty_index-3] + self.puzzle_string[empty_index+1:]
        elif direction == 3:
            if empty_index not in [6, 7, 8]:
                new_string = self.puzzle_string[:empty_index] + self.puzzle_string[empty_index+3] + self.puzzle_string[empty_index+1:empty_index+3] + '0' + self.puzzle_string[empty_index+4:]
        if new_string == "":
            return None
        else:
            self.update_puzzle_string(new_string)
            return self.puzzle_string
    

    def play(self, k):
        while k > 0:
            if self.move(random.randint(0,3)) is not None:
                k -= 1
        return self.puzzle_string
    

    def is_solved(self):
        return self.puzzle_string == self.goal_state
    

    def manhattan_distance(self):
        distance = 0
        for i in range(9):
            distance += abs(i - self.puzzle_string.index(str(i)))
        return distance
    

    


def print_path(message, path, end):
    puzzle_path = []
    print(message)
    if path is None:
        print("No solution found")
    else:
        for direction in path:
            if direction == 0:
                puzzle_path.append("L")
            elif direction == 1:
                puzzle_path.append("R")
            elif direction == 2:
                puzzle_path.append("U")
            elif direction == 3:
                puzzle_path.append("D")
        print("".join(puzzle_path))
    print(end)


puzzle = Puzzle()
puzzle.play(10)
print("Initial State: ", puzzle.puzzle_string, "\n")    
print_path("A* Search: ", puzzle.A_star_search(), "\n")
