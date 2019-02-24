
BOOTCAMP_FRED_API_KEY = "4b208f3c49c58b57081514bb13a81577"


def download_data_from_url():
    import requests

    DOWNLOAD_URL = f"https://api.stlouisfed.org/fred/series/observations?series_id=UNRATE&api_key={BOOTCAMP_FRED_API_KEY}"

    response = requests.get(DOWNLOAD_URL)
    print(response.text)


def download_data_from_url_as_json():
    import requests

    DOWNLOAD_URL = f"https://api.stlouisfed.org/fred/series/observations?series_id=UNRATE&api_key={BOOTCAMP_FRED_API_KEY}" + "&file_type=json"

    response = requests.get(DOWNLOAD_URL)

    print(response.text)
    print(type(response.text))
    print(response.json())
    print(type(response.json()))


def download_data_from_url_as_json():
    import requests

    DOWNLOAD_URL = f"https://api.stlouisfed.org/fred/series/observations?series_id=UNRATE&api_key={BOOTCAMP_FRED_API_KEY}" + "&file_type=json"
    print(DOWNLOAD_URL)     # take a look in Firefox

    response = requests.get(DOWNLOAD_URL)

    print(response.text)
    print(type(response.text))
    print(response.json())
    print(type(response.json()))


def download_and_save_json_data_from_url():
    import requests

    DOWNLOAD_URL = f"https://api.stlouisfed.org/fred/series/observations?series_id=UNRATE&api_key={BOOTCAMP_FRED_API_KEY}" + "&file_type=json"

    response = requests.get(DOWNLOAD_URL)

    content = response.text
    with open("fred_data.json", "w") as f:
        f.write(content)


def download_json_data_into_dataframe_and_process():
    import requests
    import pandas as pd
    from datetime import datetime as dt

    DOWNLOAD_URL = f"https://api.stlouisfed.org/fred/series/observations?series_id=UNRATE&api_key={BOOTCAMP_FRED_API_KEY}" + "&file_type=json"

    response = requests.get(DOWNLOAD_URL)

    json_res = response.json()
    df = pd.DataFrame(json_res['observations'])
    print(df.head())

    print("""
    -------------------------------------------
    """)

    df.index = [dt.strptime(s, '%Y-%m-%d') for s in df.date]
    del df['date']
    del df['realtime_end']
    del df['realtime_start']
    df.columns = ['UNEMPLOYMENT']

    print(df.head())
    return df


def pull_from_fred_api():
    # https://github.com/mortada/fredapi

    from fredapi import Fred
    import pandas as pd

    fred = Fred(api_key=BOOTCAMP_FRED_API_KEY)

    fred_series_id_list = ["CSUSHPINSA", "CPIAUCSL"]
    fred_raw = {}
    for i in fred_series_id_list:
        fred_raw[i] = fred.get_series(series_id=i)

    fred_list = []
    for i in fred_series_id_list:
        raw = fred_raw[i]
        processed = pd.Series(raw, name=i)
        fred_list.append(processed)

    print(fred_list)
    return fred_list


if __name__ == "__main__":
    # download_data_from_url()
    # download_data_from_url_as_json()
    # download_and_save_json_data_from_url()
    # download_json_data_into_dataframe_and_process()
    # use_fred_api()

    pass

