#1)

#1.2 de clari

def contar_lineas(archivo:str)->int:
    miArchivo = open(archivo, "r")
    lineas:list[str] = miArchivo.readlines()
    cont:int = len(lineas)
    miArchivo.close()
    return cont

#2)

from queue import LifoQueue as pila

# p = pila()
# p.put(1) #apilar
# elemento = p.get() #desapilar
# p.empty() #vacia?

#8.1

from typing import List

import random

def generarNrosAlAzar(n:int, desde:int, hasta:int)-> List[int]:
   return random.sample(range(desde,hasta+1,1), n)

#9.1 clari. me parece que deshace la pila in. no me toma empty

def cantidadElementosPila(p : pila) -> int:
    contador:int = 0 
    while p.empty()== False:
       p.get()
       contador += 1
    return contador

#10.1 clari. no me toma empty

def buscarElMaxPila(p:pila) -> int:
   max:int = -1
   while p.empty() == False:
      num:int = p.get()
      if  num > max:
         max = num
   return max 

#3)

from queue import Queue as cola

#13.1

# c = Cola()
# c.put(1) #encolar
# elemento = c.get() #desencolar()
# c.empty() #vacia?


