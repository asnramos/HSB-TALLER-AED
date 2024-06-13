
def evaluacion(promedio):
    if promedio >= 6:
        estado = "APROBADO"
        if promedio == 10:
            estado = "APROBADO y es EL ABANDERADO"
        if promedio == 9:
            estado = "APROBADO y es 1er Escolta"
        if promedio == 8:
            estado = "APROBADO y es 2do Escolta"
    else:
        estado = "DESAPROBADO"
        
    print("El alumno esta: ", estado)
    
    return 

estado = "No Evaluado"
promedio = 0

promedio = int(input("Ingrese Promedio: "))
print("Promedio ingresado: ", promedio)
evaluacion(promedio)


