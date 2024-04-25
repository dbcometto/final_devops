# This file pins the model that the api uses

from palmerpenguins import penguins
from pandas import get_dummies
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing
from vetiver import VetiverModel
from vetiver import VetiverAPI
import duckdb

# Setup dataframe

con = duckdb.connect('my-db.duckdb')
frame = penguins.load_penguins()

con.execute('DROP TABLE IF EXISTS penguins')
con.execute('CREATE TABLE penguins AS SELECT * FROM frame')
df = con.execute('SELECT * FROM PENGUINS').fetchdf().dropna()

con.close()

# Build model

X = get_dummies(df[['bill_length_mm', 'species', 'sex']], drop_first = True)
y = df['body_mass_g']

model = LinearRegression().fit(X, y)
v = VetiverModel(model, model_name='penguin_model', prototype_data=X)

# Start api

app = VetiverAPI(v, check_prototype = True)
app.run(port = 8080, host = "0.0.0.0")