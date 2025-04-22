# Market Data Tracker

A Python utility to automatically fetch and compile historical closing values for the S&P 500 index and the US Dollar Index into a single Excel spreadsheet.

## Overview

This tool uses the yfinance library to retrieve historical market data through Yahoo Finance's API. The resulting spreadsheet contains three columns:
- Date
- SP500_Close (S&P 500 closing value)
- DXY_Close (US Dollar Index proxy closing value)

## Requirements

- Python 3.6 or higher
- Required Python packages (see `requirements.txt`)

## Installation

1. Clone this repository or download the source files
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Simply run the script to generate an Excel file with the last year of market data:

```bash
python get_market_data.py
```

The script will create a file named `DXY_SP500_Data.xlsx` in the same directory.

## How It Works

The script:
1. Creates Ticker objects for SPY (S&P 500 ETF) and UUP (Dollar Index proxy)
2. Uses the `history()` method to retrieve historical price data
3. Converts timezone-aware datetimes to timezone-naive format for Excel compatibility
4. Merges the datasets and exports to Excel

## Troubleshooting Common Issues

- **"No timezone found, symbol may be delisted"**: This can occur due to rate limiting or connection issues. Try adding delays between API calls or running the script again later.
- **Empty data frames**: Check that the ticker symbols are correct and that you have a working internet connection.
- **Excel timezone errors**: The script handles this by converting datetimes to timezone-naive format before export.

## Customization Options

You can modify the script to:

- Change the date range (default is 1 year of historical data)
- Use different ticker symbols (e.g., "^GSPC" instead of "SPY" for S&P 500)
- Add additional market indices or securities
- Change the output format (CSV, JSON, etc.)

## Example Modification

To change the date range to 5 years instead of 1 year:

```python
# Change this line
start_date = end_date - timedelta(days=365)

# To
start_date = end_date - timedelta(days=365*5)
```

## Files

- `get_market_data.py` - Main script to fetch and compile market data
- `requirements.txt` - List of required Python packages
- `README.md` - This documentation file

## License

This project is released under the MIT License.

## Disclaimer

This tool is for informational purposes only. Historical market data may not be complete or accurate. Do not use this data for making investment decisions.