
from setuptools import setup, find_packages

setup(
    name='dataforge',
    version='0.1',
    description='Synthetic Data Generator Library',
    author='Vishnu Devarajan',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'scikit-learn',
    ],
)
    
