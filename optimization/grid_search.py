import itertools

from .base_optimizer import BaseOptimizer


class GridSearchOptimizer(BaseOptimizer):
    def optimize(self, param_grid):
        """
        پیاده‌سازی جستجوی شبکه‌ای.
        ورودی:
            - param_grid: دیکشنری شامل پارامترها و مقادیر ممکن
        خروجی:
            - بهترین پارامترها و مقدار متریک
        """
        keys, values = zip(*param_grid.items())
        param_combinations = [dict(zip(keys, v)) for v in itertools.product(*values)]

        best_params = None
        best_score = float("-inf")

        for params in param_combinations:
            strategy = self.strategy_class(params)
            results = strategy.run(self.data)
            score = self.evaluate(results)
            if score > best_score:
                best_score = score
                best_params = params

        return best_params, best_score
