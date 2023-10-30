from typing import List
from typing import Tuple

#1)

#1.1

def pertenece1(s:list,e:int) -> bool :
    indice_actual : int = 0
    pertenece : bool = False
    while indice_actual < len(s) :
        if e == s[indice_actual] :
            pertenece = True
        indice_actual = indice_actual + 1
    return pertenece

def pertenece2(s:list,e:int) -> bool :
    for i in range(0,len(s)) :
        if e == s[i] :
            return True
    return False

def pertenece_generico(s:[],e:any) :
    for elemento in s :
        if elemento == e :
            return True
    return False

#1.2

def divideATodos(s:[int],e:int) -> bool :
    for elemento in s :
        if elemento%e != 0 :
            return False
    return True

#1.3

def sumaTotal(s:[int]) -> int :
    indice_actual : int = 0
    suma : int = 0
    while indice_actual < len(s) :
        suma = suma + s[indice_actual]
        indice_actual = indice_actual + 1
    return suma

#1.4

def ordenados(s:[int]) -> bool :
    indice_actual : int = 0
    indice_mayor : int = 1
    res : bool = True
    while indice_mayor < len(s) :
        if s[indice_actual] < s[indice_mayor] and res :
            res = True
            indice_actual += 1
            indice_mayor += 1
        else:
            res = False
            indice_actual += 1
            indice_mayor += 1
    return res

#1.5

def palabraLarga1(s:List[str]) -> bool :
    indice_actual : int = 0
    while indice_actual < len(s) :
        if len(s[indice_actual]) > 7 :
            return True
        else :
            indice_actual += 1 
    return False

def palabraLarga2(s:List[str]) -> bool :
    for palabra in s:
        if len(palabra) > 7 :
            return True
    return False

#clari
def hayPalabraDe7Letras(s:List[str]) -> bool:
  res = False
  for i in (0,len(s),1):
     if len(s[i]) < 8 and not res:
         res=False
     else: res=True    
  return res

#1.6

def esPalindromo1(s:str) -> bool :
    res : bool = True
    indice_primero : int = 0
    indice_ultimo : int = len(s) - 1
    while indice_ultimo > indice_primero :
        if s[indice_primero] == s[indice_ultimo] and res :
            res = True
            indice_primero += 1
            indice_ultimo = indice_ultimo - 1
        else :
            res = False
            indice_primero += 1
            indice_ultimo -= 1
    return res

# de clari

def esPalindromo2(s:str) -> bool :
    res : bool = True
    for i in range(0,(len(s)//2),1) :
        if (s[i] == s[len(s) - i - 1]) and res :
            res = True
        else :
            res = False
    return res

#1.7 mal

def fortalezaContraseña(contraseña:str) -> str :
    longitud_mayor_a_8 : bool = len(contraseña) > 8
    longitud_menor_a_5 : bool = len(contraseña) < 5
    tiene_una_mayuscula : bool = False
    tiene_una_minuscula : bool = False
    tiene_digito_numerico : bool = False
    indice_actual : int = 0
    while indice_actual < len(contraseña) :
        if contraseña[indice_actual] >= 'a' and contraseña[indice_actual] <= 'z' :
            tiene_una_minuscula = True
            indice_actual += 1
    while indice_actual < len(contraseña) :
        if contraseña[indice_actual] >= 'A' and contraseña[indice_actual] <= 'Z' :
            tiene_una_mayuscula = True
            indice_actual += 1
    while indice_actual < len(contraseña) :
        if contraseña[indice_actual] >= '0' and contraseña[indice_actual] <= '9' :
            tiene_digito_numerico = True
            indice_actual += 1
    if longitud_mayor_a_8 and tiene_una_mayuscula and tiene_una_minuscula and tiene_digito_numerico :
        return "VERDE"
    elif longitud_menor_a_5 :
        return "ROJO"
    else :
        return "AMARILLO"

#1.7

def fortaleza_contraseña(contraseña:str) -> str :
    res : str = "AMARILLO"
    if len(contraseña) < 5 :
        res = "ROJO"
    elif len(contraseña) > 8 and contiene_minuscula(contraseña) and contiene_mayuscula(contraseña) and contiene_numero(contraseña) :
        res = "VERDE"
    return res

def contiene_minuscula(contraseña:str) -> bool :
    res : bool = False
    for letra in contraseña :
        if letra <= 'z' and letra >= 'a' :
            res = True
    return res

def contiene_mayuscula(contraseña:str) -> bool :
    res : bool = False
    for letra in contraseña :
        if letra >= 'A' and letra <= 'Z' :
            res = True
    return res

def contiene_numero(contraseña:str) -> bool :
    res : bool = False
    for digito in contraseña :
        if digito >= '0' and digito <= '9' :
            res = True
    return res

#1.8 no se porque no corre

def saldo(movimientos:List[Tuple]) -> int :
    total : int = 0
    for x in movimientos :
        if x[0] == "I" :
            total = total + x[1]
        else :
            total = total - x[1]
    return total

#1.9

def distintasVocales(palabra:str) -> bool :
    res : bool = False
    vocales1 : list = []
    for letra in palabra :
        if esVocal(letra) and not perteneceGenerico(vocales1,letra) :
            vocales1.append(letra)
    if len(vocales1) >= 3 :
        res = True
    return res

def esVocal(letra:str) -> bool :
    res : bool = False
    vocales2 : list = ['a','e','i','o','u','A','E','I','O','U']
    if perteneceGenerico(vocales2,letra) :
        res = True
    return res

def pertenece_clari2(s:[],e:any) :
    for elemento in s :
        if elemento == e :
            return True
    return False

#2)

#2.1

def cambiarPosicionesPares(s:list) :
    for i in range(0,len(s)-1,2) :
        s[i] = 0

#2.2

def cambioPosicionesPares(s:list) -> list :
    t : list = []
    for i in range(0,len(s),1) :
        if i % 2 == 0 :
            t.append(s[i]) 
        else :
            t.append(0)
    return t

#2.3


