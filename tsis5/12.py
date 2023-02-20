import math

a = int(input("Input number of sides:"))
b = int(input("Input the length of a side:"))

print(b*b*a/4*math.tan(math.pi/a))