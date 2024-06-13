# CASOS DE USO
# https://4geeks.com/es/how-to/anadir-columna-dataframe-python

import pandas as pd

# Crear un DataFrame 

data = {Error: ['Car computer hacked', 'Wheels misaligned', 'Windshield broken', 'Ran out of battery'],

        'Date': ['1/2/2023', '26/2/2023', '4/4/2023', '6/22/2023']}

df = pd.DataFrame(data)

# Agregar una nueva columna al DataFrame

severity = ['high', 'medium', 'high', 'low']

df2 = df.assign(Severity = severity)

print(df2)

# Resultado esperado

#            Error             Date      Severity

#0    Car computer hacked    1/2/2023      high

#1     Wheels misaligned     26/2/2023    medium

#2     Windshield broken     4/4/2023      high

#3    Ran out of battery     6/22/2023     low
