# joe richter
# Mar. 22, 21
# 4.3 Programs with Loops
# Find all the prime factors of a positive integer or state that the integer is prime. 
import math
#So the program can easily exit loops:
from sys import exit

#Gets the number to be determined whether it's prime or composite: 
#Most of the manipulation the program does is with integers, so I did that from the start: 
#I replaced the possible negative with nothing just to make it easier for the user: 
a = int(input("Enter the number: ").replace("-", ""))

#Checks to make sure whether what was entered was both a whole number and not letters or symbols: 
a1 = float(a).is_integer()
#Trying to keep it nice and verbose so the user can figure out where they may be going wrong and so on: 
#The actual thought is that {.is_integer()} will return either a True or False value for a's float: 
if a1 == True: 
    print("The number is an integer.")
#If there is in fact stuff that keeps this from being an integer in the input, the program will exit...
#...here with this message: 
else: 
    print("Not an integer, therefore not prime.")  
    exit(0)

#Important to check because if the number is less, it can't be prime: 
#Still wanting to keep things in depth: 
if a > 1: 
    print("The number is greater than 1.")
#Follows through with the above argument: 
else: 
    print("Either 1 or 0, therefore not prime.") 
    exit(0)

#Separate from above inequality because 2 is the only even number that is prime, so I think that should be noted: 
if a == 2: 
    print("2 is prime, and it is the only even number that is prime.")
    exit(0)
#If it passes the above check, the program can continue into the more important and useful part: 
else: 
    a2 = a/2
    
    #Thought is that an odd number will not be an integer when divided by two, so will move along to the next else: 
    a3 = a2.is_integer()
    #Again, {.is_integer()} produces either a True or False variable: 
    if a3 == True: 
        print("The number is even and not 2 or 1 or 0, therefore making it a composite number.")
    
    #If the number is odd and not one, it can go into this conditional: 
    else: 
        #Produces a sequence of numbers beginning from two to a/2: 
        for b in range(2, int(a2)+1): 
            #It's composite if the above equation finds a to be divisible by any of the numbers it iterates through:  
            if (a%b)==0: 
                print("This number is composite.")
                exit(0)
        #If the above conditionals don't find the number to be composite, the number is prime. 
        else: 
            print("This number is indeed prime!")
