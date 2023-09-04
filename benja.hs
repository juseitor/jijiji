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
