def sentinel():
    numbers=[]
    n=input('Enter a number: ')
    while n!="":
        numbers.append(int(n))
        print(numbers)
        n=input('Enter a number: ')
    if n=="":
        print('You are done entering numbers.')
        

sentinel()
