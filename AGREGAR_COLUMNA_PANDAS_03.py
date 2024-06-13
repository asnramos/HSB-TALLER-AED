# METODO INSERT()
# https://4geeks.com/es/how-to/anadir-columna-dataframe-python

import pandas as pd


# Crear un DataFrame 

data = {'Brand': ['Toyota', 'Ford', 'Tesla', 'Mitsubishi'],

        'Model': ['Hilux', 'Escape', 'Model S', 'Lancer']}

df = pd.DataFrame(data)


# Agregar una nueva columna al DataFrame

year = ['2020', '2019', '2022', '2015']

df.insert(1, 'Year', year)


print(df)


# Resultado esperado

#        Brand    Year   Model

#0      Toyota    2020    Hilux

#1        Ford    2019   Escape

#2       Tesla    2022  Model S

#3  Mitsubishi    2015   Lancer
