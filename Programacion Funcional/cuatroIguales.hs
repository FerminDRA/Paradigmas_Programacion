tresIguales::Int->Int->Int->Bool

tresIguales x y z= x==y&&y==z

cuatroIguales::Int->Int->Int->Int->Bool

cuatroIguales w x y z= w==x && tresIguales x y z