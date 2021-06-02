class Empleado():

    def __init__(self,nom,ape,edad,suel):
        self.nombre=nom
        self.apellido=ape
        self.edad=edad
        self.sueldo=suel

    def getNombre(self):
        return self.nombre

    def getApellido(self):
        return self.apellido

    def getEdad(self):
        return self.edad

    def getSueldo(self):
        return self.sueldo

class Obrero(Empleado):

    def __init__(self,nom,ape,edad,suel,asis):
        Empleado.__init__(self,nom,ape,edad,suel)
        #self.asistencia=Asistencia(asis)
        self.Asistencia(asis)

    def getAsistencia(self):
        return self.asistencia

    def getBono(self):
        return self.Bono

    def Asistencia(self,asi):
        res=asi
        if(res=="S" or res=="s"):
            self.sueldo=self.sueldo+(self.sueldo*0.1)
            self.asistencia="Trabajando"
            self.Bono="Obtenido"

        else:
            self.sueldo=self.sueldo-(self.sueldo*0.1)
            self.asistencia="No asistio"
            self.Bono="No obtenido"

class Administrador(Empleado):

    def __init__(self,nom,ape,edad,suel,venta):
        Empleado.__init__(self,nom,ape,edad,suel)
        self.ventas=venta
        self.BonoM(self.ventas)

    def getVentas(self):
        return self.ventas

    def getBono(self):
        return self.Bono

    def BonoM(self,vent):
        if(vent>=100000):
            self.Bono=vent*0.1

        else:
            self.Bono=0

class Intendente(Empleado):

    def __init__(self,nom,ape,edad,suel,asis,turn):
        Empleado.__init__(self,nom,ape,edad,suel)
        #self.asistencia=Asistencia(asis)
        self.Asistencia(asis)
        self.Turno=turn

    def getAsistencia(self):
        return self.asistencia

    def getTurno(self):
        return self.Turno
    
    def getBono(self):
        return self.Bono


    def Asistencia(self,asi):

        res=asi
        if(res=="S" or res=="s"):
            self.sueldo=self.sueldo+(self.sueldo*0.1)
            self.asistencia="Trabajando"
            self.Bono="Obtenido"

        else:
            self.sueldo=self.sueldo-(self.sueldo*0.1)
            self.asistencia="No asistio"
            self.Bono="No obtenido"


