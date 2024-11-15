import json


class InputHandler:
    def __init__(self, input_file):
        self.input_file = input_file

    def load_input(self):
        with open(self.input_file, 'r') as file:
            data = json.load(file)
        self.validate_input(data)
        return data

    def validate_input(self, data):
        if "strategy_name" not in data or "parameters" not in data:
            raise ValueError("Invalid input: 'strategy_name' and 'parameters' are required.")
        if "time_periods" not in data or not isinstance(data["time_periods"], list):
            raise ValueError("Invalid input: 'time_periods' must be a list.")
