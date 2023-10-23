def clonar_sin_comentarios(nombre_archivo : str) :
    # Abro el archivo para leer
    archivo = open(nombre_archivo, "r")
    # Abro el archivo en el que voy a escribir
    arch_sin_comentarios = open("clonadoSinComentarios.py","w")
    # Leo todas las lineas
    lineas = archivo.readlines()
    for linea in lineas :
        # Si no una linea NO comienza con # entonces la escribo
        # if not linea.lstrip().startwih("#")
        if not linea.strip()[0] == "#" :
            arch_sin_comentarios.write(linea)
    archivo.close()
    arch_sin_comentarios.close()

clonar_sin_comentarios("ejemploComentado.py")

# para usar pila

from queue import lifoQueue as Pila

p = Pila()
p.put(1) # apilar
p.put(2) # apilar


from queue import Queue as Cola

c = Cola()
c.put(1) # encolar
c.put(2) # encolar
c.put(3) # encolar
print(list(c.queue))
elemento = c.get()
print(elemento) # desapilar
print(c.empty()) # vacia ?
print(list(c.queue))

# EJERCICIO 10

def buscar_el_maximo(p:Pila) -> int :
    maximo = p.get()
    while (not p.empty()) :
        elem = p.get()
        if (elem>maximo) :
            maximo = elem
    return maximo

# Como estamos destruyendo la cola, no respetando la especificacion de "In". Hacemos un for y apilamos cada elemento que vamos sacando en otra pila.

# que la pila no es vacia. FALTA COPIAR ACA
def buscarElMaximo(p: Pila) -> int :
    res: int = p.get()
    paux: Pila = Pila()

    while not p.empty() :
        elem : int = p.get()
        paux.put(elem)
        if elem > res :
            res = elem



print("El maximo de la pila es:")

# funcion en clase
def cantidad_elementos(p: Pila) -> int :
    res: int = 0
    paux : Pila = Pila() 

    while not p.empty() :
        elem = p.get()
        paux.put(elem)
        res = res + 1
    
    while not paux.empty() :
        elem =paux.get()
        p.put(elem)

        return res
    
# OTRO EJERCICIO

# armo una lista con los numeros del 0 al 9
    list: list = list (range(0,9))
# mezcla de la lista. Hay que importar la funcion random
    random.shuffle(lista)