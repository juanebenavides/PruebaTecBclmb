import db
import os
import pandas as pd
from etl import load, extract, transform

DB_PATH = 'flores_db.sqlite'

def reset_db():
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    db.Base.metadata.create_all(db.engine)

def run():
    df = pd.read_csv('data/iris.csv')
    df = transform.add_id(df)
    df.columns = df.columns.str.replace('.', '_', regex=False)
    load.load_data(db.session, df)
    extract.compare_data(db.session, df, 0, 20)
    moda_df = df.drop(columns='id').mode()
    print(df.describe())
    print(moda_df)

if __name__ == '__main__':
    reset_db()
    run()