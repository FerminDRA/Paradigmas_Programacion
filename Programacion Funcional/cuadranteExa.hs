cuadrante::(Int,Int)->Int

cuadrante n
    |fst n>0 && snd n>0= 1
    |fst n<0 && snd n>0= 2
    |fst n<0 && snd n<0= 3
    |fst n>0 && snd n<0= 4
    |otherwise = 0