from math import *
class StatSet:
    def __init__(self):
        numbers=[]
        self.numbers=numbers

    def getaddNumber(self,x):
        x=input('Enter a number: ')
        while x!="":
            self.numbers.append(int(x))
            print(self.numbers)
            x=input('Enter a number: ')
        if x=="":
            print('You are done entering numbers.')
        return self.numbers

    def getmean(self):
        total=0.0
        for i in self.numbers:
            total=total+i
        mean= total/len(self.numbers)
        return mean

    def getmedian(self):
        self.numbers.sort()
        items=len(self.numbers)
        middle=(items//2)+1
        if middle%2==0:
            median=(self.numbers[middle]-self.numbers[middle-1])/2.0
        else:
            median=middle
        return median     

    def getstdDev(self):
        sumdevsq=0.0
        for i in self.numbers:
            dev=i- self.getmean()
            sumdevsq=sumdevsq+dev*dev
        standarddev=sqrt(sumdevsq/(len(self.numbers)-1))
        return standarddev

    def getmin(self):
        least=self.numbers[0]
        for i in self.numbers:
            if i<least:
                least=i
            else:
                least=least
        return least

    def getmax(self):
        greatest=self.numbers[0]
        for i in self.numbers:
            if i>greatest:
                greatest=i
            else:
                greatest=greatest
        return greatest

values=StatSet()
print(values.getaddNumber('x'))
print(values.getmean())
print(values.getmedian())
print(values.getstdDev())
print(values.getmin())
print(values.getmax())
        
