import matplotlib.pyplot as plt


class ProfitabilityPlot:
    @staticmethod
    def plot_param_vs_profit(param_values, profits, param_name, title="Profitability Analysis"):
        """
        رسم نمودار سوددهی بر اساس مقادیر پارامتر.
        ورودی‌ها:
            - param_values: لیست مقادیر پارامتر
            - profits: لیست سودهای متناظر
            - param_name: نام پارامتر
            - title: عنوان نمودار
        """
        plt.figure(figsize=(10, 6))
        plt.plot(param_values, profits, marker='o')
        plt.title(title)
        plt.xlabel(param_name)
        plt.ylabel("Total Profit")
        plt.grid(True)
        plt.show()

    @staticmethod
    def plot_results_over_time(results, title="Strategy Results Over Time"):
        """
        رسم نمودار نتایج استراتژی در طول زمان.
        ورودی‌ها:
            - results: لیست نتایج استراتژی (هر نتیجه شامل profit و timestamp)
            - title: عنوان نمودار
        """
        timestamps = [result.get("timestamp") for result in results]
        profits = [result.get("profit", 0) for result in results]

        plt.figure(figsize=(10, 6))
        plt.plot(timestamps, profits, marker='o')
        plt.title(title)
        plt.xlabel("Time")
        plt.ylabel("Profit")
        plt.grid(True)
        plt.show()
