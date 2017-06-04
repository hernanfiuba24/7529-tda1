from readGraph import *

class FloydWarshall(object):

	def __init__(self, graph):
		self.distancias = [[float("inf") for x in range(graph.cantidadVertices())] for x in range(graph.cantidadVertices())]
		for i in range(graph.cantidadVertices()):
			self.distancias[i][i] = 0
		self.distancias = graph.iterarSobreAristas(self.__inicializarMatriz, self.distancias)
		for k in range(graph.cantidadVertices()):
			for i in range(graph.cantidadVertices()):
				for j in range(graph.cantidadVertices()):
					if i != j and self.distancias[i][j] > self.distancias[i][k] + self.distancias[k][j]:
						self.distancias[i][j] = self.distancias[i][k] + self.distancias[k][j]


	def __inicializarMatriz(self, arista, distancias):
		distancias[arista.getSource()][arista.getDest()] = arista.getWeight()
		return distancias

	def getDistancia(self, src, dest):
		return self.distancias[src][dest]

