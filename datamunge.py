# This example takes all the data collected in the *_example.py files and puts them together with visualization
# libraries to demonstrate how to consume and visualize data in a dynamic workflow.

# Imagine... we want to run an analysis of how certain financial indicators vary with unemployment. We can get
# unemployment rates from the St. Louis Fed's (FRED) API. Some of the indicators we want are from our own in-house
# database. Some we pulled from FTP in CSV and others are in regular old Excel.

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

import db_examples, api_examples


# get the data we've been using from the example files
some_close_prices = pd.read_csv("DataStores/close_data.csv",
                                index_col=0, parse_dates=True)

xl_io = pd.ExcelFile("DataStores/all_data.xlsx")
tickers = xl_io.sheet_names
lows = pd.DataFrame(columns=[t + "_low" for t in tickers])

monthly_stock_data = db_examples.read_db_and_combine_and_sample_monthly(some_close_prices, lows)

# merge data together
df = api_examples.download_json_data_into_dataframe_and_process()
fred_list = api_examples.pull_from_fred_api()

fred_df = pd.concat([df] + fred_list, axis=1).loc[monthly_stock_data.index]
all_data = pd.concat([fred_df, monthly_stock_data], axis=1).astype(float)

print("DATA MERGED")

print(all_data.head())
print(all_data.tail())
print("DROPNA")
all_data.dropna(inplace=True)
print(all_data.describe())

# compute month-over-month returns
rets = np.log(all_data.iloc[1:,:]/all_data.iloc[:-1,:].values).dropna()
correlation = rets.corr()
print(correlation)

fig, ax = plt.subplots()
fig.canvas.set_window_title('Correlation')
fig.set_size_inches(10, 10)
sns.heatmap(correlation, xticklabels=correlation.columns,
            yticklabels=correlation.columns, ax=ax, cmap='jet')
plt.show()

corr_with_unemp = correlation["UNEMPLOYMENT"]
min_level = 0.1
big_corr_names = corr_with_unemp[np.abs(corr_with_unemp) >= min_level].index.values

big_corr = correlation[big_corr_names].loc[big_corr_names]

fig, ax = plt.subplots()
fig.canvas.set_window_title('Unemployment')
fig.set_size_inches(15, 2)
sns.heatmap(pd.DataFrame(big_corr["UNEMPLOYMENT"][1:].sort_values(ascending=False)).T,
            ax=ax, cmap='jet', annot=True, yticklabels=False, cbar=False)
plt.show()

p = sns.pairplot(rets[big_corr_names[:5]], kind='reg', diag_kind='kde')
p.fig.set_size_inches(10, 10)
plt.show()

print("DONE")
