from readGraph import *

def kosaraju(path):
	graph = createGraph(path, True)
	visitados = [False for i in range(graph.cantidadVertices())]
	L = []
	args = graph.iterarSobreNodos(visitar, [graph, visitados, L])
	visitados = args[1]
	L = args[2]	
	asignaciones = {}
	visitados = [False for i in range(graph.cantidadVertices())]
	for nodo in L:
		args = asignar(nodo, [asignaciones, visitados, graph, nodo])
	print "Termino la ejecucion."
	print "Resultados:"
	print "asignaciones:", asignaciones

def visitar(nodo, args):
	if not args[1][nodo]:
		args[1][nodo] = True
		args = args[0].iterarSobreAdyacentes(nodo, visitar, args)
		args[2] = [nodo] + args[2]
	return args

def asignar(nodo1, args):
	if not args[1][nodo1]:
		args[1][nodo1] = True
		if(args[3] in args[0]):
			args[0][args[3]].append(nodo1)
		else:
			args[0][args[3]] = [nodo1]
		args = args[2].iterarSobreIncidentes(nodo1, asignar, args)
	return args
		



kosaraju("ejercicio3/d1.txt")