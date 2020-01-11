def str_finder(lst):#If the argument you want to enter is a word kindly put it in quotation marks.
    print(lst)
    b=False
    for i in lst:
        if i==str(i):
            b=True
    print(b)

    
'''def equation_solver(a,b,c):
    if (b**2-4*a*c)>=0:
        disc=(b**2-(4*a*c))**0.5
        x=(-b+disc)/(2*a)
        y=(-b-disc)/(2*a)
        solution=[x,y]
        print(solution)
    elif (b**2-4*a*c)<0:
        print('No real roots')


def factors(num):#number has to be an integer to return factors
    numb=[]
    if num>0:
        for i in range(1,num+1):
            if num%i==0:
                numb.append(int(i))
        return numb
    elif num<0:
        for i in range(num,0):
            if num%i==0:
                numb.append(int(i))
        return numb
    elif num==0:
        return 'None' 

from statistics import mean


def bikes_to_mean():
    readfile = open("sf_bike_data.csv", "r")
    total = 0.0
    lst = []
    readfile.readline()
    for i in range(1, 365):
        value = readfile.readline()
        rvalue = value.split(',')
        lst.append(int(rvalue[1]))
        total = total + int(rvalue[1])
    r_mean = total / 364
    s_mean = mean(lst)
    if r_mean == s_mean:
        is_equal = True
    else:
        is_equal = False

    print((r_mean, is_equal))

    readfile.close()



from random import random
def pi_estimator():
    n=int(input('Enter total number of points: '))
    h=0 #This is the number of random points that get to be in the circle initially set at 0.
#We assume our square is a 2*2 square
    for i in range(n):
        x=2*random()-1 #This generates random x coordinates to the amount n.
        y=2*random()-1 #This generates random y coordinates to the amount n.
        if (x**2)+(y**2)<=1:#Checks if the distance of the point(x,y) to the centre of the circle is less than or equal to the square of the radius of the circle
            i==h
            h=h+1
    pi=4*(h/n)
    print(pi)'''


        


