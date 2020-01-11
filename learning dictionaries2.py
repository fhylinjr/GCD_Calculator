def display():
    ydict={"username":"Mike","Pass":"12345","Age":"25"}
    ydict["Email"]="mike@email.com"
    print(ydict)
    print(len(ydict))
    ydict["Pass"]="abcde"
    print(ydict)
    if ydict["username"]=="Mike":
        print('Welcome, Mike.')
    ydict.popitem()
    print(ydict)
    print(sorted(ydict))
    ydict.setdefault("favourite colour","red")
    print(ydict)
    dicto=ydict.copy()
    print(dicto)
    ydict.clear()
    print(ydict,dicto)
    dict1={"one":"1","two":"2"}
    dict2={"three":"3","four":"4"}
    dict1.update(dict2)
    print(dict1)

    data={"data1":100,"data2":-20,"data3":250}
    print(sum(data.values()))
    
    

display()
