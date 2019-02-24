import sqlite3
import pandas as pd
import numpy as np


def read_from_db_connection():
    conn = sqlite3.connect('DataStores/test_db.db')

    db_res = pd.read_sql("SELECT * FROM close_data",
                         conn, index_col='date', parse_dates=True)
    conn.close()

    print(db_res.head())
    print(db_res.describe())


def read_db_and_clean():
    conn = sqlite3.connect('DataStores/test_db.db')

    db_res = pd.read_sql("SELECT * FROM close_data",
                         conn, index_col='date', parse_dates=True)
    conn.close()

    print(db_res.head())
    print(db_res.describe())

    db_res.replace(to_replace=np.NaN, value=db_res.mean(), inplace=True)

    print(db_res.head())
    print(db_res.describe())


def read_db_and_combine_and_sample_monthly(some_close_prices, lows):
    from datetime import timedelta as td

    with sqlite3.connect('DataStores/test_db.db') as conn:
        db_res = pd.read_sql("SELECT * FROM close_data",
                             conn, index_col='date', parse_dates=True)
        db_res.replace(to_replace=np.NaN, value=db_res.mean(), inplace=True)

    all_stock_data = pd.concat([some_close_prices, lows, db_res], axis=1)

    # Resample stock data to match monthly frequency of economic indicators from FRED.
    monthly_stock_data = all_stock_data.resample('M').mean()

    monthly_stock_data.index = [d + td(days=1) for d in monthly_stock_data.index]

    return monthly_stock_data


if __name__ == "__main__":
    # read_from_db_connection()
    # read_db_and_clean()

    pass

