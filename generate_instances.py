import	sys, datetime, random

def takeInput(paramenters):
	try:
		words = sys.argv[1].split('=')
		paramenters['n'] = int(words[1])
		
		words = sys.argv[2].split('=')
		paramenters['m'] = int(words[1])
	except IndexError as e:
		print "Error in data input", e
		print "Take default value n = 3 y m = 4"
		paramenters['n'] = 3
		paramenters['m'] = 4

def generateNlinesOfMValuesRamdonAndSave(n, m, f, minRandom, maxRandom):
	i = 0
	while (i < n):
		preferenceHospitalsByStudent = ""
		j = 0
		while (j < m):
			if (j == 0):
				preferenceHospitalsByStudent += str(random.randint(minRandom, maxRandom))
			else:
				preferenceHospitalsByStudent += " " + str(random.randint(minRandom, maxRandom))
			j += 1
		f.write(preferenceHospitalsByStudent + "\n")
		i += 1

if __name__ == "__main__":
	starTime = datetime.datetime.now().strftime('%H:%M:%S');
	paramenters = {'n':-1, 'm':-1}
	takeInput(paramenters)
	print "n = ", paramenters['n'], "m = ", paramenters['m']

	path = "files/instances_" + str(datetime.datetime.now().strftime('%Y-%m-%d')) + ".txt"
	try:
		f = open(path, 'w')
	except IOError as e:
		print "Error to write a file", e
		print "Take default path file"
		path = "files/instances_default.txt"
		f = open(path, 'w')

	maxAlumnos = paramenters['n']
	maxHospitals = paramenters['m']

	f.write(str(maxAlumnos) + "\n")
	generateNlinesOfMValuesRamdonAndSave(maxAlumnos, maxHospitals, f, 1, maxHospitals)
	f.write(str(maxHospitals) + "\n")
	generateNlinesOfMValuesRamdonAndSave(maxHospitals, maxAlumnos, f, 0, 10)
	generateNlinesOfMValuesRamdonAndSave(1, maxHospitals, f, 0, maxAlumnos)

	f.close()
	print "Se genero correctamente las instancias en el archivo " + path
	print "time of executing = " + str(datetime.datetime.now().strftime('%H:%M:%S') - starTime)