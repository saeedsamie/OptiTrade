class Backtester:
    def __init__(self, strategy, data):
        """
        مقداردهی اولیه سیستم بک‌تست.
        ورودی‌ها:
            - strategy: نمونه‌ای از استراتژی (BaseStrategy یا فرزند آن)
            - data: داده‌های تاریخی (لیستی از کندل‌استیک‌ها یا داده‌های مشابه)
        """
        self.strategy = strategy
        self.data = data

    def run(self):
        """
        اجرای استراتژی بر روی داده‌ها.
        """
        results = self.strategy.run(self.data)
        return results

    def evaluate(self, results):
        """
        ارزیابی نتایج بک‌تست.
        این متد می‌تواند شامل محاسبه:
            - سود و زیان کل
            - درصد موفقیت معاملات
            - تعداد معاملات انجام‌شده
        """
        profit = sum([trade["profit"] for trade in results if "profit" in trade])
        num_trades = len(results)
        win_rate = len([trade for trade in results if trade.get("profit", 0) > 0]) / num_trades if num_trades > 0 else 0

        return {
            "total_profit": profit,
            "num_trades": num_trades,
            "win_rate": win_rate
        }
