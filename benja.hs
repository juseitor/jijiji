doubleMe x = x + x

algunoEs0::Integer->Integer->Bool
algunoEs0 a b | a == 0 = True
              | b == 0 = True
              | otherwise = False

algunoEs0x::Rational->Rational->Bool
algunoEs0x 0 a = True
algunoEs0x b 0 = True
algunoEs0x a b = False

ambosSon0::Rational->Rational->Bool
ambosSon0 a b | a == 0 && b ==0 = True
              | otherwise = False

todoMenor::(Float , Float)->(Float , Float)->Bool
todoMenor (x,y) (v,w) | x<v && y<w = True
                      | otherwise = False  

todoMenorx::(Float , Float)->(Float , Float)->Bool
todoMenorx t1 t2 | fst t1 < fst t2 && snd t2 < snd t2 = True
                 | otherwise = False

posPrimerPar::(Integer , Integer , Integer)->Integer
posPrimerPar (x,y,z) | mod x 2 == 0 = 1
                     | mod y 2 == 0 = 2
                     | mod z 2 == 0 = 3
                     | otherwise = 4

ambosSon0x::Integer->Integer->Bool
ambosSon0x 0 0 = True
ambosSon0x a b = False

mismoIntervalo::Integer->Integer->Bool
mismoIntervalo a b | a<=3 && b<=3 = True
                   | a>3 && a<=7 && b>3 && b<=7 = True
                   | a>7 && b>7 = True
                   | otherwise = False

sumaDistintos::Integer->Integer->Integer->Integer
sumaDistintos a b c | a == b = a + c
                    | b == c = a + b
                    | otherwise = a + b + c

esMultiploDe::Integer->Integer->Bool
esMultiploDe a b | mod a b == 0 = True
                 | otherwise = False

digitoUnidades::Integer->Integer
digitoUnidades a | a < 10 = a
                 | otherwise = mod a 10

digitoDecenas::Integer->Integer
digitoDecenas a | a<10 = 0
                | a >= 10 = div (mod a 100) 10

ultimoDigito :: Integer -> Integer
ultimoDigito n = mod n 10

sacarUltimo :: Integer -> Integer
sacarUltimo n = div n 10

tDI::Integer->Bool
tDI n | n < 10 = True
      | mod n 10 == n = True
  
parteEntera:: Float -> Integer
parteEntera x | 0 <= x && x < 1 = 0
              | otherwise = 1 + parteEntera (x-1)  

prodInt :: (Float , Float) -> (Float , Float) -> Float
prodInt t1 t2 = (fst t1 * fst t2) + (snd t1 * snd t2)

distanciaPuntos :: (Float , Float) -> (Float , Float) -> Float
distanciaPuntos t1 t2 = sqrt ((fst t1 - fst t2) * (fst t1 - fst t2) + (snd t1 - snd t2) * (snd t1 - snd t2))
 
sumaTerna :: (Float , Float , Float) -> Float
sumaTerna (x,y,z) = x + y + z

sumarSoloMultiplos :: (Integer , Integer , Integer) -> Integer -> Integer
sumarSoloMultiplos (x,y,z) n | mod x n == 0 && mod y n == 0 && mod z n == 0 = x + y + z
                             | mod x n == 0 && mod y n == 0 = x + y
                             | mod x n == 0 && mod z n == 0 = x + z
                             | mod y n == 0 && mod z n == 0 = y + z
                             | mod x n == 0 = x
                             | mod y n == 0 = y
                             | mod z n == 0 = z