#program prints even numbers from a given list
def main():
    numbers=(input('Enter your list of numbers, each separated by single space: '))
    numbers=numbers.split()
    even=[int(i) for i in numbers]
    for a in even:
        if a%2==0:
            print(a)
        else:
            continue
