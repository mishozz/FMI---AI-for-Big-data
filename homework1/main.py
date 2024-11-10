from bfs import bfs
from visualizer import visualize_search
from maze import Maze
from astar_algorithm import a_star
import ast

if __name__ == "__main__":
    n_input = input("Enter N (or press ENTER for default 10): ")
    m_input = input("Enter M (or press ENTER for default 10): ")
    n = int(n_input) if n_input else 10
    m = int(m_input) if m_input else 10  
    obstacles_input = input("Enter array of obstacles (e.g., [(0, 2), (1, 2)]), or press Enter Defaults: ")
    obstacles = ast.literal_eval(obstacles_input) if obstacles_input else [(0, 2), (1, 2), (2, 2), (2, 3), (3, 1),(4, 1), (4, 2), (4, 3), (5, 3), (6, 3)]
    start_node_input = input("Enter start node (or press Enter for default (0, 0): ")
    start_node = ast.literal_eval(start_node_input) if start_node_input else (0, 0)
    end_node_input = input("Enter end node (or press Enter for default (9,9): ")
    end_node = ast.literal_eval(end_node_input) if end_node_input else (9, 9)
    
    maze = Maze(n, m, obstacles)
    
    path = a_star(maze, start_node, end_node)
    if path:
        print(f"Path found by A* algorithm: {path}")
    else:
        print("No path exists!")
    
    
    path, visited_nodes, success = bfs(maze, start_node, end_node)
    if success:
        print(f"Path found by BFS: {path}")
        visualize_search(maze.grid, start_node, end_node, path, visited_nodes)
    else:
        print("No path exists!")
