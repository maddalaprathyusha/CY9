#DATA FILTERING
import pandas as pd
from sklearn.ensemble import IsolationForest

def remove_outliers(df, column):
    outlier_detector = IsolationForest(contamination=0.1)
    outliers = outlier_detector.fit_predict(df[[column]])
    return df[outliers != -1]


import pandas as pd
def remove_null_values(data):
    df = pd.DataFrame(data, columns=["Data"])
    df = df.dropna()
    return df["Data"].tolist()

def remove_invalid_data(data, condition):
    return [item for item in data if condition(item)]


#DATA ANALYSIS

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



