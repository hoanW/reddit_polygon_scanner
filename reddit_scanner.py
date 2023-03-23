import requests
import pandas as pd
import os

URL = "https://api.polygonscan.com/api"

DATA = {
    "module": "account",
    "action": "txlist",
    "address": "0x36FB3886CF3Fc4E44d8b99D9a8520425239618C2",
    "startblock": int(4e7),
    "endblock": 99999999,
    "page": 1,
    "offset": 10,
    "sort": "desc",
    "apikey": os.environ.get("POLYGONSCAN_API_KEY"),
}


def get_data(limit=10, columns=["blockNumber", "timeStamp", "hash"]):

    try:
        with requests.Session() as session:
            res = session.get(url=URL, params=DATA).json()
    except Exception as e:
        print("Failed to get data from API")
        return None

    if res["status"] == "0":
        print("Failed call to API")
        return None
    else:
        result = res["result"]
        result = result[:limit]
        # convert result to dataframe
        df = pd.DataFrame(result)
        # convert timestamp to datetime
        df["timeStamp"] = pd.to_datetime(df["timeStamp"], unit="s")
        df = df[columns]
        return df
