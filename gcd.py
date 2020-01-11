def gcd():
    n=int(input('Enter the bigger number of the two you would like to enter: '))
    m=int(input('Enter the smaller number: '))
    while n>0:
        if n%m==0:
            GCD=m%n
            print('The GCD of the two numbers is ',GCD)
        elif n%m==1:
            print('There is no available GCD for the entered numbers')

        break
    else:
        print('Enter appropriate integers')
        


      
gcd()
     
