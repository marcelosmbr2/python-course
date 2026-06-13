# Files
# Pandas provides robust functionalities for reading and writing data in various file formats
import pandas as pd

# Reading CSV files
df_csv = pd.read_csv('data.csv')
# Reading Excel files
df_excel = pd.read_excel('data.xlsx')
# Reading JSON files
df_json = pd.read_json('data.json')
# Writing to CSV files
df_csv.to_csv('output.csv', index=False)
# Writing to Excel files
df_excel.to_excel('output.xlsx', index=False)
# Writing to JSON files
df_json.to_json('output.json', orient='records', lines=True)