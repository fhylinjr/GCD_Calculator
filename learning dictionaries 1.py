def display():
    list={"ID":"23","Name":"Philip"}
    print(list)#prints the whole list
    for n in list:
        print(n)#prints the keys
    print(list.keys())#alternative
    print(list["Name"])#prints a specific value
    print(list.get("Name"))#alternative
    '''list["Name"]="Joe"#change a value in a list'''
    print(list)
    print(list.values())#returns all the values
    print(list.items())#returns every item
    for x,y in list.items():
        print(x,y)#returns items column-wise
    print(len(list))#returns number of items
    list["Age"]=25#adds new item to list
    print(list)
    list.pop("Age")#removes item from list
    print(list)
    list.popitem()#removes last item in list
    print(list)
    '''del list''' #deletes the whole list
    '''list.clear()'''#removes all items and leaves dict. empty
    '''list.update({"color":"red"})'''
    dict2=list.copy()#copies items from one dictionary to another
    dict2=dict(list)#alternative
    k=("key1","key2")#attaches keys to values
    y=0
    list.fromKeys(k,y)
    list.setdefault("username","Philip")#first checks if key exist if not then creates this item
    
    

display()
