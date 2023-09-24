--1)

--1.1

longitud :: [t] -> Integer
longitud [] = 0
longitud (x:xs) = 1 + longitud xs

--1.2

ultimo :: [t] -> t
ultimo (x:[]) = x
ultimo (x:xs) = ultimo (tail (x:xs))

--1.3

principio :: [t] -> [t]
principio (x:xs) | longitud (x:xs) == 1 = []
                 | otherwise =  x : principio (xs)

--1.4

reverso :: [t] -> [t]
reverso [] = []
reverso [x] = [x]
reverso (x:xs) = [ultimo (x:xs)] ++ reverso (principio (x:xs))

--2)

--2.1

pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece x (y:xs) | x == y = True
                   | otherwise = pertenece x xs

--2.2

todosIguales :: (Eq t) => [t] -> Bool
todosIguales [] = True
todosIguales (x:[]) = True
todosIguales (x:y:xs) | x == y = todosIguales (x:xs)
                      | otherwise = False

--2.3

todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos [] = True
todosDistintos (x:[]) = True
todosDistintos (x:xs) | pertenece x xs == True = False
                      | otherwise = todosDistintos xs


--2.4

hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos [] = True
hayRepetidos (x:[]) = False
hayRepetidos (x:xs) | pertenece x xs == True = True
                    | otherwise = hayRepetidos xs

hayRepetidosClari ::  (Eq t) => [t] -> Bool
hayRepetidosClari (xs) | todosDistintos xs = False
                       | otherwise = True

--2.5

quitar :: (Eq t) => t -> [t] -> [t]
quitar _ [] = []
quitar x xs | x == head(xs) = tail(xs)
            | otherwise = [head(xs)] ++ quitar x (tail(xs)) 
--quitar x (y:z:xs) | x == y = (z:xs) 
--                  | otherwise = quitar x (z:xs) 

-- 2.6

quitarTodos :: (Eq t) => t -> [t] -> [t]
quitarTodos _ [] = []
--quitarTodos x (y:[]) | x == y = []. funco esto pero estaba de mas
quitarTodos x xs | x == head xs = quitarTodos x (tail xs)
                 | otherwise = [head xs] ++ quitarTodos x (tail xs)

--2.7

eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos [] = []
-- --eliminarRepetidos (x:y:[]) | x == y = [y]
eliminarRepetidos xs | pertenece (head xs) (tail xs) == True = eliminarRepetidos (quitar (head xs) xs)
                     | otherwise = [head xs] ++ eliminarRepetidos (tail xs)

eliminarRepetidosClari :: (Eq t) => [t] -> [t]
eliminarRepetidosClari [] = []
-- eliminarRepetidos [x] = [x]
eliminarRepetidosClari (x:xs) | pertenece x xs = eliminarRepetidos (quitar x (x:xs)) 
                         | otherwise = [x] ++ eliminarRepetidos(xs) 

--2.8

mismosElementos :: (Eq t) => [t] -> [t] -> Bool
mismosElementos [] [] = True
mismosElementos (x:xs) ys | pertenece x ys == True = mismosElementos (quitarTodos x xs) (quitarTodos x ys)
mismosElementos xs (y:ys) | pertenece y xs == True = mismosElementos (quitarTodos y xs) (quitarTodos y ys)
                          | otherwise = False  

mismosElementosClari :: (Eq t) => [t] -> [t] -> Bool
mismosElementosClari (x:xs) (y:ys) = pertenecenTodos (x:xs) (y:ys) && pertenecenTodos (y:ys) (x:xs)

pertenecenTodos :: (Eq t) => [t] -> [t] -> Bool
pertenecenTodos [] _ = True
pertenecenTodos (x:xs) ys = pertenece x ys && pertenecenTodos xs ys

--2.9

capicua :: (Eq t) => [t] -> Bool
capicua [] = True
capicua (x:[]) = True
capicua xs | head (xs) == ultimo xs = capicua (tail (principio(xs)))
           | otherwise = False

--3)

--3.1

sumatoria :: [Integer] -> Integer
sumatoria [] = 0
sumatoria xs = head xs + sumatoria(tail xs)

--3.2

productoria :: [Integer] -> Integer
productoria [] = 1
-- productoria [] = 0 . asi es como lo habìa hecho antes
-- productoria (x:[]) = x
productoria xs = head xs * productoria (tail xs)

--3.3

maximo :: [Integer] -> Integer
maximo (x:[]) = x
maximo (x:y:xs) | x >= y = maximo (x:xs) 
                | otherwise = maximo (y:xs)

--3.4

sumarN :: Integer -> [Integer] -> [Integer]
sumarN _ [] = []
sumarN x xs = [x + head xs] ++ sumarN x (tail xs)

--3.5

