from data_analysis_filtering_library import remove_outliers
import pandas as pd
from sklearn.ensemble import IsolationForest

# Create a sample DataFrame
data = {
    'column1': [1, 2, 3, 4, 5, 200],
    'column2': [10, 20, 30, 40, 50, 300],


}
df = pd.DataFrame(data)

# Specify the column containing outliers
column = 'column1'


# Apply the outlier removal function
filtered_df = remove_outliers(df, column)

# Print the original DataFrame
print("Original DataFrame:")
print(df)

# Print the filtered DataFrame without outliers
print("Filtered DataFrame:")
print(filtered_df)