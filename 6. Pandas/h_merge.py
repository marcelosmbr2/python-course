# Merge
# Is the operation of combining two or more DataFrames based on common columns or indices
import pandas as pd

# Create two DataFrames
df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie']
})

df2 = pd.DataFrame({
    'ID': [2, 3, 4],
    'Age': [30, 35, 40]
})

# Merge the DataFrames on the 'ID' column
merged_df = pd.merge(df1, df2, on='ID', how='inner')
print(merged_df)