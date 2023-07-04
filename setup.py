from setuptools import setup, find_packages

setup(
    name='data_analysis_filtering_library',
    version='1.0',
    packages=find_packages('DataAnalysisFilteringLib'),
    author='prathyusha',
    description='Data Analysis and Filtering Library',
    install_requires=[
        'pandas',
        'numpy',
        'scipy',
        'scikit-learn',
        # Add other dependencies here
    ]
)
