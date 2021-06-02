class Administrador(Empleado):

    def __init__(self,nom,ape,edad,suel,venta):
        Empleado.__init__(self,nom,ape,edad,suel)
        self.ventas=venta
        self.Bono=BonoM(ventas)

    def BonoM(vent):
        if(self.ventas>=100000):
            return ventas*0.1

        else:
            return 0