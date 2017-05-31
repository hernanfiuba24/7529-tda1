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
	generateInstance("testBF10000.txt", 10000)
	graph = createGraph("testBF10000.txt", True)
	inicio = time()
	bf = BellmanFord(graph, 0)
	fin = time()
	print "Tiempo de ejecucion 10000 aristas: %f" %(fin - inicio)

	generateInstance("testBF20000.txt", 20000)
	graph = createGraph("testBF20000.txt", True)
	inicio = time()
	bf = BellmanFord(graph, 0)
	fin = time()
	print "Tiempo de ejecucion 20000 aristas: %f" %(fin - inicio)

	generateInstance("testBF30000.txt", 30000)
	graph = createGraph("testBF30000.txt", True)
	inicio = time()
	bf = BellmanFord(graph, 0)
	fin = time()
	print "Tiempo de ejecucion 30000 aristas: %f" %(fin - inicio)

	generateInstance("testBF40000.txt", 40000)
	graph = createGraph("testBF40000.txt", True)
	inicio = time()
	bf = BellmanFord(graph, 0)
	fin = time()
	print "Tiempo de ejecucion 40000 aristas: %f" %(fin - inicio)

	generateInstance("testBF50000.txt", 50000)
	graph = createGraph("testBF50000.txt", True)
	inicio = time()
	bf = BellmanFord(graph, 0)
	fin = time()
	print "Tiempo de ejecucion 50000 aristas: %f" %(fin - inicio)

	generateInstance("testBF100000.txt", 100000)
	graph = createGraph("testBF100000.txt", True)
	inicio = time()
	bf = BellmanFord(graph, 0)
	fin = time()
	print "Tiempo de ejecucion 100000 aristas: %f" %(fin - inicio)

run()
timeTests()