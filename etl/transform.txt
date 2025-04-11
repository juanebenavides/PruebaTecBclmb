def add_id(df):
    df["id"] = range(1, len(df) + 1)
    return df