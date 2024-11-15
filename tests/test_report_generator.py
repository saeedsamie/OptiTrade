import json
import os
import unittest

from outputs.report_generator import ReportGenerator


class TestReportGenerator(unittest.TestCase):
    def setUp(self):
        self.best_params = {"rsi_threshold": 30}
        self.evaluation = {"total_profit": 25, "num_trades": 2, "win_rate": 1.0}
        self.filename = "test_report.json"

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_generate_report(self):
        ReportGenerator.generate_report(self.best_params, self.evaluation, self.filename)
        self.assertTrue(os.path.exists(self.filename))

        with open(self.filename, "r") as file:
            report = json.load(file)
            self.assertEqual(report["best_parameters"], self.best_params)
            self.assertEqual(report["evaluation"], self.evaluation)

    def test_print_report(self):
        try:
            ReportGenerator.print_report(self.best_params, self.evaluation)
        except Exception as e:
            self.fail(f"print_report raised an exception: {e}")


if __name__ == "__main__":
    unittest.main()
