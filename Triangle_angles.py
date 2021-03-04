#Simon Phipps
#3/2/21
#Triangle Program

from math import acos, sin, degrees
s1 = float(input("Enter side 1: "))
s2 = float(input("Enter side 2: "))
s3 = float(input("Enter side 3: "))

print("Angle 1: ", degrees(acos((s1**2-s2**2-s3**2)/(-2*s2*s3))))
print("Angle 2: ", degrees(acos((s2**2-s1**2-s3**2)/(-2*s1*s3))))
print("Angle 3: ", degrees(acos((s3**2-s1**2-s2**2)/(-2*s1*s2))))

print("Area: ", .5*s1*s2*sin(acos((s3**2-s1**2-s2**2)/(-2*s1*s2))))
