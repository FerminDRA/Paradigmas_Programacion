class Persona(object):

	def __init__(self,nombre,edad):
		self.nom=nombre
		self.eda=edad


	def mostrar(self):
		print("\nSu nombre es: ",self.nom,"\nSu edad es: ",self.eda)


class Empleado(Persona):

	def __init__(self,nombre,edad,SueldoBruto):
		
		Persona.__init__(self,nombre,edad)
		self.SueldoBruto=SueldoBruto


	def mostrar(self):
		print("\nSu nombre es: ",self.nom,"\nSu edad es: ",self.eda,"\nSueldo: $",self.SueldoBruto)

	def Calculo_Salario_Neto(self):
		return ("\nCalculo de sueldo es: ",self.SueldoBruto)

class Cliente(Persona):

	def __init__(self,nombre,edad,nomEmp,telContacto):

		Persona.__init__(self,nombre,edad)
		self.nombreEmpresa=nomEmp
		self.telefonoContacto=telContacto

	def mostrar(self):

		print("\nSu nombre es: ",self.nom,"\nSu edad es: ",self.eda
			,"\nNombre de la empresa: ",self.nombreEmpresa,"\nTelefono: ",self.telefonoContacto)

class Empresa(object):

	def __init__(self,nombre):

		self.nombreEmp=nombre
		self.emp1=Empleado("Juan",32,3500)
		self.emp2=Empleado("Pedro",23,5000)
		self.cli1=Cliente("Antonio",22,"Desarrollo",9876543210)
		self.cli2=Cliente("Manuel",35,"Progreso",1234567890)

	def mostrar(self):

		print("\nEmpresa: ",self.nombreEmp)
		self.emp1.mostrar()
		self.emp2.mostrar()
		self.cli1.mostrar()
		self.cli2.mostrar()


class Directivo(Empleado):

	def __init__(self,nombre,edad,SueldoBruto,cat):

		Empleado.__init__(self,nombre,edad,SueldoBruto)
		self.categoria=cat

	def mostrar(self):

		print("Su nombre es: ",self.nom,"\nSu edad es: ",self.eda,"\nSueldo: ",self.SueldoBruto
			,"\nCategoria: ",self.categoria)


def main():
	p1= Persona("Maria",17)
	p1.mostrar()

	emplea=Empleado("Marco",33,4230)
	emplea.mostrar()

	emp1=Empresa("Pegaso")
	emp1.mostrar()

	emp2=Empresa("Elemental")
	emp2.mostrar()

	dir1=Directivo("Luis",32,5500,"Comercio")
	dir1.mostrar()

main()