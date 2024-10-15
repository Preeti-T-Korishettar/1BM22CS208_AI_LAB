import heapq

# A class representing the 8-puzzle state
class PuzzleState:
    def __init__(self, matrix, goal, parent=None, move=None, depth=0):
        self.matrix = matrix
        self.goal = goal
        self.parent = parent
        self.move = move
        self.depth = depth
        self.zero_pos = self.find_zero()  # Find the position of 0 (empty space)
        self.heuristic = self.calculate_heuristic()
        self.total_cost = self.depth + self.heuristic  # f(n) = g(n) + h(n)

    def find_zero(self):
        # Find the position of the empty space (0)
        for i in range(3):
            for j in range(3):
                if self.matrix[i][j] == 0:
                    return (i, j)
        return None

    def calculate_heuristic(self):
        # Heuristic based on number of mismatched tiles
        mismatches = 0
        for i in range(3):
            for j in range(3):
                if self.matrix[i][j] != 0 and self.matrix[i][j] != self.goal[i][j]:
                    mismatches += 1
        return mismatches

    def generate_new_states(self):
        # Generate all possible moves (up, down, left, right) from the current state
        moves = []
        x, y = self.zero_pos
        possible_moves = [
            ('up', (x - 1, y)),
            ('down', (x + 1, y)),
            ('left', (x, y - 1)),
            ('right', (x, y + 1))
        ]
        for move, (new_x, new_y) in possible_moves:
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_matrix = [row[:] for row in self.matrix]
                # Swap the 0 (empty space) with the new position
                new_matrix[x][y], new_matrix[new_x][new_y] = new_matrix[new_x][new_y], new_matrix[x][y]
                moves.append(PuzzleState(new_matrix, self.goal, self, move, self.depth + 1))
        return moves

    def is_goal(self):
        # Check if the current state is the goal state
        return self.matrix == self.goal

    def __lt__(self, other):
        # Less than operator for priority queue (based on total cost)
        return self.total_cost < other.total_cost

    def __str__(self):
        # Print the matrix in a readable format
        return '\n'.join([' '.join(map(str, row)) for row in self.matrix]) + '\n'

def a_star(start_state):
    # A* search algorithm
    open_list = []
    heapq.heappush(open_list, start_state)
    closed_set = set()

    while open_list:
        current_state = heapq.heappop(open_list)

        if current_state.is_goal():
            return current_state

        closed_set.add(tuple(map(tuple, current_state.matrix)))

        for new_state in current_state.generate_new_states():
            state_tuple = tuple(map(tuple, new_state.matrix))
            if state_tuple not in closed_set:
                heapq.heappush(open_list, new_state)

    return None

def print_solution(solution):
    # Backtrack through the parent states and print each step
    steps = []
    current = solution
    while current:
        steps.append(current)
        current = current.parent

    steps.reverse()
    for i, step in enumerate(steps):
        print(f"Step {i}:")
        print(step)

def read_matrix(prompt):
    print(prompt)
    matrix = []
    elements = set()
    for i in range(3):
        while True:
            try:
                row = list(map(int, input(f"Enter row {i + 1} (space-separated, include 0 for empty): ").strip().split()))
                if len(row) != 3:
                    print("Each row must have exactly 3 numbers. Please try again.")
                    continue
                matrix.append(row)
                elements.update(row)
                break
            except ValueError:
                print("Invalid input. Please enter integers only.")
    # Validate that all numbers from 0 to 8 are present
    if elements != set(range(9)):
        raise ValueError("Invalid matrix. The matrix must contain all numbers from 0 to 8 exactly once.")
    return matrix

def main():
    try:
        initial_matrix = read_matrix("Enter the initial state:")
        goal_matrix = read_matrix("Enter the goal state:")

        start_state = PuzzleState(initial_matrix, goal_matrix)
        solution = a_star(start_state)

        if solution:
            print("\nSolution found:")
            print_solution(solution)
        else:
            print("No solution exists.")
    except ValueError as ve:
        print(f"Error: {ve}")

if __name__ == '__main__':
    main()
