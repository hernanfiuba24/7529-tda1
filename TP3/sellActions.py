import sys

class SellActions(object):
    """docstring for SellAction"""
    def __init__(self,path):
        self.dateToBuyActual = -1
        self.dateToSell = -1
        self.dateToBuyFollowing = -1
        self.path = path
        file = open(self.path, "r")
        self.days = int(file.readline())
        file.close()
        self.valueActions = [None] * self.days
        self.benefits = [None] * self.days

    def initialize(self):
        self.dateToBuyActual = 0
        self.dateToSell = 0
        self.benefits[0] = 0

    def setValueAction(self, day, value):
        self.valueActions[day] = value

    def showSellAcctions(self):
        print self.valueActions

    def setBenefit(self, day):
        newValue = self.valueActions[day]
        valueNewisGreaterThanValueToSell = self.valueActions[self.dateToSell] < newValue
        valueNewisLessThanValueToBuyActual = newValue < self.valueActions[self.dateToBuyActual]
        if (valueNewisGreaterThanValueToSell):
            self.dateToSell = day
            self.benefits[day] = newValue - self.valueActions[self.dateToBuyActual]
            existDateToBuyFollowing = self.dateToBuyFollowing != -1
            if (existDateToBuyFollowing):
                benefitWithBuyFollowing = (self.valueActions[self.dateToSell] - self.valueActions[self.dateToBuyFollowing])
                existBenefitGreaterThanBefore = self.benefits[day] < benefitWithBuyFollowing
                if (existBenefitGreaterThanBefore):
                    self.benefits[day] = benefitWithBuyFollowing
                    self.dateToBuyActual = self.dateToBuyFollowing
                    self.dateToBuyFollowing = -1
        elif (valueNewisLessThanValueToBuyActual):
            self.dateToBuyFollowing = day
            self.benefits[day] = self.benefits[day-1]
        else:
            self.benefits[day] = self.benefits[day-1]

    def findTheDaysToBuyAndSellAcctions(self):
        file = open(self.path, "r")
        self.days = int(file.readline())
        for self.day in xrange(0, self.days):
            value = int(file.readline())
            self.setValueAction(self.day, value)
            if (self.day > 0):
                self.setBenefit(self.day)
            else:
                self.initialize()
        file.close()
        print "Day to buy is " + str(self.dateToBuyActual)
        print "Day to sell is " + str(self.dateToSell)
        print "The benefit is " + str(self.benefits[self.days-1])