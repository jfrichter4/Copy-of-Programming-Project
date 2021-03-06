#Simon Phipps
#3/4/21
#Quadratic equation program

a1 = float(input("Enter a: "))
b1 = float(input("Enter b: "))
c1 = float(input("Enter c: "))

r1 = (-b1+((b1**2)-(4*a1*c1))**.5)/2*a1
r2 = (-b1-((b1**2)-(4*a1*c1))**.5)/2*a1

if (b1**2)-(4*a1*c1) < 0:
    print ("Your roots are imaginary")
else:
    print ("Your roots are real")

if r1 != r2:
    print("Your roots are",(-b1+((b1**2)-(4*a1*c1))**.5)/2*a1,"and",(-b1-((b1**2)-(4*a1*c1))**.5)/2*a1)
elif r1 == r2:
    print("Your root is",(-b1+((b1**2)-(4*a1*c1))**.5)/2*a1)
