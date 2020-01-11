def count(myList,x):
    b=0
    for i in myList:
        if i==x:
            b+=1
    return b

def isin(myList,x):
    b=False
    for i in myList:
        if x==i:
            b=True
            break
        elif x!=i:
            b=False
    return b

def index(myList,x):
    for i in range(len(myList)):
        if myList.count(x)!=0:
            if myList[i]==x:
                return i
        elif myList.count(x)==0:
            return None
    

def  reverse(myList):
    return myList[-1::-1]

def sort(myList):
    sorted=False
    while not sorted:
        sorted=True
        for i in range(1,len(myList)):
            if myList[i-1]>myList[i]:
                myList[i-1],myList[i]=myList[i],myList[i-1]
                sorted=False
    return myList
            

myList=[]
n=input('Enter a number: ')
while n!="":
    myList.append(int(n))
    print(myList)
    n=input('Enter a number: ')#Tap enter key to end entering numbers.
if n=="":
    print('You are done entering numbers.')
print(myList)

x=eval(input('Enter a number in your list you would like info on: '))

print(x,' appears ',count(myList,x),' time(s) in your list.')
print(x,' in your list is ',isin(myList,x))
print(x,' is found at index ',index(myList,x),' of your list.')
print('Reversed list: ',reverse(myList))
print('Sorted list: ',sort(myList))
