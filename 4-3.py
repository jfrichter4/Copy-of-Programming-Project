# joe richter
# Mar. 22, 21
# 4.3 Programs with Loops
# Find all the prime factors of a positive integer or state that the integer is prime. 
import math
from sys import exit

a = int(input("Enter the number: ").replace("-", ""))

a1 = a.is_integer()
if a1 == True: 
    print("The number is an integer.")
else: 
    print("Not an integer, therefore not prime.")  
    exit(0)

if a > 1: 
    print("The number is greater than 1.")
else: 
    print("Either 1 or 0, therefore not prime.") 
    exit(0)

if a == 2: 
    print("2 is prime, and it is the only even number that is prime.")
    exit(0)
else: 
    a2 = a/2
    a3 = a2.is_integer()

    if a3 == True: 
        print("The number is even and not 2 or 1 or 0, therefore making it a composite number.")
    else: 
        for b in range(3), a+1, 2: 
            print(b)
