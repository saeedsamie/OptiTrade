import unittest

from evaluation.backtesting import Backtester
from strategies.rsi_strategy import RSIStrategy


class TestBacktester(unittest.TestCase):
    def setUp(self):
        self.data = [
            {"rsi": 25, "price": 100, "profit": 10},
            {"rsi": 35, "price": 110, "profit": -5},
            {"rsi": 20, "price": 90, "profit": 15},
        ]
        self.parameters = {"rsi_threshold": 30}
        self.strategy = RSIStrategy(self.parameters)
        self.backtester = Backtester(self.strategy, self.data)

    def test_run(self):
        results = self.backtester.run()
        self.assertEqual(len(results), 2)  # دو معامله باید سیگنال دهد
        self.assertEqual(results[0]["action"], "BUY")

    def test_evaluate(self):
        results = self.backtester.run()
        evaluation = self.backtester.evaluate(results)
        self.assertEqual(evaluation["total_profit"], 25)
        self.assertEqual(evaluation["num_trades"], 2)
        self.assertAlmostEqual(evaluation["win_rate"], 1.0)


if __name__ == "__main__":
    unittest.main()
