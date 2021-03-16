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
    #If side too short to reach the base, no solutions
elif s1>s2:
    #Side one is longer than side two there can be only one solution
    print("There is one solution")
    ad2=degrees(asin(s2*sin(a1)/s1))
    print("Angle B is",ad2)
    #solve angle with law of sines
    ad3=180-ad1-ad2
    print("Angle C is",ad3)
    #solve with subtraction 
    s3=(s1*sin(radians(ad3)))/sin(a1)
    print("Side C is", s3)
    #solve with law of sines
elif s1>=(s2*sin(a1)) and s1<s2:
    #Side is between size of height and side 2, so two solutions
    print("There are two solutions")
    ad2=degrees(asin(s2*sin(a1)/s1))
    ad4=180-ad2
    #solve for two solutions with law of sines and subtraction
    print("Angle B is",ad2,"or", ad4)
    ad3=180-ad1-ad2
    ad5=180-ad3
    #solve for two solutions with subtraction
    print("Angle C is",ad3,"or",ad5)
    s3=(s1*sin(radians(ad3)))/sin(a1)
    s4=sqrt(s1**2+s2**2-2*s1*s2*cos(radians(ad5)))
    #solve for third side with law of cosines and sines
    print("Side C is", s3,"or",s4)
else:
    print("something is wrong")
    #just an error message left over from earlier prototyping
