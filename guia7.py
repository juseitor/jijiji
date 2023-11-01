from typing import List
from typing import Tuple
import random

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
    if pertenece_clari2(vocales2,letra) :
        res = True
    return res

def pertenece_clari2(s:[],e:any) :
    for elemento in s :
        if elemento == e :
            return True
    return False

#2)

#2.1

def cambiarPosicionesPares(s:list) -> list:
    for i in range(1,len(s),2) :
        s[i] = 0

# t:list = [1,1,1,1]
# print(t)
# cambiarPosicionesPares(t)
# print(t)

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

def sacarVocales(palabra:str) -> str :
    palabra_sin_vocales : list = []
    for letra in palabra :
        if not esVocal(letra) :
            palabra_sin_vocales.append(letra)
    return palabra_sin_vocales

#2.4

def reemplazaVocales(palabra:str) -> str :
    palabra_sin_vocales : list = []
    for letra in palabra :
        if esVocal(letra) :
            palabra_sin_vocales.append(' ')
        else : 
            palabra_sin_vocales.append(letra)
    return palabra_sin_vocales

#2.5

def daVueltaStr(palabra:str) -> str :
    palabra_dada_vuelta : str = []
    for letra in range (len(palabra)-1,(-1),(-1)) :
        palabra_dada_vuelta.append(palabra[letra])
    return palabra_dada_vuelta

# si en la linea 262 en vez de lo escrito pongo:
# palabra_dada_vuelta = palabra_dada_vuelta + palabra[letra]
# me tira :
# File "/home/jusa/Downloads/guia7.py", line 262, in daVueltaStr
#     palabra_dada_vuelta = palabra_dada_vuelta + palabra[letra]
# TypeError: can only concatenate list (not "str") to list

#2.6

# def eliminarRepetidos(palabra:str) -> str :
#     palabra_nueva : str = []
#     for letra in palabra :
#         if not pertenece_generico(quitarPrimeraAparicion(palabra),letra) :
#             palabra_nueva.append(letra)
#         else :

# def quitarPrimeraAparicion(palabra:str,letra:str) -> str :
#     palabra_sin_primera : str = []
#     indice_actual = 0
#     while indice_actual < len(palabra) :
#         if palabra[indice_actual] != letra :
#             palabra_sin_primera.append(palabra[indice_actual])
#             indice_actual += 1
#         else :

def eliminarRepetidos(palabra:str) -> str :
    palabra_nueva : str = []
    indice_actual : int = 0
    while indice_actual < len(palabra) :
        if not pertenece_generico(palabra_nueva,palabra[indice_actual]) :
            palabra_nueva.append(palabra[indice_actual])
            indice_actual += 1
        else :
            indice_actual += 1
    return palabra_nueva

def eliminarRepetidosGabi(s:str) -> str :
    res : str = ""
    for x in range(0,len(s),1) :
        if not pertenece_generico(res,s[x]) :
            res = res + s[x]
    return res

#3) con elem me toma como que si al menos hay algun numero que sea mayor a 4 ya puede ser 1 o 2, en vez de que al haber al menos un numero menor a 4 es si o si 3

def aprobado(s:list) -> int :
    res : int = 3
    for elem in s :
        if promedio(s) >= 7 and not elem <= 4 :
            res = 1
        elif promedio(s) < 7 and promedio(s) >= 4 and not elem <= 4 :
            res = 2
    return res

def promedio(s:list) -> float :
    res : int = sumaTotal(s) / len(s)
    return res

#4)

#4.1 

def nombresEstudiantes()->list:
    estudiantes:list=[]
    nombre=input()
    while not(nombre == "listo"):
        estudiantes.append(nombre)
        nombre = input()
    return estudiantes   

#print(nombresEstudiantes())

#4.2 clari

def cargasDeLaSube():
    eleccion=input()
    historial:list=[]
    while not (eleccion == "X"):
        monto=input()
        historial.append((eleccion, monto))
        eleccion=input()
    else: return historial   

#4.3 clari

def sieteYmedio():
    mazo:list=[1,2,3,4,5,6,7,10,11,12]
    eleccion="y"
    historial:list[float]=[]
    puntos:float=0
    res=[]
    while eleccion=="y": 
      carta = random.choice(mazo)
      historial.append(carta)
      if pertenece_generico([10,11,12],carta):
          puntos = puntos + 0.5
      else: puntos = puntos + carta      
      if puntos > 7.5: 
        print("Ha perdido. Este es su historial de cartas:")
        return historial
      print("¿Desea plantarse (x) o seguir (y)?:")
      eleccion=input()    
    print("Se ha plantado. Este es su historial de cartas:")
    return historial  

#5)

#5.1

def perteneceACadaUno(s:[[int]],e:int) -> [bool] :
    res : [bool] = []
    indice_actual : int = 0
    while indice_actual < len(s) :
        if pertenece_generico(s[indice_actual],e) :
            res.append(True)
            indice_actual += 1
        else:
            res.append(False)
            indice_actual += 1
    return res

#5.2

def esMatrizClari(s:List[list])->bool:
    res:bool = True
    if len(s)>0 and len(s[0])>0:
        for i in range(0,len(s),1):
           if len(s[i]) == len(s[0]) and res:
               res=True
           else: res = False 
    else: res = False
    return res 

def esMatriz(s:[[int]]) -> bool :
    res : bool = True
    if len(s) > 0 and len(s[0]) > 0 :
        for fila in range(0,len(s),1) :
            if len(s[0]) == len(s[fila]) and res:
                res = True
            else :
                res = False
    else :
        res = False
    return res
        

#5.3

#def filasOrdenadas(m:[[int]]) -> bool :