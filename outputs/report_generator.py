import json


class ReportGenerator:
    @staticmethod
    def generate_report(best_params, evaluation, filename="report.json"):
        """
        تولید گزارش نهایی و ذخیره به‌صورت فایل JSON.
        ورودی‌ها:
            - best_params: بهترین پارامترهای استراتژی
            - evaluation: ارزیابی عملکرد بهترین استراتژی
            - filename: نام فایل خروجی
        """
        report = {
            "best_parameters": best_params,
            "evaluation": evaluation
        }

        # ذخیره گزارش به فایل JSON
        with open(filename, "w") as file:
            json.dump(report, file, indent=4)

        print(f"Report saved to {filename}")

    @staticmethod
    def print_report(best_params, evaluation):
        """
        نمایش گزارش به‌صورت خوانا در کنسول.
        """
        print("\n--- Optimization Report ---")
        print("Best Parameters:")
        for key, value in best_params.items():
            print(f"  {key}: {value}")

        print("\nEvaluation Metrics:")
        for key, value in evaluation.items():
            print(f"  {key}: {value}")
