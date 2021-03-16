#Simon Phipps
#3/4/21
#Quadratic equation program

a1 = float(input("Enter a: "))
b1 = float(input("Enter b: "))
c1 = float(input("Enter c: "))
#Input equation constants

r1 = (-b1+((b1**2)-(4*a1*c1))**.5)/2*a1
r2 = (-b1-((b1**2)-(4*a1*c1))**.5)/2*a1
#Quadratic formula

if (b1**2)-(4*a1*c1) < 0:
    print ("Your roots are imaginary")
    #If value under square root is negative, the roots are imaginary
else:
    print ("Your roots are real")
    #Otherwise, the roots are real

if r1 != r2:
    print("Your roots are",(-b1+((b1**2)-(4*a1*c1))**.5)/2*a1,"and",(-b1-((b1**2)-(4*a1*c1))**.5)/2*a1)
    #If the two roots are not equal, print roots
    
elif r1 == r2:
    print("Your root is",(-b1+((b1**2)-(4*a1*c1))**.5)/2*a1)
    #If roots are equal, print root
