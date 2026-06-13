# Filtering
# allows you to select subsets of data from a DataFrame or Series based on one or more conditions
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, 45],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}

df = pd.DataFrame(data)
# Filter rows where Age is greater than 30
filtered_df = df[df['Age'] > 30]
print(filtered_df)