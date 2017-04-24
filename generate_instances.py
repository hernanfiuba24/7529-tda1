import	sys, datetime, random

def takeInput(paramenters):
    try:
        words = sys.argv[1].split('=')
        paramenters['n'] = int(words[1])
        words = sys.argv[2].split('=')
        paramenters['m'] = int(words[1])
    except Exception:
        print "Error in data input"
        print "Take default value n = 10 y m = 10"
        paramenters['n'] = 10
        paramenters['m'] = 10
        raise Exception("Error to reading parameters")

def generateNlinesOfMValuesRamdonAndSave(n, m, f, minRandom, maxRandom, bunchsize):
    i = 0
    bunch = []
    preferenceHospitalsByStudent = []
    while (i < n):
        j = 0
        allow_values = list(range(minRandom, maxRandom+1))
        # print allow_values
        while (j < m):
            element_random = 1
            if (maxRandom > 1):
                element_random = random.choice(allow_values)
                allow_values.remove(element_random)
            preferenceHospitalsByStudent.append(str(element_random))
            j += 1
        #preferenceHospitalsByStudent += "\n"
        bunch.append(' '.join(preferenceHospitalsByStudent) + "\n")
        preferenceHospitalsByStudent = []
        if (len(bunch) == bunchsize):
            #bunch.sort(reverse=True)
            # print bunch
            f.writelines(bunch)
            bunch = []
            print "line : " + str(i)
        i += 1

if __name__ == "__main__":

    FORMAT = '%H:%M:%S'
    startTime = datetime.datetime.now().strftime(FORMAT);
    paramenters = {'n':-1, 'm':-1}
    try:
        takeInput(paramenters)
        path = "files/instances_" + str(datetime.datetime.now().strftime('%Y-%m-%d')) + ".txt"
        f = open(path, 'w')
    except (IOError, Exception):
        print "Error to write a file"
        print "Take default path file"
        path = "files/instances_default.txt"
        f = open(path, 'w')

    maxAlumnos = paramenters['n']
    maxHospitals = paramenters['m']

    f.write(str(maxAlumnos) + "\n")
    generateNlinesOfMValuesRamdonAndSave(maxAlumnos, maxHospitals, f, 0, maxHospitals-1, 1000)
    f.write(str(maxHospitals) + "\n")
    generateNlinesOfMValuesRamdonAndSave(maxHospitals, maxAlumnos, f, 0, maxAlumnos-1, 1000)
    generateNlinesOfMValuesRamdonAndSave(1, maxHospitals, f, 1, 1, 1)

    f.close()
    print "\nThe file " + path + " was created ok"
    finishTime = datetime.datetime.now().strftime(FORMAT);
    deltaTime = datetime.datetime.strptime(finishTime, FORMAT) - datetime.datetime.strptime(startTime, FORMAT)
    print "Time of executing is " + str(deltaTime)	
