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
    i: int = 1
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

#4)

#4.1

def peso_pino(altura:float) -> float :
    if altura - 3 > 0 :
        return 900 + (altura - 3) * 2 * 100
    else :
        return altura * 3 * 100
    
#4.2

def es_peso_util(peso:float) -> bool :
    res : bool = 400 <= peso <= 1000
    return res

#4.3

def sirve_pino(altura:float) -> bool :
    res : bool = 400 <= peso_pino(altura) <= 1000
    return res

#5)

#5.1

def devolver_el_doble_si_es_par(n:int) -> int :
    if n % 2 == 0 :
        return 2*n
    else :
        return n
    
#5.2

def devolver_valor_si_es_par_sino_el_que_sigue(n:int) -> int :
    if n % 2 == 0 :
        return n
    else :
        return n + 1
    
#5.3

def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(n:int) -> int :
    if n % 3 == 0 :
        return 2 * n
    if n % 9 == 0 :
        return 3 * n
    else :
        return n
    
#5.4

def lindo_nombre(nombre:str) -> str :
    if len(nombre) >= 5 :
        print("Tu nombre tiene muchas letras!")
    else :
        print("Tu nombre tiene menos de 5 caracteres. Es horrrible y chico, como tu verga")

#5.6

def que_te_toca(sexo:str,edad:int) -> str :
    if edad < 18 :
        return "Anda de vacaciones"
    if sexo == "F" and edad >= 60 :
        return "Anda de vacaciones"
    if sexo == "M" and edad >= 65 :
        return "Anda de vacaciones"
    else :
        return "Te toca laburar pajin"

# print(que_te_toca("F",17))
# print(que_te_toca("M",7))
# print(que_te_toca("F",37))
# print(que_te_toca("M",57))
# print(que_te_toca("F",60))
# print(que_te_toca("M",60))
# print(que_te_toca("M",65)) 

#6)

#6.1

def del_1_al_10() :
    i = 1
    while i <= 10 :
        print (i)
        i = i + 1

#6.2

def pares_del_10_al_40() :
    i = 10
    while i <= 40 :
        print(i)
        i = i + 2

#6.3
