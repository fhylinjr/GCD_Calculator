def windchill(t,v):
    chillindex=35.74+0.6215*t-35.75*(v**0.16)+0.4275*t*(v**0.16)
    return chillindex


def main():
    print('V/T',end=' ')
    for t in range(-20,70,10):
        a='   T={0:3.0f}'.format(t)
        print(' {0:^1}'.format(a),end='')
        
    print()
    for v in range(0,55,5):
        print('V={0:2.0f}'.format(v),end='')
        for t in range(-20,70,10):
            print('{0:9.2f}'.format(windchill(t,v)),end='')
        print()


main()
