from statistics import mean


def bikes_to_mean():
    readfile = open("sf_bike_data.csv", "r")
    total = 0.0
    lst = []
    readfile.readline()
    for i in range(1, 365):
        value = readfile.readline()
        rvalue = value.split(',')
        lst.append(int(rvalue[1]))
        total = total + int(rvalue[1])
    print(lst)
    r_mean = total / 364
    s_mean = mean(lst)
    if r_mean == s_mean:
        is_equal = True
    else:
        is_equal = False

    print((r_mean, is_equal))

    readfile.close()

bikes_to_mean()
