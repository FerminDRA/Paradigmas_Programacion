calificaciones::Float->String

calificaciones n
    |n<5 && n>=0 = "SS"
    |n<7 &&n>=5 = "AP"
    |n<9 &&n>=7 = "NT"
    |n<10 &&n>=9 = "SB"
    |otherwise = "MH"

notas::[Float]->[String]
notas n= map calificaciones n