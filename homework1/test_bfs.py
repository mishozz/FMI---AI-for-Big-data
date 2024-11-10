import unittest
from maze import Maze
from bfs import bfs

class TestBFS(unittest.TestCase):
    def setUp(self):
        n = 3
        m = 3
        self.maze = Maze(n, m)
    
    def test_valid_path(self):
        start_node = (0, 0)
        end_node = (2, 2)
        path, visited, is_end_node_found = bfs(self.maze, start_node, end_node)
        self.assertEqual(path, [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)])
        self.assertEqual(visited, [(0, 0), (0, 1), (1, 0), (0, 2), (1, 1), (2, 0), (1, 2), (2, 1), (2, 2)])
        self.assertTrue(is_end_node_found)

    def test_invalid_start_node(self):
        start_node = (-1, 0)
        end_node = (2, 2)
        with self.assertRaises(Exception):
            bfs(self.maze, start_node, end_node)

    def test_invalid_end_node(self):
        start_node = (0, 0)
        end_node = (3, 3)
        with self.assertRaises(Exception):
            bfs(self.maze, start_node, end_node)

    def test_no_path(self):
        self.maze.set_obstacles([(0,1),(1, 1), (2,1)])
        start_node = (0, 0)
        end_node = (2, 2)
        path, visited, is_end_node_found = bfs(self.maze, start_node, end_node)
        self.assertEqual(path, [])
        self.assertEqual(visited, [(0, 0), (1, 0), (2, 0)])
        self.assertFalse(is_end_node_found)

if __name__ == '__main__':
    unittest.main()