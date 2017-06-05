from testUtils import *
from dijkstra import *
from createInstance import *
from time import time

def run():
    graph = createGraph("test.txt", True)
    d = Dijkstra(graph, 0)
    test("0->0 = 0", d.getDistanceTo(0), 0)
    test("0->1 = 8", d.getDistanceTo(1), 8)
    test("0->2 = 32", d.getDistanceTo(2), 32)
    test("0->3 = 25", d.getDistanceTo(3), 25)
    test("optimal path from 0 -> 2 = [2, 3, 1, 0]", str(d.getPathTo(2)), "[2, 3, 1, 0]")
    d = Dijkstra(graph, 1)
    test("1->0 = 13", d.getDistanceTo(0), 13)
    test("1->1 = 0", d.getDistanceTo(1), 0)
    test("1->2 = 24", d.getDistanceTo(2), 24)
    test("1->3 = 17", d.getDistanceTo(3), 17)
    test("optimal path from 1 -> 2 = [2, 3, 1]", str(d.getPathTo(2)), "[2, 3, 1]")
    d = Dijkstra(graph, 2)
    test("2->0 = 34", d.getDistanceTo(0), 34)
    test("2->1 = 21", d.getDistanceTo(1), 21)
    test("2->2 = 0", d.getDistanceTo(2), 0)
    test("2->3 = 38", d.getDistanceTo(3), 38)
    test("optimal path from 2 -> 2 = [2]", str(d.getPathTo(2)), "[2]")
    d = Dijkstra(graph, 3)
    test("3->0 = 16", d.getDistanceTo(0), 16)
    test("3->1 = 24", d.getDistanceTo(1), 24)
    test("3->2 = 7", d.getDistanceTo(2), 7)
    test("3->3 = 0", d.getDistanceTo(3), 0)
    test("optimal path from 3 -> 2 = [2, 3]", str(d.getPathTo(2)), "[2, 3]")

def timeTests():
    print "Creo el archivo y el grafo"
    generateInstance("testD100.txt", 100)
    graph = createGraph("testD100.txt", True)
    print "Creo el archivo y el grafo -- DONE"
    inicio = time()
    d = Dijkstra(graph, 0)
    fin = time()
    print "Tiempo de ejecucion 100 aristas: %f" %(fin - inicio)

    print "Creo el archivo y el grafo"
    generateInstance("testD200.txt", 200)
    graph = createGraph("testD200.txt", True)
    print "Creo el archivo y el grafo -- DONE"
    inicio = time()
    d = Dijkstra(graph, 0)
    fin = time()
    print "Tiempo de ejecucion 200 aristas: %f" %(fin - inicio)

    print "Creo el archivo y el grafo"
    generateInstance("testD300.txt", 300)
    graph = createGraph("testD300.txt", True)
    print "Creo el archivo y el grafo -- DONE"
    inicio = time()
    d = Dijkstra(graph, 0)
    fin = time()
    print "Tiempo de ejecucion 300 aristas: %f" %(fin - inicio)

    print "Creo el archivo y el grafo"
    generateInstance("testD400.txt", 400)
    graph = createGraph("testD400.txt", True)
    print "Creo el archivo y el grafo -- DONE"
    inicio = time()
    d = Dijkstra(graph, 0)
    fin = time()
    print "Tiempo de ejecucion 400 aristas: %f" %(fin - inicio)

    print "Creo el archivo y el grafo"
    generateInstance("testD500.txt", 500)
    graph = createGraph("testD500.txt", True)
    print "Creo el archivo y el grafo -- DONE"
    inicio = time()
    d = Dijkstra(graph, 0)
    fin = time()
    print "Tiempo de ejecucion 500 aristas: %f" %(fin - inicio)

    print "Creo el archivo y el grafo"
    generateInstance("testD1000.txt", 1000)
    graph = createGraph("testD1000.txt", True)
    print "Creo el archivo y el grafo -- DONE"
    inicio = time()
    d = Dijkstra(graph, 0)
    fin = time()
    print "Tiempo de ejecucion 1000 aristas: %f" %(fin - inicio)

run()
timeTests()
