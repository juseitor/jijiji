module Solucion where

-- Ejercicio 1
votosEnBlanco :: [(String, String)] -> [Int] -> Int -> Int
votosEnBlanco rs xs x | sumatoriaVotos xs == x = 0
                      | sumatoriaVotos xs < x = 1 + votosEnBlanco rs xs (x-1)  

sumatoriaVotos :: [Int] -> Int
sumatoriaVotos [] = 0
sumatoriaVotos xs = head xs + sumatoriaVotos (tail xs)


-- Ejercicio 2
formulasValidas :: [(String,String)] -> Bool
formulasValidas [] = True
formulasValidas ((c1,c2):rs) | (distintosComponentes (c1,c2) == True) && not(pertenece c1 (todosLosCandidatos rs)) == True && not (pertenece c2 (todosLosCandidatos rs)) == True = formulasValidas rs
                             | otherwise = False

distintosComponentes :: (String,String) -> Bool
distintosComponentes (c1,c2) | c1 == c2 = False
                         | otherwise = True 

todosLosCandidatos :: [(String,String)] -> [String]
todosLosCandidatos [] = []
todosLosCandidatos ((c1,c2):rs) = c1 : c2 : todosLosCandidatos rs

pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece x xs | x == head xs = True
               | otherwise = pertenece x (tail xs)

-- Ejercicio 3
porcentajeDeVotos :: String -> [(String,String)] -> [Int] -> Float
porcentajeDeVotos cp ((c1,c2):rs) (x:xs) | cp == c1 = porcentaje x (sumatoriaVotos (x:xs))
                                         | otherwise = porcentajeDeVotos cp rs (ponerAlFinal x xs)

porcentaje :: Int -> Int -> Float
porcentaje x n = ((fromIntegral x) * 100)/(fromIntegral n)

ponerAlFinal :: Int -> [Int] -> [Int]
ponerAlFinal x [] = [x]
ponerAlFinal x (y:xs) = [y] ++ ponerAlFinal x xs


-- Ejercicio 4
proximoPresidente :: [(String, String)] -> [Int] -> String
proximoPresidente [] [] = [] 
proximoPresidente ((c1,c2):rs) (x:xs) | esMaximo x (x:xs) = c1
                                      | otherwise = proximoPresidente rs xs 

maximo :: [Int] -> Int
maximo (x:[]) = x
maximo (x:y:xs) | x >= y = maximo (x:xs)
                | otherwise = maximo (y:xs)

esMaximo :: Int -> [Int] -> Bool
esMaximo _ [] = False
esMaximo x xs | maximo xs == x = True
              | otherwise = False