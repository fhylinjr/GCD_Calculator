from random import random

def main():
    n=int(input('Enter the number of thrown darts: '))
    h=0
    for i in range(n):
        x=2*random()-1
        y=2*random()-1
        if (x**2)+(y**2)<=1:
            i==h
            h=h+1
    pi=4*(h/n)
    print(pi)
          
