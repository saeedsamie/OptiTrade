import unittest
from data.data_loader import DataLoader
import pandas as pd


class TestDataLoader(unittest.TestCase):
    def setUp(self):
        # ساخت یک فایل CSV نمونه برای تست
        self.csv_file = "test_data.csv"
        sample_data = pd.DataFrame({
            "timestamp": ["2023-01-01", "2023-01-02", "2023-01-03"],
            "price": [100, 105, 110],
            "volume": [10, 12, 14]
        })
        sample_data.to_csv(self.csv_file, index=False)

    def tearDown(self):
        # حذف فایل CSV پس از تست
        import os
        if os.path.exists(self.csv_file):
            os.remove(self.csv_file)

    def test_load_from_csv(self):
        loader = DataLoader(source_type="csv", source_path=self.csv_file)
        data = loader.load_data()
        self.assertEqual(len(data), 3)
        self.assertIn("price", data.columns)

    def test_invalid_source(self):
        loader = DataLoader(source_type="unknown")
        with self.assertRaises(ValueError):
            loader.load_data()


if __name__ == "__main__":
    unittest.main()
