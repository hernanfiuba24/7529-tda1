from kosaraju import *
from time import time

for i in range(1, 7):
	inicio = time()
	kosa = Kosaraju("ejercicio3/d" + str(i) + ".txt")
	fin = time()
	print "Tiempo de ejecucion de d" + str(i) + ":", fin-inicio, "segundos."
	print "Cantidad de SCC", kosa.getCantidadSCC()