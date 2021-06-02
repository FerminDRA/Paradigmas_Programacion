import Data.Char

mayuscula :: String -> String
mayuscula []= []
mayuscula n= map toUpper n

calificaciones::Float->String

calificaciones n
    |n<5 && n>0 = "SS"
    |n<7 &&n>4 = "AP"
    |n<9 &&n>6 = "NT"
    |n<10 &&n>8 = "SB"
    |otherwise = "MH"

aprobado::(String,String)->Bool
aprobado x= (snd x)/="SS"

notas::[(String,Float)]->[(String,String)]
notas x= filter aprobado (zip(map mayuscula (map fst x))(map calificaciones (map snd x)))