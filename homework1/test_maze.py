import unittest
from maze import Maze

class TestMaze(unittest.TestCase):
    def setUp(self): 
        self.maze = Maze(3, 3)
    
    def test_valid_maze_dimensions(self):
        self.assertEqual(self.maze.n, 3)
        self.assertEqual(self.maze.m, 3)
        self.assertEqual(self.maze.grid.shape, (3, 3))

    def test_invalid_maze_dimensions(self):
        with self.assertRaises(ValueError):
            Maze(0, 3)
        with self.assertRaises(ValueError):
            Maze(3, -1)

    def test_set_obstacles(self):
        obstacles = [(0, 1), (1, 1)]
        self.maze.set_obstacles(obstacles)
        self.assertEqual(self.maze.grid[0][1], 1)
        self.assertEqual(self.maze.grid[1][1], 1)
        self.assertEqual(self.maze.grid[2][2], 0)

    def test_is_valid_move(self):
        self.assertTrue(self.maze.is_valid_move(0, 0))
        self.assertTrue(self.maze.is_valid_move(2, 2))
        self.assertFalse(self.maze.is_valid_move(3, 3))
        self.assertFalse(self.maze.is_valid_move(-1, 0))

    def test_is_in_grid(self):
        self.assertTrue(self.maze.is_in_grid(0, 0))
        self.assertTrue(self.maze.is_in_grid(2, 2))
        self.assertFalse(self.maze.is_in_grid(3, 3))
        self.assertFalse(self.maze.is_in_grid(-1, 0))

    def test_is_obstacle(self):
        obstacles = [(0, 1), (1, 1)]
        self.maze.set_obstacles(obstacles)
        self.assertTrue(self.maze.is_obstacle(0, 1))
        self.assertTrue(self.maze.is_obstacle(1, 1))
        self.assertFalse(self.maze.is_obstacle(0, 0))
        self.assertFalse(self.maze.is_obstacle(2, 2))

    def test_manhattan_distance(self):
        self.assertEqual(self.maze.manhattan_distance((0, 0), (2, 2)), 4)
        self.assertEqual(self.maze.manhattan_distance((1, 1), (1, 2)), 1)
        self.assertEqual(self.maze.manhattan_distance((2, 2), (0, 0)), 4)

    def test_get_neighbors(self):
        neighbors = self.maze.get_neighbors((1, 1))
        self.assertEqual(neighbors, [(1, 2), (2, 1), (1, 0), (0, 1)])

if __name__ == '__main__':
    unittest.main()
