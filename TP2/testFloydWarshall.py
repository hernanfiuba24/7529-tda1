from testUtils import *
from floydWarshall import *
from createInstance import *
from time import time

def run():
	graph = createGraph("test.txt", True)
	fw = FloydWarshall(graph)
	test("0->0 = 0", fw.getDistancia(0, 0), 0)
	test("0->1 = 8", fw.getDistancia(0, 1), 8)
	test("0->2 = 32", fw.getDistancia(0, 2), 32)
	test("0->3 = 25", fw.getDistancia(0, 3), 25)
	test("1->0 = 13", fw.getDistancia(1, 0), 13)
	test("1->1 = 0", fw.getDistancia(1, 1), 0)
	test("1->2 = 24", fw.getDistancia(1, 2), 24)
	test("1->3 = 17", fw.getDistancia(1, 3), 17)
	test("2->0 = 34", fw.getDistancia(2, 0), 34)
	test("2->1 = 21", fw.getDistancia(2, 1), 21)
	test("2->2 = 0", fw.getDistancia(2, 2), 0)
	test("2->3 = 38", fw.getDistancia(2, 3), 38)
	test("3->0 = 16", fw.getDistancia(3, 0), 16)
	test("3->1 = 24", fw.getDistancia(3, 1), 24)
	test("3->2 = 7", fw.getDistancia(3, 2), 7)
	test("3->3 = 0", fw.getDistancia(3, 3), 0)

def timeTests():
	print "Creo el archivo y el grafo"
	generateInstance("testFW100.txt", 100)
	graph = createGraph("testFW100.txt", True)
	print "Creo el archivo y el grafo -- DONE"
	inicio = time()
	fw = FloydWarshall(graph)
	fin = time()
	print "Tiempo de ejecucion 100 aristas: %f" %(fin - inicio)

	print "Creo el archivo y el grafo"
	generateInstance("testFW200.txt", 200)
	graph = createGraph("testFW200.txt", True)
	print "Creo el archivo y el grafo -- DONE"
	inicio = time()
	fw = FloydWarshall(graph)
	fin = time()
	print "Tiempo de ejecucion 200 aristas: %f" %(fin - inicio)

	print "Creo el archivo y el grafo"
	generateInstance("testFW300.txt", 300)
	graph = createGraph("testFW300.txt", True)
	print "Creo el archivo y el grafo -- DONE"
	inicio = time()
	fw = FloydWarshall(graph)
	fin = time()
	print "Tiempo de ejecucion 300 aristas: %f" %(fin - inicio)
	
	print "Creo el archivo y el grafo"
	generateInstance("testFW400.txt", 400)
	graph = createGraph("testFW400.txt", True)
	print "Creo el archivo y el grafo -- DONE"
	inicio = time()
	fw = FloydWarshall(graph)
	fin = time()
	print "Tiempo de ejecucion 400 aristas: %f" %(fin - inicio)
	
	print "Creo el archivo y el grafo"
	generateInstance("testFW500.txt", 500)
	graph = createGraph("testFW500.txt", True)
	print "Creo el archivo y el grafo -- DONE"
	inicio = time()
	fw = FloydWarshall(graph)
	fin = time()
	print "Tiempo de ejecucion 500 aristas: %f" %(fin - inicio)
	
	print "Creo el archivo y el grafo"
	generateInstance("testFW1000.txt", 1000)
	graph = createGraph("testFW1000.txt", True)
	print "Creo el archivo y el grafo -- DONE"
	inicio = time()
	fw = FloydWarshall(graph)
	fin = time()
	print "Tiempo de ejecucion 1000 aristas: %f" %(fin - inicio)

run()
timeTests()