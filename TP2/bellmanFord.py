from readGraph import *

class BellmanFord(object):

	def __init__(self, graph, src):
		self.distancias = [float("inf") for i in range(graph.cantidadVertices())]
		self.distancias[src] = 0
		for i in range(graph.cantidadVertices()):
			self.distancias = graph.iterarSobreAristas(self.__calcularDistancia, self.distancias)


	def __calcularDistancia(self, arista, distancias):
		if distancias[arista.getDest()] > distancias[arista.getSource()] + arista.getWeight():
			distancias[arista.getDest()] = distancias[arista.getSource()] + arista.getWeight()
		return distancias

	def getDistanciaTo(self, dest):
		return self.distancias[dest]

