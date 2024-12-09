
import unittest
from dataforge.utils import save_to_csv, load_from_csv
import pandas as pd
import os

class TestUtils(unittest.TestCase):
    def test_save_and_load_csv(self):
        df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
        file_path = 'test.csv'
        save_to_csv(df, file_path)
        loaded_df = load_from_csv(file_path)
        self.assertTrue(df.equals(loaded_df))
        os.remove(file_path)

if __name__ == "__main__":
    unittest.main()
        