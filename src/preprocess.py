import pandas as pd

def load_and_clean_data():

    df = pd.read_csv("../data/raw_stock_data.csv")

    df["Date"] = pd.to_datetime(df["Date"])
    df.set_index("Date", inplace=True)

    df = df[["Open","High","Low","Close","Volume"]]

    df.columns = ["open","high","low","close","volume"]

    df.dropna(inplace=True)

    return df