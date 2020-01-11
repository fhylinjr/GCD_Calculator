from math import *
class Math:
    def __init__(self):
        numbers=[]
        self.numbers=numbers

    def getNumbers(self):
        n=input('Enter a number: ')
        while n!="":
            self.numbers.append(int(n))
            print(self.numbers)
            n=input('Enter a number: ')
        if n=="":
            print('You are done entering numbers.')
        return self.numbers

    def getMean(self):
        total=0.0
        for i in self.numbers:
            total=total+i
        mean= total/len(self.numbers)
        return mean

    def getStandardDev(self):
        sumdevsq=0.0
        for i in self.numbers:
            dev=i- self.getMean()
            sumdevsq=sumdevsq+dev*dev
        standarddev=sqrt(sumdevsq/(len(self.numbers)-1))
        return standarddev

    def getMeanAndStandardDev(self):
        return self.getMean(),self.getStandardDev()

    def getMin(self):
        return min(self.numbers)

    def getMax(self):
        return max(self.numbers)

values=Math()
print(values.getNumbers())
print(values.getMean())
print(values.getStandardDev())
print(values.getMeanAndStandardDev())
print(values.getMin())
print(values.getMax())
        
