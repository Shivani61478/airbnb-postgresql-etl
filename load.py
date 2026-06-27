from sqlalchemy import create_engine
import logging

logging.basicConfig(
    filename='log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def load(df):
    logging.info("Data loading started.")
    try:
        engine = create_engine('postgresql+psycopg2://username:password@localhost:5432/airbnb_db')

        df.to_sql("airbnb_listings", engine, index=False, if_exists="replace")

        logging.info("Data loaded into PostgreSQL successfully")
        print("Data loaded successfully")

    except Exception as e:

        logging.error(f"Failed to load data: {e}")
        print(f"Error loading data: {e}")
    