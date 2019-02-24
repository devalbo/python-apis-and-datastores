
def read_lines_with_file_open():
    with open("./DataStores/close_data.csv", "r") as close_data:
        for l in close_data.readlines():
            print(l)


def read_values_with_file_open():
    with open("./DataStores/close_data.csv", "r") as close_data:
        for l in close_data.readlines():
            print(l.strip())
            values = l.strip().split(",")
            print(values)
            print()


def read_with_pandas():
    import pandas as pd

    some_close_prices = pd.read_csv("DataStores/close_data.csv",
                                    index_col=0, parse_dates=True)

    print(some_close_prices.head())
    print(some_close_prices.describe())


def plot_with_matplotlib():
    import pandas as pd
    from matplotlib import pyplot as plt

    some_close_prices = pd.read_csv("DataStores/close_data.csv",
                                    index_col=0, parse_dates=True)

    ((some_close_prices - some_close_prices.mean()) / some_close_prices.std()).plot(figsize=(15, 7))
    plt.figure(1).canvas.set_window_title("Normalized time series")
    plt.show()


if __name__ == "__main__":
    # read_lines_with_file_open()
    # read_values_with_file_open()
    # read_with_pandas()
    # plot_with_matplotlib()

    pass

