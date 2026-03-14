import yfinance as yf
import os

SYMBOL = "IBM"

def fetch_stock_data():
    
    df = yf.download(
        SYMBOL,
        start="2015-01-01",
        end="2024-01-01",
        interval="1d"
    )

    os.makedirs("../data", exist_ok=True)

    df.to_csv("../data/raw_stock_data.csv")

    print("Stock data downloaded and saved.")
    
    return df