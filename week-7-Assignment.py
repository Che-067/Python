'''
Task 1: Load and Explore the Dataset
Choose a dataset in CSV format (for example, you can use datasets like the Iris dataset, a sales dataset, or any dataset of your choice).
Load the dataset using pandas.
Display the first few rows of the dataset using .head() to inspect the data.
Explore the structure of the dataset by checking the data types and any missing values.
Clean the dataset by either filling or dropping any missing values.

Task 2: Basic Data Analysis
Compute the basic statistics of the numerical columns (e.g., mean, median, standard deviation) using .describe().
Perform groupings on a categorical column (for example, species, region, or department) and compute the mean of a numerical column for each group.
Identify any patterns or interesting findings from your analysis.
'''

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\DELL\Downloads\python programs\Gold_Analysts.csv')

framing = pd.DataFrame(df)

# handling commas from excel data
df['Shorts'] = df['Longs'].astype(str).str.replace(',','').astype(int)
df['Total'] = df['Longs'].astype(str).str.replace(',','').astype(int)
df['Net Size'] = df['Longs'].astype(str).str.replace(',','').astype(int)

df['Longs'] = df['Longs'].astype(str).str.replace(',','').astype(int)

# print any base on > 320000
 print(df[df['Longs'] > 320000])
# display 1st 5 rows
 print(df.head())

# checking the data types and any missing values.

df.dtypes

# sum of all the missing values
null_per_col = df.isnull().sum()

print(null_per_col)

# drop rows with any missing values
df_cleansed = df.dropna()

# drop rows where all values are missing

df_cleaned = df.dropna(how='all')

# drop rows with missing values in specific columns
df_cleansed = df.dropna(subset=['column_name'])

# drop columns with too many missing values (e.g ..,> 50%)
threshold = len(df) * 0.5
 df_cleaned = df.dropna(axis=1, thresh=threshold)
 
 # check percentage of missing values
 df_cleaned = df.isnull().mean() * 100





