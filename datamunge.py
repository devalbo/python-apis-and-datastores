import pandas as pd
import numpy as np
import sqlite3
from datetime import timedelta as td
from matplotlib import pyplot as plt
import seaborn as sns

import api_examples

# Imagine... we want to run an analysis of how certain financial indicators vary with unemployment. We can get
# unemployment rates from the St. Louis Fed's (FRED) API. Some of the indicators we want are from our own in-house
# database. Some we pulled from FTP in CSV and others are in regular old Excel.

some_close_prices = pd.read_csv("DataStores/close_data.csv",
                                index_col=0, parse_dates=True)

xl_io = pd.ExcelFile("DataStores/all_data.xlsx")
tickers = xl_io.sheet_names
lows = pd.DataFrame(columns = [t + "_low" for t in tickers])

with sqlite3.connect('DataStores/test_db.db') as conn:
    db_res = pd.read_sql("SELECT * FROM close_data",
                         conn, index_col='date', parse_dates=True)
    db_res.replace(to_replace=np.NaN, value=db_res.mean(), inplace=True)


all_stock_data = pd.concat([some_close_prices, lows, db_res], axis=1)
print(all_stock_data.describe())

# Resample stock data to match monthly frequency of economic indicators from FRED.
monthly_stock_data = all_stock_data.resample('M').mean()
print(monthly_stock_data.head())

monthly_stock_data.index = [d + td(days=1) for d in monthly_stock_data.index]
print(monthly_stock_data.head())

# merge data together
df = api_examples.download_json_data_into_dataframe_and_process()
fred_list = api_examples.pull_from_fred_api()

fred_df = pd.concat([df] + fred_list, axis=1).loc[monthly_stock_data.index]
all_data = pd.concat([fred_df, monthly_stock_data], axis=1).astype(float)

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
fig.set_size_inches(10,10)
sns.heatmap(correlation, xticklabels=correlation.columns,
            yticklabels=correlation.columns, ax = ax, cmap = 'jet')
plt.show()

corr_with_unemp = correlation["UNEMPLOYMENT"]
min_level = 0.1
big_corr_names = corr_with_unemp[np.abs(corr_with_unemp) >= min_level].index.values

big_corr = correlation[big_corr_names].loc[big_corr_names]

fig, ax = plt.subplots()
fig.set_size_inches(15,1)
sns.heatmap(pd.DataFrame(big_corr["UNEMPLOYMENT"][1:].sort_values(ascending = False)).T,
            ax = ax, cmap = 'jet', annot = True,yticklabels=False, cbar=False)
plt.show()

p = sns.pairplot(rets[big_corr_names[:5]],kind = 'reg', diag_kind = 'kde')
p.fig.set_size_inches(10,10)
plt.show()

print("DONE")