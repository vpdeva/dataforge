
import pandas as pd
import numpy as np

def generate_synthetic_data(num_samples=100, num_features=5):
    """
    Generates a synthetic dataset with random values.
    """
    data = np.random.rand(num_samples, num_features)
    df = pd.DataFrame(data, columns=[f"feature_{i}" for i in range(num_features)])
    return df

def add_noise(data, noise_level=0.1):
    """
    Adds Gaussian noise to the dataset.
    """
    noise = np.random.normal(0, noise_level, data.shape)
    return data + noise
        