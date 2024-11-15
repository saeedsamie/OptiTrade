import unittest

from strategies.rsi_strategy import RSIStrategy


class TestRSIStrategy(unittest.TestCase):
    def setUp(self):
        """
        مقداردهی اولیه تست. پارامترها و داده‌های نمونه برای استراتژی تعریف می‌شوند.
        """
        self.parameters = {"rsi_threshold": 30}
        self.strategy = RSIStrategy(self.parameters)
        self.data = [
            {"rsi": 25, "price": 100},  # سیگنال خرید
            {"rsi": 35, "price": 110},  # بدون سیگنال
            {"rsi": 20, "price": 90}  # سیگنال خرید
        ]

    def test_check_buy_signal(self):
        """
        تست بررسی سیگنال خرید توسط متد `check`.
        """
        cs = {"rsi": 25}
        result = self.strategy.check(cs)
        self.assertTrue(result["reached"])
        self.assertEqual(result["details"]["action"], "BUY")
        self.assertEqual(result["details"]["rsi"], 25)

    def test_check_no_signal(self):
        """
        تست بررسی شرایطی که سیگنالی وجود ندارد.
        """
        cs = {"rsi": 35}
        result = self.strategy.check(cs)
        self.assertFalse(result["reached"])

    def test_run(self):
        """
        تست اجرای کامل استراتژی با متد `run`.
        """
        results = self.strategy.run(self.data)
        self.assertEqual(len(results), 2)  # دو سیگنال خرید باید تولید شود
        self.assertEqual(results[0]["action"], "BUY")
        self.assertEqual(results[1]["action"], "BUY")


if __name__ == "__main__":
    unittest.main()
