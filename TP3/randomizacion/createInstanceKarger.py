from random import *

def generateInstance(path, cantidadVertices):
	file = open(path, "w")
	file.write(str(cantidadVertices) + "\n")
	file.write(str(cantidadVertices * 2) + "\n")
	aristas = []
	noConectados = [ x for x in range(cantidadVertices)]
	conectados = []
	
	nodoInicio = choice(noConectados)
	conectados.append(nodoInicio)
	noConectados.remove(nodoInicio)
	while len(noConectados) != 0:
		src = choice(noConectados)
		noConectados.remove(src)
		dst = choice(conectados)
		line = [src, dst]
		aristas.append(line)
		file.write(" ".join([str(x) for x in line]) + "\n")
	
	while len(aristas) < cantidadVertices * 2:
		while True:
			src = randint(0, cantidadVertices - 1)
			dst = randint(0, cantidadVertices - 1)
			while src == dst:
				dst = randint(0, cantidadVertices - 1)
			if [src, dst] not in aristas and [dst, src] not in aristas:
				break
		line = [src, dst]
		aristas.append(line)
		file.write(" ".join([str(x) for x in line]) + "\n")
	
	file.close()

