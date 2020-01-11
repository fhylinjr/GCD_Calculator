
def sum(x,y):
    sum=x+y
    return sum
    
def area(x,y):
    area=x*y
    return area


"""
x=int(input("Enter length"))
y=int(input("Enter breadth"))
"""
def perimeter(x,y):
    perimeter=2*(x+y)
    return perimeter
"""
result=perimeter(x,y)
print(result)
"""

x=int(input("Enter first number"))
y=int(input("Enter second number"))
operator = input("Enter either area, sum or perimeter")
def genericfunction(x,y,operator):
    if operator=="sum":
        return sum(x,y)
    elif operator=="area":
        return area(x,y)
    elif operator=="perimeter":
        return perimeter(x,y)
    else:
        return("invalid operator")
var = genericfunction(x,y,operator)
print(var)