import sqlalchemy
from sqlalchemy import Column, Float, String, Integer
from db import Base 

class Iris(Base):
    __tablename__ = "Iris"
    id = Column(Integer, primary_key=True)
    sepal_length = Column(Float, nullable=False)
    sepal_width = Column(Float, nullable=False)
    petal_length = Column(Float, nullable=False)
    petal_width = Column(Float, nullable=False)
    variety = Column(String, nullable=False)

    def __init__(self, sepal_length, sepal_width, petal_length, petal_width, variety):
        self.sepal_length = sepal_length
        self.sepal_width = sepal_width
        self.petal_length = petal_length
        self.petal_width = petal_width
        self.variety = variety
