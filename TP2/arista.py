class Arista:

	def __init__(self, src, dst, weight = 1):
		self.src = src
		self.dst = dst
		self.weight = weight

	def getSource(self):
		return self.src

	def getDest(self):
		return self.dst

	def getWeight(self):
		return self.weight