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

--11)

eAprox :: Integer -> Float
eAprox n | n == 0 = 1
         | otherwise = eAproxAux (fromInteger n) + eAprox (n-1)

eAproxAux :: Float -> Float
eAproxAux n = (1/factorial n)

factorial :: Float -> Float
factorial n | n == 1 = n
              | otherwise = n * factorial(n-1)

--12)

terminoN :: Float -> Float
terminoN n | n == 1 = 2
           | otherwise = 2 + (1 / terminoN (n-1))   

raizDe2Aprox :: Integer -> Float
raizDe2Aprox n = -1 + terminoN(fromIntegral(n))

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
sumaRacionales p q | p == 1 = sumaRacionalesAux (1.0) (fromInteger q)
                   | otherwise = sumaRacionalesAux (fromInteger p) (fromInteger q) + sumaRacionales (p-1) q

sumaRacionalesAux :: Float -> Float -> Float
sumaRacionalesAux p q | q == 1 = p
                      | otherwise = p/q + sumaRacionalesAux p (q-1)

-- sumaRacionalesAux :: Integer -> Integer -> Integer
-- -sumaRacionalesAux p q | 

--16)
--a)

menorDivisor :: Integer -> Integer
menorDivisor n = menorDivisorDesde n 2

menorDivisorDesde :: Integer -> Integer -> Integer
menorDivisorDesde n m | mod n m == 0 = m
                      | otherwise = menorDivisorDesde n (m+1)

--b)

esPrimo :: Integer -> Bool
esPrimo n | n == 1 = False
          | menorDivisorDesde n 2 == n = True
          | otherwise = False     

--c)

sonCoprimos :: Integer -> Integer -> Bool
sonCoprimos n m | (n == 1 && m == 1) = True
                | menorDivisorDesde n 2 == menorDivisorDesde m 2 = False
                | otherwise = True

--d) 

nEsimoPrimo :: Integer -> Integer
nEsimoPrimo n | n == 1 = 2
              | otherwise = siguientePrimo (nEsimoPrimo (n-1) + 1)

esPrimo2 :: Integer -> Bool
esPrimo2 n = cantidadDeDivisoresHasta n n == 2 

cantidadDeDivisoresHasta :: Integer -> Integer -> Integer
cantidadDeDivisoresHasta n m | m == 1 = 1
                             | mod n m == 0 = 1 + cantidadDeDivisoresHasta n (m-1)
                             | otherwise = cantidadDeDivisoresHasta n (m-1)

siguientePrimo :: Integer -> Integer
siguientePrimo n | esPrimo2 n = n
                 | otherwise = siguientePrimo (n+1)
              
--17)

--fibonacci :: Integer -> Integer
-- fibonacci n | n == 0 = 0
--             | n == 1 = 1
--             | otherwise = fibonacci(n-1) + fibonacci(n-2)

esFibonacci :: Integer -> Bool 
esFibonacci n = auxEsFib n 0

auxEsFib :: Integer -> Integer -> Bool
auxEsFib n i | fibonacci (i) > n = False
             | fibonacci (i) == n = True
             | otherwise = auxEsFib n (i+1)

--18) Lo copie y solo lo entendì una vez hecho. No lo hubiese podido hacer solo

mayorDigitoPar :: Integer -> Integer
mayorDigitoPar n | todosDigitosImpares n == True = -1
                 | otherwise = mayorDigitoParAux n 1 (-1)

mayorDigitoParAux :: Integer -> Integer -> Integer -> Integer
mayorDigitoParAux n i m | n < 10 && mod n 2 == 1 = -1
                        | i == cantDigitos n + 1 = m 
                        | esPar (iesimoDigito n i) == True = mayorDigitoParAux n (i+1) (max (iesimoDigito n i) m)
                        | otherwise = mayorDigitoParAux n (i+1) m

esPar :: Integer -> Bool
esPar n | mod n 2 == 0 = True
        | otherwise = False

todosDigitosImpares :: Integer -> Bool
todosDigitosImpares n | mod n 2 == 0 = False
                      | mod n 2 == 1 && n < 10 = True
                      | mod n 2 == 1 = todosDigitosImpares(sacarUltimo n)

--19)

esSumaInicialDePrimos :: Integer -> Bool
esSumaInicialDePrimos n | n == 0 = False
                        | n == esSIDPAux n 2 0 = True
                        | otherwise = False

esSIDPAux :: Integer -> Integer -> Integer -> Integer
esSIDPAux n m p | n <= p = p
                | esPrimo m == True = esSIDPAux n (m+1) (p+m)
                | otherwise = esSIDPAux n (m+1) p
