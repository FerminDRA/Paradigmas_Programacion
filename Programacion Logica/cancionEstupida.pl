cancionestupida(0):-nl,write('Como que ya no hay chevecha,-hic- mevo a domi....').
cancionestupida(N):-N>1,nl,write(N),write('Botellas de cerveza en el suelo'),nl,write(N),write('Botellas de cerveza'),nl,write('Cojo una y me la bebo'),nl,A is N-1,cancionestupida(A).
cancionestupida(N):-N=1,nl,write(N),write('Boteshita de shevesha en el suelo'),nl,write(N),write('Botesha de shevesha'),nl,write('La gojo y me la bobho'),nl,A is N-1,cancionestupida(A).

