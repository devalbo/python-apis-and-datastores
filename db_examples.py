
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


if __name__ == "__main__":
    # read_from_db_connection()
    # read_db_and_clean()

    pass

