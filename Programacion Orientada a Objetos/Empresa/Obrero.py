class Obrero(Empleado):

    def __init__(self,nom,ape,edad,suel,asis):
        Empleado.__init__(self,nom,ape,edad,suel)
        self.asistencia=Asistencia(asis)


    def Asistencia(asi):

        if(res=="S" or res=="s"):
            self.sueldo=sueldo+(sueldo*0.1)
            return "Trabajando"

        else:
            self.sueldo=sueldo-(sueldo*0.1)
            return "No asistio"