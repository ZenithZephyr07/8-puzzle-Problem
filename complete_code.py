import sys 
sys.setrecursionlimit(2000)  # Increase recursion limit if needed
class Node:
    def __init__(self, state=None, parent=None):
        self.state = state
        self.parent = parent
        if self.state is None:
            self.state = [[]]

    def __str__(self):
        string = ""
        for i in range(len(self.state)):
            for j in range(len(self.state[i])):
                string += str(self.state[i][j]) + " "
            string += "\n"
        return string

class PuzzleSolver:
    def __init__(self, start, goal):
        self.start = start
        self.goal = goal

    def is_solvable(self, state):
        # Check if puzzle is solvable or not --> if inversion_count is even then solvable else not solvable
        array1D = []
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] != ' ':
                    array1D.append(state[i][j])
        invertibility_count = 0
        for i in range(len(array1D)):
            for j in range(i + 1, len(array1D)):
                if array1D[i] > array1D[j]:
                    invertibility_count += 1
        return invertibility_count % 2 == 0

    def find_space(self, state):
        # Find empty space in the 2D array
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] == ' ':
                    return (i, j)
        return None

    def find_moves(self, pos):
        # Find all possible moves by sliding the space with number up, down, right, left
        x, y = pos
        return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

    def is_valid(self, move):
        # Check from moves array that which moves are Valid
        # Validity depends upon the bounds of array ---> if within bounds of 2D array then valid move else not
        x, y = move
        return (0 <= x < len(self.start.state)) and (0 <= y < len(self.start.state[0]))

    def play_move(self, move, space, state):
        # Swapping the space with the number on the move index in 2D array but here keep in mind that the lists are mutable,so in order to create all the possible moves we need to create a copy of the current state
        x1, y1 = move
        x2, y2 = space
        new_state = [row[:] for row in state]
        if not self.is_valid(move):
            return None
        new_state[x2][y2], new_state[x1][y1] = new_state[x1][y1], new_state[x2][y2]
        return new_state

    def generate_children(self, state):
        # Generate all the possible children of the current state by using play_move that returns a new state by applying a valid move
        children = []
        space = self.find_space(state)
        moves = self.find_moves(space)
        for move in moves:
            if self.is_valid(move):
                new_state = self.play_move(move, space, state)
                if new_state is not None:
                    children.append(new_state)
        return children

    def solve_puzzle_bfs(self):
        # BFS works on the principle of FIFO, so implement by keeping in mind the queue working using list
        queue = [self.start]
        visited = set()  # To keep track of the visited nodes, in order to avoid infinite loop
        while queue:
            current_state = queue.pop(0)  # pop 1st element
            if self.goal == current_state.state:
                self.displaySolutionPath(current_state)
                return True
            state_as_tuple = ()#Converting 2D array in tuple into tuple as we can't directly add the 2D array into set, because set can't be mutable
            for row in current_state.state:
                row_tuple = ()
                for item in row:
                    row_tuple += (item,)
                state_as_tuple += (row_tuple,)
            if state_as_tuple not in visited:
                visited.add(state_as_tuple)
                children = self.generate_children(current_state.state)
                for child in children:
                    if child is not None:
                        child_node = Node(state=child, parent=current_state)
                        queue.append(child_node)
        return False
    def solve_puzzle_dfs(self):
        # DFS works on the principle of LIFO, so implement by keeping in mind the stack working using list
        stack = [self.start]
        visited = set()  # To keep track of the visited nodes, in order to avoid infinite loop
        while stack:
            current_state = stack.pop()  # pop last element
            if self.goal == current_state.state:
                self.displaySolutionPath(current_state)
                return True
            state_as_tuple = ()#Converting 2D array in tuple into tuple as we can't directly add the 2D array into set, because set can't be mutable
            for row in current_state.state:
                row_tuple = ()
                for item in row:
                    row_tuple += (item,)
                state_as_tuple += (row_tuple,)
            if state_as_tuple not in visited:
                visited.add(state_as_tuple)
                children = self.generate_children(current_state.state)
                for child in children:
                    if child is not None:
                        child_node = Node(state=child, parent=current_state)
                        stack.append(child_node)
        return False
    def solve_puzzle_dfid(self):
        #DFID is combination of the DFS and BFS, it uses the depth first search to explore the deepest node first and then it uses the breadth first search to explore the nodes in the breadth first manner
        depth = 0
        while True: #Increase depth until solution is found
            visited = set()
            result = self.dls(self.start,depth,visited)
            if result :
                self.displaySolutionPath(result)
                return True
            depth += 1#Increment depth, if goal not found at current depth
    def dls(self, node, depth_limit, visited):
        if self.goal == node.state:#Goal is reached return True & start displaying solution path
            return node
        if depth_limit == 0:#DLS search at a specified depth, like generate the children of the node at a specified depth, & check in dfs manner means moving down to up , 1st checking the 1st children of the parent node then 2nd children of the parent node and so on
            return None
        state_as_tuple = ()#Converting 2D array in tuple into tuple as we can't directly add the 2D array into set, because set can't be mutable
        for row in node.state:
            row_tuple = ()
            for item in row:
                row_tuple += (item,)
            state_as_tuple += (row_tuple,)
            if state_as_tuple not in visited:
                visited.add(state_as_tuple)#Mark node as visited
                children = self.generate_children(node.state)
                for child in children:
                    if child is not None:
                        child_node = Node(state=child, parent=node)
                        result = self.dls(child_node,depth_limit-1,visited)
                        if result:
                            return result
        return None
    def solve_puzzle_backtracking(self):
        #Backtracking is a technique used to solve problems by trying out different possibilities and undoing ("backtracking") them if they lead to a dead end.
        max_depth = 100#Set a depth limit to avoid exceeding recursion limit
        visited = set()
        def backtracking(node,depth):
            if depth == 0 :#explored all the paths & reached the depth limit without finding goal
                return None
            state_as_tuple = ()#Converting 2D array in tuple into tuple as we can't directly add the 2D array into set, because set can't be mutable
            for row in node.state:
                row_tuple = ()
                for item in row:
                    row_tuple += (item,)
                state_as_tuple += (row_tuple,)
            if state_as_tuple in visited:
                return None
            visited.add(state_as_tuple)
            if node.state == self.goal:
                self.displaySolutionPath(node)
                return True
            children = self.generate_children(node.state)
            for child in children:
                if child is not None:
                    child_node = Node(state=child,parent=node)
                    result = backtracking(child_node,depth-1)
                    if result:
                        return result
            return None
        return backtracking(self.start,sys.getrecursionlimit()-10)
    def displaySolutionPath(self, final_node):
        path = []
        while final_node is not None:
            path.append(final_node)
            final_node = final_node.parent
        path.reverse()
        Depth = len(path)
        for i in range(len(path)):
            print(f"Depth : {i}\n{path[i]}")
        print("\n",Depth)
            
start = Node([[4, 7, 8], [3, 6, 5], [1, 2, ' ']])
goal = [[1, 2, 3], [4, 5, 6], [7, 8, ' ']]
solver = PuzzleSolver(start=start, goal=goal)
# print("Puzzle Solution Using the BFS Algorithm\n----------------------------------------------------")
# solver.solve_puzzle_bfs()
# print("----------------------------------------------------")
# print("Puzzle Solution Using the DFS Algorithm\n----------------------------------------------------")
# solver.solve_puzzle_dfs()
# print("----------------------------------------------------")
# print("Puzzle Solution Using the DFID Algorithm\n----------------------------------------------------")
# solver.solve_puzzle_dfid()
# print("----------------------------------------------------")
print("Puzzle Solution Using the backtracking Algorithm\n----------------------------------------------------")
solver.solve_puzzle_backtracking()
print("----------------------------------------------------")
