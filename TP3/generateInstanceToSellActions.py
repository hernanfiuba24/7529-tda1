import random, sys

def generateInstance(path, days):
    file = open(path, "w")
    file.write(str(days) + "\n")
    for i in xrange(days):
        rand = random.randint(0, sys.maxint)
        file.write(str(rand) + "\n")
    file.close()
generateInstance("pru5.txt", 100)