# joe richter
# Mar. 22, 21
# 4.3 Programs with Loops
# Find all the prime factors of a positive integer or state that the integer is prime. 
import math

#Gets the number to be determined whether it's prime or composite: 
#Most of the manipulation the program does is with integers, so I did that from the start: 
#I replaced the possible negative with nothing just to make it easier for the user: 
a = int(input("Enter the number: ").replace("-", ""))

#Produces a sequence of numbers beginning from two to a/2: 
for b in range(2,int(a/2)+1):
    #It's composite if the above equation finds a to be divisible by any of the numbers it iterates through:  
    while (a%b)==0:
        #Prints b-values: 
        print("A prime factor: ", b),
        #Makes the a-value a new one and divides by b, so if the input is 12, ... 
        #...the a value will go from 12 to 6 to 3: 
        a = a/b
