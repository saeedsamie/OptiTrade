import json
import os
import unittest

from strategies.input_handler import InputHandler


class TestInputHandler(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_input.json"
        sample_input = {
            "strategy_name": "RSI",
            "parameters": {"rsi_threshold": 30},
            "time_periods": ["2023-01-01:2023-01-31"]
        }
        with open(self.test_file, 'w') as file:
            json.dump(sample_input, file)

    def tearDown(self):
        os.remove(self.test_file)

    def test_load_input(self):
        handler = InputHandler(self.test_file)
        data = handler.load_input()
        self.assertEqual(data["strategy_name"], "RSI")
        self.assertEqual(data["parameters"]["rsi_threshold"], 30)

    def test_invalid_input(self):
        invalid_file = "invalid_input.json"
        with open(invalid_file, 'w') as file:
            json.dump({"strategy_name": "Test"}, file)
        handler = InputHandler(invalid_file)
        with self.assertRaises(ValueError):
            handler.load_input()
        os.remove(invalid_file)


if __name__ == "__main__":
    unittest.main()
