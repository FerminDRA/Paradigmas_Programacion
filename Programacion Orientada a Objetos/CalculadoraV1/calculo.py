class calculo(object):

    def __init__(self,nu1,nu2):
        self.n1=nu1
        self.n2=nu2

    def suma(self):
        print("\nLa suma de los dos numeros es: ",self.n1,"+",self.n2,"=",self.n1+self.n2)

    def resta(self):
        print("La resta de los dos numeros es: ",self.n1,"-",self.n2,"=",self.n1-self.n2)

    def multi(self):
        print("La multiplicacion de los dos numeros es: ",self.n1,"*",self.n2,"=",self.n1*self.n2)
    def divicion(self):
        if(self.n2!=0):
            print("La divicion de los dos numeros es: ",self.n1,"/",self.n2,"=",self.n1/self.n2,"\n")
        else:
            print("La divicion de los dos numeros es: ",self.n1,"/",self.n2,"=INDEFINIDO\nDivicion entre cero!!!\n")