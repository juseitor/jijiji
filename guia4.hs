fibonacci :: Integer -> Integer
fibonacci n | n == 0 = 0
            | n == 1 = 1
            | otherwise = fibonacci(n-1) + fibonacci(n-2)

parteEnteraG4 :: Float -> Integer
parteEnteraG4 x | x > 0 && x < 1 = 0
                | x >= 1 = parteEnteraG4 (x-1) + 1

sumaImpares :: Integer -> Integer
sumaImpares x | x == 1 = 1
              | x == 2 = 1 + 3  
              | x > 2 = sumaImpares (x-1) + x + 2
