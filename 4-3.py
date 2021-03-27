# joe richter
# Mar. 22, 21
# 4.3 Programs with Loops
# Find all the prime factors of a positive integer or state that the integer is prime. 
from sys import exit
#Gets the number to undergo prime factorization: 
#I replaced the possible negative with nothing just to make it easier for the user: 
a = int(input("Enter the integer: ").replace("-", ""))
if a == 0 or a == 1: 
    print("Input was zero or one, therefore not prime.")
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

    for b in range(2,int(a/2)+1):
        if (a%b)!=0: 
            print("This integer is indeed prime!")
            quit(0)