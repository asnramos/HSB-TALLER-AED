# Es necesario importar la librería de Pandas
# https://4geeks.com/es/how-to/anadir-columna-dataframe-python

import pandas as pd


# Crear un DataFrame de muestra

data = {'Company ': ['Facebook', 'Apple', 'Google', 'Neftlix'],

        'Started At': [2004, 1976, 1998, 1997]}

df = pd.DataFrame(data)


# Agregar una nueva columna al DataFrame

publicly_traded_company = [True, True, True, True]  # Data de muestra para nueva columna

df['publicly_traded_company'] = publicly_traded_company


# Imprimir el DataFrame actualizado

print(df)


# Resultado esperado

#   Company     Started At   publicly_traded_company

#0  Facebook       2004             True

#1     Apple       1976             True

#2    Google       1998             True

#3   Neftlix       1997             True
