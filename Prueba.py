def valores():
    global resultado
    n1= int(input("ingrese el valo 1: "))
    n2= int(input("ingrese el valor 2: "))
    resultado= n1 + n2
    print("el resultado es:", resultado)
    return resultado


valores()