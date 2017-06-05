from readGraph import *
from heapq import *
import sys

class Dijkstra(object):
    def __init__(self, graph, source):
        self.source = source
        self.distances = [sys.maxint for i in range(graph.cantidadVertices())]
        self.distances[source] = 0
        self.vertexes_covered = 0
        self.heap = []
        self.size_heap = 0
        self.path = [ -1 for i in range(graph.cantidadVertices())]
        self.path[source] = source
        for i in range(len(self.distances)):
            heappush(self.heap, (self.distances[i], i))
            self.size_heap += 1
        isTheFinal = self.vertexes_covered == graph.cantidadVertices()
        while (not isTheFinal):
            try:
                min_vertex_tupla = heappop(self.heap)
                self.size_heap -= 1
                min_vertex = min_vertex_tupla[1]
                min_vertex_distances = min_vertex_tupla[0]
                self.distances = graph.iterarSobreAdyacentes(min_vertex, self.__distancesFunction, self.distances)
                self.vertexes_covered += 1
                self.heap = self.__redefineHeap(self.distances)
                isTheFinal = self.vertexes_covered == graph.cantidadVertices()
            except Exception:
                print "Heap empty"
                isTheFinal = True;

    def __distancesFunction(self, arista, distances):
        if distances[arista.getDest()] > distances[arista.getSource()] + arista.getWeight():
            distances[arista.getDest()] = distances[arista.getSource()] + arista.getWeight()
            self.path[arista.getDest()] = arista.getSource()
        return distances

    def getPathTo(self, destination):
        path = []
        path.append(destination)
        isInitial = self.source == destination
        while (not isInitial):
            next_destination = self.path[destination]
            path.append(next_destination)
            destination = next_destination
            isInitial = self.source == destination
        return path

    def __redefineHeap(self, distances):
        heap = []
        size_heap = 0
        for i in range(self.size_heap):
            min_vertex_tupla = heappop(self.heap)
            self.size_heap -= 1
            min_vertex = min_vertex_tupla[1]
            min_vertex_distances = min_vertex_tupla[0]
            if (min_vertex_distances > self.distances[min_vertex]):
                min_vertex_distances = self.distances[min_vertex]
            heappush(heap, (min_vertex_distances, min_vertex))
            size_heap += 1
        self.size_heap = size_heap
        return heap

    def getDistanceTo(self, vertex):
        return self.distances[vertex]