# write a python program which accepts the radius of a circle from user and computes the area 

import math 

radius = int(input("Enter the radius of a circle: "))

area = math.pi*radius*radius 

print(f"The area of the circle with radius {radius} is {area} sq cm.")