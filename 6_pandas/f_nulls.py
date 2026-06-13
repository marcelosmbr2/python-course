# Nulls
# Null (or missing) values are common in real-world datasets and need to be handled appropriately to avoid errors or biases in analysis
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, None, 35, 40],
    'City': ['New York', 'Los Angeles', None, 'Houston']
}

df = pd.DataFrame(data)
# Check for null values
print(df.isnull())
# Fill null values in 'Age' with the mean age
df['Age'] = df['Age'].fillna(df['Age'].mean())
# Fill null values in 'City' with 'Unknown'
df['City'] = df['City'].fillna('Unknown')
print(df)