class Arista:

	def __init__(self, src, dst, weight = 1):
		self.src = src
		self.dst = dst
		self.weight = weight

	def getSource(self):
		return self.src
		
	def setSource(self, new):
		self.src = new

	def getDest(self):
		return self.dst
		
	def setDest(self, new):
		self.dst = new

	def getWeight(self):
		return self.weight