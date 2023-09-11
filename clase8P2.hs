doubleMe x = x + x

pertenece _ [] = False
pertenece l (x:xs) = l==x || pertenece l xs

hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos [] = False
hayRepetidos (x:xs) = pertenece x xs || hayRepetidos xs

-- significa que me quedo con la segunda variable

maximo [x] = x
maximo (x:y:xs) | x>y = maximo (x:xs)
                | otherwise = maximo (y:xs)

eliminar x (y:ys) | x==y = ys
                | otherwise = y : (eliminar x ys)

ordenar [] = []
ordenar xs = ordenar ( eliminar (maximo xs)) ++ [maximo xs]

descomponerEnPrimos :: [Integer] -> [[Integer]]
descomponerEnPrimos (x:xs) = descomposicionPrima x : descompomerEnPrimos xs

primosQueDividenDesde d n | d > n = []
                          | esPrimo d && mod n d == 0 = d : primoQueDivideDesde (d+1) n
                          | otherwise primosQueDividenDesde (d+1) n

descomposicionPrima n = primosQueDividenDesde 2 n 