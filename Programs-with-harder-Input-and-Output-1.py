# Name: joe richter
# Date: Feb. 26, 21 - Unknown
# Programs-with-harder-Input-and-Output-1.py
# Dirxns: Input 2 pts and a 3rd x-val. Output the 3rd y-val if the pts are on an exponential fnxn. 
import math
x1 = float(input("Input the x-value of the first point: "))
y1 = float(input("Input the y-value of the first point: "))
x2 = float(input("Input the x-value of the second point: "))
y2 = float(input("Input the y-value of the second point: "))
x3 = float(input("Input the x-value of a third point: "))
#ty1 = ((y2/y1)/y1)
#tx1 = (x2-x1)
#print(ty1)
#y3 = ((ty1/tx1)**x3)
#print("x1: ", x1, ", ", "y2: ", y1, ", ", "x2: ", x2, ", " "y2: ", y2, ", ", "x3: ", x3, ", " "y3: ", y3)
#a1 = (y1/(b1**x1))
#eq1 = (a1*(b2**x2))
#print(a1)
#print(eq1)
if (y1/x1)==(y2/x2): 
    print("Not Exponential")
else: 
    c = x2-x1
    d = y2/y1
    b = d**(1/c)
    a = y1/(b**x1)
    y3 = a*(b**x3)
    print("C: ", c)
    print("D: ", d)
    print("B: ", b)
    print("A: ", a)
    print("This is the y-value of the third point: ", y3)