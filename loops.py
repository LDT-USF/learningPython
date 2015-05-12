#!/usr/bin/python3


myArray = [42, 24, 789, 1492];

for i in myArray :
     print("The next item is a", i)


print("After for loop i = ", i)

for i in range(4): 
     print("Ranged for loop says", myArray[i])

print("After second for loop i = ", i)

i = 0


while(i < len(myArray)):
     print("While loop says ", myArray[i])
     i+=1

print("After while loop i = ", i)
