class BaseOptimizer:
    def __init__(self, strategy_class, data, evaluation_metric="total_profit"):
        """
        مقداردهی اولیه بهینه‌ساز.
        ورودی‌ها:
            - strategy_class: کلاس استراتژی برای بهینه‌سازی (مثلاً RSIStrategy)
            - data: داده‌های تاریخی
            - evaluation_metric: متریک ارزیابی
        """
        self.strategy_class = strategy_class
        self.data = data
        self.evaluation_metric = evaluation_metric

    def optimize(self, param_grid):
        """
        متد پایه برای بهینه‌سازی. باید در کلاس‌های فرزند بازنویسی شود.
        """
        raise NotImplementedError("Subclasses must implement the 'optimize' method.")

    def evaluate(self, results):
        """
        ارزیابی نتایج استراتژی بر اساس متریک.
        """
        if self.evaluation_metric == "total_profit":
            return sum([trade.get("profit", 0) for trade in results])
        return 0
