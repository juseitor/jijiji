#1)

#1.1 de clari

def contar_lineas(archivo:str)->int:
    miArchivo = open(archivo, "r")
    lineas:list[str] = miArchivo.readlines()
    cont:int = len(lineas)
    miArchivo.close()
    return cont

#1.2 no funciona para lineas que tengan mas de una palabra. al de clari le pasa parecido pero no agrego siquiera el \n

def existe_palabra(palabra:str,nombre_archivo:str) -> bool :
    miArchivo = open(nombre_archivo,"r")
    contenido : list[str] = miArchivo.readlines()
    si_pertenece : bool = pertenece(contenido,(palabra + "\n"))
    miArchivo.close()
    return si_pertenece

def existe_palabra_clari(palabra:str, archivo:str)->bool:
    miArchivo = open(archivo, "r")
    contenido:list[str] = miArchivo.readlines()
    res:bool= pertenece(contenido, palabra)
    miArchivo.close()
    return res

def pertenece(s:[],e:any) -> bool :
    res : bool = False
    for x in s :
        if x == e :
            return True
    return res

#1.3 no funciona para lineas que tengan mas de una palabra

def cantidad_apariciones(nombre_archivo:str,palabra:str) -> int :
    miArchivo = open(nombre_archivo,"r")
    contenido : list[str] = miArchivo.readlines() 
    res : int = 0
    for linea in contenido :
        if linea == (palabra + "\n") :
            res += 1
    miArchivo.close()
    return res

def cantidad_de_apariciones_clari(archivo:str, palabra:str)->int:
    miArchivo = open(archivo,"r")
    contenido:list = miArchivo.readlines()
    contador:int= 0
    for linea in contenido:
        palabras_linea:list[str]= linea.split()
        while (pertenece(palabras_linea, palabra)==True):
            contador += 1
            palabras_linea.remove(palabra)
    miArchivo.close()
    return contador

def xd(nombre_archivo:str) :
    miArchivo = open(nombre_archivo,"r")
    contenido : list[str] = miArchivo.readlines() 
    miArchivo.close()
    return contenido

#2.1

# def clonar_sin_comentarios(nombre_archivo:str) -> str :
#     miArchivo = open(nombre_archivo,"")

#2)

from queue import LifoQueue as Pila

# p = pila()
# p.put(1) #apilar
# elemento = p.get() #desapilar
# p.empty() #vacia?

#8.1

from typing import List

import random

def generarNrosAlAzar(n:int, desde:int, hasta:int)-> List[int]:
   return random.sample(range(desde,hasta+1,1), n)

#9.1 clari.

def cantidadElementosPilaClari(p: Pila) -> int:
    contador:int = 0 
    while p.empty()== False:
       p.get()
       contador += 1
    return contador

# miPila: Pila = Pila()
# miPila.put(2)
# miPila.put(4)
# print(cantidadElementosPilaClari(miPila))

def cantidadElementosPilaGabi(p:Pila) -> int :
    i:int = 0
    copiaPila = Pila()
    while p.empty() == False:
        elemento1 = p.get()
        copiaPila.put(elemento1)
        i = i + 1
    print(str(i))
    while copiaPila.empty() == False:
        elemento2 = copiaPila.get()
        p.put(elemento2)
    imprimirQueue(p)

def imprimirQueue(p) :
    while not (p.empty()) :
        elemento:int=p.get()
        print(elemento)

# miPila: Pila = Pila()
# miPila.put(2)
# miPila.put(4)
# miPila.put(3)
# print(cantidadElementosPilaGabi(miPila))

#10.1 clari.

def buscarElMaxPilaClari(p:Pila) -> int:
   max:int = -1
   while p.empty() == False:
      num:int = p.get()
      if  num > max:
         max = num
   return max 

# miPila: Pila = Pila()
# miPila.put(2)
# miPila.put(4)
# miPila.put(3)
# print(buscarElMaxPilaClari(miPila))

def buscarElMaxPila(p:Pila) -> int :
    #copiaPila = Pila()
    num_mas_alto: int = (-1)
    siguente_num = p.get()
    while p.empty == False :
        siguiente_num
 #       copiaPila.put(siguiente_num)
        if siguiente_num >= num_mas_alto :
            num_mas_alto = siguiente_num
    return num_mas_alto
    # while copiaPila.empty() == False :
    #     cada_elemento = copiaPila.get()
    #     p.put(cada_elemento)
    # imprimirQueue2(p)

def imprimirQueue2(pila:Pila) :
    while pila.empty() == False :
        elementos = pila.get()
        print(elementos)

# miPila: Pila = Pila()
# miPila.put(2)
# miPila.put(4)
# miPila.put(3)
# print(buscarElMaxPila(miPila))

#3)

from queue import Queue as cola

# c = Cola()
# c.put(1) #encolar
# elemento = c.get() #desencolar()
# c.empty() #vacia?

#13.1

# 4) DICCIONARIOS

#19.1

def agrupar_por_longitud(nombre_archivo:str) -> dict :
    miArchivo = open(nombre_archivo,"r")
    contenido : list = miArchivo.read()
    diccionario : dict[int,int] = {}
    palabras : list[str] = contenido.split()
    for palabra in palabras :
        longitud_palabra : int = len(palabra)
        if longitud_palabra in diccionario :
            cantidad_palabras : int = diccionario[longitud_palabra]
            diccionario[longitud_palabra] = cantidad_palabras + 1
        else :
            diccionario[longitud_palabra] = 1
    miArchivo.close()
    return diccionario

#de nuevo para practicar

def agruparPorLongitud(nombre_archivo:str) -> dict :
    miArchivo = open(nombre_archivo,"r")
    contenido : str = miArchivo.read()
    palabras : list[str] = contenido.split()
    diccionario : dict[int,int] = {}
    for palabra in palabras :
        longitud_palabra : int = len(palabra)
        if longitud_palabra in diccionario : 
            diccionario[longitud_palabra] += 1
        else :
            diccionario[longitud_palabra] = 1
    miArchivo.close()
    return diccionario

# print(agruparPorLongitud("lista_compras.txt"))

#21.1

def la_palabra_mas_frecuente(nombre_archivo:str) :#-> str :
    miArchivo = open(nombre_archivo,"r")
    contenido : list = miArchivo.read()
    palabras : list[str] = contenido.split()
    diccionario : dict[str,int] = {}
    for palabra in palabras :
#        cantidad_apariciones : int = 0 NO. toma todos como 1
        if palabra in diccionario :
#            diccionario[palabra] = cantidad_apariciones + 1 NO
            diccionario[palabra] = diccionario[palabra] + 1
        else : 
            diccionario[palabra] = 1
    repeticiones : int = 0
    palabra_mas_repetida : str = ""
    for palabra in diccionario.keys() :
        if diccionario[palabra] > repeticiones :
            repeticiones = diccionario[palabra]
            palabra_mas_repetida = palabra
    miArchivo.close()
    return palabra_mas_repetida

#22.1

historiales : dict[str,Pila] = {}
historialesAtrasAdelante : dict[str,Pila] = {}

def visitar_sitio(historiales:dict,usuario:str,sitio:str) -> dict :
#    for user in historiales.keys() :
    if usuario in historiales :
        historiales[usuario].put(sitio)
    else :
        historiales[usuario] = Pila()
        historiales[usuario].put(sitio)
    return historiales

print(visitar_sitio(historiales,"Usuario2","google.com"))

# miPila1 : Pila = Pila()
# miPila1.put("google.com")
# miPila1.put("facebook.com")
# print(imprimirQueue2(miPila1))

# miPila2 : Pila = Pila()
# miPila2.put("youtube.com")

