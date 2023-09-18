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
        queue = [(self, [], 0)]
        while queue:
            (vertex, path, depth) = queue.pop(0)
            if vertex.is_solved():
                return path
            if vertex not in visited:
                visited.add(vertex)
                for direction in range(4):
                    new_puzzle = Puzzle(vertex.puzzle_string)
                    if new_puzzle.move(direction) is not None:
                        queue.append((new_puzzle, path + [direction], depth+1))
        return None
    

    def depth_first_search(self):
        visited = set()
        stack = [(self, [], 0,"")]
        while stack:
            (vertex, path, depth, state) = stack.pop()
            if vertex.is_solved():
                return path
            if vertex.puzzle_string not in visited:
                visited.add(vertex.puzzle_string)
                for direction in range(4):
                    new_puzzle = Puzzle(vertex.puzzle_string)
                    if new_puzzle.move(direction) is not None:
                        stack.append((new_puzzle, path + [direction], depth+1, state + vertex.puzzle_string))
                
        return None
    

    def depth_limited_search(self, limit):
        visited = set()
        stack = [(self, [], 0,"")]
        while stack:
            (vertex, path, depth, state) = stack.pop()
            if vertex.is_solved():
                return path
            if vertex.puzzle_string not in visited and depth < limit:
                visited.add(vertex.puzzle_string)
                for direction in range(4):
                    new_puzzle = Puzzle(vertex.puzzle_string)
                    if new_puzzle.move(direction) is not None:
                        stack.append((new_puzzle, path + [direction], depth+1, state + vertex.puzzle_string))
                
        return None
    

    def iterative_deepening_search(self,depth=5,increment=1):
        while True:
            result = self.depth_limited_search(depth)
            if result is not None:
                print("Treshold depth before solution: ",depth) 
                return result
            depth += increment


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
print("Generated puzzle: ", puzzle.play(10), "\n")
print_path("Breadth First Search : : ",puzzle.breadth_first_search(),'\n')
print_path("Depth Limiting Search : ",puzzle.depth_limited_search(10),'\n')
print_path("Iterative Deepening search : ",puzzle.iterative_deepening_search(),'\n')
print_path("Depth First Search : ",puzzle.depth_first_search(),'\n')

