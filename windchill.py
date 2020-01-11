def windIndex(t,v):
    chill=35.74+0.6215*t-35.75*v**.16+.4275*t*v**.16
    return chill

def main():
    for v in range(0,51,5):
        for t in range(-20,61,10):
            print(windIndex(t,v),end='')
        print()

main()
