#!/usr/bin/python3


myArray = [42, 24, 789, 1492];


print("What kind of loop would you like to run:")
print("(1) For Loop")
print(" (2) Ranged For Loop")
print(" (3) While Loop")
uInput = input(" : ")

print("You entered ", uInput, " which did not cause a new line")
print("but input+input, ", uInput+uInput, "does not look right...")
uInput = int(uInput)
print("Maybe this helped, ", uInput+uInput)


if(uInput == 1):
     for i in myArray :
          print("For loop says", i)

elif(uInput == 2):
     for i in range(4):
          print("Ranged for loop says", myArray[i])
else:
     i = 0

     while(i < len(myArray)):
          print("While loop says ", myArray[i])
          i+=1



