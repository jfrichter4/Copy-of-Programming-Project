# Name: joe richter
# Date: Feb. 26, 21 - Mar. 26, 21
# Programs-with-harder-Input-and-Output-2.py
# Dirxns: Input a vertex and second pt. Output the general form (y = Ax**2 + Bx +C) quadratic equation. 
#Gets the inputs for the desired values: 
h = float(input("Input the x-value of the vertex: "))
k = float(input("Input the y-value of the vertex: "))
x = float(input("Input the x-value of the second point on the line: "))
y = float(input("Input the y-value of the second point on the line: "))
#Puts this part of vertex form in a variable: 
d = (x-h)**2
#Subtracts y from k because that's a move to make early on: 
e = y-k
#If the result of d wasn't 0, it's worthwhile to do the following: 
if d != 0: 
    #Finds the A-val.: 
    a = e/d
    #Finds the B-val.: 
    f = (-h*2)*a
    #Finds the C-val.: 
    g = (h**2)*a+k
    #Prints these values in an understandable form: 
    print("y = ((x^2) *", a, ") + (x * ", f, ") + ", g)
#Say that d is zero, though: 
else: 
    #The a-val. will be zero: 
    a = 0
    #An explanation for what happened: 
    print("The inputted x-values amount to zero, thus eliminating all values except for the vertex's y-value, making this line horizontal: ")
    #Final result: 
    print("y = ", k)