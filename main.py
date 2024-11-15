from config.settings import (
    DATA_SOURCE, CSV_FILE_PATH, DATABASE_PATH, API_ENDPOINT,
    DEFAULT_STRATEGY_PARAMS
)
from data.data_loader import DataLoader
from optimization.grid_search import GridSearchOptimizer
from outputs.report_generator import ReportGenerator
from strategies.rsi_strategy import RSIStrategy
from visualization.profitability_plot import ProfitabilityPlot


def main():
    print("Welcome to OptiTrade - Strategy Optimization Tool")

    # مرحله 1: بارگذاری داده‌ها
    print("Loading data...")
    if DATA_SOURCE == "csv":
        loader = DataLoader(source_type="csv", source_path=CSV_FILE_PATH)
    elif DATA_SOURCE == "database":
        loader = DataLoader(source_type="database", source_path=DATABASE_PATH)
    elif DATA_SOURCE == "api":
        loader = DataLoader(source_type="api", source_path=API_ENDPOINT)
    else:
        raise ValueError("Unsupported DATA_SOURCE in settings.")

    data = loader.load_data()
    print(f"Data loaded successfully. {len(data)} records found.")

    # مرحله 2: تعریف استراتژی
    print("Initializing strategy...")
    strategy = RSIStrategy(DEFAULT_STRATEGY_PARAMS)

    # مرحله 3: بهینه‌سازی استراتژی
    print("Optimizing strategy using Grid Search...")
    param_grid = {
        "rsi_threshold": [20, 25, 30, 35]
    }
    optimizer = GridSearchOptimizer(RSIStrategy, data)
    best_params, best_score = optimizer.optimize(param_grid)
    print(f"Optimization completed. Best Parameters: {best_params}, Best Score: {best_score}")

    # مرحله 4: اجرای استراتژی با بهترین پارامترها
    print("Running strategy with best parameters...")
    best_strategy = RSIStrategy(best_params)
    results = best_strategy.run(data)

    # مرحله 5: ارزیابی نهایی
    print("Evaluating best strategy...")
    evaluation = optimizer.evaluate(results)

    # مرحله 6: تجسم نتایج
    print("Visualizing results...")
    ProfitabilityPlot.plot_results_over_time(
        results=results,
        title="Best Strategy Results Over Time"
    )

    # مرحله 7: تولید گزارش
    print("Generating report...")
    ReportGenerator.print_report(best_params, evaluation)
    ReportGenerator.generate_report(best_params, evaluation, filename="final_report.json")

    print("Process completed. Report saved to 'final_report.json'.")


if __name__ == "__main__":
    main()
