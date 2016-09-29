"""Juan el callado"""
ciclo = 1
while ciclo == 1:
    control = 0
    frase = input(("Dile algo a Juan: "))
    cont = len(frase)
    if cont == 0:
        print("Juan: Mmmmmm")
    for letra in frase:
        if letra == "?":
            print("Juan: Ofi")
            control = 1
    if frase.isupper() and control != 1:
        print("Juan: Chilea")
        control = 0
    if frase.islower() and control != 1:
        print("Juan: Me da igual")
        control = 0