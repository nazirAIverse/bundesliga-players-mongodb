import pandas as pd

DROP_COLUMNS = [
    "unnamed:_0", "full_name", "place_of_birth", "shirt_nr",
    "foot", "contract_expires", "joined_club", "player_agent", "outfitter"
]

def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    return df

def clean_prices(df: pd.DataFrame) -> pd.DataFrame:
    df["price"] = (
        df["price"]
        .astype(str)
        .str.replace(",", "", regex=False)
        .str.replace(" euros", "", regex=False)
        .astype(float)
        .astype(int)
    )

    df["max_price"] = (
        df["max_price"]
        .astype(str)
        .str.replace(",", "", regex=False)
        .str.replace(" euros", "", regex=False)
        .astype(float)
        .astype(int)
    )
    return df

def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna()
    df = df.reset_index(drop=True)
    df = clean_column_names(df)
    df = df.drop(columns=DROP_COLUMNS)
    df = clean_prices(df)
    return df