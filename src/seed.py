import pandas as pd
from src.cleaning import clean_dataframe
from src.db import get_pymongo_collection

CSV_PATH = "data/bundesliga_player.csv"

def seed_database():
    df = pd.read_csv(CSV_PATH)
    df = clean_dataframe(df)
    records = df.to_dict(orient="records")

    collection = get_pymongo_collection()
    collection.delete_many({})
    collection.insert_many(records)

    print(f"Inserted {len(records)} records into MongoDB.")

if __name__ == "__main__":
    seed_database()