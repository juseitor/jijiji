import math
import numpy

math.sqrt()
numpy.sin()

def prueba():
    print("Funciona")

#prueba()

def imprimir_hola():
    print("Hola")

def es_multiplo_de(n:int,m:int) -> bool:
    res:bool = (n%m)==0 # mod n m == 0
    return res
# defino el valor de una variable, y le digo que devuelva res

def es_nombre_largo(nombre:str) -> bool:
    res : bool = 3<=len(nombre) and len(nombre)<=8 # && and
    return res

def devolver_el_doble_si_es_par( n : int) -> int :
    if es_multiplo_de(n,2):
        res : int = 2*n
    else:
        res : int = n
    return res

def imprimir_pares() :
    i : int = 10
    while i <= 40 :
        print(i)
        i=i+2

def imprimir_pares_for():
    for i in range(10,41,2):
        print(i)

