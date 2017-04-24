from readGraph import *
from time import time

class Kosaraju(object):

	def __init__(self, path):
		graph = createGraph(path, True)
		transposeGraph = createTransposeGraph(path, True)
		visitados = [False for i in range(graph.cantidadVertices())]
		L = []
		args = graph.iterarSobreNodos(self.__visitar, [graph.iterarSobreAdyacentes, visitados, L])
		visitados = args[1]
		L = args[2]	
		asignaciones = {}
		visitados = [False for i in range(graph.cantidadVertices())]
		for nodo in L:
			args = self.__asignar(nodo, [asignaciones, visitados, transposeGraph.iterarSobreAdyacentes, nodo])
		self.componentesConexas = asignaciones.values()

	def getCantidadSCC(self):
		return len(self.componentesConexas)
		
	def getSCC(self, id):
		return self.componentesConexas[id]

	def __asignar(self, nodo1, args):
		if not args[1][nodo1]:
			args[1][nodo1] = True
			if(args[3] in args[0]):
				args[0][args[3]].append(nodo1)
			else:
				args[0][args[3]] = [nodo1]
			args = args[2](nodo1, self.__asignar, args)
		return args
		
	def __visitar(self, nodo, args):
			if not args[1][nodo]:
				args[1][nodo] = True
				args = args[0](nodo, self.__visitar, args)
				args[2] = [nodo] + args[2]
			return args		

