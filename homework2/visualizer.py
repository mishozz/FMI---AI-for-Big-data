import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from enum import Enum
from matplotlib import colors
from matplotlib.patches import Patch

FRAME_INTERVAL = 100

class NODE_COLOR(Enum):
    NOT_VISITED = 'gray'
    OBSTACLE = 'red'
    VISITED = 'lightblue'
    PATH = 'yellow'
    START = 'green'
    END = 'purple'

class Node(Enum):
    NOT_VISITED = 0
    OBSTACLE = 1
    VISITED = 2
    PATH = 3
    START = 4
    END = 5


def visualize_search(maze, start_node, end_node, path, visited_nodes, plot_title):
    fig, ax = plt.subplots(figsize=(8, 8))
    
    def update(frame):
        ax.clear()
        maze_plot = np.copy(maze)
        
        for node in visited_nodes[:frame]:
            if node != start_node and node != end_node:
                maze_plot[node] = Node.VISITED.value
        
        if frame == len(visited_nodes):
            for node in path:
                if node != start_node and node != end_node:
                    maze_plot[node] = Node.PATH.value
        
        maze_plot[start_node] = Node.START.value
        maze_plot[end_node] = Node.END.value
            
        cmap = colors.ListedColormap([
            NODE_COLOR.NOT_VISITED.value,
            NODE_COLOR.OBSTACLE.value,
            NODE_COLOR.VISITED.value,
            NODE_COLOR.PATH.value,
            NODE_COLOR.START.value,
            NODE_COLOR.END.value
        ])
        bounds = [0, 1, 2, 3, 4, 5, 6]
        norm = colors.BoundaryNorm(bounds, cmap.N)
        ax.imshow(maze_plot, cmap=cmap, norm=norm)
        ax.grid(True)
        ax.set_title(plot_title + f' with visited nodes: {frame}')
        
        legend_labels = [
            ("Not Visited", NODE_COLOR.NOT_VISITED.value),
            ("Obstacle", NODE_COLOR.OBSTACLE.value),
            ("Visited", NODE_COLOR.VISITED.value),
            ("Path", NODE_COLOR.PATH.value),
            ("Start Node", NODE_COLOR.START.value),
            ("End Node", NODE_COLOR.END.value)
        ]
        legend_patches = [
            Patch(color=color, label=label) for label, color in legend_labels
        ]
        ax.legend(handles=legend_patches, loc="upper right")
        
    _ = FuncAnimation(
        fig, 
        update,
        frames=len(visited_nodes) + 1,
        interval=FRAME_INTERVAL,
        repeat=False
    )
    plt.show(block=True)
