# ASIGNACION DIRECTA
# https://4geeks.com/es/how-to/anadir-columna-dataframe-python

import pandas as pd

# Crear un DataFrame 

data = {'Brand': ['Toyota', 'Ford', 'Tesla', 'Mitsubishi'],

        'Model': ['Hilux', 'Escape', 'Model S', 'Lancer']}

df = pd.DataFrame(data)

# Agregar una nueva columna al DataFrame

df['Year'] = ['2020', '2019', '2022', '2015']

print(df)

# Resultado esperado

#        Brand    Model  Year

#0      Toyota    Hilux  2020

#1        Ford   Escape  2019

#2       Tesla  Model S  2022

#3  Mitsubishi   Lancer  2015
