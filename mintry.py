from statistics import mean
def bikes_to_mean():
    readfile=open("sf_bike_data.csv","r")
    total=0.0
    lst=[]
    readfile.readline()
    for i in range(1,365):
        value=readfile.readline()
        rvalue=value.split(',')
        lst.append(int(rvalue[1]))
        total=total+int(rvalue[1])
    rmean=total/365
    print(rmean)
    amean=statistics.mean(lst)
    print(amean)
    if rmean==amean:
        print(rmean,True)
    elif rmean!=amean:
        print(rmean,False)

    readfile.close()
