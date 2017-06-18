from testUtils import *
from sellActions import *
from generateInstanceToSellActions import *
from time import time

def run():
    sa = SellActions("test.txt")
    sa.findTheDaysToBuyAndSellAcctions()
    test("Day to buy  =  6", sa.dateToBuyActual, 6)
    test("Day to sell =  7", sa.dateToSell, 7)
    test("The benefit is =  100", sa.benefits[len(sa.benefits)-1], 100)

def timeTests():
    print "Generate instances to buying and selling"
    generateInstance("testSA100.txt", 100)
    print "Find the optimal days to buying and selling"
    inicio = time()
    sa = SellActions("testSA100.txt")
    sa.findTheDaysToBuyAndSellAcctions()
    fin = time()
    print "Execution time with 100 days: %f" %(fin - inicio)

    print "Generate instances to buying and selling"
    generateInstance("testSA1000.txt", 1000)
    print "Find the optimal days to buying and selling"
    inicio = time()
    sa = SellActions("testSA1000.txt")
    sa.findTheDaysToBuyAndSellAcctions()
    fin = time()
    print "Execution time with 1000 days: %f" %(fin - inicio)

    print "Generate instances to buying and selling"
    generateInstance("testSA10000.txt", 10000)
    print "Find the optimal days to buying and selling"
    inicio = time()
    sa = SellActions("testSA10000.txt")
    sa.findTheDaysToBuyAndSellAcctions()
    fin = time()
    print "Execution time with 10000 days: %f" %(fin - inicio)

    print "Generate instances to buying and selling"
    generateInstance("testSA100000.txt", 100000)
    print "Find the optimal days to buying and selling"
    inicio = time()
    sa = SellActions("testSA100000.txt")
    sa.findTheDaysToBuyAndSellAcctions()
    fin = time()
    print "Execution time with 100000 days: %f" %(fin - inicio)

    print "Generate instances to buying and selling"
    generateInstance("testSA1000000.txt", 1000000)
    print "Find the optimal days to buying and selling"
    inicio = time()
    sa = SellActions("testSA1000000.txt")
    sa.findTheDaysToBuyAndSellAcctions()
    fin = time()
    print "Execution time with 1000000 days: %f" %(fin - inicio)

    print "Generate instances to buying and selling"
    generateInstance("testSA10000000.txt", 10000000)
    print "Find the optimal days to buying and selling"
    inicio = time()
    sa = SellActions("testSA10000000.txt")
    sa.findTheDaysToBuyAndSellAcctions()
    fin = time()
    print "Execution time with 10000000 days: %f" %(fin - inicio)

run()
timeTests()
