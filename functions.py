#!/usr/bin/python3

def forLoop(myArray):
     count = 0
     for i in myArray :
          print("For loop says", i)
          count += 1
     return count

def forRangedLoop(myArray):
     for i in range(4):
          print("Ranged for loop says", myArray[i])

def whileLoop(myArray):
     i = 0

     while(i < len(myArray)):
          print("While loop says ", myArray[i])
          i+=1


myArray = [42, 24, 789, 1492]
uInput = 0

while(uInput != 4):
     print("What kind of loop would you like to run:")
     print("(1) For Loop")
     print(" (2) Ranged For Loop")
     print(" (3) While Loop")
     print(" (4) Quit")
     uInput = input(" : ")

     uInput = int(uInput)

     if(uInput == 1):
          fnReturn = forLoop(myArray)
          print("From function", fnReturn)
     elif(uInput == 2):
          forRangedLoop(myArray)
     elif(uInput == 3):
          whileLoop(myArray)
     else:
          print("Goodbye!")


