doubleMe x = x + x

sumatoria 1 = f 1
sumatoria n = f n + sumatoria (n-1)

sumaPotencias 1 m = sumaPotenciasIFijo 1 m 
sumaPotencias n m = sumaPotenciasIFijo n m + sumaPotencias (n-1) m 

sumaPotenciasIFijo i 1 = i
sumaPotenciasIFijo i m = i^m + sumaPotenciasIFijo i (m-1)

menorDivisor :: Integer -> Integer
menorDivisor n = menorDivisorDesde n 2

menorDivisorDesde :: Integer -> Integer -> Integer
menorDivisorDesde n m | mod n m == 0 = m
                      | otherwise menorDivisorDesde n (m+1)

cantidadDeDivisoresHasta :: Integer -> Integer -> Integer
cantidadDeDivisoresHasta n 1 = 1
cantidadDeDivisoresHasta n d | mod n d == 0 = 1 + cantidadDeDivisoresHasta n (d-1)
                             | otherwise = cantidadDeDivisoresHasta n (d-1)

esPrimo n = cantidadDeDivisoresHasta n n == 2

esPrimo2 1 = False
esPrimo2 n = menorDivisor n == n

siguientePrimo n | esPrimo n = n
                 | otherwise = siguientePrimo (n+1)

enesimoPrimo 1 = 2
enesimoPrimo n = siguientePrimo (enesimoPrimo (n-1) + 1)

sumaKPrimos 1 = 2
sumaKPrimos k = enesimoPrimo k + sumaKPrimos (k-1)

esSumaDePrimerosKPrimos :: Int -> Int -> Bool
esSumaDePrimerosKPrimos k n | sumaKPrimos k == n = True
                            | sumaKPrimos k > n = False
                            | otherwise = esSumaDePrimerosKPrimos (k+1) n

esSumaInicialDePrimos n = esSumaDePrimerosKPrimos 1 n
