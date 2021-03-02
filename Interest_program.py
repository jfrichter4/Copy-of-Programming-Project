#Simon Phipps
#3/2/21
#Interest Program

from math import log10
A1 = float(input("Enter A1: "))
P1 = float(input("Enter P1: "))
n1 = float(input("Enter n1: "))
r1 = float(input("Enter r1: "))

print("Time:",((log10(A1/P1))/(n1*(log10(1+(r1/n1))))))
