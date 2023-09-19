import random
from collections import deque

class Puzzle:
    def __init__(self, state):
        self.state = list(state)

    def move(self, direction):
        index = self.state.index('0')
        if direction == 0:  # Move blank to the left
            if index % 3 != 0:
                self.state[index], self.state[index - 1] = self.state[index - 1], self.state[index]
            else:
                return None
        elif direction == 1:  # Move blank to the right
            if index % 3 != 2:
                self.state[index], self.state[index + 1] = self.state[index + 1], self.state[index]
            else:
                return None
        elif direction == 2:  # Move blank up
            if index - 3 >= 0:
                self.state[index], self.state[index - 3] = self.state[index - 3], self.state[index]
            else:
                return None
        elif direction == 3:  # Move blank down
            if index + 3 < len(self.state):
                self.state[index], self.state[index + 3] = self.state[index + 3], self.state[index]
            else:
                return None
        return ''.join(self.state)

    def play(self, k):
        for _ in range(k):
            move_direction = random.randint(0, 3)
            new_state = self.move(move_direction)
            if new_state is not None:
                self.state = list(new_state)

def dfs(puzzle, goal):
    stack = [(puzzle, [])]
    while stack:
        node, path = stack.pop()
        if ''.join(node) == goal:
            return path
        for direction in range(4):
            new_puzzle = Puzzle(node[:])
            new_state = new_puzzle.move(direction)
            if new_state is not None and new_state not in path:
                stack.append((list(new_state), path + [new_state]))

def bfs(puzzle, goal):
    queue = deque([(puzzle, [])])
    while queue:
        node, path = queue.popleft()
        if ''.join(node) == goal:
            return path
        for direction in range(4):
            new_puzzle = Puzzle(node[:])
            new_state = new_puzzle.move(direction)
            if new_state is not None and new_state not in path:
                queue.append((list(new_state), path + [new_state]))

def dls(puzzle, goal, limit):
    stack = [(puzzle, [])]
    while stack:
        node, path = stack.pop()
        if ''.join(node) == goal:
            return path
        if len(path) < limit:
            for direction in range(4):
                new_puzzle = Puzzle(node[:])
                new_state = new_puzzle.move(direction)
                if new_state is not None and new_state not in path:
                    stack.append((list(new_state), path + [new_state]))

def ids(puzzle, goal):
    for limit in range(100):  
        result = dls(puzzle, goal, limit)
        if result is not None:
            return result

# Testing the code
puzzle = Puzzle('012345678')
print("Initial state:", ''.join(puzzle.state))
puzzle.play(10)
print("State after playing:", ''.join(puzzle.state))
print("Path to goal (BFS):", bfs(puzzle.state[:], '012345678'))
print("Path to goal (DLS):", dls(puzzle.state[:], '012345678', 10))
print("Path to goal (IDS):", ids(puzzle.state[:], '012345678'))
print("Path to goal (DFS):", dfs(puzzle.state[:], '012345678'))