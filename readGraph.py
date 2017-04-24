from grafo import *

def createGraph(path, dirigido):
	file = open(path, "r")
	cantidadVertices = file.readline()
	grafo = Grafo(int(cantidadVertices))
	cantidadAristas = int(file.readline())
	for x in range(cantidadAristas):
		linea = file.readline()
		nodos = [int(x) for x in linea.split(" ")]
		grafo.agregarArista(nodos[0], nodos[1])
		if(not dirigido):
			grafo.agregarArista(nodos[1], nodos[0])
	return grafo
	
def createTransposeGraph(path, dirigido):
	file = open(path, "r")
	cantidadVertices = file.readline()
	grafo = Grafo(int(cantidadVertices))
	cantidadAristas = int(file.readline())
	for x in range(cantidadAristas):
		linea = file.readline()
		nodos = [int(x) for x in linea.split(" ")]
		grafo.agregarArista(nodos[1], nodos[0])
		if(not dirigido):
			grafo.agregarArista(nodos[0], nodos[1])
	return grafo
