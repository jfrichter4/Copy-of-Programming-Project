# Name: joe richter
# Date: Feb. 26, 21 - Unknown
# Programs-with-harder-Input-and-Output-2.py
# Dirxns: Input a vertex and second pt. Output the general form (y = Ax**2 + Bx +C) quadratic equation. 

h = float(input("Input the x-value of the vertex: "))
k = float(input("Input the y-value of the vertex: "))
x = float(input("Input the x-value of the second point on the line: "))
y = float(input("Input the y-value of the second point on the line: "))

d = (x-h)**2
e = y-k
a = e/d
print(d)
print(e)
print(a)

f = (-h*2)*a
g = (h**2)*a+k
print("y = ((x^2) *", a, ") + (x * ", f, ") + ", g)