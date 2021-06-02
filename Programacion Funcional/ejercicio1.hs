descuento::(Float,Float)->Float

descuento (pre,des)=pre-pre*des/100

iva::(Float,Float)->Float
iva (pre,por)= pre+pre*por/100
--iva x= (fst x)-(fst x)*(snd x)/100

--diccionario::x->[(Float,Float)]->Float

diccionario funcion n= sum(map funcion n)