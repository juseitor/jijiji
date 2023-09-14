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
              | otherwise = 2*x - 1 + sumaImpares (x-1)

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
    
--8)

cantDigitos :: Integer -> Integer
cantDigitos n | (n >= 0 && n < 10) = 1 
              | otherwise = 1 + cantDigitos (div n 10)

iesimoDigito :: Integer -> Integer -> Integer
iesimoDigito n i | i == cantDigitos(n) = mod n 10
                 | otherwise = iesimoDigito (div n 10) i

--9)

primerDigito :: Integer -> Integer
primerDigito n | cantDigitos n == 1 = n
               | otherwise = primerDigito (div n 10) 

sacarPrimerDigito :: Integer -> Integer
sacarPrimerDigito n = n - (primerDigito n * conversion n)

conversion :: Integer -> Integer
conversion n | n < 10 && n > 0 = 1
             | otherwise = 10 * conversion (div n 10)

esCapicua :: Integer -> Bool
esCapicua n | cantDigitos n == 1 = True
            | (cantDigitos n == 2 && primerDigito n == ultimoDigito n) = True   
            | cantDigitos n >= 3 = esCapicua (div (sacarPrimerDigito n) 10)
            | otherwise = False

--10)

--f1

f1 :: Integer -> Integer
f1 n | n == 0 = 1
     | otherwise = 2^n + f1 (n-1)

--f2

f2 :: (Integer , Float) -> Float
f2 (n , q) | n == 1 = q
       | otherwise = q^n + f2 ((n-1) , q)

--f3

auxF2 :: (Integer , Float) -> Float
auxF2 (n , q) | n == 0 = 1
              | otherwise = q^n + auxF2 ((n-1) , q)

f3 :: (Integer , Float) -> Float
f3 (n , q) | n == 0 = 1
       | otherwise = auxF2 ((2*n) , q)

--13)

-- -- f :: Integer -> Integer -> Integer
-- f i j | i==1 = fAux 1 j 
--       | otherwise = fAux i j + f(i-1) j

-- fAux :: Integer -> Integer -> Integer
-- fAux i j | j == 1 = i 
--          | otherwise = i^j + fAux i (j-1)

-- salio choto pero debería haber salido bien

sumatoriaDoble :: Integer-> Integer-> Integer 
sumatoriaDoble n m | n == 1 = m
                   | otherwise = f2' n m + sumatoriaDoble (n-1) m

f2' :: Integer -> Integer -> Integer
f2' n m | n == 1 = m
        | otherwise = m^n + f2' (n-1) m

--14)

sumaPotencias :: Integer -> Integer -> Integer -> Integer
sumaPotencias q n m | n == 1 && m == 1 = q^2
                    | otherwise =  q^(sumatoria n + sumatoria m)

sumatoria :: Integer -> Integer
sumatoria x | x == 1 = 1
            | otherwise = x + sumatoria (x-1)

--15)
sumaRacionales :: Integer -> Integer -> Float
sumaRacionales p q | p == 1 = sumaRacionalesAux 1 q
                   | otherwise = sumaRacionalesAux p q + sumaRacionales p (q-1)

sumaRacionalesAux :: Float -> Float -> Float
sumaRacionalesAux p q | q == 1 = p
                      | otherwise = p/q + sumaRacionalesAux (p-1) q

sumatoria' :: Float -> Float
sumatoria' x | x == 1 = 1
             | otherwise = x + sumatoria' (x-1)

-- sumaRacionalesAux :: Integer -> Integer -> Integer
-- -sumaRacionalesAux p q | 