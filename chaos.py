def main() :
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: ") )
    y = eval(input("Enter number of values you would like to print: "))
    for i in range(y) :
        x= 3.9*x*(1-x)
        print(x)