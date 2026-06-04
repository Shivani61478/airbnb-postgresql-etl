import logging
import pandas as pd

logging.basicConfig(
    filename='log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def transform(df):
    logging.info("Transformation started.")

    df = df[
        [
        "NAME",
            "host name",
            "price",
            "room type",
            "neighbourhood group",
            "availability 365"
    ]
    ]

    logging.info("Selected Required columns")

    df.columns = df.columns.str.lower()
    df = df.drop_duplicates()
    

    logging.info("Removed duplicates")

    df = df.dropna()
    
    logging.info("Removed null values")

    df["price"] = df["price"].replace("[$,]", "",regex = True)
    df["price"] = df["price"].astype(float)

    logging.info("price column cleaned and converted to float")

    df.to_csv('processed_data/cleaned_data.csv', index=False)

    logging.info("Transformed CSV saved as cleaned_data.csv")
    


    return df


 