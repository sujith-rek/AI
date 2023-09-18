# The eight puzzle has 8 movable tiles within a 3 × 3 frame with one blank square. Imagine that in
# each move the blank can be moved Up—Down—Left—Right. Note some moves may not be
# possible in certain states. The goal of the puzzle is to reach from an initial configuration to a final
# goal configuration that looks as follows: 1 2 3 4 5 6 7 8.
# Clearly, the puzzle has 9! = 362880 states. It turns out that the goal state cannot be reached
# from any arbitrary initial state. So, the set of states can be broken into two subsets a) states that
# are reachable from the goal state and b) the rest that cannot be reached from the goal state. A
# state can be represented as a string of length 9 where we write row1, row2, row3 as a sequence
# with the blank symbolized by 0. So the goal state will be the string 012345678.


# Based on the above description answer the questions below.
# 1. Model the eight puzzle as a class named Puzzle using the above state representation. Define
# methods that allow the puzzle to transition from state to state on a move. The move() method
# can take a single integer argument that can have values 0, 1, 2, 3, that represents moving the
# blank to the left, right, up, down respectively. If a particular move is impossible then it should
# return the state None.


# Also, implement a method named play() that takes a single positive integer as argument, say k,
# and makes k moves starting with the current state of a puzzle object. Each move is chosen
# randomly from the set of possible moves in the current state at each stage. [10,10,10=30]
# 2. implement a) depth first search, b) breadth first search, c) depth limited search and d)
# iterative deepening search. You can use default arguments in the generic graph method to pass
# necessary arguments to reorder OPEN as needed for each type of search. [10,10,10,10=40]


# 3. Use the four uninformed search algorithms in the previous question to search for a solution to
# the 8-puzzle from a start state to a goal state. You can generate legal start states by using the
# play() method with the initial state as the goal state. [10,10,10,10=40]

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
    
    def breadth_first_search(self):
        visited = set()
        queue = [(self, [])]
        init_state = self.puzzle_string
        while queue:
            current_puzzle, path = queue.pop(0)
            visited.add(current_puzzle.puzzle_string)
            if current_puzzle.is_solved():
                path.insert(0, init_state)
                return path
            for direction in range(4):
                new_puzzle = Puzzle(current_puzzle.puzzle_string)
                new_state = new_puzzle.move(direction)
                if new_state is not None and new_state not in visited:
                    new_path = path + [new_state]
                    queue.append((new_puzzle, new_path))
        return None

puzzle = Puzzle()
print(puzzle.play(10))
print(puzzle.breadth_first_search())

    

            

    
    
        


        

