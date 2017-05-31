from arista import Arista

class Grafo:

	def __init__(self, cantidadAristas):
		self.adyacencias = []
		for x in range(cantidadAristas):
			self.adyacencias.append([])

	def cantidadVertices(self):
		return len(self.adyacencias)

	'''Devuelve la cantidad de aristas si el grafo es no dirigido. 
	Si es dirigido, devuelvo el doble'''
	def cantidadAristas(self):
		cantidadAristas = 0
		for nodo in self.adyacencias:
			cantidadAristas += len(nodo)
		return cantidadAristas

	def agregarArista(self, nodo1, nodo2, peso):
		arista = Arista(nodo1, nodo2, peso)
		self.adyacencias[nodo1].append(arista)

	def iterarSobreNodos(self, funcion, args):
		for nodo in range(len(self.adyacencias)):
			args = funcion(nodo, args)
		return args

	def iterarSobreAdyacentes(self, nodo, funcion, args):
		for adyacente in self.adyacencias[nodo]:
			args = funcion(adyacente, args)
		return args

	def iterarSobreIncidentes(self, nodo, funcion, args):
		for incidente in range(len(self.adyacencias)):
			if(nodo in self.adyacencias[incidente]):
				args = funcion(incidente, args)
		return args

	def iterarSobreAristas(self, funcion, args):
		for aristas in self.adyacencias:
			for arista in aristas:
				args = funcion(arista, args)
		return args

