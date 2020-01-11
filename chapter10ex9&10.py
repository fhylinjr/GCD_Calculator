from math import *
class Sphere:
    def __init__(self,r):
        self.radius=r
        self.area=4*pi*r**2
        self.volume=(4/3)*pi*r**3

sphere1=Sphere(6)
print(sphere1.radius)
print(sphere1.area)
print(sphere1.volume)
print()

class Cube:
    def __init__(self, l):
        self.side_length=l
        self.area=2*(3*l**2)
        self.volume=l**3

cube1=Cube(8)
print(cube1.side_length)
print(cube1.area)
print(cube1.volume)
