# Name: joe richter
# Date: Feb. 26, 21 - Unknown
# Programs-with-harder-Input-and-Output-2.py
# Dirxns: Input a vertex and second pt. Output the general form (y = Ax**2 + Bx +C) quadratic equation. 

x1 = float(input("Input the x-value of the vertex: "))
y1 = float(input("Input the y-value of the vertex: "))
x2 = float(input("Input the x-value of the second point on the line: "))
y2 = float(input("Input the y-value of the second point on the line: "))

a = ((y2-y1)/((x2-x1)**2))
b = (5*(-2*x1))
c = (y1+(5*(x1**2)))
print(a)
print("y = ", a, "x^2 + ", b, "x + ", c)
