from heapq import heappush, heappop
from dataclasses import dataclass, field
from typing import Tuple, Optional

@dataclass(order=True)
class Node:
    total_estimated_cost: float
    cost_from_start: float = field(compare=False)
    position: Tuple[int, int] = field(compare=False)
    parent: Optional['Node'] = field(default=None, compare=False)
    
    def __eq__(maze, other):
        if isinstance(other, Node):
            return maze.position == other.position
        return False


def a_star(maze, start, end):
        if not (maze.is_valid_move(*start) and maze.is_valid_move(*end)):
            return None
        
        # This is implemented as a list but is used as a priority queue (min-heap) through Python's heapq module
        # Contains nodes that have been discovered but not yet evaluated
        # Think of it as your "to-visit" list
        # Uses a list because we need to maintain order based on f_scores (f_score = g_score + heuristic)
        # Elements are ordered by f_score (estimated total cost) to always explore the most promising nodes first
        to_be_visited_set = []
        
        # Think of it as your "already-visited" list
        # Uses a set because we only care about whether a position has been visited (no duplicates needed)
        # Prevents the algorithm from re-exploring the same positions
        visited_set = set()
        
        start_node = Node(
            total_estimated_cost=maze.manhattan_distance(start, end),
            cost_from_start=0,
            position=start
        )
        
        # Add the start node to the open set
        heappush(to_be_visited_set, start_node)
        
        while to_be_visited_set:
            current = heappop(to_be_visited_set)
            
            # If we've reached the end, reconstruct and return the path
            if current.position == end:
                path = []
                while current:
                    path.append(current.position)
                    current = current.parent
                # Return the path in reverse order
                return path[::-1]
            
            # Add current position to closed set
            visited_set.add(current.position)
            
            # Check all neighbors
            for neighbor_node in maze.get_neighbors(current.position):
                if neighbor_node in visited_set:
                    continue
                
                # Calculate cost_from_start for the neighbor
                cost_from_start = current.cost_from_start + 1
                
                # Create neighbor node
                neighbor = Node(
                    total_estimated_cost=cost_from_start + maze.manhattan_distance(neighbor_node, end),
                    cost_from_start=cost_from_start,
                    position=neighbor_node,
                    parent=current
                )
                
                # Check if this is a better path to the neighbor
                existing_better = False
                for node in to_be_visited_set:
                    if node.position == neighbor_node and node.cost_from_start <= cost_from_start:
                        existing_better = True
                        break
                
                if not existing_better:
                    heappush(to_be_visited_set, neighbor)
        
        # No path found
        return None