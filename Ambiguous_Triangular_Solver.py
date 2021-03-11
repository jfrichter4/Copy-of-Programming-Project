#Simon Phipps
#3/4/21
#Ambiguous Triangle Solver

from math import sin, radians, degrees, asin, sqrt, cos

s1 = float(input("Enter side A: "))
s2 = float(input("Enter side B: "))
ad1 = float(input("Enter angle A in degrees: "))
a1 = radians(ad1)

if s1<(s2*sin(a1)):
    print("There are no solutions")
elif s1>s2:
    print("There is one solution")
    ad2=degrees(asin(s2*sin(a1)/s1))
    print("Angle B is",ad2)
    ad3=180-ad1-ad2
    print("Angle C is",ad3)
    s3=(s1*sin(radians(ad3)))/sin(a1)
    print("Side C is", s3)
elif s1>=(s2*sin(a1)) and s1<s2:
    print("There are two solutions")
    ad2=degrees(asin(s2*sin(a1)/s1))
    ad4=180-ad2
    print("Angle B is",ad2,"or", ad4)
    ad3=180-ad1-ad2
    ad5=180-ad3
    print("Angle C is",ad3,"or",ad5)
    s3=(s1*sin(radians(ad3)))/sin(a1)
    s4=sqrt(s1**2+s2**2-2*s1*s2*cos(radians(ad5)))
    print("Side C is", s3,"or",s4)
else:
    print("something is wrong")
