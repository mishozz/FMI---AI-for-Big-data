import numpy as np

DIRECTIONS = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0)
]

class Maze:
    def __init__(self, n, m, obstacles=None):
        if n <= 0 or m <= 0:
            raise ValueError('Invalid maze dimensions. N and M must be greater than 0')             
        self.n = n
        self.m = m
        self.grid = np.zeros((n, m))
        self.set_obstacles(obstacles)
                    
    def set_obstacles(self, obstacles=None):
        if not obstacles:
            return
        for i, j in obstacles:
            if 0 <= i < self.n and 0 <= j < self.m:
                self.grid[i][j] = 1
    
    def is_valid_move(self, row, col):
        return (self.is_in_grid(row, col) and not self.is_obstacle(row, col))
    
    def is_in_grid(self, row, col):
        return (0 <= row < self.n and 0 <= col < self.m)
    
    def is_obstacle(self, row, col):
        return (self.grid[row][col] == 1)
    
    def get_neighbors(self, node):
        row, col = node
        neighbors = []
        
        for dx, dy in DIRECTIONS:
            new_row, new_col = row + dx, col + dy
            if self.is_valid_move(new_row, new_col):
                neighbors.append((new_row, new_col))
                
        return neighbors
    
    def get_predecessors(self, node):
        row, col = node
        predecessors = []
        
        for dx, dy in DIRECTIONS:
            new_row, new_col = row - dx, col - dy
            if self.is_valid_move(new_row, new_col):
                predecessors.append((new_row, new_col))
                
        return predecessors
