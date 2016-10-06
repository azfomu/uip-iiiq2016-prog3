"""Contador de palabras Agua y Fuego"""
elemento = {"agua":1,"fuego":2}
lista = []
contador1 = 0
contador2 = 0
frase = "dentro"
while frase != "salir":
    frase = input(("Escriba frase: "))
    if "agua" in frase:
        contador1 = contador1 + 1
        lista.append(frase)
    elif ("fuego") in frase:
        contador2 = contador2 + 1
        lista.append(frase)
print("Agua:  ", contador1)
print("Fuego: ", contador2)
print(lista)
