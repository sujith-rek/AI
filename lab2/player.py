import random


class Puzzle:
    puzzle_string = ""
    goal_state = "012345678"

    def __init__(self, puzzle_string="012345678"):
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
                new_string = self.puzzle_string[:empty_index-1] + '0' + \
                    self.puzzle_string[empty_index-1] + \
                    self.puzzle_string[empty_index+1:]
        elif direction == 1:
            if empty_index not in [2, 5, 8]:
                new_string = self.puzzle_string[:empty_index] + \
                    self.puzzle_string[empty_index+1] + \
                    '0' + self.puzzle_string[empty_index+2:]
        elif direction == 2:
            if empty_index not in [0, 1, 2]:
                new_string = self.puzzle_string[:empty_index-3] + '0' + self.puzzle_string[empty_index -
                                                                                           2:empty_index] + self.puzzle_string[empty_index-3] + self.puzzle_string[empty_index+1:]
        elif direction == 3:
            if empty_index not in [6, 7, 8]:
                new_string = self.puzzle_string[:empty_index] + self.puzzle_string[empty_index+3] + \
                    self.puzzle_string[empty_index+1:empty_index +
                                       3] + '0' + self.puzzle_string[empty_index+4:]
        if new_string == "":
            return None
        else:
            self.update_puzzle_string(new_string)
            return self.puzzle_string

    def play(self, k):
        while k > 0:
            if self.move(random.randint(0, 3)) is not None:
                k -= 1
        return self.puzzle_string

    def is_solved(self):
        return self.puzzle_string == self.goal_state

    def heuristic(self):
        puzzle_string = self.puzzle_string
        misplaced = 0
        for i in range(9):
            if puzzle_string[i] != str(i):
                misplaced += 1
        return misplaced

    def greedy(self):
        visited = set()
        priority_queue = [(self, [], 0)]
        while priority_queue:
            priority_queue.sort(key=lambda x: x[0].heuristic())
            (vertex, path, depth) = priority_queue.pop(0)
            if vertex.is_solved():
                return path
            if vertex not in visited:
                visited.add(vertex)
                for direction in range(4):
                    new_puzzle = Puzzle(vertex.puzzle_string)
                    if new_puzzle.move(direction) is not None:
                        priority_queue.append(
                            (new_puzzle, path + [direction], depth + 1))
        return None

    def a_star(self):
        visited = set()
        priority_queue = [(self, [], 0)]
        while priority_queue:
            priority_queue.sort(key=lambda x: x[2] + x[0].heuristic())
            (vertex, path, depth) = priority_queue.pop(0)
            if vertex.is_solved():
                return path
            if vertex not in visited:
                visited.add(vertex)
                for direction in range(4):
                    new_puzzle = Puzzle(vertex.puzzle_string)
                    if new_puzzle.move(direction) is not None:
                        priority_queue.append(
                            (new_puzzle, path + [direction], depth + 1))
        return None


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
print_path("A* Search: ", puzzle.a_star(), "\n")
print_path("Greedy Search: ", puzzle.greedy(), "\n")
