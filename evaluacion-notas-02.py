
def evaluacion(promedio):
    if promedio >= 6:
        estado = "APROBADO"
        if promedio == 10:
            estado = "APROBADO ABANDERADO"
        if promedio == 9:
            estado = "APROBADO 1er Escolta"
        if promedio == 8:
            estado = "APROBADO 2do Escolta"
    else:
        estado = "DESAPROBADO"
        
    print("El alumno esta: ", estado)
    return 

estado = "No Evaluado"
promedio = 0
contador = 0
print("#####################################")
print(estado)
print(promedio)
print(contador)
print("#####################################")

promedio = int(input("Ingrese Promedio: "))

while (promedio > 0) and (promedio < 11):
    print("Promedio ingresado: ", promedio)
    evaluacion(promedio) #Llamada a la FUNCION para evaluar el promedio
    contador += 1
    print("#####################################")
    promedio = int(input("Ingrese Promedio: "))

print("Alumnos evaluados: ", contador)

