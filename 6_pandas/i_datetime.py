# Datetime
# Pandas has comprehensive support for manipulating date and time data, which is crucial for time series analysis
import pandas as pd

# Creating a datetime object
date = pd.to_datetime('2024-01-01')
print(date)
# Creating a datetime series
dates = pd.to_datetime(['2024-01-01', '2024-02-01', '2024-03-01'])
print(dates)
# Extracting components from datetime
print(date.year)  # Output: 2024
print(date.month)  # Output: 1
print(date.day)  # Output: 1