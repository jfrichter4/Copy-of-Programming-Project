#Simon Phipps
#3/22/21
#Multiplication Game

from random import randint
c=0
#Set correct answers to 0
w=0
#Set wront answers to 0
while c<5:
    n1=randint(1,12)
    n2=randint(1,12)
    #Pick random values
    print("What is", n1,"x",n2,"?")
    a1=float(input())
    #Ask question and receive answer
    if a1==n1*n2:
        print("Nice work!")
        c=c+1
        #If correct, add 1 to correct answers
    else:
       print("Wrong. The correct answer is", n1*n2)
       w=w+1
       #If wrong, print correct answer
if c==5:
    print("You win!!")
    #When 5 are correct, you win!!
