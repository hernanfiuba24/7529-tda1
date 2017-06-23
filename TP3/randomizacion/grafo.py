from nodo import Nodo
from arista import Arista
from random import *

class Grafo:

	def __init__(self, cantidadAristas):
		self.vertices = [Nodo(str(x)) for x in range(cantidadAristas)]
		self.aristas = []

	def cantidadVertices(self):
		return len(self.vertices)

	def cantidadAristas(self):
		return len(self.aristas)

	def agregarArista(self, nodo1, nodo2, peso = 1):
		arista = Arista(self.vertices[nodo1], self.vertices[nodo2], peso)
		self.aristas.append(arista)
		
	def contraerNodo(self, nodoSrc, nodoDst):
		newNode = Nodo.merge(nodoSrc, nodoDst)
		self.vertices.append(newNode)
		self.vertices.remove(nodoSrc)
		self.vertices.remove(nodoDst)
		
		aristasAEliminar = []
		for arista in self.aristas:
			if arista.getSource() == nodoDst:
				arista.setSource(newNode)
			if arista.getSource() == nodoSrc:
				arista.setSource(newNode)
			if arista.getDest() == nodoDst:
				arista.setDest(newNode)
			if arista.getDest() == nodoSrc:
				arista.setDest(newNode)
			if arista.getSource() == arista.getDest():
				aristasAEliminar.append(arista)
		self.aristas = [arista for arista in self.aristas if not arista in aristasAEliminar]

	def getRandomEdge(self):
		if len(self.aristas) == 0:
			print "Se acabaron las aristas y hay %i vertices" %(self.cantidadVertices())
		return choice(self.aristas)
		
	def getVertice(self, nodo):
		return self.vertices[nodo]

