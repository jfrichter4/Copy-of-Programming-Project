#Simon Phipps
#3/4/21
#Point Connection program

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

if (y2-y1)==0:
    print("y=",y2)
    print("Your line is horizantal!")
elif(x2-x1)==0:
    print("x=",x2)
    print("Your line is vertical!")
else:
    m = (y2-y1)/(x2-x1)
    print("Your line is", "y-",y1,"=",m,"(x-",x1,")")
