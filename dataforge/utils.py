
import pandas as pd

def save_to_csv(data, file_path):
    """
    Save DataFrame to CSV file.
    """
    data.to_csv(file_path, index=False)

def load_from_csv(file_path):
    """
    Load DataFrame from CSV file.
    """
    return pd.read_csv(file_path)
        