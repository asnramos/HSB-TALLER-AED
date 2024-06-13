import pandas as pd

#ruta = 'https://github.com/asnramos/HSB-TALLER-AED/blob/main/employees.csv'
#datos = pd.read_csv(ruta)
#ruta = 'https://github.com/asnramos/HSB-TALLER-AED/blob/main/DATOS-PRACTICA-CEUNSASB-01.xlsx'
#datos = pd.read_excel(ruta)

datos = pd.read_csv('employees.csv')

print(datos.columns.values)
print(datos.shape)
#datos.columns = []

print(datos)

#defining function filter
def filter(x):
    if x <= 60000:
        return 'low'
    if (x > 60000 and x <= 120000):
        return 'medium'
    if x > 120000:
        return 'high'
    
#applying the filter function to 'Salary' column
datos['category'] = datos['Salary'].apply(filter)

print("==========================================================")
print(datos['category'])

print("==========================================================")
print(datos)

print("==========================================================")
print(datos['category'].value_counts())
