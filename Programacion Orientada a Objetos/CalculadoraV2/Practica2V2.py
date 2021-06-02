from calculadora import *

num=[]
num.append(int(input("Escribe un numero: ")))
num.append(int(input("Escribe otro numero: ")))
res=input(("\nDeseas agregar otro numero?\nS/N\n"))

if(res=="S" or res=="s"):
    while (res=="S" or res=="s"):
        num.append(int(input("Escribe otro numero: ")))
        res=input(("\nDeseas agregar otro numero?\nS/N\n"))
    
    c= calculadora(num)
    c.sumaM()
    c.restaM()
    c.multiM()
else:
    c= calculadora(num)
    c.suma()
    c.resta()
    c.multi()
    c.div()
    c.modulo()
