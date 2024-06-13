import pandas as pd
import plotly.express as px

ruta = "https://raw.githubusercontent.com/cocodibuja/scipyla2021/main/weatherdata--304-622.csv"
df_weather = pd.read_csv(ruta)
print(df_weather)

fig = px.line(df_weather, x='Date', y="Precipitation")
fig.show()

