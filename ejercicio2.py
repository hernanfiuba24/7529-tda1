from time import time
from articulationPoints import *

for i in range(1, 7):
    inicio = time()
    articulationPointsCalculator = ArticulationPoints("ejercicio2/g" + str(i) + ".txt")
    articulationPoints = articulationPointsCalculator.getArticulationPoints()
    fin = time()
    print "Tiempo de ejecucion de g" + str(i) + ":", fin-inicio, "segundos."
    print "Hay " + str(articulationPoints) + " puntos de articulacion.\n"