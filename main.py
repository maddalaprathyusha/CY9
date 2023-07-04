#DATA FILTERING


#1.REMOVE NULL VALUES
from data_analysis_filtering_library import remove_null_values

# Create some sample data
data = [1, 2, None, 4, 5]

# Apply the filter to remove null values
filtered_data = remove_null_values(data)

# Print the filtered data
print("Original Data:", data)
print("Filtered Data:", filtered_data)



#1.1 using excel file 

import pandas as pd

# Define a function to remove null values
def remove_null_values(file_path):
    # Read the Excel file into a DataFrame
    df = pd.read_excel(file_path)
    
    # Remove rows with null values
    df = df.dropna()
    
    return df

# Provide the file path of your Excel file
file_path = 'C:\\Users\\PRATYU\\Downloads\\house_test.xlsx'

# Apply the filter to remove null values
filtered_data = remove_null_values(file_path)

# Print the updated data
print("Original Data:")
print(pd.read_excel(file_path))
print("\nFiltered Data:")
print(filtered_data)



#2.REMOVE OUTLIERS

from data_analysis_filtering_library import remove_outliers
import pandas as pd
from sklearn.ensemble import IsolationForest

# Create a sample DataFrame
data = {
    'column1': [1, 2, 3, 4, 5, 200],
    'column2': [10, 20, 30, 40, 50, 300]


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


#3.REMOVE INVALID DATA

from data_analysis_filtering_library import remove_invalid_data

# Define a list of numbers
data = [1, 2, 3, 4, 5]

# Define a condition to filter the list
condition = lambda x: x % 2 == 0  # Filter even numbers

# Apply the filter to remove invalid data
filtered_data = remove_invalid_data(data, condition)

# Print the filtered data
print("Original Data:", data)
print("Filtered Data:", filtered_data)



#DATA ANALYSIS

from data_analysis_filtering_library import perform_feature_selection

from data_analysis_filtering_library import calculate_correlation
import pandas as pd

data = pd.DataFrame({
    'Feature1': [1, 2, 3, 4, 5],
    'Feature2': [2, 4, 6, 8, 10],
    'Feature3': [3, 6, 9, 12, 15],
    'Target': [5, 10, 15, 20, 25]
})

# 1.PERFORM FEATURE SELECTION
selected_features = perform_feature_selection(data[['Feature1', 'Feature2', 'Feature3']], data['Target'], n_features=2)

# Create a new DataFrame with selected features
selected_data = pd.DataFrame(selected_features, columns=['SelectedFeature1', 'SelectedFeature2'])

#2.CALCULATE CORRELATION MATRIX
correlation_matrix = calculate_correlation(selected_data)

# Print the correlation matrix
print(correlation_matrix)










