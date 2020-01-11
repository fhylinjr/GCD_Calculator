def main():
    for i in range(1,51):
        if i%3==0:
            print('Fizz')
        elif i%5==0:
            print('Buzz')
        if i%5==0 or i%3==0:
            print('FizzBuzz')
        
            print(i)

main()
