def gradient():
    print("This program determines the slope of a line from 2 points")
    
    x1=float(input("Enter the x-value of the first point "))
    x2=float(input("Enter the x-value of the second point "))
    y1=float(input("Enter the y-value of the first point "))
    y2=float(input("Enter the y-value of the second point "))
    
    slope=(y2-y1)/(x2-x1)
    print("The slope is ",slope)
    