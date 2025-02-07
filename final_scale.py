import pandas as pd

def scale_performance_scores(df, column_name):
    # Find the minimum and maximum values of the specified column
    min_value = df[column_name].min()
    max_value = df[column_name].max()
    
    # Apply Min-Max scaling and replace the original values
    df[column_name] = (df[column_name] - min_value) / (max_value - min_value)
    
    return df

# Load the data from CSV
df = pd.read_csv('final.csv')  # Replace 'your_data.csv' with your file path

# Scale the 'Performance Score' column and replace original values
df = scale_performance_scores(df, 'Performance Score')

# Save the updated DataFrame to a new CSV file
df.to_csv('very_final.csv', index=False)

print(df)
