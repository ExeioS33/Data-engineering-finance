from com_exeio_utils.fetch_data import FetchData
from com_exeio_utils.get_connection import GetConnection
from com_exeio_utils.store_data import StoreData
import os
import logging

def main():
    try:
        db_connector = GetConnection(
            dbname=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASS'),
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT')
        )
        db_connector.connect()

        ticker_fetcher = FetchData()
        data_inserter = StoreData(db_connector)

        tickers = ticker_fetcher.get_tickers()
        for ticker in tickers:
            data = ticker_fetcher.fetch_recent_data(ticker)
            if not data.empty:
                # Mise à jour des noms des colonnes pour correspondre exactement aux noms dans PostgreSQL
                data.columns = [col.lower().replace(' ', '_') for col in data.columns]  # Transforme toutes les colonnes en minuscules et remplace les espaces par des underscores
                data_inserter.insert_data(ticker, data)

    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        db_connector.close()

if __name__ == "__main__":
    main()
