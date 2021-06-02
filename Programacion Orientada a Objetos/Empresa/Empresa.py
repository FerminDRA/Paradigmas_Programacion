from Empleado import *

class Empresa():

    def __init__(self,nom):
        self.nombreEmp=nom
        self.emp=[]

    def AgregarEmpleados(self):
        #emp=[]
        self.emp.append(Obrero("Fermin","Rosario","55",900,"s"))
        self.emp.append(Intendente("Fermin","Rosario","55",900,"n","0"))
        self.emp.append(Administrador("Fermin","Rosario","55",900,150000))
        res="S"
        while(res=="S" or res=="s"):
            opc=input(("\nSelecciona el tipo de empleado que deseas agregar:\n1)Obrero\n2)Administrador\n3)Intendente\n"))

            if(opc!="1" and opc!="2" and opc!="3"):
                print("Opcion incorrecta\nVuelve a intentar")
            
            else:
                nom=input(("\nEscribe el nombre del empleado: "))
                ape=input(("\nEscribe el apellido del empleado: "))
                edad=input(("\nEscribe la edad del empleado: "))
                suel=int(input("\nEscribe el sueldo del empleado: $ "))
                if(opc=="1"):
                    asis=input(("El elmpeado asistio a trabajar\nS/N\n"))

                    self.emp.append(Obrero(nom,ape,edad,suel,asis))
                elif(opc=="2"):
                    vent=int(input("Ingresa la cantidad de ventas que ha hecho el empleado: $ "))

                    self.emp.append(Administrador(nom,ape,edad,suel,vent))
                elif(opc=="3"):
                    asis=input(("El empleado asistio a trabajar\nS/N\n"))
                    if(asis=="S"or asis=="s"):
                        tur=input(("Escribe el numero de turnos que trabajo:\nDe 1 a 3 turnos\n"))

                    else:
                        tur="0"

                    self.emp.append(Intendente(nom,ape,edad,suel,asis,tur))

            res=input(("\nDeseas agregar otro empleado?\nS/N\n"))

        #res=input(("Deseas agregar otro empleado?\nS/N"))

    def tabla(self,pal):
        if(pal.__class__.__name__!="str"):
            pal=str(pal)
        for i in range(len(pal),14):
            pal=pal+" "
        return pal

    
    def mostrarEmpleados(self):
        res="s"
        while(res=="S" or res=="s"):
            opc=input(("\nSelecciona el tipo de empleados que deseas mostrar:\n1)Obrero\n2)Administrador\n3)Intendente\n4)Todos\n"))
            if(opc!="1" and opc!="2" and opc!="3" and opc!="4"):
                print("Opcion incorrecta\nVuelve a intentar")
            
            else:
                if(opc=="1"):
                    print("Lista de Obreros")
                    print("*******************************************************************************************************")
                    print("*Nombre          *Apellido        *Edad            *Sueldo          *Asistencia      *Bono            *")
                    print("*******************************************************************************************************")
                    for i in range(0,len(self.emp)):
                        if(self.emp[i].__class__.__name__=="Obrero"):
                            print("*",self.tabla(self.emp[i].getNombre()),"*",self.tabla(self.emp[i].getApellido()),"*"
                            ,self.tabla(self.emp[i].getEdad()),"*",self.tabla(self.emp[i].getSueldo()),"*",self.tabla(self.emp[i].getAsistencia()),"*",self.tabla(self.emp[i].getBono()),"*")
                        
                            print("*******************************************************************************************************")

                if(opc=="2"):
                    print("Lista de Administradores")
                    print("*******************************************************************************************************")
                    print("*Nombre          *Apellido        *Edad            *Sueldo          *Venta           *Bono por Venta  *")
                    print("*******************************************************************************************************")
                    for i in range(0,len(self.emp)):
                        if(self.emp[i].__class__.__name__=="Administrador"):
                            print("*",self.tabla(self.emp[i].getNombre()),"*",self.tabla(self.emp[i].getApellido()),"*"
                            ,self.tabla(self.emp[i].getEdad()),"*",self.tabla(self.emp[i].getSueldo()),"*",self.tabla(self.emp[i].getVentas())
                            ,"*",self.tabla(self.emp[i].getBono()),"*")
                            
                            print("*******************************************************************************************************")

                if(opc=="3"):
                    print("Lista de Intendentes")
                    print("************************************************************************************************************************")
                    print("*Nombre          *Apellido        *Edad            *Sueldo          *Asistencia      *Turnos          *Bono            *")
                    print("************************************************************************************************************************")
                    for i in range(0,len(self.emp)):
                        if(self.emp[i].__class__.__name__=="Intendente"):
                            print("*",self.tabla(self.emp[i].getNombre()),"*",self.tabla(self.emp[i].getApellido()),"*"
                            ,self.tabla(self.emp[i].getEdad()),"*",self.tabla(self.emp[i].getSueldo()),"*"
                            ,self.tabla(self.emp[i].getAsistencia()),"*",self.tabla(self.emp[i].getTurno()),"*",self.tabla(self.emp[i].getBono()),"*")
                            
                            print("************************************************************************************************************************")

                if(opc=="4"):
                    print("Lista de Empleados")
                    print("**********************************************************************************************************************************************************")
                    print("*Tipo de Empleado*Nombre          *Apellido        *Edad            *Sueldo          *Asistencia      *Turnos          *Venta           *Bono            *")
                    print("**********************************************************************************************************************************************************")
                    for i in range(0,len(self.emp)):
                        if(self.emp[i].__class__.__name__=="Obrero"):
                            print("*",self.tabla(self.emp[i].__class__.__name__),"*",self.tabla(self.emp[i].getNombre()),"*",self.tabla(self.emp[i].getApellido()),"*"
                            ,self.tabla(self.emp[i].getEdad()),"*",self.tabla(self.emp[i].getSueldo()),"*"
                            ,self.tabla(self.emp[i].getAsistencia()),"*",self.tabla("Null"),"*",self.tabla("Null"),"*",self.tabla(self.emp[i].getBono()),"*")

                            print("**********************************************************************************************************************************************************")
                        
                        if(self.emp[i].__class__.__name__=="Administrador"):
                            print("*",self.tabla(self.emp[i].__class__.__name__),"*",self.tabla(self.emp[i].getNombre()),"*",self.tabla(self.emp[i].getApellido()),"*"
                            ,self.tabla(self.emp[i].getEdad()),"*",self.tabla(self.emp[i].getSueldo()),"*",self.tabla("Null"),"*",self.tabla("Null"),"*",self.tabla(self.emp[i].getVentas())
                            ,"*",self.tabla(self.emp[i].getBono()),"*")

                            print("**********************************************************************************************************************************************************")
                        
                        if(self.emp[i].__class__.__name__=="Intendente"):
                            print("*",self.tabla(self.emp[i].__class__.__name__),"*",self.tabla(self.emp[i].getNombre()),"*",self.tabla(self.emp[i].getApellido()),"*"
                            ,self.tabla(self.emp[i].getEdad()),"*",self.tabla(self.emp[i].getSueldo()),"*"
                            ,self.tabla(self.emp[i].getAsistencia()),"*",self.tabla(self.emp[i].getTurno()),"*",self.tabla("Null"),"*",self.tabla(self.emp[i].getBono()),"*")
                        
                            print("**********************************************************************************************************************************************************")
            res=input(("\nMostrar otra tabla?\nS/N\n"))            