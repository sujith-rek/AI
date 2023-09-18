import random
class Puzzle:

    initial_state = (1,2,3,4,5,6,7,8,0)
    goal_state = (1,2,3,4,5,6,7,8,0)

    def __init__(self, initial_state = (1,2,3,4,5,6,7,8,0), goal_state = (1,2,3,4,5,6,7,8,0)):
        self.initial_state = initial_state
        self.goal_state = goal_state

    
    def get_zero_index(self):
        return self.initial_state.index(0)
    
    
    def update_initial_state(self, new_initial_state):
        self.initial_state = new_initial_state
    

    def update_goal_state(self, new_goal_state):
        self.goal_state = new_goal_state
    

    # we check if the direction is valid
    # if valid, we split the list and swap the 0 with the number in the direction
    # then we join the list back together
    # if not valid, we return None
    def move(self, direction):
        z_index = self.get_zero_index()
        new_initial_state = list(self.initial_state)
        if direction == 'U':
            if z_index not in [0, 1, 2]:
                new_initial_state[z_index], new_initial_state[z_index - 3] = new_initial_state[z_index - 3], new_initial_state[z_index]
        elif direction == 'D':
            if z_index not in [6, 7, 8]:
                new_initial_state[z_index], new_initial_state[z_index + 3] = new_initial_state[z_index + 3], new_initial_state[z_index]
        elif direction == 'L':
            if z_index not in [0, 3, 6]:
                new_initial_state[z_index], new_initial_state[z_index - 1] = new_initial_state[z_index - 1], new_initial_state[z_index]
        elif direction == 'R':
            if z_index not in [2, 5, 8]:
                new_initial_state[z_index], new_initial_state[z_index + 1] = new_initial_state[z_index + 1], new_initial_state[z_index]
        else:
            return None
        self.update_initial_state(tuple(new_initial_state))
        return self.initial_state
    

    def play(self, k):
        while k > 0:
            if self.move(random.choice(['U', 'D', 'L', 'R'])) is not None:
                k -= 1
        return self.initial_state
    

    def is_puzzle_solved(self):
        return self.initial_state == self.goal_state
    

    def breadth_first_search(self, goal_path = []):
        completed_states = set()
        return self.bfs(self.initial_state, goal_path, completed_states)


    def bfs(self, state, goal_path, completed_states):
        st = [(state, [])]
        st.append((state, []))
        while st:
            (state, path) = st.pop(0)
            if state == self.goal_state:
                return path
            else:
                completed_states.add(state)
                for direction in ['U', 'D', 'L', 'R']:
                    new_puzzle = Puzzle(state)
                    if new_puzzle.move(direction) is not None and new_puzzle.initial_state not in completed_states:
                        st.append((new_puzzle.initial_state, path + [direction]))
        return None
        
    
    def depth_first_search(self, goal_path = []):
        completed_states = set()
        return self.dfs(self.initial_state, goal_path, completed_states)
    

    def dfs(self, state, goal_path, completed_states):
        st = [(state, [])]
        while st:
            (state, path) = st.pop()
            if state == self.goal_state:
                return path
            else:
                completed_states.add(state)
                for direction in ['U', 'D', 'L', 'R']:
                    new_puzzle = Puzzle(state)
                    if new_puzzle.move(direction) is not None and new_puzzle.initial_state not in completed_states:
                        st.append((new_puzzle.initial_state, path + [direction]))
        return None

    
    def iterative_deepening_search(self, goal_path = [], depth = 10,increment = 1):
        completed_states = set()
        return self.ids(self.initial_state, goal_path, depth, increment,completed_states)
    

    def ids(self, state, goal_path, depth, increment, completed_states):
        current_depth = depth
        while current_depth > 0:
            path = self.dls(state, goal_path, completed_states, current_depth)
            if path is not None:
                return path
            current_depth += increment
        return None
    
    
    def depth_limited_search(self, goal_path = [], limit = 10):
        completed_states = set()
        return self.dls(self.initial_state, goal_path, completed_states, limit)
    

    def dls(self, state, goal_path,completed_states, limit=10):
        st = [(state, [])]
        while st:
            (state, path) = st.pop()
            if state == self.goal_state:
                return path
            else:
                completed_states.add(state)
                for direction in ['U', 'D', 'L', 'R']:
                    new_puzzle = Puzzle(state)
                    if new_puzzle.move(direction) is not None and new_puzzle.initial_state not in completed_states and len(path) < limit:
                        st.append((new_puzzle.initial_state, path + [direction]))
    

    def print_path(self, path):
        if path is None:
            print("No solution found")
        else:
            print(path, end = " ")
            print("\n\n")


def main():
    puzzle = Puzzle()
    puzzle.play(20)
    print("Initial state: ", puzzle.initial_state)
    print("Goal state: ", puzzle.goal_state)
    print("BFS: ", end = "")
    puzzle.print_path(puzzle.breadth_first_search())
    print("DLS: ", end = "")
    puzzle.print_path(puzzle.depth_limited_search())
    print("IDS: ", end = "")
    puzzle.print_path(puzzle.iterative_deepening_search())
    print("DFS: ", end = "")
    puzzle.print_path(puzzle.depth_first_search())


if __name__ == "__main__":
    main()
        
