-- relacionesValidas :: [(String,String)] -> Bool
-- relacionesValidas [] = True
-- relacionesValidas (x:[]) = True
-- relacionesValidas (x:y:xs) | x == y = False
--                            | otherwise = relacionesValidas (x:xs) && relacionesValidas (y:xs) 

relacionesValidas :: [(String,String)] -> Bool
relacionesValidas [] = True
relacionesValidas ((x,y):rs) = cadaRelValida && noHayRelRep && relacionesValidas rs
                            where
                                cadaRelValida = x /= y
                                noHayRelRep = not (pertenece (x,y) rs) && not (pertenece (y,x) rs)

pertenece :: (Eq t) => t -> [t] -> Bool
pertenece - [] = False
pertenece x (y:xs) | x == y = True
                   | otherwise = pertenece x xs

--2.

personas :: [(String,String)] -> [String]
personas rs = sacarRepetidos(todasLasPersonas rs)

todasLasPersonas :: [(String,String)] -> [String]
todasLasPersonas [] = []
todasLasPersonas ((c1,c2):rs) = c1 : c2 : todasLasPersonas rs

sacarRepetidos :: [String] -> [String]
sacarRepetidos [] = []
sacarRepetidos (x:xs) | pertenece x xs = pasoRecursivo
                      | otherwise = x : pasoRecursivo
                        where pasoRecursivo = sacarRepetidos xs 

--3.

amigosDe :: String -> [(String,String)] -> [String]
amigosDe _ [] = []
amigosDe x ((c1,c2):rs) | x == c1 || x == c2 = c1 : c2 : amigosDe x rs
                        | otherwise = amigosDe x rs

amigosDeClase :: String -> [(String,String)] -> [String]
amigosDeClase _ [] = []
amigosDeClase p ((p1,p2):rs)  | (p == p1) = p2 : pasoRecursivo
                         | (p == p2) = p1 : pasoRecursivo
                         | otherwise = pasoRecursivo
                         where pasoRecursivo = amigosDe p rs

--4.

personaConMasAmigos :: [(String,String)] -> String
personaConMasAmigos rs = maximo listaPersonas cantAmigosPersonas
                    where
                        listaPersonas = personas rs
                        cantAmigosPersonas = cantidadDeAmigos listaPersonas rs 

cantidadDeAmigos :: [String] -> [(String,String)] -> [Int]
cantidadDeAmigos [] _ = []
cantidadDeAmigos (p:ps) rs = (cantidadDeAmigosDe p rs) : (cantidadDeAmigos ps rs)

cantidadDeAmigosDe :: String -> [(String,String)] -> Int
cantidadDeAmigosDe p rs = length (amigosDe p rs)

maximo :: [String] -> [Int] -> String
maximo [p] _ = p
maximo (p0:p1:ps) (c0,c1,cs) | c0 > c1 = maximo (p0:ps) (c0:cs)
                             | otherwise = maximo (p1:ps) (c1:cs)

cantidadApariciones :: [(String,String)] -> Integer
cantidadApariciones ((c1,c2):rs) | c1 = 1 + cantidadApariciones rs
                                 | c2 = 1 + cantidadApariciones rs
                                  | otherwise = cantidadApariciones rs
