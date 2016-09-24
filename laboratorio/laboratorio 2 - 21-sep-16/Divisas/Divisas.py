"""
Elabodado por Azael Fonseca
Este programa calcula las conversion
en diferentes monedas
"""

cent = int(input ("Centavos:"))
usd = cent/100
print("Dolares: "+str(usd))
eur= usd*0.8965
print("Euro: "+str(eur))
yen= usd*101.5744
print("YEN: "+str(yen))
BP= usd*0.7702
print("BP: "+str(BP))
MXN= usd*19.7843
print("MXN: "+str(MXN))
print("Hasta luego")