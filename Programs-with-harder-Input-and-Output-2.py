# Name: joe richter
# Date: Feb. 26, 21 - Mar. 26, 21
# Programs-with-harder-Input-and-Output-2.py
# Dirxns: Input the 6 constants for system Ax + By = C and Dx + Ey = F. Output the (x, y) solution. 
import math
#The below get the inputs for values A-F: 
A = float(input("For the systems Ax+By=C and Dx+Ey=F, input A: "))
B = float(input("For the systems Ax+By=C and Dx+Ey=F, input B: "))
C = float(input("For the systems Ax+By=C and Dx+Ey=F, input C: "))
D = float(input("For the systems Ax+By=C and Dx+Ey=F, input D: "))
E = float(input("For the systems Ax+By=C and Dx+Ey=F, input E: "))
F = float(input("For the systems Ax+By=C and Dx+Ey=F, input F: "))

#The g is what I worked out to be the numerator for y:
g = (A*F) - (D*C)
#The h is what I worked out to be the denominator for y:
h = (A*E) - (D*B)
#The y simply divides g by h:
y = g/h
#The i is what I worked out to be the numerator for x:
i = (B*F) - (E*C)
#The j is what I worked out to be the denominator for x:
j = (B*D) - (A*E)
#This x simply divides i by j: 
x = i/j
#This prints the results in a form familiar to us: 
print("(", x, ",", y, ")")