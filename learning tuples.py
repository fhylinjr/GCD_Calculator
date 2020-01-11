'''myset={"apple","banana","orange"}
print(myset)#may print unordered results.
myset.add("guava")#adds a single item
print(myset)
myset.update(["melon","pineapple"])#adds multiple items
print(myset)
myset.remove("orange")#removes a specified item
myset.discard("apple")#alt
myset.pop()#removes last item
print(myset)
def display():
    num=[10,20,-2,100]
    print(sum(num))
    product=1.0
    for i in num:
        product=product*i
    print(product)
    print(max(num))

    items={"banana","orange","pineapple"}
    items.update(["Berry","pawpaw"])

    alpha=["abc","xyz","aba","1221"]
    count=0
    for i in alpha:
        if len(i)>=2 and i[0]==i[-1]:
            count=count+1
    print(count)

display()

def addition(x,y):
    print(x+y)
def multiplication(x,y):
    print(x*y)
def division(x,y):
    print(x/y)
def subtraction(x,y):
    print(x-y)

def operation(x,y):
    n=eval(input('Enter a number for an operation.\n1-addition, 2-multiplication, 3-division, 4-subtraction: '))
    if n==1:
        return addition(x,y)
    elif n==2:
        return multiplication(x,y)
    elif n==3:
        return division(x,y)
    elif n==4:
        return subtraction(x,y)
    else:
        print('You entered a wrong character.')

operation(2,3)

def unique():
    olist=eval(input('Enter your list of numbers separated by commas: '))
    nlist=[]
    for i in olist:
        while i not in nlist:
            nlist.append(i)
    print(nlist)

unique()'''
class Students:
    fullname="John Doe"
    age=23


newstudent=Students()
newstudent.fullname="Chris Brown"
newstudent.age=34
print(newstudent.fullname)
print(newstudent.age)
    
