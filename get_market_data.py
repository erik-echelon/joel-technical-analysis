import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import time

# Define the date range
end_date = datetime.now()
start_date = end_date - timedelta(days=365*20)  # Last 365 days
start_str = start_date.strftime('%Y-%m-%d')
end_str = end_date.strftime('%Y-%m-%d')

try:
    # Create ticker objects with the original tickers
    print("Creating ticker objects...")
    sp500 = yf.Ticker("^GSPC")  # S&P 500 Index
    dxy = yf.Ticker("DX-Y.NYB")  # US Dollar Index
    
    # Get historical data using the history() method
    print("Getting historical data for S&P 500...")
    sp500_data = sp500.history(start=start_str, end=end_str)
    
    # Add delay to avoid rate limiting
    time.sleep(2)
    
    print("Getting historical data for DXY...")
    dxy_data = dxy.history(start=start_str, end=end_str)
    
    # Check if we have data
    if sp500_data.empty:
        print("S&P 500 data is empty. Falling back to SPY ETF...")
        sp500 = yf.Ticker("SPY")
        sp500_data = sp500.history(start=start_str, end=end_str)
        
    if dxy_data.empty:
        print("DXY data is empty. Falling back to UUP ETF...")
        dxy = yf.Ticker("UUP")
        dxy_data = dxy.history(start=start_str, end=end_str)
    
    # Check again after fallback
    if sp500_data.empty or dxy_data.empty:
        print("Still couldn't retrieve data. Please check your connection and try again.")
        exit(1)
        
    # Create combined dataframe
    combined_data = pd.DataFrame()
    
    # Convert datetime index to timezone-naive by converting to string and back to datetime
    combined_data['Date'] = pd.to_datetime(sp500_data.index.strftime('%Y-%m-%d'))
    combined_data['SP500_Close'] = sp500_data['Close'].values
    
    # Create a temporary dataframe for DXY data
    dxy_df = pd.DataFrame({
        'Date': pd.to_datetime(dxy_data.index.strftime('%Y-%m-%d')),
        'DXY_Close': dxy_data['Close'].values
    })
    
    # Merge the dataframes on Date
    combined_data = pd.merge(combined_data, dxy_df, on='Date', how='inner')
    
    # Export to Excel
    if not combined_data.empty:
        combined_data.to_excel('DXY_SP500_Data.xlsx', index=False)
        print(f"Data exported to DXY_SP500_Data.xlsx with {len(combined_data)} rows")
    else:
        print("No data to export.")
        
except Exception as e:
    print(f"Error: {e}")
    print("Try installing the latest version of yfinance: pip install yfinance --upgrade")