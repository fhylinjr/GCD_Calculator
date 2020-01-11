def innerProd(x,y):
    total=0.0
    '''for i in range(len(x)):'''
    for a in x:
        for b in y:
            if x.index(a)==y.index(b):
                p=a*b
                total=total+p
    return total
    
x=[]
n=input('Enter a number: ')
while n!="":
    x.append(int(n))
    n=input('Enter a number: ')#Tap enter key to end entering numbers.
if n=="":
    print('You are done entering numbers.')
print(x)

y=[]
n=input('Enter a number: ')
while n!="":
    y.append(int(n))
    n=input('Enter a number: ')#Tap enter key to end entering numbers.
if n=="":
    print('You are done entering numbers.')
print(y)


print('Inner product is ',innerProd(x,y))
