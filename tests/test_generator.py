
import unittest
from dataforge.generator import generate_synthetic_data, add_noise
import numpy as np

class TestGenerator(unittest.TestCase):
    def test_generate_synthetic_data(self):
        data = generate_synthetic_data(10, 3)
        self.assertEqual(data.shape, (10, 3))

    def test_add_noise(self):
        data = np.random.rand(5, 5)
        noisy_data = add_noise(data, 0.1)
        self.assertEqual(data.shape, noisy_data.shape)

if __name__ == "__main__":
    unittest.main()
        