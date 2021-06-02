from Linea import *

print("Escribe las coordenadas la linea en el punto 1:")
x=int(input("Eje de las x: "))
y=int(input("Eje de las y: "))
lin=[x,y]

print("\nEscribe las coordenadas la linea en el punto 2:")
x2=int(input("Eje de las x: "))
y2=int(input("Eje de las y: "))
lin2=[x2,y2]

l1=Linea(lin,lin2)

res="s"
while (res=="S" or res=="s"):
    op=int(input("\nSelecciona la operacion a realizar a la linea:\n1)Mover a la izquierda\n2)Mover a la derecha\n3)Mover arriba\n4)Mover abajo\n"))
    if(op==1):
        m=int(input("\nNumero de puntos a mover: "))
        l1.mueveIzquierda(m)
        l1.mostrarPuntos()
    elif(op==2):
        m=int(input("\nNumero de puntos a mover: "))
        l1.mueveDerecha(m)
        l1.mostrarPuntos()
    elif(op==3):
        m=int(input("\nNumero de puntos a mover: "))
        l1.mueveArriba(m)
        l1.mostrarPuntos()
    elif(op==4):
        m=int(input("\nNumero de puntos a mover: "))
        l1.mueveAbajo(m)
        l1.mostrarPuntos()
    
    res=input(("\nDeseas realizar otra operacion?\nS/N\n"))

l2=Linea()
l2.mostrarPuntos()