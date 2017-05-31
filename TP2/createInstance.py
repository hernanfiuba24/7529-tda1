import random

def generateInstance(path, cantidadAristas):
	file = open(path, "w")
	file.write(str(cantidadAristas) + "\n")
	file.write(str(cantidadAristas * (cantidadAristas - 1)) + "\n")
	allow_values = list(range(1, 99))
	for i in range(cantidadAristas):
		for j in range(cantidadAristas):
			if i != j:
				line = [i, j, random.choice(allow_values)]
				file.write(" ".join([str(x) for x in line]) + "\n")
	file.close()

