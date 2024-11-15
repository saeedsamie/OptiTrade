from .base_strategy import BaseStrategy


def result_format(reached, details):
    return {"reached": reached, "details": details}


class RSIStrategy(BaseStrategy):
    def check(self, cs):
        rsi = cs.get("rsi", 0)
        threshold = self.parameters.get("rsi_threshold", 30)
        if rsi < threshold:
            return result_format(True, {"action": "BUY", "rsi": rsi})
        return result_format(False, {})
