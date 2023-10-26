from typing import List

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

def perteneceGenerico(s:[],e:any) :
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

# def esPalindromo(s:str) -> bool :

