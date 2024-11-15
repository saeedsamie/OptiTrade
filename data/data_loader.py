import pandas as pd


class DataLoader:
    def __init__(self, source_type, source_path=None):
        """
        مقداردهی اولیه.
        ورودی‌ها:
            - source_type: نوع منبع داده (csv, database, api)
            - source_path: مسیر فایل یا اطلاعات اتصال دیتابیس/API
        """
        self.source_type = source_type
        self.source_path = source_path

    def load_data(self):
        """
        بارگذاری داده‌ها از منبع مشخص‌شده.
        """
        if self.source_type == "csv":
            return self._load_from_csv()
        elif self.source_type == "database":
            return self._load_from_database()
        elif self.source_type == "api":
            return self._load_from_api()
        else:
            raise ValueError(f"Unsupported source type: {self.source_type}")

    def _load_from_csv(self):
        """
        بارگذاری داده‌ها از فایل CSV.
        """
        if not self.source_path:
            raise ValueError("CSV source path is required.")
        return pd.read_csv(self.source_path)

    def _load_from_database(self):
        """
        بارگذاری داده‌ها از دیتابیس.
        (در این مثال یک قالب ساده برای اتصال دیتابیس در نظر گرفته شده است.)
        """
        import sqlite3
        if not self.source_path:
            raise ValueError("Database source path is required.")
        connection = sqlite3.connect(self.source_path)
        query = "SELECT * FROM market_data"
        return pd.read_sql_query(query, connection)

    def _load_from_api(self):
        """
        بارگذاری داده‌ها از یک API.
        """
        import requests
        if not self.source_path:
            raise ValueError("API endpoint URL is required.")
        response = requests.get(self.source_path)
        if response.status_code != 200:
            raise ConnectionError(f"Failed to fetch data from API. Status code: {response.status_code}")
        return pd.DataFrame(response.json())
