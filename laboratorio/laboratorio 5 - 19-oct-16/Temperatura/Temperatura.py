"""Programa para evaluar temperatura"""

def evalua(t,c):
    if (t > 37.5):
        archivo = open("temp.dat", "a")
        archivo.write(str(c)+","+str(t)+",fiebre\n")
        archivo.close()
    elif (t >= 30) and\
            (t <= 37.5):
        archivo = open("temp.dat", "a")
        archivo.write(str(c)+","+str(t)+",normal\n")
        archivo.close()
    elif (t < 30) and (t > 5):
        archivo = open("temp.dat", "a")
        archivo.write(str(c)+","+str(t)+",enfermo\n")
        archivo.close()
    elif (t < 5):
        archivo = open("temp.dat", "a")
        archivo.write(str(c)+","+str(t)+",muerto\n")
        archivo.close()



control=1
cont=0
while control==1:
    try:
        temp = float(input("Introduzca la tempetarura- salir temperatura=0 : "))
        if (temp == 0):
            control=0
            break
    except:
        print("Valor Invalido")
    else:
        cont = cont + 1
        evalua(temp,cont)