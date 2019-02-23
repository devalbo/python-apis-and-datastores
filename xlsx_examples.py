
def read_workbook_with_pandas():
    import pandas as pd

    xl_io = pd.ExcelFile("DataStores/all_data.xlsx")
    print(xl_io.sheet_names)


def read_worksheets_with_pandas():
    import pandas as pd

    xl_io = pd.ExcelFile("DataStores/all_data.xlsx")
    tickers = xl_io.sheet_names

    lows = pd.DataFrame(columns=[t + "_low" for t in tickers])
    for t in tickers:
        lows[t + "_low"] = pd.read_excel(xl_io, sheet_name=t, index_col=0, parse_dates=True)["low"]

    print(lows.head())
    print(lows.describe())


def plot_with_matplotlib():
    import pandas as pd
    from matplotlib import pyplot as plt

    xl_io = pd.ExcelFile("DataStores/all_data.xlsx")
    tickers = xl_io.sheet_names

    lows = pd.DataFrame(columns=[t + "_low" for t in tickers])
    for t in tickers:
        lows[t + "_low"] = pd.read_excel(xl_io, sheet_name=t, index_col=0, parse_dates=True)["low"]

    ((lows-lows.mean())/lows.std()).plot(figsize=(15,7))
    plt.show()


def read_xlsx_with_headers():
    import pandas as pd

    h = pd.read_excel("DataStores/all_data_header.xlsx",
                      sheet_name='AAPL', index_col=0, parse_dates=True).head()
    print(h)

    print("""
    -------------------------------------------
    """)

    skip3_h = pd.read_excel("DataStores/all_data_header.xlsx",
                            sheet_name = 'AAPL',
                            index_col=0, parse_dates=True, skiprows=3).head()
    print(skip3_h)


if __name__ == "__main__":
    # read_workbook_with_pandas()
    # read_worksheets_with_pandas()
    # plot_with_matplotlib()
    # read_xlsx_with_headers()

    pass
