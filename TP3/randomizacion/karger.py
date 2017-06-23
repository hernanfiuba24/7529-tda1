from readGraph import *
import random
from math import *

class Karger(object):

	def __init__(self, path):
		graph = createGraph(path, True)
		self.minCut = (None, None, float("inf"))
		iteraciones = factorial(graph.cantidadVertices()) / (factorial(2) * factorial(graph.cantidadVertices() - 2)) * int(ceil(log(graph.cantidadVertices())))
		for i in range(iteraciones):
			# print "Iteracion %d/%d" %(i, iteraciones)
			while graph.cantidadVertices() > 2:
				edge = graph.getRandomEdge()
				graph.contraerNodo(edge.getSource(), edge.getDest())
			if graph.cantidadAristas() < self.getMinCut()[2]:
				self.minCut = (graph.getVertice(0).getId(), graph.getVertice(1).getId(), graph.cantidadAristas())
		
	def getMinCut(self):
		return self.minCut
		