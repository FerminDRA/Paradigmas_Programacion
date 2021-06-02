animal(perro,es_cuadrupedo,tiene_cola,ladra,es_mamifero).
animal(pajaro_carpintero,es_rojo,vuela,tiene_pico,oviparo).
animal(canguro,es_marsupial,salta,es_grande,es_territorial).
animal(pinguino,no_vuela,nada,habitad_frio,oviparo).
animal(elefante,es_gris,es_grande,tiene_colmillos,grandes_orejas).
animal(gato,es_pequeño,maulla,tiene_garras,tiene_cola).
animal(cocodrilo,sangre_fria,es_grande,reptil,es_carnivoro).
animal(vaca,es_grande,es_herbivoro,tiene_cuernos,da_leche).
animal(oveja,es_herbivoro,mucho_pelo,come_pasto,es_suave).
animal(caballo,es_grande,es_rapido,es_herbivoro,corre).

aleatorio():-random_between(1,10,X),selecion(X).
selecion(X):-X==1,preguntas(perro);X==2,preguntas(pajaro_carpintero);X==3,preguntas(canguro);X==4,preguntas(pinguino);X==5,preguntas(elefante);X==6,preguntas(gato);X==7,preguntas(cocodrilo);X==8,preguntas(vaca);X==9,preguntas(oveja);X==10,preguntas(caballo).

adivina(A,Z):-animal(A,Z,_,_,_),acierto(A);animal(A,_,Z,_,_),acierto(A);animal(A,_,_,Z,_),acierto(A);animal(A,_,_,_,Z),acierto(A);nl,write('El animal no tiene esa caracteristica'),preguntas(A).
acierto(A):-nl,write('El animal si tiene esa caracteristica'),nl,write('Ya sabes cual es? s/n'),read(Resp),Resp==s,respuesta(A);preguntas(A).
respuesta(X):-nl,write('Escribe cual animal crees que es'),read(Ani),Ani==X,nl,write('Es correcto el animal en el que pense fue: '),write(X),reinicio();write('Incorrecto, vuelve a intentar'),preguntas(X).

reinicio():-nl,write('Deseas volver a jugar? s/n'),read(Re),Re==s,aleatorio();nl,write('Adios espero haya sido entretenido!!!').

start():-nl,write('Escribe caracteristicas que pueda tener el animal que estoy pensando'),aleatorio().
preguntas(A):-nl,write('Escribe una caracteristica'),nl,read(Res),adivina(A,Res).
