from setuptools import setup, find_packages

setup(
    name='radar_simulator',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib',
    ],
    author='Your Name',
    description='A modular radar simulator project',
    python_requires='>=3.7',
)
