from karger import Karger
from createInstanceKarger import generateInstance
from time import time

def run():
	for i in range(1, 6):
		cantidadVertices = i*1000
		print "Creo la instancia de %d" %(cantidadVertices)
		generateInstance("test" + str(i) + ".txt", cantidadVertices)
		print "Empiezo el algoritmo"
		inicio = time()
		karg = Karger("test" + str(i) + ".txt")
		fin = time()
		print karg.getMinCut()[2]
		print "Termine la ejecucion en %d segundos" %(fin - inicio)
			
		