
import pandas as pd
import numpy as np

def custom_date_parser(date_str):
    """
    Custom date parser function for parsing dates in the format '19-JAN-2023'.
    """
    return pd.to_datetime(date_str, format='%d-%b-%Y')

def calculate_daily_returns(data):
    """
    Calculate daily returns based on the provided dataset.
    Formula: (current close / previous close) - 1
    """
    data['Daily Returns'] = (data['Close'] / data['Close'].shift(1)) - 1
    return data['Daily Returns'].dropna()

def calculate_daily_volatility(daily_returns):
    """
    Calculate daily volatility using standard deviation.
    """
    daily_volatility = daily_returns.std()
    return daily_volatility

def calculate_annualized_volatility(daily_volatility, data_length):
    """
    Calculate annualized volatility using the daily volatility.
    Formula: Daily Volatility * Square Root (length of data)
    """
    annualized_volatility = daily_volatility * np.sqrt(data_length)
    return annualized_volatility

def main():
    try:
        data = pd.read_csv(r'D:\Finzome\stock_data.csv', parse_dates=['Date '], date_parser=custom_date_parser, dayfirst=True).rename(columns=lambda x: x.strip())
        print("Read CSV successful.")
        print("Columns in the loaded data:", data.columns)
        print("Sample data:", data.head())

        
        daily_returns = calculate_daily_returns(data)

        
        daily_volatility = calculate_daily_volatility(daily_returns)

        
        data_length = len(data)
        annualized_volatility = calculate_annualized_volatility(daily_volatility, data_length)

       
        print(f"Daily Volatility: {daily_volatility:.4f}")
        print(f"Annualized Volatility: {annualized_volatility:.4f}")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
