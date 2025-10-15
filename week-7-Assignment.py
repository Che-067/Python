'''
Task 1: Load and Explore the Dataset
Choose a dataset in CSV format (for example, you can use datasets like the Iris dataset, a sales dataset, or any dataset of your choice).
Load the dataset using pandas.
Display the first few rows of the dataset using .head() to inspect the data.
Explore the structure of the dataset by checking the data types and any missing values.
Clean the dataset by either filling or dropping any missing values.

Task 2: Basic Data Analysis
Compute the basic statistics of the numerical columns (e.g., mean, median, standard deviation) using .describe().
Perform groupings on a categorical column (for example, species, region, or department) and
compute the mean of a numerical column for each group.
Identify any patterns or interesting findings from your analysis.
'''

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv(r'C:\Users\DELL\Downloads\python programs\Gold_Analysts.csv', encoding='utf-8')
# df = df.loc[:, ~df.Shorts.duplicate()]

# handling commas from excel data
df['Longs'] = df['Longs'].astype(str).str.replace(',','').astype(int)
df['Shorts'] = df['Shorts'].astype(str).str.replace(',','').astype(int)
df['Total'] = df['Total'].astype(str).str.replace(',','').astype(int)
df['Net size'] = df['Net size'].astype(str).str.replace(',','').astype(int)


# print any base on > 320000
# print(df[df['Longs'] > 320000])

# display 1st 5 rows
# print(df.head())
# print(df)
# checking the data types and any missing values
print(df)

print(df.dtypes)

null_per_col = df.isnull().sum()
print(null_per_col)

# Drop rows with ANY missing values
df_cleaned = df.dropna()
# print(df_cleaned)

# Drop rows where ALL values are missing
df_cleaned = df.dropna(how='all')

# Drop rows with missing values in specific columns
df_cleaned = df.dropna(subset=['Longs'])
# print(df_cleaned)
# Drop columns with too many missing values (e.g., >50%)
threshold = len(df) * 0.5
df_cleaned = df.dropna(axis=1, thresh=threshold)
# Fill with mean
df['Longs'] = df['Longs'].fillna(df['Longs'].mean())
# print(df['Longs'])

'''
# Fill with median (less sensitive to outliers)
df['COLUMN_NAME'] = df['COLUMN_NAME'].fillna(df['COLUMN_NAME']['OTHER_column'].median())

# Fill with mode
df['COLUMN_NAME'] = df['COLUMN_NAME'].fillna(df['column'].mode()[0])

# Fill with forward fill (carry last valid observation forward)
df['COLUMN_NAME'] = df['COLUMN_NAME'].fillna(method='ffill')

# Fill with backward fill
df['COLUMN_NAME'] = df['COLUMN_NAME'].fillna(method='bfill')

# Fill with a specific value
df['COLUMN_NAME'] = df['COLUMN_NAME'].fillna(0)


# Interpolation for time series
df['COLUMN_NAME'] = df['COLUMN_NAME'].interpolate()

# Using KNN Imputation
from sklearn.impute import KNNImputer
imputer = KNNImputer(n_neighbors=5)
df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)

'''
df_analyse = df.describe()
print(df_analyse)

df_sorted = df.sort_index()
print(df_sorted)
df_sort = df.groupby(['Dates'])

# df_group = df_sort.groupby('Dates')[['Longs','Total']].mean()
# print(df_group)

df_reversed = df[: : -1].reset_index(drop=True)

df_reversed.plot(kind='line', x='Dates', y=['Longs','Shorts','Total','Net size'], linewidth=2)
plt.title('ANALYSIS OF GOLD MARKETS')
plt.legend(fontsize=7)
plt.grid(True,alpha=0.3)

plt.xticks(rotation=45,ha='right')
plt.tight_layout()
plt.show()
print()
# Print detailed analysis
print("🔍 DETAILED MARKET ANALYSIS:\n")
print("="*50)
print(f"1. BULLISH BIAS: Long positions dominate by {289054/65890:.1f}x")
print(f"2. VOLATILITY: Longs are {36782/14196:.1f}x more volatile than Shorts")
print(f"3. RANGE: Longs vary by {356500-234087:,} vs Shorts by {99938-36505:,}")
print(f"4. CONSISTENCY: 50% of Longs are between {258829:,} and {322459:,}")
print(f"5. NET EXPOSURE: Average net position: {223164:,}")

print("\n📈 TRADING IMPLICATIONS:")
print("- Market has strong long-term bullish gold sentiment")
print("- Short positions are more speculative (higher relative volatility)")
print("- Large net long position suggests institutional confidence in gold")
print("- Watch for Shorts exceeding 70,000 as potential reversal signals")
