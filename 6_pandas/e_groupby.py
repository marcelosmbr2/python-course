# Group by
# Is a powerful tool for grouping data based on one or more keys and applying various operations to the grouped data
# It allows you to split your data into groups, apply a function to each group independently, and then combine the results back into a single DataFrame or Series
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, 45],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
    'Salary': [70000, 80000, 90000, 100000, 110000]
}

df = pd.DataFrame(data)
# Group by 'City' and calculate the average salary for each city
grouped = df.groupby('City')['Salary'].mean()
print(grouped)