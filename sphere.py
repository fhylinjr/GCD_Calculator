def rad():
        print("Would you like to calcuate for volume or surface area of a sphere?\nEnter 1 for Volume or 2 for Surface Area: ")
        reply=int(input())
        from math import pi
        r=float(input("Ener the value of radius "))
        if reply==1:
            volume=(4/3)*pi*r**3
            print("The volume of the sphere is ",volume)
        elif reply==2:
            area=4*pi*r**2
            print("The surface area of the sphere is ", area)
        else:
            print("You did not take a valid choice")