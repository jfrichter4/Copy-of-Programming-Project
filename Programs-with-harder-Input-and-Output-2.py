# Name: joe richter
# Date: Feb. 26, 21 - Unknown
# Programs-with-harder-Input-and-Output-2.py
# Dirxns: Input the 6 constants for system Ax + By = C and Dx + Ey = F. Output the (x, y) solution. 
import math
import numpy
A = float(input("For the systems Ax+By=C and Dx+Ey=F, input A: "))
B = float(input("For the systems Ax+By=C and Dx+Ey=F, input B: "))
C = float(input("For the systems Ax+By=C and Dx+Ey=F, input C: "))
D = float(input("For the systems Ax+By=C and Dx+Ey=F, input D: "))
E = float(input("For the systems Ax+By=C and Dx+Ey=F, input E: "))
F = float(input("For the systems Ax+By=C and Dx+Ey=F, input F: "))
#g = (-E*y+F/D)
#print(g)

g = numpy.array([[A, B], [D, E]])
h = numpy.array([C, F])
i = numpy.linalg.solve(g, h)
j = i[0]
k = i[1]
print("(", j, ",", k, ")")
