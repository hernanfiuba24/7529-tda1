from testUtils import *
from bellmanFord import *
from createInstance import *
from time import time

def run():
	graph = createGraph("test.txt", True)
	bf = BellmanFord(graph, 0)
	test("0->0 = 0", bf.getDistanciaTo(0), 0)
	test("0->1 = 8", bf.getDistanciaTo(1), 8)
	test("0->2 = 32", bf.getDistanciaTo(2), 32)
	test("0->3 = 25", bf.getDistanciaTo(3), 25)
	bf = BellmanFord(graph, 1)
	test("1->0 = 13", bf.getDistanciaTo(0), 13)
	test("1->1 = 0", bf.getDistanciaTo(1), 0)
	test("1->2 = 24", bf.getDistanciaTo(2), 24)
	test("1->3 = 17", bf.getDistanciaTo(3), 17)
	bf = BellmanFord(graph, 2)
	test("2->0 = 34", bf.getDistanciaTo(0), 34)
	test("2->1 = 21", bf.getDistanciaTo(1), 21)
	test("2->2 = 0", bf.getDistanciaTo(2), 0)
	test("2->3 = 38", bf.getDistanciaTo(3), 38)
	bf = BellmanFord(graph, 3)
	test("3->0 = 16", bf.getDistanciaTo(0), 16)
	test("3->1 = 24", bf.getDistanciaTo(1), 24)
	test("3->2 = 7", bf.getDistanciaTo(2), 7)
	test("3->3 = 0", bf.getDistanciaTo(3), 0)

def timeTests():
	print "Creo el archivo y el grafo"
	generateInstance("testBF100.txt", 100)
	graph = createGraph("testBF100.txt", True)
	print "Creo el archivo y el grafo -- DONE"
	inicio = time()
	bf = BellmanFord(graph, 0)
	fin = time()
	print "Tiempo de ejecucion 100 aristas: %f" %(fin - inicio)

	print "Creo el archivo y el grafo"
	generateInstance("testBF200.txt", 200)
	graph = createGraph("testBF200.txt", True)
	print "Creo el archivo y el grafo -- DONE"
	inicio = time()
	bf = BellmanFord(graph, 0)
	fin = time()
	print "Tiempo de ejecucion 200 aristas: %f" %(fin - inicio)

	print "Creo el archivo y el grafo"
	generateInstance("testBF300.txt", 300)
	graph = createGraph("testBF300.txt", True)
	print "Creo el archivo y el grafo -- DONE"
	inicio = time()
	bf = BellmanFord(graph, 0)
	fin = time()
	print "Tiempo de ejecucion 300 aristas: %f" %(fin - inicio)

	print "Creo el archivo y el grafo"
	generateInstance("testBF400.txt", 400)
	graph = createGraph("testBF400.txt", True)
	print "Creo el archivo y el grafo -- DONE"
	inicio = time()
	bf = BellmanFord(graph, 0)
	fin = time()
	print "Tiempo de ejecucion 400 aristas: %f" %(fin - inicio)

	print "Creo el archivo y el grafo"
	generateInstance("testBF500.txt", 500)
	graph = createGraph("testBF500.txt", True)
	print "Creo el archivo y el grafo -- DONE"
	inicio = time()
	bf = BellmanFord(graph, 0)
	fin = time()
	print "Tiempo de ejecucion 500 aristas: %f" %(fin - inicio)

	print "Creo el archivo y el grafo"
	generateInstance("testBF1000.txt", 1000)
	graph = createGraph("testBF1000.txt", True)
	print "Creo el archivo y el grafo -- DONE"
	inicio = time()
	bf = BellmanFord(graph, 0)
	fin = time()
	print "Tiempo de ejecucion 1000 aristas: %f" %(fin - inicio)

run()
timeTests()