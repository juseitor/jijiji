--1)
fibonacci :: Integer -> Integer
fibonacci n | n == 0 = 0
            | n == 1 = 1
            | otherwise = fibonacci(n-1) + fibonacci(n-2)

--2)

parteEnteraG4 :: Float -> Integer
parteEnteraG4 x | x > 0 && x < 1 = 0
                | x >= 1 = parteEnteraG4 (x-1) + 1

--3)

esDivisible :: Integer -> Integer -> Bool
esDivisible x y | x == y = True
                | x < y = False
                | otherwise = esDivisible (x-y) y

--4)

sumaImpares :: Integer -> Integer
sumaImpares x | x == 1 = 1
              | mod x 2 == 0 = sumaImpares (x-1) + x + 1
              | otherwise = sumaImpares (x-2) + x

--5)

medioFact :: Integer -> Integer
medioFact x | x == 0 = 1
            | x == 1 = 1
            | otherwise = x * medioFact(x-2)

--6)

sumaDigitos :: Integer -> Integer
sumaDigitos n | n < 10 = n
              | n >= 10 = (mod n 10) + sumaDigitos (div n 10)

--7)

ultimoDigito :: Integer -> Integer
ultimoDigito x = mod x 10

sacarUltimo :: Integer -> Integer
sacarUltimo x = div x 10

todosDigitosIguales :: Integer -> Bool
todosDigitosIguales n | n < 10 = True
                      | otherwise = (ultimoDigito n == ultimoDigito(sacarUltimo n)) && todosDigitosIguales (sacarUltimo n)
    