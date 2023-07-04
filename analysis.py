import pandas as pd
from sklearn.feature_selection import RFE
from sklearn.linear_model import LinearRegression

def perform_feature_selection(X, y, n_features):
    model = LinearRegression()
    rfe = RFE(model, n_features_to_select=n_features)
    rfe = rfe.fit(X, y)
    return rfe.transform(X)

def calculate_correlation(df):
    return df.corr()
