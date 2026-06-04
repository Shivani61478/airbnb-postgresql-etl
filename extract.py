import pandas as pd
import logging

logging.basicConfig(
    filename='log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def extract():
    logging.info("Data extraction started.")

    df = pd.read_csv(
    'Airbnb_Open_Data.csv',
    low_memory=False
)

    logging.info("Data extraction completed")

    return df



