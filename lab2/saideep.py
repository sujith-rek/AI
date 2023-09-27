import random
from collections import deque

class PuzzleState:
    def __init__(self, state,parent = None):
        self.state = state
        self.parent = parent
    
    def get_blank_index(self):
        return self.state.index(0)
    
    def move_blank(self, direction):
        blank = self.get_blank_index()
        if direction == 'U':
            if blank >= 3: 
                self.state[blank], self.state[blank-3] = self.state[blank-3], self.state[blank]
        elif direction == 'D':
            if blank < 6:
                self.state[blank], self.state[blank+3] = self.state[blank+3], self.state[blank]
        elif direction == 'L':
            if blank not in [0, 3, 6]:
                self.state[blank], self.state[blank-1] = self.state[blank-1], self.state[blank]
        elif direction == 'R':
            if blank not in [2, 5, 8]:
                self.state[blank], self.state[blank+1] = self.state[blank+1], self.state[blank]
    
    def play_random_moves(self, num_moves):
        directions = ['U', 'D', 'L', 'R']
        for _ in range(num_moves):
            direction = random.choice(directions)
            self.move_blank(direction)
                

# Heuristic 1 - number of misplaced tiles
def h1(state):
    count = 0
    for i in range(9):
        if state.state[i] != i:
            count += 1
    return count

# Heuristic 2 - sum of Manhattan distances    
def h2(state):
    sum_dist = 0
    for i in range(9):
        val = state.state[i]
        if val != 0:
            target_row = val // 3
            target_col = val % 3
            current_row = i // 3
            current_col = i % 3
            sum_dist += abs(target_row - current_row) + abs(target_col - current_col)
    return sum_dist
    

# Generate random initial state
puzzle = PuzzleState([0,1,2,3,4,5,6,7,8])  
puzzle.play_random_moves(10)

print("Initial state:")
print(puzzle.state)

print("h1:", h1(puzzle))
print("h2:", h2(puzzle))

# Greedy search
def greedy_search(initial_state, heuristic):
    
    explored = set()
    frontier = deque([initial_state])
    candidates = []
    
    while frontier:
      
        state = frontier.popleft()
        
        if state.state == [0,1,2,3,4,5,6,7,8]:
            return reconstruct_path(state)
            
        explored.add(tuple(state.state))

        for d in ['L', 'R', 'U', 'D']:
          
            new_state = PuzzleState(state.state[:], state)
            new_state.move_blank(d)
            
            if tuple(new_state.state) not in explored:
                frontier.append(new_state)
                candidates.append(new_state)
                
        candidates.sort(key=lambda s: heuristic(s))
        frontier = deque(candidates)
        candidates = []
        
# Reconstruct path
def reconstruct_path(state):
    path = []
    while state:
        path.append(state.state)
        state = state.parent
    return path[::-1]

# A* search 
def astar_search(initial_state, heuristic):

    explored = set()
    frontier = deque([(initial_state, 0)]) 
    candidates = []

    while frontier:

        state, cost = frontier.popleft()
        
        if state.state == [0,1,2,3,4,5,6,7,8]:
            return reconstruct_path(state)
            
        explored.add(tuple(state.state))

        for d in ['L', 'R', 'U', 'D']:

            new_state = PuzzleState(state.state[:], state)  
            new_state.move_blank(d)
            new_cost = cost + 1
            
            if tuple(new_state.state) not in explored:
                frontier.append((new_state, new_cost))
                candidates.append((new_state, new_cost))
                
        candidates.sort(key=lambda x: x[1] + heuristic(x[0]))
        frontier = deque(candidates)
        candidates = []
        
# Main
path = greedy_search(puzzle, h1)
print("Greedy (h1):", path)

path = greedy_search(puzzle, h2)
print("Greedy (h2):", path) 

path = astar_search(puzzle, h1)
print("A* (h1):", path)

path = astar_search(puzzle, h2)
print("A* (h2):", path)