import unittest

from optimization.grid_search import GridSearchOptimizer
from strategies.rsi_strategy import RSIStrategy


class TestGridSearchOptimizer(unittest.TestCase):
    def setUp(self):
        self.data = [
            {"rsi": 25, "price": 100, "profit": 10},
            {"rsi": 35, "price": 110, "profit": -5},
            {"rsi": 20, "price": 90, "profit": 15},
        ]
        self.param_grid = {
            "rsi_threshold": [20, 25, 30, 35]
        }
        self.optimizer = GridSearchOptimizer(RSIStrategy, self.data)

    def test_optimize(self):
        best_params, best_score = self.optimizer.optimize(self.param_grid)
        self.assertIn("rsi_threshold", best_params)
        self.assertGreaterEqual(best_score, 25)  # حداقل سود مورد انتظار


if __name__ == "__main__":
    unittest.main()
حر