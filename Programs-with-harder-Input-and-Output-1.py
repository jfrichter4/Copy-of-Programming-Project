# Name: joe richter
# Date: Feb. 26, 21 - Mar. 26, 21
# Programs-with-harder-Input-and-Output-1.py
# Dirxns: Input 2 pts and a 3rd x-val. Output the 3rd y-val if the pts are on an exponential fnxn. 
import math
x1 = float(input("Input the x-value of the first point: "))
y1 = float(input("Input the y-value of the first point: "))
x2 = float(input("Input the x-value of the second point: "))
y2 = float(input("Input the y-value of the second point: "))
x3 = float(input("Input the x-value of a third point: "))
#Checks if the two divided are equivalent because if they are, it's not exponential: 
if (y1/x1)==(y2/x2): 
    #Carries out intention stated in above comment: 
    print("Not Exponential")
#If the above aren't equivalent: 
else: 
    #Subtracts x2 from x1: 
    c = x2-x1
    #Divides y2 by y1: 
    d = y2/y1
    #Exponentiates y2/y1 by 1/c: 
    b = d**(1/c)
    #Divides y1 by b^x1: 
    a = y1/(b**x1)
    #Multiplies a by b exponentiated by x3: 
    y3 = a*(b**x3)
    #Prints what the program got for y3: 
    print("This is the y-value of the third point: ", y3)