ciudadfuria = """
Me verás volar
Por la ciudad de la furia
Donde nadie sabe de mí
Y yo soy parte de todos
Nada cambiará
Con un aviso de curva
En sus caras veo el temor
Ya no hay fábulas
En la ciudad de la furia
Me verás caer
Como un ave de presa
Me verás caer
Sobre terrazas desiertas
Te desnudaré
Por las calles azules
Me refugiaré
Antes que todos despierten
Me dejarás dormir al amanecer
Entre tus piernas
Entre tus piernas
Sabrás ocultarme bien y desaparecer
Entre la niebla
Entre la niebla
Un hombre alado extraña la tierra
Me verás volar
Por la ciudad de la furia
Donde nadie sabe de mí
Y yo soy parte de todos
Con la luz del sol
Se derriten mis alas
Solo encuentro en la oscuridad
Lo que me une
Con la ciudad de la furia
Me verás caer
Como una flecha salvaje
Me verás caer
Entre vuelos fugaces
Buenos Aires se ve
Tan susceptible
Es el destino de furia, es
Lo que en sus caras persiste
Me dejarás dormir al amanecer
Entre tus piernas
Entre tus piernas
Sabrás ocultarme bien y desaparecer
Entre la niebla
Entre la niebla
Un hombre alado prefiere la noche
Me verás volver
Me verás volver
A la ciudad de la furia
"""

ciudadfuria.split()

len(ciudadfuria)

len(ciudadfuria.split())

buscadas =["furia", "cuidad", "caer", "noche", "tierra", "alado"]

buscadas
['furia', 'cuidad', 'caer', 'noche', 'tierra', 'alado']

buscadas.append("manzana")
buscadas

for palabra in buscadas:
    print(palabra)

buscadas.append("ciudad")
buscadas
['furia', 'cuidad', 'caer', 'noche', 'tierra', 'alado', 'manzana', 'verás', 'veras', 'ciudad']
for palabra in buscadas:
    if palabra in ciudadfuria:
        cantidad = ciudadfuria.count(palabra)
        print(palabra, "SI esta en la cancion.", cantidad, "veces")
        print("======================================================")
    else:
        print(palabra, "No esta en la cancion.")
        print("======================================================")
