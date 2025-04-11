import pandas as pd
from models import iris

def load_data(session, df):
    for index, row in df.iterrows():
        sepal_length = row['sepal_length']
        sepal_width = row['sepal_width']
        petal_length = row['petal_length']
        petal_width = row['petal_width']
        variety = row['variety']
        flower = iris.Iris(sepal_length, sepal_width, 
        petal_length, petal_width, variety)
        session.add(flower)
    session.commit()

###### otra funcion para cargar los datos en la nueva tabla
def load_data(session, df):
    for index, row in df.iterrows():
        sepal_length = row['sepal_length']
        sepal_width = row['sepal_width']
        petal_length = row['petal_length']
        petal_width = row['petal_width']
        variety = row['variety']
        flower = iris.Iris(sepal_length, sepal_width, 
        petal_length, petal_width, variety)
        session.add(flower)
    session.commit()