sumarElPrimero :: [Integer] -> [Integer]
sumarElPrimero [] = []
sumarElPrimero xs = sumarN (head xs) xs

--3.6

sumarElUltimo :: [Integer] -> [Integer]
sumarElUltimo [] = []
sumarElUltimo xs = sumarN (ultimo xs) xs

--3.7

pares :: [Integer] -> [Integer]
pares [] = []
pares (x:xs) | mod x 2 == 0 = [x] ++ pares xs
             | otherwise = pares xs

--3.8

multiplosDeN :: Integer -> [Integer] -> [Integer]
multiplosDeN _ [] = []
multiplosDeN n xs | mod (head xs) n == 0 = [head xs] ++ multiplosDeN n (tail xs)
                  | otherwise = multiplosDeN n (tail xs)

--3.9

ordenar :: [Integer] -> [Integer]
ordenar [] = []
ordenar xs = [menor xs] ++ ordenar(quitar (menor xs) xs)

menor :: [Integer] -> Integer
menor [x] = x
menor (x:y:xs) | x <= y = menor (x:xs)
               | otherwise = menor (y:xs) 

--4)

--4.1

sacarBlancosRepetidos :: [Char] -> [Char]
sacarBlancosRepetidos [] = []
sacarBlancosRepetidos (x:[]) = [x]
sacarBlancosRepetidos (x:y:xs) | x == ' ' && x == y = sacarBlancosRepetidos (y:xs)
                               | otherwise = x:sacarBlancosRepetidos(y:xs)

--4.2

contarPalabras :: [Char] -> Integer
contarPalabras (x:xs) = 1 + contarEspacios(sacarBlancosFin(sacarBlancosIni(sacarBlancosRepetidos xs)))

contarEspacios :: [Char] -> Integer
contarEspacios [] = 0
contarEspacios (x:xs) | x == ' ' = 1 + contarEspacios xs
                      | otherwise = contarEspacios xs  

sacarBlancosIni :: [Char] -> [Char]
sacarBlancosIni [] = []
sacarBlancosIni (x:y:xs) | x /= ' ' = (x:y:xs)
                         | x == ' ' && y /= ' ' = (y:xs)
                         | x == ' ' && y == ' ' = sacarBlancosIni (y:xs)

sacarBlancosFin :: [Char] -> [Char]
sacarBlancosFin [] = []
sacarBlancosFin (x:[]) | x == ' ' = []
                       | otherwise = [x] 
sacarBlancosFin (x:xs) = x:(sacarBlancosFin xs) 

--4.3

palabras :: [Char] -> [[Char]]
palabras xs = palabrasAux (sacarBlancosFin(sacarBlancosIni(sacarBlancosRepetidos xs)))

palabrasAux :: [Char] -> [[Char]]
palabrasAux [] = []
palabrasAux xs = primeraPalabra xs : (palabrasAux(sacarPrimeraPalabra xs))
-- palabrasAux (x:[]) | x == ' ' = [[]]
--                    | otherwise = [[x]]
-- palabrasAux (x:y:xs) | x /= ' ' = [[x]] ++ palabrasAux xs
--                      | x == ' ' = palabrasAux xs 

primeraPalabra :: [Char] -> [Char]
primeraPalabra [] = []
primeraPalabra (x:xs) | x /= ' ' = x : primeraPalabra xs
                      | x == ' ' = []

sacarPrimeraPalabra :: [Char] -> [Char]
sacarPrimeraPalabra [] = []
sacarPrimeraPalabra (x:xs) | x == ' ' = xs 
                           | otherwise = sacarPrimeraPalabra xs 

--4.4

palabraMasLarga :: [Char] -> [Char]
palabraMasLarga xs = palabraMasLargaAux (sacarBlancosFin(sacarBlancosIni(sacarBlancosRepetidos xs)))

palabraMasLargaAux :: [Char] -> [Char]
palabraMasLargaAux xs | sacarPrimeraPalabra xs == [] = primeraPalabra xs
                      | length (primeraPalabra xs) >= length (palabraMasLargaAux(sacarPrimeraPalabra xs)) = primeraPalabra xs
                      | otherwise = palabraMasLargaAux(sacarPrimeraPalabra xs)

--4.5 no lo hice este

aplanar :: [[Char]] -> [Char]
aplanar [] = []
aplanar (xs:xss) = xs ++ (aplanar xss)
 
--4.6

aplanarConBlancos :: [[Char]] -> [Char]
aplanarConBlancos [] = []
aplanarConBlancos (xs:xss) = sacarBlancosFin (xs ++ [' '] ++ aplanarConBlancos (xss))

--4.7

-- aplanarConNBlancos :: [[Char]] -> Integer -> [Char]
-- aplanarConNBlancos [] _ = []
-- aplanarConNBlancos
