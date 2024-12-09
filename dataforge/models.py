
from sklearn.datasets import make_classification
import pandas as pd

def generate_classification_data(samples=100, features=5, classes=2):
    """
    Generate synthetic classification data using sklearn.
    """
    X, y = make_classification(n_samples=samples, n_features=features, n_classes=classes)
    df = pd.DataFrame(X, columns=[f"feature_{i}" for i in range(features)])
    df['target'] = y
    return df
        