****8-Puzzle Solver****

This Python script implements various algorithms to solve the 8-Puzzle problem. The 8-Puzzle is a sliding puzzle that consists of a 3x3 grid with 8 numbered tiles and one empty space. The goal is to move the tiles around to reach a target arrangement.

**Features**

The script includes implementations of the following algorithms to solve the 8-Puzzle problem:

1. Breadth-First Search (BFS)

2. Depth-First Search (DFS)

3. Depth-First Iterative Deepening (DFID)

4. Backtracking
**Algorithms******
**Breadth-First Search (BFS)**
Explores all nodes at the present depth level before moving on to nodes at the next depth level, using a queue.

**Depth-First Search (DFS)**

Explores as far down a branch as possible before backtracking, using a stack.

**Depth-First Iterative Deepening (DFID)**

Combines the depth-bounded nature of DFS with the completeness of BFS by progressively deepening the search depth.

**Backtracking**

Tries out different possibilities and backtracks by undoing steps if a dead end is reached until a solution is found.

****Classes and Methods****


**Node Class**

Represents a state of the puzzle and its parent state.

__init__(self, state=None, parent=None)

__str__(self)

**PuzzleSolver Class**

Solves the 8-puzzle problem using various algorithms.

__init__(self, start, goal)

is_solvable(self, state)

find_space(self, state)

find_moves(self, pos)

is_valid(self, move)

play_move(self, move, space, state)

generate_children(self, state)

solve_puzzle_bfs(self)

solve_puzzle_dfs(self)

solve_puzzle_dfid(self)

dls(self, node, depth_limit, visited)

solve_puzzle_backtracking(self)

displaySolutionPath(self, final_node)
