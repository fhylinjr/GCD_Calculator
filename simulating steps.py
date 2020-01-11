from random import random
def main():
    n=int(input('Enter total number of steps: '))
    s=0
    for i in range(n):
        if random()<0.5:
            i==s
            s=s+1
        else:
            s=s-1
    return s
