class Linea():

    def __init__(self):
        self.puntoA=[0,0]
        self.puntoB=[0,0]

    def __init__(self,a,b):
        self.puntoA=a
        self.puntoB=b

    def mueveDerecha(self,n):
        l1=self.puntoA[0]+n
        self.puntoA[0]=l1

        l2=self.puntoB[0]+n
        self.puntoB[0]=l2

    def mueveIzquierda(self,n):
        l1=self.puntoA[0]-n
        self.puntoA[0]=l1

        l2=self.puntoB[0]-n
        self.puntoB[0]=l2

    def mueveArriba(self,n):
        l1=self.puntoA[1]+n
        self.puntoA[1]=l1

        l2=self.puntoB[1]+n
        self.puntoB[1]=l2

    def mueveAbajo(self,n):
        l1=self.puntoA[1]-n
        self.puntoA[1]=l1

        l2=self.puntoB[1]-n
        self.puntoB[1]=l2

    def mostrarPuntos(self):
        print("La ubicacion de los puntos son",self.puntoA,"--",self.puntoB)