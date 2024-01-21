# volatility_app/utils.py
import pandas as pd
import numpy as np

def calculate_volatility(file):
    data = pd.read_csv(file, parse_dates=['Date'], dayfirst=True).rename(columns=lambda x: x.strip())
    daily_returns = (data['Close'] / data['Close'].shift(1)) - 1
    daily_volatility = daily_returns.std()
    data_length = len(data)
    annualized_volatility = daily_volatility * np.sqrt(data_length)
    return {'daily_volatility': daily_volatility, 'annualized_volatility': annualized_volatility}
