mayorRectangulo::(Int,Int)->(Int,Int)->(Int,Int)

mayorRectangulo a b
    |(fst a)*(snd a) >= (fst b)*(snd b)= a
    |otherwise = b