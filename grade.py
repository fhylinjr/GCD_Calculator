def marks():
    grade=float(input("Enter your mark "))
    if grade==5:
            print("You had an A")
    elif grade<5 and grade>=4:
            print("You had a B")
    elif grade<4 and grade>=3:
            print("You had a C")
    elif grade<3 and grade>=2:
            print("You had a D")
    elif grade<2 and grade>=0:
            print("You had F")
    else:
            print("Input the required mark range")