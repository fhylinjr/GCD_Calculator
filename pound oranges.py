'''def oranges(x):
    cost=(0.32*x + 7.5)
    premium=cost-1.5
    if x>100:
        print('The cost of your order is ',premium,' dollars.')
    else:
        print('The cost of your order is ',cost,' dollars.')'''

# write a function that takes 2 parameters- a pay rate and the hours works and
#returns pay. any extra hour over 40 is paid at that extra time and and a half of payrate.

def wages(r,h):
    pay=r*h
    payp=(40*r)+((h-40)*(1.5*r))#means first 40hrs are paid at norm rate then the remaining are paid with the extra rate
    if h>40:
        print('Your pay is ',payp,' dollars.')
    else:
        print('Your pay is ',pay,' dollars.')
    
