import logging
import psycopg2

class StoreData:
    def __init__(self, db_connector):
        self.db_connector = db_connector

    def insert_data(self, table_name, df):
        if not self.db_connector.cursor:
            self.db_connector.connect()
        
        try:
            columns = ", ".join(f'"{col}"' for col in df.columns)
            values = ", ".join(["%s"] * len(df.columns))
            insert_query = f'INSERT INTO stocks."{table_name}" ({columns}) VALUES ({values})'
            self.db_connector.cursor.executemany(insert_query, df.values.tolist())
            self.db_connector.conn.commit()
            logging.info(f"Data inserted into table {table_name} successfully.")
        except psycopg2.Error as e:
            logging.error(f"Error inserting data into table {table_name}: {e}")
            self.db_connector.conn.rollback()