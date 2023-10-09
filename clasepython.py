#1.3

def sumaTotal(s:[int]) -> int :
    total : int = 0
    longitud: int = len(s)
    indice_actual: int = 0
    while indice_actual < longitud:
        total += s[indice_actual] # total = total + s[indice_actual] y despues s[0] sería el head
        indice_actual += 1

    return total

#1.1

def pertenece (s:[(int)] , e : int) -> bool :
    longitud : int = len(s)
    indice_actual : int = 0
    pertenece : bool = False
    while indice_actual < longitud :
        if e == s[indice_actual] :
            pertenece = True
        indice_actual += 1 
    return pertenece

def pertenece_for(s:[(int)] , e : int) -> bool :
    longitud : int = len(s)
    pertenece : bool = False
    for i in range (0,longitud) :
        if e == s[i] :
            return True
    return False

def pertenece_generico(s : [] , e : any) -> bool :
    for elem in s:
        if elem == e :
            return True
    return False

#1.7

def fortaleza_contrasena(contrasena:str) -> str :
    # Verifico longitud mayor a 8
    longitud_mayor_a_8 : bool = len(contrasena) > 8
    # Verifico longitud menor a 5
    longitud_menor_a_5 : bool = len(contrasena) < 5
    # Verifico tiene una mayuscula
    tiene_una_mayuscula : bool = False
    indice_actual : int = 0
    while indice_actual < len(contrasena) :
        if contrasena[indice_actual] <= 'A' and contrasena[indice_actual] <= 'Z' :
            tiene_una_mayuscula = True
        indice_actual += 1
    # Verifico tiene una minuscula
    tiene_una_minuscula : bool = False
    indice_actual = 0
    while indice_actual < len(contrasena) :
        if contrasena[indice_actual] >= 'a' and contrasena[indice_actual] <= 'z' :
            tiene_una_minuscula = True
        indice_actual += 1
    # Verifico tiene un digito numericoef pertenece_a_cada_uno_2(s:[[int]],e:int) -> bool : 
    res_pertenece : [bool] = []
    for val in s :
        res_pertenece.append(pertenece)
    tiene_un_numero : bool = False
    indice_actual : int = 0
    while indice_actual < len(contrasena) and not (contrasena[indice_actual] >= '0' and (contrasena[indice_actual] <= '9')) :
        indice_actual += 1
    tiene_un_numero : bool = indice_actual < len(contrasena)
    #devuelvo color segun condiciones
    if longitud_mayor_a_8 and tiene_un_numero and tiene_una_mayuscula and tiene_una_minuscula:
        return "VERDE"
    elif longitud_menor_a_5 : # else if
        return "ROJA"
    else :
        return "AMARILLA"

#5.1

def pertenece_a_cada_uno(s:[[int]],e:int) -> [bool]
    res : [bool] = []
    for i in range(0,len(s)) :
        if i in range(0,len(s)) :
            res.append(pertenece_generico(s[i],e))
    return res

def pertenece_a_cada_uno_1(s:[[int]],e:int) -> [bool] :
    res_pertenece : [] = []
    indice_actual : int = 0
    longitud : int = len(s)
    while(indice_actual < longitud) :
        lista_actual : [int] = s [indice_actual]
        res_pertenece.append(pertenece(lista_actual,e))
        indice_actual += 1
    return res_pertenece


