#Simon Phipps
#3/22/21
#Radical Simplification

n1=float(input("Enter value to take the square root:" ))
a1=n1

while n1%a1**2!=0:
        a1=a1-1
        #works backward until value is divisible by a perfect square
if n1/a1==a1:
    print("Your radical is", a1)
    #if initial value is a perfect square, print square root
else:
    print("Your radical is", a1,"(",n1/a1**2,")^.5")
    #otherwise print simplified radical
