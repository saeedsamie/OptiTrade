# تنظیمات عمومی پروژه
PROJECT_NAME = "OptiTrade"
VERSION = "0.1.0"

# تنظیمات مربوط به داده‌ها
DATA_SOURCE = "csv"  # csv, database, or api
CSV_FILE_PATH = "market_data.csv"
DATABASE_PATH = "market_data.db"
API_ENDPOINT = "http://example.com/api/data"

# تنظیمات پیش‌فرض استراتژی‌ها
DEFAULT_STRATEGY_PARAMS = {
    "rsi_threshold": 30,
}

# تنظیمات لاگ‌گیری
LOG_FILE = "outputs/logs/optitrade.log"

# تنظیمات نمودارها
CHART_SETTINGS = {
    "figure_size": (10, 6),
    "dpi": 100,
}
