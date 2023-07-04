import pandas as pd
from sklearn.ensemble import IsolationForest

def remove_outliers(df, columns):
    outlier_detector = IsolationForest(contamination=0.1)
    outliers = outlier_detector.fit_predict(df[[columns]])
    return df[outliers != -1]

def remove_null_values(df):
    return df.dropna()

def remove_invalid_data(df, condition):
    return df[condition]
