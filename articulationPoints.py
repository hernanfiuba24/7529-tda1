from readGraph import *

class ArticulationPoints(object):

    def __init__(self, path):
        # Inicializacion
        self.graph = createGraph(path, False)
        self.visitedStatus = [False for i in range(self.graph.cantidadVertices())]
        self.discoveryTime = [float("Inf") for i in range(self.graph.cantidadVertices())]
        self.lowTime = [float("Inf") for i in range(self.graph.cantidadVertices())]
        self.parent = [False for i in range(self.graph.cantidadVertices())]
        self.articulationPoints = [False for i in range(self.graph.cantidadVertices())]
        self.childrenCount = [0 for i in range(self.graph.cantidadVertices())]
        self.time = 0
        self.nodesToProcess = []

    def getArticulationPoints(self):
        # Iterar para cada nodo
        self.graph.iterarSobreNodos(self.__processPoints, "")
        self.graph.iterarSobreNodos(self.__detectArticulationPoints, "")
        articulationPointsQuantity = 0
        for nodo in range(len(self.articulationPoints)):
            if self.articulationPoints[nodo]:
                articulationPointsQuantity += 1
        return articulationPointsQuantity

    def __processPoints(self, node, unused):
        self.nodesToProcess.append(node)
        while len(self.nodesToProcess) > 0:
            nodeToProcess = self.nodesToProcess.pop()
            if not self.visitedStatus[nodeToProcess]:
                # Actualizar las propiedades del nodo. 
                self.visitedStatus[nodeToProcess] = True
                self.discoveryTime[nodeToProcess] = self.time
                self.lowTime[nodeToProcess] = self.time
                self.time += 1
                self.graph.iterarSobreAdyacentes(node, self.__pushChildsUpdateStats, node)
        return None

    def __pushChildsUpdateStats(self, child, parent):
        if not self.visitedStatus[child]:
            # Representacion del arbol DFS como array.
            self.parent[child] = parent
            self.childrenCount[parent] += 1
            # Aca se detecta si hay un camino (arista de restroceso)
            # que llegue a algun hijo.
            self.lowTime[parent] = min(self.lowTime[parent], self.lowTime[child])
            # Apilar hijos a processar.
            self.nodesToProcess.append(child)
        elif child != self.parent[parent]:
            # Actualizacion del tiempo para el padre, si el hijo tiene un tiempo menor.
            # Solamente si el hijo se puede conectar a un antecesor al padre.
            self.lowTime[parent] = min(self.lowTime[parent], self.discoveryTime[child])
        return parent

    def __detectArticulationPoints(self, node, unused):
        # Es la raiz un punto de articulacion?
        if self.parent[node] == False and self.childrenCount[node] > 1:
            self.articulationPoints[node] = True
        # Es el nodo, no raiz, un punto de articulacion?
        if not self.articulationPoints[node]:
            self.graph.iterarSobreAdyacentes(node, self.__markParentIfArtculationPoint, node)
        return None

    def __markParentIfArtculationPoint(self, child, parent):
        if self.parent[parent] != False and self.lowTime[child] >= self.discoveryTime[parent]:
                self.articulationPoints[parent] = True
        return parent
