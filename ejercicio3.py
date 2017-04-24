from kosaraju import *
from time import time

for i in range(1, 7):
	kosa = Kosaraju("ejercicio3/d" + str(i) + ".txt")
	print "Cantidad de SCC", kosa.getCantidadSCC()