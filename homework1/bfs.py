from collections import deque

DIRECTIONS = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0)
]

def bfs(maze, start_node, end_node):
        start_x = start_node[0]
        start_y = start_node[1]
        end_x = end_node[0]
        end_y = end_node[1]
        if not maze.is_valid_move(start_x, start_y) or not maze.is_valid_move(end_x, end_y):
            raise Exception(f'Invalid start or end nodes. Values must be within the maze and not obstacles. N: {maze.n}, M: {maze.m}, Start: {start_node}, End: {end_node}')
            
        queue = deque([(start_x, start_y)])
        visited = [(start_x, start_y)]
        child_parent_map = {(start_x, start_y): None}
        is_end_node_found = False
        
        while queue:
            current_x, current_y = queue.popleft()
            
            if (current_x, current_y) == (end_x, end_y):
                is_end_node_found = True
                break
                
            for dx, dy in DIRECTIONS:
                next_x, next_y = current_x + dx, current_y + dy
                if (maze.is_valid_move(next_x, next_y) and (next_x, next_y) not in visited):
                    queue.append((next_x, next_y))
                    visited.append((next_x, next_y))
                    child_parent_map[(next_x, next_y)] = (current_x, current_y)
        
        path = []
        if is_end_node_found:
            path = get_path_to(end_node ,child_parent_map)
            
        return path, visited, is_end_node_found


def get_path_to(end_node, child_parent_map):
        path = []
        current_node = end_node
        
        while current_node is not None:
            path.append(current_node)
            current_node = child_parent_map[current_node]
        path.reverse()
        
        return path