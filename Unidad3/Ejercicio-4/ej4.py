from Lista import Lista
from os import path
import csv

class Designacion:
	__año: int
	__materia: str
	__tipoCargo: str
	__esMujer: str

	def __init__(self, año, tipoCargo, materia, genero):
		self.__año = int(año)
		self.__tipoCargo = tipoCargo
		self.__materia = materia
		self.__esMujer = genero == 'Femenino'

	def getAño(self):
		return self.__año

	def getMateria(self):
		return self.__materia

	def getTipoCargo(self):
		return self.__tipoCargo

	def esMujer(self):
		return self.__esMujer

class ManejadorDesignaciones:
	__designaciones: Lista

	def __init__(self, tamaño):
		self.__designaciones = Lista(tamaño)

	def incisoC(self, cargo):
		if self.__designaciones.estaVacia():
			print('No hay datos cargados')
		else:
			año = self.__designaciones.primerElemento().getAño() # type: ignore
			cantidad = 0
			for designacion in self.__designaciones:
				if designacion.getAño() != año:
					print(f'{año}: {cantidad}')
					año = designacion.getAño()
					cantidad = 0

				if designacion.getTipoCargo() == cargo and designacion.esMujer():
					cantidad += 1

			print(f'{año}: {cantidad}')


	def incisoD(self, materia, cargo, año):
		cantidad = 0

		for designacion in self.__designaciones:
			if designacion.getMateria() == materia and designacion.getTipoCargo() == cargo and designacion.getAño() == año:
				cantidad += 1

		return cantidad

	def cargar(self, archivo):
		if not path.isfile(archivo):
			raise Exception('El archivo no existe')

		with open(archivo, 'r') as f:
			reader = csv.reader(f, delimiter=';')
			next(reader)
			
			for linea in reader:
				self.__designaciones.insertar(Designacion(*linea))

if __name__ == '__main__':
	manejador = ManejadorDesignaciones(100)
	manejador.cargar(path.dirname(__file__) + '/designaciones.csv')

	manejador.incisoC(input('\nIngrese un cargo: '))

	materia = input('\nIngrese una materia: ')
	año = int(input('Ingrese un año: '))
	cargo = input('Ingrese un cargo: ')
	cant = manejador.incisoD(materia, cargo, año)
	print(f'\nLa cantidad de agentes designados a la materia {materia} en el cargo {cargo} en el año {año} es {cant}')
