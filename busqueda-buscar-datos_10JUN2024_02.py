import pandas as pd

datos = pd.read_excel('DATOS-PRACTICA-CEUNSASB-01.xlsx')
print(datos.columns.values)

#['ORDEN' 'ESCUELA' 'TIPO DE EJEMPLAR' 'NOMBRE' 'CLASE' 'GENERO']

#datos.columns = ['ORDEN', 'ESCUELA', 'TIPO DE EJEMPLAR', 'MATRICULA', 'APELLIDO', 'NOMBRE', 'CLASE', 'GENERO', 'DOMICILIO',
 #                'SECCION', 'CIRCUITO', 'MESA.1', 'ORDEN_MESA', 'ESCUELA.1', 'TX_SECC_NUMERO', 'TX_CIRC_NUMERO']


print(datos)
##DNI_CONSULTA = input 41820982
print("========================================================")

CONSULTA = 'BETSABE AMERICA'
#CONSULTA = 'DOROTEA'
#CONSULTA = 'CRISTIAN ARIEL'
#CONSULTA = 'BELEN ZULEMA'
#CONSULTA = 'CELESTE NOEMI'
#CONSULTA = 'RAUL MANUEL'

print ("Información requerida: ", CONSULTA)

#busqueda = datos.loc[datos["NOMBRE"] == CONSULTA,['ORDEN', "ESCUELA","TIPO DE EJEMPLAR","CLASE","GENERO"]]

#busqueda = datos.loc[datos["NOMBRE"] == CONSULTA,["ESCUELA",'TIPO DE EJEMPLAR',"CLASE","GENERO"]]

#busqueda = datos.loc[datos["NOMBRE"] == CONSULTA,["TIPO DE EJEMPLAR",'CLASE',"GENERO"]]

#busqueda = datos.loc[datos["NOMBRE"] == CONSULTA,["CLASE","GENERO"]]

busqueda = datos.loc[datos["NOMBRE"] == CONSULTA,['NOMBRE',"CLASE"]]

filas = len(busqueda['CLASE'])

if (filas == 1):
    print("========================================================")
    print("Existen 1 resultado: ")
    print("Edad: ", 2024 - int(busqueda['CLASE']), " años")
else:
    print("========================================================")
    print("Existen mas de 1 resultado, cantidad: ", filas, "REGISTROS")
    for i in (busqueda['CLASE']):
        print("--------------------------------------------------------")
        print(CONSULTA, "del año de nacimiento: ", i)
        print("Edad: ", 2024 - int(i), " años")

print("========================================================")        
print("DATASET Resultante (Filas x Columnas): ", busqueda.shape)
print("--------------------------------------------------------")
print (busqueda)
print("========================================================")    

