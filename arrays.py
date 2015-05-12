#!/usr/bin/python3

#list declaration
myArray1 = [1, 2, 3]
print("testing for 1", myArray1[0])
print("testing for 2", myArray1[1])
print("testing for 3", myArray1[2])


#tuple declaration
myArray2 = (1, 2, 3)
print("testing for 1", myArray2[0])
print("testing for 2", myArray2[1])
print("testing for 3", myArray2[2])


myArray1[0] = 42
#myArray2[0] = 42

print("There are ", len(myArray1), " elements in the array")
print("The largest element in the array is ", max(myArray1))

myArray1[1] = "Goodbye!"
print(myArray1[1])
