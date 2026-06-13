# Transforming
# Transforming data in pandas involves modifying, reshaping, or manipulating the data to make it more suitable for analysis
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)
# Add a new column 'Age in 5 years' by transforming the 'Age' column
df['Age in 5 years'] = df['Age'] + 5
print(df)