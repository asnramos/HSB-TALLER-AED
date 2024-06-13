import pandas as pd
import plotly.express as px

#archivo = "D:/python3107/Padron-Final-2019JUJUY.xlsx"
archivo = "D:/python3107/LAQUIACA-2019-JUNIO.xlsx"
datos = pd.read_excel(archivo)

print(datos.columns.values)
print(datos)

#px.bar(x=["a", "b", "c"], y=[1, 3, 2])
fig = px.bar(x=["FEMENINO", "MASCULINO"], y=[7310, 6994], colors)
fig.show()

#F    7310
#M    6994
