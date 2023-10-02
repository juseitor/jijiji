# 1)

#1.1

def imprimir_hola_mundo() :
    print("¡Hola mundo!")

#1.2

def imprimir_un_verso() :
    print("Ya me voy volando, \npor el parabrisas. \nMe estas esperando, \njunto a tu sonrisa.")

#1.3

import math

def raiz_de_2() :
    res = round(math.sqrt(2),4) 
    return res

#1.4

def factorial_de_2() :
    res = 2
    return res

def factorial(n:int) -> int :
    res : int = 1
    for i in range(1,n+1):
        res = res * i
        print(res)
    return res

def factorial_w(n:int) -> int :
    res: int = 1
    I: int = 1
    while i>0 :
        res=res*1
        i=i-1
        print(res)
    return res

#1.5

def perimetro() :
    res = 2 * math.pi
    return res

#2)

#2.1

def imprimir_saludo(nombre:str) :
    print("Hola " + nombre)

#2.2

def raiz_cuadrada_de(n:float) :
    res : float = math.sqrt(n)
    return res

#2.3

def fahrenheit_a_celsius(t:float) :
    res : float = ((t-32)*5)/9
    return res

#2.4

def imprimir_dos_veces(estribillo:str) :
    print ((estribillo + " \n") * 2)

#2.5

def es_multiplo_de(n:int,m:int) :
    res : bool = (n%m) == 0
    return res

#2.6

def es_par(numero:int) :
    res : bool = es_multiplo_de(numero,2) == True
    return res
    
#2.7

def cantidad_de_pizzas(comensales:int,min_cant_de_porciones:int) :
    res : int = math.ceil((comensales * min_cant_de_porciones)/8)
    return res

#3)

#3.1

def alguno_es_0(numero1:float,numero2:float) :
    res : bool = numero1 == 0 or numero2 == 0
    return res

#3.2

def ambos_son_0(numero1:float,numero2:float) :
    res : bool = numero1 == 0 and numero2 == 0
    return res

#3.3

def es_nombre_largo(nombre:str) :
    res : bool = len(nombre)>=3 and len(nombre)<=8
    return res

#3.4

def es_bisiesto(año:int) :
    res : bool = (año%400 == 0) or (año%4 == 0 and año%100 != 0)
    return res

