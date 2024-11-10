import unittest
from maze import Maze
from astar_algorithm import a_star

class TestAStar(unittest.TestCase):
    def setUp(self):
        n = 3
        m = 3
        self.maze = Maze(n, m)
    
    def test_valid_path(self):
        start_node = (0, 0)
        end_node = (2, 2)
        path = a_star(self.maze, start_node, end_node)
        self.assertEqual(path, [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)])

    def test_invalid_start_node(self):
        start_node = (-1, 0)
        end_node = (2, 2)
        path = a_star(self.maze, start_node, end_node)
        self.assertIsNone(path)

    def test_invalid_end_node(self):
        start_node = (0, 0)
        end_node = (3, 3)
        path = a_star(self.maze, start_node, end_node)
        self.assertIsNone(path)

    def test_no_path(self):
        self.maze.set_obstacles([(0,1),(1, 1), (2,1)])
        start_node = (0, 0)
        end_node = (2, 2)
        path = a_star(self.maze, start_node, end_node)
        self.assertIsNone(path)

if __name__ == '__main__':
    unittest.main()
