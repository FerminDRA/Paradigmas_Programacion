class calculadora(object):

    def __init__(self,n):
        self.numeros=n

    def suma(self):
        print("\nLa suma de los dos numeros es: ",self.numeros[0],"+",self.numeros[1],"=",self.numeros[0]+self.numeros[1])

    def resta(self):
        print("La resta de los dos numeros es: ",self.numeros[0],"-",self.numeros[1],"=",self.numeros[0]-self.numeros[1])

    def multi(self):
        print("La multiplicacion de los dos numeros es: ",self.numeros[0],"*",self.numeros[1],"=",self.numeros[0]*self.numeros[1])

    def div(self):
        if(self.numeros[1]!=0):
            print("La divicion de los dos numeros es: ",self.numeros[0],"/",self.numeros[1],"=",self.numeros[0]/self.numeros[1])
        else:
            print("La divicion de los dos numeros es: ",self.numeros[0],"/",self.numeros[1],"= INDEFINIDO\nDivicion entre cero!!!")

    def modulo(self):
        print("El modulo de",self.numeros[0],"/",self.numeros[1],"es: ",self.numeros[0]%self.numeros[1])

    def sumaM(self):
        sum=0
        for i in range(0,len(self.numeros)):
            sum=sum+self.numeros[i]

        print("La suma de los numeros : ",self.numeros,"=",sum)

    def restaM(self):
        res=self.numeros[0]
        for i in range(1,len(self.numeros)):
            res=res-self.numeros[i]

        print("La resta de los numeros",self.numeros,"=",res)

    def multiM(self):
        mul=self.numeros[0]
        for i in range(1,len(self.numeros)):
            mul=mul*self.numeros[i]

        print("La multiplicacion de los numeros: ",self.numeros,"=",mul)