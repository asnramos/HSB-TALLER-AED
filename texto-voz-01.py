import pyttsx3

estaciones = ["Verano", "Otoño", "Invierno", "Primavera"]
estaciones2 = ["verano", "otoño", "invierno", "primavera"]

listado_palabras = ['Hoy', 'es', 'el', 'inicio', 'de', 'la', 'primavera', 'aqui', 'en', 'el', 'hemisferio', 'sur', 'del', 'planeta', 'tierra']

if estaciones2[3] in listado_palabras:
    engine = pyttsx3.init()
    engine.say("Hola Daniela, muy bueno verte, Si esta la palabra que buscas")
    engine.runAndWait()
else:
    engine = pyttsx3.init()
    engine.say("No esta la palabra")
    engine.runAndWait()
    
