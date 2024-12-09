
# DataForge

DataForge is a lightweight Python library for generating and handling synthetic datasets. Ideal for data science, machine learning, and experimentation.

## Features
- Generate random synthetic datasets.
- Add noise to existing data.
- Create classification datasets.
- Save and load data with ease.

## Installation
Run the following command to install:
```
pip install .
```

## Usage
### Generate Synthetic Data
```python
from dataforge.generator import generate_synthetic_data

data = generate_synthetic_data(num_samples=100, num_features=5)
print(data)
```

### Add Noise to Data
```python
from dataforge.generator import add_noise
import numpy as np

data = np.random.rand(5, 5)
noisy_data = add_noise(data, noise_level=0.1)
```

## Testing
Run tests using:
```
python -m unittest discover tests
```
    