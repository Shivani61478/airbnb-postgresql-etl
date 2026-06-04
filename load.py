from sqlalchemy import create_engine
import logging

logging.basicConfig(
    filename='log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)



def load(df):
    logging.info("Data loading started.")

    engine = create_engine('postgresql+psycopg2://your_username:your_password@localhost:5432/airbnb_db')

    logging.info("Data loaded into Postgresql")

    print("Data loaded sucessfully")

    