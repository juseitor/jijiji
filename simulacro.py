# Ejercicio 1

def ultima_aparicion(s:list,e:int) -> int :
    indice_actual : int = len(s) - 1
    while indice_actual > 0 :
        if s[indice_actual] == e :
            return indice_actual
        else :
            indice_actual = indice_actual - 1

def ultima_aparicion_fir(s:list,e:int) -> int :
    ultima_pos : int
    for i in range(0,len(s)) :
        if s[i] == e :
            ultima_pos = i 
    return ultima_pos

# Ejercicio 2

def pertenece(s:[],e:any) -> bool :
    for x in s :
        if x == e :
            return True
    return False

def elementos_exclusivos(s:list,t:list) -> list :
    res : list = []
    for i in s :
        if not pertenece(t,i) and not pertenece(res,i) :
            res.append(i)
    for x in t :
        if not pertenece(s,x) and not pertenece(res,x) :
            res.append(x)
    return res

# Ejercicio 3

def contar_traducciones_iguales(ingles:dict,aleman:dict) -> int :
    res : int = 0
    itemsingles : list = list(ingles.items())
    itemsaleman : list = list(aleman.items())
    for x in items.ingles() :
        if pertenece(items.aleman(),x) :
            res += 1
    return res

# Ejercicio 4 de joel

def convertir_a_diccionario(lista:list) -> dict :
    diccionario : dict[int,int] = {}
    for i in lista :
        if i in diccionario :
            diccionario[i] = diccionario [i] + 1
        else :
            diccionario[i] = 1
    return diccionario

# print(convertir_a_diccionario([(-1),0,4,100,100,(-1),(-1)]))





