import ast
from maze import Maze
from visualizer import visualize_search

class KnowledgeBasedMazeSolver:
    def __init__(self, maze):
        self.maze = maze

    def forward_chain(self, start, end):
        visited = []
        explorable = [(start, [start])]
        
        while explorable:
            current, path = explorable.pop(0)
            visited.append(current)
            
            if current == end:
                return path, visited
            
            for neighbor in self.maze.get_neighbors(current):
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    explorable.append((neighbor, new_path))
            
        return None, None

    def find_path(self, start, end):
        if (not self.maze.is_valid_move(start[0], start[1]) or
            not self.maze.is_valid_move(end[0], end[1])):
            return None
        
        return self.forward_chain(start, end)


if __name__ == "__main__":
    # Uncomment the following lines if you want custom input for Maze and comment out the default maze
    #
    # n_input = input("Enter N (or press ENTER for default 10): ")
    # m_input = input("Enter M (or press ENTER for default 10): ")
    # n = int(n_input) if n_input else 10
    # m = int(m_input) if m_input else 10  
    # obstacles_input = input("Enter array of obstacles (e.g., [(0, 2), (1, 2)]), or press Enter Defaults: ")
    # obstacles = ast.literal_eval(obstacles_input) if obstacles_input else [(0, 2), (1, 2), (2, 2), (2, 3), (3, 1),(4, 1), (4, 2), (4, 3), (5, 3), (6, 3)]
    # start_node_input = input("Enter start node (or press Enter for default (0, 0): ")
    # start_node = ast.literal_eval(start_node_input) if start_node_input else (0, 0)
    # end_node_input = input("Enter end node (or press Enter for default (9,9): ")
    # end_node = ast.literal_eval(end_node_input) if end_node_input else (9, 9)
    
    # maze = Maze(n, m, obstacles)
    
    start_node = (0, 0)
    end_node = (4, 5)
    maze = Maze(5, 6, obstacles=[(0, 1), (2, 1), (3,1), (2,3), (3,4), (4,4)])
    
    solver = KnowledgeBasedMazeSolver(maze)
    path, visited = solver.find_path(start_node, end_node)
    
    if path:
        print("Solution Path:", path)
        visualize_search(maze.grid, start_node, end_node, path, visited, "Forward Chaining")
    else:
        print("No path found")