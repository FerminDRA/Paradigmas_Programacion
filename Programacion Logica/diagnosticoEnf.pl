enfermo_de(manuel,gripe).
tiene_sintoma(alicia,cansancio).
sintoma_de(fiebre,gripe).
sintoma_de(tos,gripe).
sintoma_de(congestion nasal,gripe).
sintoma_de(estornudos,gripe).
sintoma_de(cansancio,anemia).
sintoma_de(falta de aire,covid).
sintoma_de(fatiga,influenza).
sintoma_de(dolor de cabeza,influenza).
elimina(vitaminas,cansancio).
elimina(aspirinas,fiebre).
elimina(jarabe,tos).
recetar_a(X,Y):-enfermo_de(Y,A),alivia(X,A).
alivia(X,Y):-elimina(X,A),sintoma_de(A,Y).

enfermos_de(X,Y):-tiene_sintoma(X,Z),sintoma_de(Z,Y).



