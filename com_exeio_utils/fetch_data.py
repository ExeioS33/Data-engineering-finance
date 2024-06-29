import os
import logging
import yfinance as yf
import pandas as pd

class FetchData:
    def __init__(self):
        self.tickers = os.getenv('TICKERS').split(',')

    def get_tickers(self):
        logging.info(f"Tickers fetched: {self.tickers}")
        return self.tickers

    def fetch_recent_data(self, ticker_symbol: str) -> pd.DataFrame:
        """
        Retrieves the most recent historical data for a given stock symbol in intraday frequency.

        Args:
            ticker_symbol (str): The stock symbol to process.
        
        Returns:
            pd.DataFrame: A DataFrame containing the most recent data.

        Raises:
            Exception: If there is an error fetching data from yfinance.
        """
        try:
            ticker = yf.Ticker(ticker_symbol)
            data = ticker.history(period="1d", interval="1m")  # adjust the period and interval as needed
            data.index = data.index.tz_localize(None)
            data['date_modification'] = pd.Timestamp.now()
            data['date_modification'] = data['date_modification'].tz_localize(None)

            if not data.empty:
                latest_data = data.iloc[-1:]  # Selects the most recent row
                logging.info(f"Successfully fetched recent data for {ticker_symbol}.")
                return latest_data
            else:
                logging.warning(f"No data received for {ticker_symbol}.")
                return pd.DataFrame()

        except Exception as e:
            logging.error(f"Error fetching data for {ticker_symbol}: {e}")
            raise
