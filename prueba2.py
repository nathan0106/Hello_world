def suma_dos_valores(sumando1, sumando2):
    global resultado
    resultado = sumando1 + sumando2
    return resultado

#suma_dos_valores(4,5)
#print("primera suma")
#print (resultado)
#suma_dos_valores(1,2)
#print("segunda suma")
#print(resultado)


def calculadora_dos_valores(numero1, numero2, operador):
    global resultado
    if operador ==1:# si el operador es 1 es suma
        resultado = numero1 + numero2
        return resultado
    elif operador ==2:# si el operador es 2 es resta
        resultado = numero1 - numero2
        return resultado
    elif operador ==3:# si el operador es 3 es multi
        resultado = numero1 * numero2
        return resultado
    elif operador ==4:# si el operador es 4 es division
        resultado = numero1 / numero2
        return resultado
    else: # si el operador es otro numero
        print("el numero ingresado no es valido")
        return resultado
    
#calculadora_dos_valores(1,2,1)
#print("suma:", resultado)
#calculadora_dos_valores(1,2,2)
#print("resta:", resultado)
#calculadora_dos_valores(1,2,3)
#print("multiplicacion:", resultado)
#calculadora_dos_valores(1,2,4)
#print("division:", resultado)


#def pitagoras(a,b):
    global c
    c=(a**2+b**2)**0.5
    return c

#pitagoras(3,4)
#print("pitagoras",c)

#def despeje_x():
    global x
    b=int(input("ingrese el valor de b= "))
    c=int(input("ingrese el valor de c= "))
    x= (c-b)/2
    print("el valor de x es: ",x)
    return x

#despeje_x()

#def AND():
    #global resultado
    #a=bool(input("ingrese el valor de a= "))
    #b=bool(input("ingrese el valor de b= "))
    #c=bool(input("ingrese el valor de c= "))
    #x= (a and b and c)
    #print("el valor de x es:  ", x)
   #return x
#AND()

#def pitagoras_funcion_sumar():
    global resul_pitagoras
    a=int(input("ingrese el valor de a= "))
    b=int(input("ingrese el valor de b= "))
    a2= a**2
    b2= b**2
    suma= suma_dos_valores(a2,b2)
    resul_pitagoras= suma**0.5
    print("el valor de pitagoras es: ", resul_pitagoras)
    return resul_pitagoras

#pitagoras_funcion_sumar()


#def separador():
    global resultado_separador
    palabra=str(input("ingrese la palabra a contar: "))
    letra=str(input("ingrese la palabra a contar: "))
    resultado_separador = palabra.count(letra)
    print("la cantidad de letras", letra, "es= ", resultado_separador)
    print("la cantidad de letras de la palabra es=", len(palabra))
    print("palabra separada por letras= ",list(palabra))
#separador()

def piedra_papel_tijera(jugador1,jugador2,ramdon):
    global resultado
    piedra= 
    papel=
    tijera=
    computador= random.choice(piedra,pepel,tijera)

    if jugador1 : computador
    resultado= computador
    return resultado
print("el jugador1 obtuvo: ", resultado)
if jugador2 : computador
    resultado= computador
    return resultado
print("el jugador2 obtuvo: ", resultado)
piedra_papel_tijera()