def sieve():
    num=[]
    n=eval(input('Enter limit of numbers: '))
    for i in range(2,n+1):
        num.append(int(i))
    print(num)

    print(num[0],' is a prime number.')

    for i in range(2,n+1):
        while len(num)!=0:
            for a in num:
                if a%2==0:
                    num.remove(a)
            print(num)
            c=num[0]
            print(c,' is a prime number.')
            for a in num:
                if a%c==0:
                    num.remove(a)
                continue
        
    
        
    
sieve()
