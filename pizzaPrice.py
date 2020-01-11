from math import *
def pizza(size,price): #size and price should be in inches and GHC respectively.
    area=(pi*size**2)/4
    cost=price/area
    print('The area of your pizza is ',area,' square inches')
    print('The cost per square inch of your pizza is ',cost,' GHC per square inch')
    
