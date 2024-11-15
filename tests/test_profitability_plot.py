import unittest

from visualization.profitability_plot import ProfitabilityPlot


class TestProfitabilityPlot(unittest.TestCase):
    def test_plot_param_vs_profit(self):
        param_values = [20, 25, 30, 35]
        profits = [50, 60, 40, 70]
        try:
            ProfitabilityPlot.plot_param_vs_profit(
                param_values=param_values,
                profits=profits,
                param_name="RSI Threshold",
                title="Test Plot"
            )
        except Exception as e:
            self.fail(f"plot_param_vs_profit raised an exception: {e}")

    def test_plot_results_over_time(self):
        results = [
            {"timestamp": "2023-01-01", "profit": 10},
            {"timestamp": "2023-01-02", "profit": -5},
            {"timestamp": "2023-01-03", "profit": 15},
        ]
        try:
            ProfitabilityPlot.plot_results_over_time(
                results=results,
                title="Test Time Plot"
            )
        except Exception as e:
            self.fail(f"plot_results_over_time raised an exception: {e}")


if __name__ == "__main__":
    unittest.main()
