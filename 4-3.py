# joe richter
# Mar. 22, 21
# 4.3 Programs with Loops
# Find all the prime factors of a positive integer or state that the integer is prime. 
from sys import exit
#Gets the number to undergo prime factorization: 
#I replaced the possible negative with nothing just to make it easier for the user: 
a = int(input("Enter the integer: ").replace("-", ""))
#If a, because of how it can be inputted, is either 1 or 0: 
if a<=1: 
    #Print the following: 
    print("Input was zero or one, therefore not prime and without any prime factors.")
#If a is equivalent to two: 
if a==2: 
    #Print the following: 
    print("Input was two, and two is a prime number.")
if a==3: 
    #Print the following: 
    print("Input was three, and three is a prime number.")
else: 
    #Produces a sequence of numbers beginning from two to a/2: 
    for b in range(2,int(a/2)+1):
        #So long as the remainder is nothing (meaning the number being tried is prime, the following code will be carried out:  
        while (a%b)==0:
            #Prints b-values which were found to be prime factors using the above line: 
            print("A prime factor: ", b),
            #Makes the a-value a new one and divides by b, so if the input is 12, the a value will go from 12 to 6 to 3: 
            #Basically has the loop restart: 
            a = a/b
    #Introduces the same sequence of numbers, but tests for something else: 
    for b in range(2,int(a/2)+1):
        #If the remainder of the integer inputted divided by the sequence of integers generated above never equals zero: 
        if (a%b)!=0: 
            #Then print the following message: 
            print("This integer is indeed prime!")
            #And exit: 
            quit(0)