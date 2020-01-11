from random import random
def simNtoss(n):
    heads=0
    for i in range(n):
        if random()<0.5:
            heads=heads+1
    print('There were {0} heads, so the proportion of heads was {1:0.2f}'.format(heads,heads/n))
