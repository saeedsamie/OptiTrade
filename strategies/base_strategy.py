class BaseStrategy:
    def __init__(self, parameters):
        self.parameters = parameters

    def check(self, cs):
        raise NotImplementedError("Subclasses must implement the 'check' method.")

    def run(self, data):
        results = []
        for cs in data:
            check_result = self.check(cs)
            if check_result["reached"]:
                results.append(check_result["details"])
        return results
