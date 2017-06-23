class Nodo(object):
	
	def __init__(self, id):
		self.aristas = []
		self.id = id
		
	def addArista(self, arista):
		self.aristas.append(arista)
	
	def removeArista(self, arista):
		self.aristas.remove(arista)
		
	def addAristas(self, aristas):
		self.aristas += aristas
		
	def getId(self):
		return self.id

	def getAristas(self):
		return self.aristas
		
	@staticmethod
	def merge(nodo1, nodo2):
		newNode = Nodo(nodo1.getId() + "|" + nodo2.getId())
		newNode.addAristas(nodo1.getAristas() + nodo2.getAristas())
		return newNode